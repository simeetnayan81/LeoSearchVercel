import pinecone

from langchain.embeddings import HuggingFaceHubEmbeddings

from utils.key import PINECONE_KEY, HUGGINGFACE_KEY

pinecone.init(api_key=PINECONE_KEY, environment="asia-southeast1-gcp-free")
pinecone_index = pinecone.Index("leo-search")

repo_id = "sentence-transformers/all-mpnet-base-v2"
hf = HuggingFaceHubEmbeddings(
    repo_id=repo_id,
    task="feature-extraction",
    huggingfacehub_api_token=HUGGINGFACE_KEY,
)

from utils import perform_search
