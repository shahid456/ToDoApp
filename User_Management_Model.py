from DatabaseManagement import DatabaseManagement
import json
import utilities


class User_Management_Model(DatabaseManagement):
    def __init__(self):
        DatabaseManagement.__init__(self, 'test.json')
        self.f = self.read()

    def registeruser(self, usr, password):
        for x in range(len(self.f)):
            if self.f[x]['username'] == usr:
                print('Username Taken')
                return
        d = {'userid': utilities.generate_unique_id(), 'username': usr, 'password': password}
        self.f.append(d)
        self.write(self.f)

    def LoginUser(self, usr, pasword):
        check = -1
        for x in range(len(self.f)):
            if self.f[x]['username'] == usr:
                if self.f[x]['password'] == pasword:
                    check = x
                    print('User Logged In')
                    break
                else:
                    return -1
        if check != -1:
            return self.f[check]['userid']
        return -1

    def deleteUser(self, usrname):
        for x in range(len(self.f)):
            if self.f[x]['username'] == usrname:
                password = input("Enter User Password: ")
                if self.f[x]['password'] == password:
                    print('User Deleted')
                    self.f.pop(x)
                    self.write(self.f)
                    return
                else:
                    print('Incorrect Password')
                    return
        print('Username not found')


    def listUsers(self):
        for x in range(len(self.f)):
            print(self.f[x]['username'])

    def userUpdate(self, user, command, content):
        for x in range(len(self.f)):
            if self.f[x]['username'] == user:
                l = self.f[x].keys()
                if command in l:
                    pas = input('Enter User Password: ')
                    if pas==self.f[x]['password']:
                        self.f[x][command] = content
                        self.write(self.f)
                        print('Property Updated')
                        return
                    else:
                        print('Incorrect Password')
                        return
                else:
                    print('Property does not exist')
                    return
        print('Invalid User')



