# PHP Deserialization
- PHP에서는 데이터 관리를 효율적으로 하거나 전송하기 쉽게하기 위해서 직렬화라는 기능이 존재
- 하지만 변조된 객체를 역직렬화했을 때 자동으로 실행되는 `Magic Method` 때문에 악의적인 기능을 실행시킬 수 있음
-  PHP의 serialize에 의해 발생할 수 있는 `Object Injection` 취약점
- 데이터 변조나 코드인젝션까지 유연하게 사용 가능

---
# Magic Method
- 특정 PHP events에 대응해 자동실행하여 기능을 수행하는 함수
- `__`로 시작
- 생성자나 소멸자의 기능을 하여 객체가 생성되고 소멸될 때 실행되는 `__construct`, `__destruct` 도 이에 해당

---
# Example
```php
class Example
{
   private $hook;

   function __construct()
   {
      // some PHP code...
   }

   function __wakeup()
   {
      if (isset($this->hook)) eval($this->hook);
   }
}

// some PHP code...

$user_data = unserialize($_COOKIE['data']);

// some PHP code...
```
- `hook` 변수의 값이 `__wakeup()`이 실행될 때 코드로서 실행됨
- `__wakeup()`은 `unserialize()`가 실행될 때 trigger되는 magic method

- 조작된 `hook`이 포함되어있는 오브젝트를 인젝션 한다면 `unserialize`할 때 `__wakeup()`이 실행되면서 조작한 코드가 실행될 것

```php
class Example
{
   private $hook;

   function __construct()
   {
      // some PHP code...
   }

   function __wakeup()
   {
      if (isset($this->hook)) eval($this->hook);
   }
}

$Example = new Example();
$Example->hook = "echo 'exploit';";
$data = serialize($Example);
var_dump($data);
```


[[Dreamhack - Secret Document Storage]]
[[Dreamhack - 45c6]]