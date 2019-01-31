from User_Management_Model import User_Management_Model


class User_Man(User_Management_Model):
    def __init__(self):
        super().__init__()

    def register(self, user, password):
        self.registeruser(user, password)

    def login(self):
        name = input("Enter User name: ")
        password = input("Enter User's Pass: ")
        return self.LoginUser(name, password)

    def deleteuser(self, username):

        self.deleteUser(username)

    def listusers(self):
        self.listUsers()

    def userupdate(self, username, command, content):
        self.userUpdate(username, command, content)
