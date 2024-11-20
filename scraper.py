import os
import requests
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# scraper for websites

class DataIndexer:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.data_dir = 'data/'
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

    def scrape_website(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            # Entferne Skripte und Styles
            for script in soup(["script", "style"]):
                script.decompose()
            text = soup.get_text(separator=' ')
            # Bereinige den Text
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)
            return text
        except Exception as e:
            print(f"Fehler beim Scrapen der Website {url}: {e}")
            return ""

    def index_data(self, texts, index_name):
        embeddings = self.model.encode(texts)
        embeddings = np.array(embeddings).astype('float32')
        dimension = embeddings.shape[1]
        index = faiss.IndexFlatL2(dimension)
        index.add(embeddings)
        faiss.write_index(index, os.path.join(self.data_dir, f'{index_name}.faiss'))
        # Speichere die Dokumente
        with open(os.path.join(self.data_dir, f'{index_name}_docs.txt'), 'w', encoding='utf-8') as f:
            for doc in texts:
                f.write(doc + '\n')
        print(f'Indizierung von {index_name} abgeschlossen.')

    def run(self):
        # Agent 1: Research Report Website 2023 - Next 2026
        research_report_urls = [
            'https://mpib-berlin.mpg.de/research-report-2023',
            # Füge weitere relevante URLs hinzu
        ]
        research_report_texts = [self.scrape_website(url) for url in research_report_urls]
        self.index_data(research_report_texts, 'research_report')

        # Agent 2: Allgemeine MPIB Website
        mpib_website_urls = [
            'https://mpib-berlin.mpg.de/',
            # Füge weitere relevante URLs hinzu
        ]
        mpib_website_texts = [self.scrape_website(url) for url in mpib_website_urls]
        self.index_data(mpib_website_texts, 'mpib_website')

        # Agent 3: Personaldatenbank/Profile
        personnel_urls = [
            'https://mpib-berlin.mpg.de/mitarbeiter',
            # Füge weitere URLs der Mitarbeiterprofile hinzu
        ]
        personnel_texts = [self.scrape_website(url) for url in personnel_urls]
        self.index_data(personnel_texts, 'personnel')

        # Agent 4: Publikationen
        publications_urls = [
            'https://pure.mpg.de/',
            # Füge weitere relevante URLs hinzu
        ]
        publications_texts = [self.scrape_website(url) for url in publications_urls]
        self.index_data(publications_texts, 'publications')

        # Agent 5: Organigram
        organigram_urls = [
            'https://mpib-berlin.mpg.de/chm',
            # Füge weitere relevante URLs hinzu
        ]
        organigram_texts = [self.scrape_website(url) for url in organigram_urls]
        self.index_data(organigram_texts, 'organigram')

if __name__ == '__main__':
    indexer = DataIndexer()
    indexer.run()