from User_Management_Model import User_Management_Model as Model
class User_Man(Model):

    def _init_(self):
        self.model=Model
    def register(self,user,password):
        Model.registeruser(user,password)


