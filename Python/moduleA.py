__all__ = ['id', 'get_name']

id = '001'
name = 'Bob'

def get_id():
    print('Your id is', id)
    
def get_name():
    print('Your name is', name)
    
class Staff():
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        print('Your name is', self.name)