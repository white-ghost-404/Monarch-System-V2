import json

class MonarchData:
    def __init__(self):
        self.file = "save_data.json"

    def load_stats(self):
        try:
            with open(self.file, "r") as f:
                return json.load(f)
        except:
            return {"level": 1, "rank": "E", "exp": 0, "weight_limit": 1}

    def save_stats(self, lvl, rank, weight):
        data = {"level": lvl, "rank": rank, "weight_limit": weight}
        with open(self.file, "w") as f:
            json.dump(data, f)

