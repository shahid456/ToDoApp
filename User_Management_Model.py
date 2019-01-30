from DatabaseManagement import DatabaseManagement as data
import json
class User_Management_Model:
    def _init_(self):
        pass
    def registeruser(self,usr,password):
        f=data.read()
        if f[usr] in f:
            print("Already a User")
        else:
            d={'userid':' ','username':usr,'password':password}
            f.update(d)
            data.write(f)
