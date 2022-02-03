class Bot:
    def __init__(self):
        self.keys = {}

    def addkey(self, key: str, anw: str):
        self.keys[key] = anw

    def addkeys(self, keys: dict):
        for key in keys.keys():
            for value in keys.values():
                self.keys[key] = value

    def run(self):
        inp = input()
        for key in self.keys.keys():
            if inp.casefold() == key.casefold():
                print(self.keys[inp.casefold()])