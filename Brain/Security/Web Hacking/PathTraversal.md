# Concept
- `Path Traversal`이랑 `Directory Traversal`은 서로 비슷함
- `..`, `/` 두 개의 구분자를 이용해 제한된 위치를 벗어나 시스템 내부 파일과 디렉토리에 접근함
- `../../../etc/passwd`와 같이 `Relative Path`도 가능하지만, `/etc/passwd`와 같이 `Absolute Path`도 가능할 수도 있음([[RPO(RPC)]])


# Null Byte Injection
- 다양한 상황에서 확장자를 체크하는 경우가 많은데, 이를 Null Byte를 이용해 문자열을 truncate 시켜 공격의 다양성을 넓힐 수 있음

```
exploit.txt%00.php
```


# Path Traversal with `.../...//` 
- 과거에는 정규표현식 엔징 상 `../`으로 인식하는 경우가 있다고 함
- 요즘은 잘 안통하는 모양


# Direct Request
- PHP와 같은 언어에서는 페이지 이름으로 라우팅이 되는데, 이를 이용해 강제로 인증되지 않은 URL, 스크립트, 파일등을 참조할 수 있음



# Example1
- 아래와 같은 어플리케이션이 있을 때, `Path Traversal`이 가능함
```perl
my $dataPath = "/users/cwe/profiles";  
my $username = param("user");  
my $profilePath = $dataPath . "/" . $username;  
  
open(my $fh, "<", $profilePath) || ExitError("profile read error: $profilePath");  
print "<ul>\n";  
while (<$fh>) {

print "<li>$_</li>\n";

}  
print "</ul>\n";
```

사용자의 이름에 대한 파라미터로 `../../../etc/passwd` 로 넘기면 `/etc/passwd`가 읽어짐

여기서 한번 더 응용하면 공격자가 없는 페이지를 지정하면, 브라우저는 오류 페이지를 보여주게 되는데, 적절한 Neutralization을 하지 않는다면, 이를 이용해 XSS를 사용할 수 있음([CWE-79](!https://cwe.mitre.org/data/definitions/79.html))



