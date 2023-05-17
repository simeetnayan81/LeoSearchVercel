
from utils import hf
from utils import pinecone_index
def sem_search(query):
	print(query)
	qemb=hf.embed_query(query)
	print('d2')
	xc = pinecone_index.query(qemb, top_k=3, include_metadata=True)
	results=[]
	for result in xc['matches']:
		results.append({'title': result['metadata']['question'], 'url':'google.com'})
	return results