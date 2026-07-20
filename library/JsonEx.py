import json

def read(file):
    with open(file, "r") as f:
        return json.load(f)

def write(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

def parse(text):
    return json.loads(text)

def stringify(data):
    return json.dumps(data, indent=4)