import uuid
class user_id_gen:
    def __init__(self):
        pass
    def uid_gen(self):
        self.uid=uuid.uuid4()
        return self.uid

# u=user_id_gen()
# id=u.uid_gen()
# print(id)
