<?php

	$userid = $_POST['userid'];
	$userpw = $_POST['userpw'];
	
 	$conn= mysqli_connect('localhost', 'tmproot', 'rootword', 'db000');
	mysqli_query($conn, "insert into login (id, login_id, login_pw,created) values ('0','$userid','$userpw',now())");

?>
<meta charset="utf-8" />
<script type="text/javascript">alert('회원가입이 완료되었습니다.');</script>
<meta http-equiv="refresh" content="0 url=/login/login.php">


