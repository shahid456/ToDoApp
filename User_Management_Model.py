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
        if check==0:
            d={'userid':utilities.generate_unique_id(),'username':usr,'password':password}
            self.f.append(d)
            self.data.write(self.f)
    def LoginUser(self,usr,name):
        check = -1
        for x in range(len(self.f)):
            if self.f[x]['username'] == usr:
                check = x
        if  check!=-1:
            return self.f[x]['userid']
        return -1
    def deleteuser(self,usrname):
        check = 0
        for x in range(len(self.f)):
            if self.f[x]['username'] == usrname:
                self.f.pop(x)
                break



