---

---
# Keyword
- JWT


---
# 분석
- 해당 코드에서 `ES256`로 `JWT`를 사용하는 것을 확인할 수 있음
```java
@GetMapping("/")
public String index(@RequestParam(required = false) String j, Model model) {
	String sub = UNKNOWN;
	String jwt_guest = Jwts.builder().setSubject(GUEST).signWith(secretKey).compact();

	try {
		Jwt jwt = Jwts.parser().setSigningKey(secretKey).parse(j);
		Claims claims = (Claims) jwt.getBody();
		if (claims.getSubject().equals(ADMIN)) {
			sub = ADMIN;
		} else if (claims.getSubject().equals(GUEST)) {
			sub = GUEST;
		}
	} catch (Exception e) {
//            e.printStackTrace();
	}

	model.addAttribute("jwt", jwt_guest);
	model.addAttribute("sub", sub);
	if (sub.equals(ADMIN)) model.addAttribute("flag", FLAG);

	return "index";
}
```


https://jwt.io/ 와 같은 토큰 분석사이트에서 분석해보면 `sub`가 `"guest"`로 되어 있는데, 
이전 문제 처럼 `admin`으로 수정 후 `None Algorithm` 공격을 진행해도  `setSigningKey`때문에 공격 진행 불가
좀 더 찾아보니 자바 15~18 버전에서 `jwt-ES256` 사용 시 발생하는 이슈가 있었음
시그니처 부분을 `MAYCAQACAQA`로 변조하여 flag를 얻


![[Pasted image 20240326132119.png|400]]

![[Pasted image 20240326132630.png|400]]