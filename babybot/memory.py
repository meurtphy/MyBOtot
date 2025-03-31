class Memory:
    def __init__(self):
        self.jobs = []

    def store(self, jobs):
        print(f"💾 Mémorisation de {len(jobs)} offres.")
        self.jobs.extend(jobs)

    def show(self):
        print("\n📚 Mémoire de BabyBot :")
        if not self.jobs:
            print("🤷‍♂️ Aucune offre trouvée.")
        else:
            for i, job in enumerate(self.jobs[:10], 1):
                print(f"{i}. {job}")
