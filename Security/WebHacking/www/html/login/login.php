<!DOCTYPE html>
<html lang="kr">
  <head>
    <meta charset="utf-8">
    <title>php로그인</title>
    <?php   
      if(isset($_POST['userid'])&&isset($_POST['userpw'])){
        $userid=$_POST['userid'];
        $userpw=$_POST['userpw'];
        $conn= mysqli_connect('localhost', 'tmproot', 'rootword', 'db000');
        $sql="SELECT * FROM login where login_id='$userid'&&login_pw='$userpw'";
        if($result=mysqli_fetch_array(mysqli_query($conn,$sql))){
          echo "</br>".$result['created'];
          echo "</br>로그인 성공";
          echo "<script>location.href='../board/board.php'</script>";
        }
        else{	
          echo "다시 확인해주세요";
        }
        
      }
    ?>
  </head>
  
  <body>
	<form method="post">
		<h1>로그인</h1>
			<fieldset>
				<legend>환영합니다</legend>
					<table>
						<tr>
							<td>아이디</td>
							<td><input type="text" size="35" name="userid" placeholder="아이디"></td>
						</tr>
						<tr>
							<td>비밀번호</td>
							<td><input type="password" size="35" name="userpw" placeholder="비밀번호"></td>
						</tr>
					</table>

				<input type="submit" value="로그인" onclick=location.href='member_ok.php'></input>
				<button type="button" onclick="location.href='membership.php' ">회원가입</button>
			
		</fieldset>
	</form>
</body>

</html>
