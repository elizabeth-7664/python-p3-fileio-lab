def write_file(file_name, content):
    with open(f"{file_name}.txt", mode="w", encoding="utf-8") as f:
        f.write(content)

def append_file(file_name, content):
    with open(f"{file_name}.txt", mode="a", encoding="utf-8") as f:
        f.write(content)

def read_file(file_name):
    with open(f"{file_name}.txt", mode="r", encoding="utf-8") as f:
        return f.read()
