from dotenv import load_dotenv
load_dotenv()
from loguru import logger
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

CHROMA_DB_DIR = "chroma_db"

vectorstore = Chroma(
    persist_directory=CHROMA_DB_DIR,
    embedding_function=OpenAIEmbeddings()
)

logger.info(f"Number of vectors {vectorstore._collection.count()}")