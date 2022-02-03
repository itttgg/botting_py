class Bot:
    def __init__(self):
        self.running = False
        self.keys = {}

    def fun(self, key):
        def wrapper(func):
            self.keys[key.casefold()] = func
        return wrapper

    def add_fun(self, key, method):
        self.keys[key.casefold()] = method

    def run(self):
        self.running = True
        while self.running:
            inp = input()
            for key in self.keys.keys():
                if inp.casefold() == key:
                    self.keys[inp.casefold()]()
