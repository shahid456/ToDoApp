from User_Management_Model import User_Management_Model
class User_Man(User_Management_Model):

    def __init__(self):
        super().__init__()
    def register(self,user,password):
        self.registeruser(user,password)
    def login(self):
        name=input("Enter User name")
        Pass=input("Enter User's Pass")
        return self.LoginUser(name,Pass)
    def deleteuser(self,username):
        password=input("Enter User Password")
        self.deleteuser(username,password)
    def listusers(self):
        self.listUsers()
    def userupdate(self,username,task):
        i=task.find('=')
        if i!=-1:
            command=task[0:i]
            content=task[i+1:len(task)]
        else:
            print('Incorrect Command')
        self.userUpdate(username,command,content)

if __name__ == '__main__':
    user=User_Man()
    user.register("shahid","yess")




