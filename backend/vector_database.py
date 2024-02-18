from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from llama_index.embeddings.openai import OpenAIEmbedding
import chromadb
import os


class Vector_Database:
    def __init__(self, api_key='',
                  api_base='', collection_name='FAQ',
                  data_directory='backend/faqs_data/'):
        os.environ["OPENAI_API_KEY"] = api_key
        os.environ["OPENAI_API_BASE"] = api_base
        self.embedding_batch_size=10
        self.collecion_name = collection_name
        self.data_directory = data_directory
        # Create a Chroma Client
        self.chroma_client = chromadb.PersistentClient(path='backend/vectorised/')
        try:
            self.chroma_collections = self.chroma_client.create_collection(self.collecion_name)
        except:
            self.chroma_collections = self.chroma_client.get_collection(self.collecion_name)
        # Embedding models
        self.embed_model = OpenAIEmbedding(embed_batch_size=self.embedding_batch_size)
        # Load the docuemnts
        self.documents = SimpleDirectoryReader(self.data_directory).load_data()

        # Storing data
        self.vector_store = ChromaVectorStore(chroma_collection=self.chroma_collections)
        self.storage_context = StorageContext.from_defaults(vector_store=self.vector_store)

        index = VectorStoreIndex.from_documents(
            self.documents, storage_context=self.storage_context, embed_model=self.embed_model
        )
        # Query Data
        self.query_engine = index.as_query_engine()
    
    def change_vc(self, coll):
        self.collecion_name = coll
        try:
            self.chroma_collections = self.chroma_client.create_collection(self.collecion_name)
        except:
            self.chroma_collections = self.chroma_client.get_collection(self.collecion_name)

        self.vector_store = ChromaVectorStore(chroma_collection=self.chroma_collections)
        self.storage_context = StorageContext.from_defaults(vector_store=self.vector_store)

        index = VectorStoreIndex.from_documents(
            self.documents, storage_context=self.storage_context, embed_model = self.embed_model
        )
        
        self.query_engine = index.as_query_engine()

    def search(self, question) -> str:
        response = self.query_engine.query(question)
        return response.response

