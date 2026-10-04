from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
import mlflow

mlflow.langchain.autolog()

CHROMA_DB_DIR = "chroma_db"

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

embeddings = OpenAIEmbeddings()

vectorstore = Chroma(
    persist_directory=CHROMA_DB_DIR,
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever
)

ESCALATION_KEYWORDS = [
    "angry",
    "lawsuit",
    "human agent"
]

def should_escalate(query):
    return any(word in query.lower() for word in ESCALATION_KEYWORDS)

# @mlflow.trace
def ask_support_agent(query):
    if should_escalate(query):
        return {
            "success": True,
            "escalated": True,
            "answer": "Escalating to a human agent"
        }

    result = qa_chain.invoke({
        "query": query
    })

    answer = result["result"]

    return {
        "success": True,
        "escalated": False,
        "answer": answer
    }