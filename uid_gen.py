import uuid
class Userid:

    def __init__(self):
        self.uid=0
        

    def uid_gen(self):
        
        self.uid=uuid.uuid4()
        return self.uid
u=Userid()
id=u.uid_gen()
print(id)
