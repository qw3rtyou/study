<!doctype html>
<head>
    <meta charset="UTF-8">
    <title>게시판</title>
</head>
<body>
    <?php
		$conn= mysqli_connect('localhost', 'tmproot', 'rootword', 'db000');
		$bno = $_GET['bno']; 
		$rno = $_GET['rno']; 
		
		echo $bno;
		echo $rno;	
	?>

			<div>
				<form action="reply_delete_ok.php" method="post">
					<input type="hidden" name="rno" value="<?php echo $rno; ?>" /><input type="hidden" name="bno" value="<?php echo $bno; ?>">
			 		<p>비밀번호<input type="password" name="pw" /> <input type="submit" value="확인"></p>
				 </form>
			</div>
</body>
</html>
