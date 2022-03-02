def save_init():
    f = open('../Save/save.txt', 'a+')

    f.seek(0)

    file_content = []

    while True:
        line = f.readline()

        if not line:
            break

        file_content.append(line)

    if len(file_content) == 0:
        for i in range(4):
            f.write('new:True|level:None|card:None|upgrade:None\n')

def save():
    pass

def load():
    pass
