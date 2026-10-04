from dotenv import load_dotenv
load_dotenv()
from loguru import logger

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

CHROMA_DB_DIR = "chroma_db"

def build_vectorstore():
    # Load the document
    loader  = TextLoader("data/faqs.txt")
    docs = loader.load()

    # Split the documents
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 300,
        chunk_overlap = 50
    )

    split_docs = splitter.split_documents(docs)

    logger.info(f"Number of docs {len(split_docs)}")


    #Embed the documents right into Chroma
    embeddings = OpenAIEmbeddings()

    vectorstore = Chroma.from_documents(
        documents=split_docs,
        embedding=embeddings,
        persist_directory=CHROMA_DB_DIR
    )

    print("chromadb vector created success")

if __name__ == "__main__":
    build_vectorstore()