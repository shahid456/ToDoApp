from DatabaseManagement import DatabaseManagement
import json
import utilities
class User_Management_Model:
    def _init_(self):
        self.data=DatabaseManagement('user.json')
        self.f=self.data.read()
    def registeruser(self,usr,password):
        check=0
        for x in range(len(self.f)):
            if self.f[x]['username']==usr:
                check=1
                break
        if check==0:
            d={'userid':utilities.generate_unique_id(),'username':usr,'password':password}
            self.f.append(d)
            self.data.write(self.f)
    def LoginUser(self,usr,pasword):
        check = -1
        for x in range(len(self.f)):
            if self.f[x]['username'] == usr:
                if self.f[x]['password']==pasword:
                    check = x
                    break
                else:
                    print('Incorrect Password, Access Denied')
                    return ""
        if  check!=-1:
            return self.f[x]['userid']
        return -1
    def deleteuser(self,usrname,password):
        for x in range(len(self.f)):
            if self.f[x]['username'] == usrname:
                if self.f[x]['password']==password:
                    print('User Deleted')
                    self.f.pop(x)
                    self.data.write(self.f)
                    break
                else:
                    print('Incorrect Password')
                    break
    def listUsers(self):
        for x in range(len(self.f)):
            print(self.f[x]['username'])
    def userUpdate(self,user,command,content):
        for x in range(len(self.f)):
            if self.f[x]['username']==user:
                l=self.f[x].keys()
                if command in l:
                    self.f[x][command]=content
                    return
                else:
                    print('No such Command')
                    return
        print('Invalid User')



