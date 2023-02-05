with open("data/generatedfile1",'w',encoding='UTF-8') as file:
    pass

with open("data/generatedfile2",'w',encoding='UTF-8') as file:
    pass

with open("data/generatedfile3",'w',encoding='UTF-8') as file:
    pass

import os

os.rename("data/generatedfile1","data/dummyfile")
os.remove("data/generatedfile2")