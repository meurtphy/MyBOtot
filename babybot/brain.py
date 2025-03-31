from babybot.web import WebNavigator
from babybot.memory import Memory

class BabyBot:
    def __init__(self):
        self.navigator = WebNavigator()
        self.memory = Memory()
        self.goal = None

    def think(self, goal):
        print(f"🧠 BabyBot pense à : {goal}")
        self.goal = goal

    def search_jobs(self, keyword="data scientist"):
        query = keyword.replace(" ", "+")
        url = f"https://fr.indeed.com/jobs?q={query}"
        if self.navigator.visit(url):
            jobs = self.navigator.extract_titles()
            self.memory.store(jobs)
