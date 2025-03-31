import httpx
from bs4 import BeautifulSoup

class WebNavigator:
    def __init__(self):
        self.client = httpx.Client()
        self.page = None

    def visit(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        print(f"🌐 Visite de {url}")
        response = self.client.get(url, headers=headers)
        if response.status_code == 200:
            self.page = BeautifulSoup(response.text, "html.parser")
            return True
        else:
            print("❌ Erreur HTTP :", response.status_code)
            return False

    def extract_titles(self):
        if not self.page:
            print("⚠️ Aucune page chargée.")
            return []

        titles = self.page.select("h2.jobTitle")
        jobs = [t.text.strip() for t in titles if t.text.strip()]
        return jobs
