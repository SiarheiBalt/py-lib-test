import hashlib
import json


class IdGenerator:
    def __init__(self):
        self.content_map = {}

    def generate_id(self, text):
        key = text

        if key in self.content_map:
            self.content_map[key] += 1
        else:
            self.content_map[key] = 1

        content_str = json.dumps('content')

        return hashlib.sha256(content_str.encode()).hexdigest()
