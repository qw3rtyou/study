# Concept
- Http Parameter Pollution
- 중복된 파라미터를 웹 어플리케이션이 처리하는 방식의 차이를 이용한 공격 방법
- 다른 취약점으로 연결하기 위한 트릭

# Exploit
-  파라미터를 복수로 보내는 경우
```
POST /save_profile HTTP/1.1

account=15442&account=1110&name=aaa
```

|Technology|Parsing Result|outcome (par1=)|
|---|---|---|
|ASP.NET/IIS|All occurrences|a,b|
|ASP/IIS|All occurrences|a,b|
|PHP/Apache|Last occurrence|b|
|PHP/Zues|Last occurrence|b|
|JSP,Servlet/Tomcat|First occurrence|a|
|Perl CGI/Apache|First occurrence|a|
|Python Flask|First occurrence|a|
|Python Django|Last occurrence|b|
|Nodejs|All occurrences|a,b|
|Golang net/http - `r.URL.Query().Get("param")`|First occurrence|a|
|Golang net/http - `r.URL.Query()["param"]`|All occurrences|a,b|
|IBM Lotus Domino|First occurrence|a|
|IBM HTTP Server|First occurrence|a|
|Perl CGI/Apache|First occurrence|a|
|mod_wsgi (Python)/Apache|First occurrence|a|
|Python/Zope|All occurences in array|[‘a’,’b’]|



- Bypass Request (Array)
```
POST /save_profile HTTP/1.1

account[]=15442&account[]=1110&name=aaa
```