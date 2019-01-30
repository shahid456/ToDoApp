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
        pass



