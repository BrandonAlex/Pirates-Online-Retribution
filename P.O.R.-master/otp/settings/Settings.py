import json

class Settings:
    def __init__(self, filename):
        self.filename = filename

        self.data = {}
        self.read()

    def read(self):
        try:
            self.data = json.loads(filename)
        except:
            self.write()

    def write(self):
        json.dumps(self.data)

    def set(self, key, value):
        self.data[key] = value
        self.write()

    def remove(self, key, value):
        if key in self.data:
            del self.data[key]
            self.write()

    def get(self, key, default=None):
        if key in self.data:
            return self.data[key]
        return default

    def all(self):
        return self.data.keys()
