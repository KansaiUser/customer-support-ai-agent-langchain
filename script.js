
(function () {
  const API_URL = "http://localhost:8000/chat";

  // Create widget container
  const widget = document.createElement("div");
  widget.innerHTML = `
    <div id="chat-toggle">💬</div>

    <div id="chat-box">
      <div id="chat-header">Assistant</div>
      <div id="chat-messages"></div>

      <div id="chat-input-area">
        <input id="chat-input" placeholder="Type a message..." />
        <button id="chat-send">Send</button>
      </div>
    </div>
  `;

  document.body.appendChild(widget);

  // Styles
  const style = document.createElement("style");
  style.textContent = `
    #chat-toggle {
      position: fixed;
      bottom: 20px;
      right: 20px;
      width: 56px;
      height: 56px;
      border-radius: 50%;
      background: #111;
      color: white;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 24px;
      z-index: 99999;
    }

    #chat-box {
      position: fixed;
      bottom: 90px;
      right: 20px;
      width: 320px;
      height: 420px;
      background: white;
      border: 1px solid #ddd;
      border-radius: 12px;
      display: none;
      flex-direction: column;
      overflow: hidden;
      z-index: 99999;
      box-shadow: 0 4px 20px rgba(0,0,0,0.15);
      font-family: Arial, sans-serif;
    }

    #chat-header {
      padding: 12px;
      background: #111;
      color: white;
      font-weight: bold;
    }

    #chat-messages {
      flex: 1;
      overflow-y: auto;
      padding: 10px;
    }

    .msg {
      margin-bottom: 10px;
      padding: 8px 10px;
      border-radius: 8px;
      max-width: 80%;
    }

    .user {
      background: #e8f0fe;
      margin-left: auto;
    }

    .bot {
      background: #f1f1f1;
    }

    #chat-input-area {
      display: flex;
      border-top: 1px solid #eee;
    }

    #chat-input {
      flex: 1;
      border: none;
      padding: 10px;
      outline: none;
    }

    #chat-send {
      border: none;
      background: #111;
      color: white;
      padding: 10px 15px;
      cursor: pointer;
    }
  `;
  document.head.appendChild(style);

  const toggle = document.getElementById("chat-toggle");
  const box = document.getElementById("chat-box");
  const input = document.getElementById("chat-input");
  const sendBtn = document.getElementById("chat-send");
  const messages = document.getElementById("chat-messages");

  toggle.onclick = () => {
    box.style.display =
      box.style.display === "flex" ? "none" : "flex";
  };

  function addMessage(text, type) {
    const div = document.createElement("div");
    div.className = `msg ${type}`;
    div.textContent = text;
    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
  }

  async function sendMessage() {
    const text = input.value.trim();
    if (!text) return;

    addMessage(text, "user");
    input.value = "";

    try {
      const payload = {
        message: text,
        timestamp: Date.now(),
        page: window.location.href
      };

      const res = await fetch(API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
      });

      const data = await res.json();

      addMessage(
        data.answer || data.message || "No response",
        "bot"
      );
    } catch (err) {
      addMessage("Connection failed", "bot");
      console.error(err);
    }
  }

  sendBtn.onclick = sendMessage;

  input.addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
      sendMessage();
    }
  });
})();