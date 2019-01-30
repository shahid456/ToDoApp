from User_Management_Model import User_Management_Model as Model
class User_Man(Model):

    def _init_(self):
        self.model=Model()
    def register(self,user,password):
        self.model.registeruser(user,password)
    def login(self):
        name=input("Enter User name")
        Pass=input("Enter User's Pass")
        return self.model.LoginUser(name,Pass)
    def deleteuser(self,username):
        password=input("Enter User Password")
        self.model.deleteuser(username,password)
    def listusers(self):
        self.model.listUsers()
    def userupdate(self,username,task):
        i=task.find('=')
        if i!=-1:
            command=task[0:i]
            content=task[i+1:len(task)]
        else:
            print('Incorrect Command')
        self.model.userUpdate(username,command,content)





