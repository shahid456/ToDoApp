import uuid


def generate_unique_id():
    return str(uuid.uuid4())


def myDateSort(data_list):
    temp = []
    while data_list:
        minimum = data_list[0]  # arbitrary number in list
        for x in data_list:
            if int(''.join(x["date"].split('/')[::-1])) < int(''.join(minimum["date"].split('/')[::-1])):
                minimum = x
        temp.append(minimum)
        data_list.remove(minimum)
    return temp


if __name__ == '__main__':
    data = ['']
    myDateSort(data)
