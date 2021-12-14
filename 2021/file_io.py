
def read_file(filename, type=str):
    content = []
    with open(filename) as file:
        for row in file.readlines():
            content.append(type(row.strip()))
    return content
