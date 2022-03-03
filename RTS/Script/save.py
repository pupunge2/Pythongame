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

def save_to_file():
    f = open('../Save/save.txt', 'w')
    f.seek(0)
    
    for i in range(4):
        tmp_string = ''

        if var.Save.data[i]['new'] == True:
            tmp_string += 'new:True|'
            
        else:
            tmp_string += 'new:False|'

        tmp_string += 'level:'

        if len(var.Save.data[i]['level']) == 0:
            tmp_string += 'None|'

        else:
            tmp_string += str(var.Save.data[i]['level']) + '|'

        tmp_string += 'card:'

        if len(var.Save.data[i]['card']) == 0:
            tmp_string += 'None|'
        
        else:
            tmp_string += str(var.Save.data[i]['card']) + '|'

        tmp_string += 'upgrade:'

        if len(var.Save.data[i]['upgrade']) == 0:
            tmp_string += 'None'

        else:
            tmp_string += str(var.Save.data[i]['upgrade'])

        f.write(tmp_string + '\n')

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
