import var

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

    else:
        load()

def save():
    pass

def load():
    f = open('../Save/save.txt', 'r')
    f.seek(0)
    file_content = []

    while True:
        line = f.readline()

        if not line:
            break

        file_content.append(line)

    var.Save.data = []

    for i in range(4):
        file_content_string = file_content[i]
        file_content_li = file_content_string.split('|')
        temp_data = {}
        
        if file_content_li[0] == 'new:True':
            temp_data = {'new' : True, 'level' : [], 'card' : [], 'upgrade' : []}
            var.Save.data.append(temp_data)
