import json


class DatabaseManagement:
    def __init__(self, filename):
        self.filename = filename
        print('Database constructor called')

    def write(self, content):
        print('Insertion done')
        if not content:
            return False
        jcon = json.dumps(content)
        with open(self.filename, 'w') as file:
            file.write(jcon)

    def read(self):
        data = []
        with open(self.filename, 'r') as file:
            res = str.join('', file.readlines())
            if str.strip(res) != '':
                data = json.loads(res)
        return data
