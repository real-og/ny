from csv import writer, DictReader
from datetime import datetime
  

def add_line(id=0, name='', company='', isSent='False', isActive='False'):
    with open('storage.csv', 'a', newline='') as f:
        writer_object = writer(f)
        writer_object.writerow((id, name, company, isSent, isActive))

def get_user_by_id(id):
    data = get_data()
    for i in data:
        if i['id'] == str(id):
            return i

def get_data() -> list(dict()):
    with open('storage.csv', newline='') as f:
        return list(DictReader(f))

def delete_user(id):
    data = get_data()
    new_list = list()
    cur_user = None
    for i in data:
        if i['id'] != str(id):
            new_list.append(i)
        else:
            cur_user = i
    with open('storage.csv', 'w') as f:
        wr = writer(f)
        wr.writerow(('id', 'name', 'company', 'isSent', 'isActive'))
        wr.writerows([(i['id'], i['name'], i['company'], i['isSent'], i['isActive']) for i in new_list])
    return cur_user

def edit_name(id, name):
    user = delete_user(id)
    user['name'] = name
    add_line(user['id'], user['name'], user['company'], user['isSent'], user['isActive'])

def edit_company(id, company):
    user = delete_user(id)
    user['company'] = company
    add_line(user['id'], user['name'], user['company'], user['isSent'], user['isActive'])

def edit_sent_status(id, isSent):
    user = delete_user(id)
    user['isSent'] = isSent
    add_line(user['id'], user['name'], user['company'], user['isSent'], user['isActive'])

def edit_active_status(id, isActive):
    user = delete_user(id)
    user['isActive'] = isActive
    add_line(user['id'], user['name'], user['company'], user['isSent'], user['isActive'])
