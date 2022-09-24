def adding_to_file(path, data):
    file_path = path
    with open(file_path, 'w') as file:
        for i in data:
            # print("or es.content_comp like '" + "%" + i + "%'")
            file.write(i + "\n")

def gen_data(begin, end):
    in_list = []
    to_do = range(begin, end)
    for i in to_do:
        in_list.append('test' + str(i))
    print(in_list)
    return in_list
#adding_to_file('test', gen_data(0, 100))

def read_to_file(path):
    with open(path, 'r') as file:

        return file.readlines()

def result_to_file(path, data):
    with open(path, 'w') as file:
        file.write('and(' + "\n"+"or es.content_comp like '" + "%" + data[0].split('\n')[0] + "%'" )
        for i in data[1:-1]:
            # print("or es.content_comp like '" + "%" + i + "%'")
            file.write("\n"+"or es.content_comp like '" + "%" + i.split('\n')[0] + "%'" )
        file.write('\n)')

result_to_file('result', read_to_file('test'))
