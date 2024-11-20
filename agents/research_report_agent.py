from agents.base_agent import BaseAgent
import faiss
from sentence_transformers import SentenceTransformer
import numpy as np

# Agent for scraped research report

class ResearchReportAgent(BaseAgent):
    def __init__(self):
        # TODO: Exchange the dummy parts
        with open('data/dummy_data.txt', 'r', encoding='utf-8') as f:
            self.data = f.read()

        #self.index = faiss.read_index('data/research_report.faiss')
        #with open('data/research_report_docs.txt', 'r', encoding='utf-8') as f:
        #    self.documents = [line.strip() for line in f]
        #self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def execute(self, query):
        # Dummy search
        if 'mpi' in query.lower() or 'website' in query.lower():
            return f"Gefundene Information im MPIB Website Agent:\n{self.data[:500]}..."
        else:
            return "Im MPIB Website Agent wurden keine relevanten Informationen gefunden."
        
        # TODO: Exchange the dummy parts
        #query_embedding = self.model.encode([query]).astype('float32')
        #distances, indices = self.index.search(query_embedding, k=5)
        #relevant_docs = [self.documents[idx] for idx in indices[0]]
        #context = "\n".join(relevant_docs)
        #return context