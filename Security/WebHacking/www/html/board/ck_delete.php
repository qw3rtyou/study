<!DOCTYPE html>
<html lang="kr">
  <head>
    <meta charset="utf-8">
    <title>php로그인</title>
    <?php   
    	$bno = $_GET['idx'];
	$conn= mysqli_connect('localhost', 'tmproot', 'rootword', 'db000');
    	$sql = mysqli_query($conn, "select * from board where idx='$bno';");
	$board = $sql->fetch_array();
    
      if(isset($_POST['userpw'])){
        $userid=$board['name'];
        $userpw=$_POST['userpw'];
        $sql="SELECT * FROM board where name='$userid'&&pw='$userpw'";
        if($result=mysqli_fetch_array(mysqli_query($conn,$sql))){
          echo "<script>location.href='delete.php?idx=$bno'</script>";
        }
        else{	
          echo "다시 확인해주세요";
        }
        
      }
    ?>
  </head>
  
  <body>
	<form method="post">
			<fieldset>
				<legend>비밀번호를 입력해주세요</legend>
					<table>
						<tr>
							<td>비밀번호</td>
							<td><input type="password" size="35" name="userpw" placeholder="비밀번호"></td>
						</tr>
					</table>

				<input type="submit" value="로그인" />			
			</fieldset>
	</form>
</body>

</html>
