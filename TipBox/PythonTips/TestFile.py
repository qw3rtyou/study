class User:
    count=0

    def __init__(self,name,email,pw):
        self.name=name
        self.email=email
        self._pw=pw

    def auth(self, input):
        return self._pw==input

    @property
    def pw(self):
        return self._pw

    @pw.setter
    def pw(self,value):
        self._pw=value
        
Tom=User('tom','hammer@asdf.com','secret')

print(Tom.pw)

Tom.pw='I feel lucky'

print(Tom.pw)