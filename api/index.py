
from flask import Flask, render_template, request

import pinecone
from langchain.embeddings import HuggingFaceHubEmbeddings


app = Flask(__name__)


PINECONE_KEY='3b757889-ed10-4965-96b9-02e967afe9f6'
HUGGINGFACE_KEY='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'

pinecone.init(api_key=PINECONE_KEY, environment="asia-southeast1-gcp-free")
pinecone_index = pinecone.Index("leo-search")

repo_id = "sentence-transformers/all-mpnet-base-v2"
hf = HuggingFaceHubEmbeddings(
    repo_id=repo_id,
    task="feature-extraction",
    huggingfacehub_api_token=HUGGINGFACE_KEY,
)


def sem_search(query):
	print(query)
	qemb=hf.embed_query(query)
	print('d2')
	xc = pinecone_index.query(qemb, top_k=3, include_metadata=True)
	results=[]
	r=1
	for result in xc['matches']:
		results.append({'title': result['metadata']['question'], 'rank': 'Rank' + str(r)})
		r=r+1
	return results

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    results = sem_search(query)  #Replace with your search logic
    return render_template('results.html', query=query, results=results)
