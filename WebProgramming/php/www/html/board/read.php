<!doctype html>
<head>
<meta charset="UTF-8">
<title>게시판</title>
</head>
<body>
	<?php
		$conn= mysqli_connect('localhost', 'tmproot', 'rootword', 'db000');
		$bno = $_GET['idx'];
		$hit = mysqli_fetch_array(mysqli_query($conn, "select * from board where idx ='$bno'"));
		$hit = $hit['hit'] + 1;
		$fet = mysqli_query($conn, "update board set hit = '$hit' where idx = '$bno'");
		$sql = mysqli_query($conn, "select * from board where idx='$bno'");
		$board = $sql->fetch_array();
		
		//$file= mysqli_fetch_array(mysqli_query($conn, "select * from file where board_num='$bno'"));
	?>
<div id="board_read">
	<h2><?php echo $board['title']; ?></h2>
		<div id="user_info">
			<?php echo $board['name']; ?> <?php echo $board['date']; ?> 조회:<?php echo $board['hit']; ?>
				<div id="bo_line"></div>
			</div>
			<div id="bo_content">
				<?php echo nl2br("$board[content]"); ?>
			</div>
			<?php
			$sql2=mysqli_query($conn, "select * from file where board_num='$bno'");
			while($file= mysqli_fetch_array($sql2)) {
			?>
			파일 : <a href="/var/www/upload/<?php echo $file['file'];?>" download><?php echo $file['file']; ?></a>	
			<?php			
			}	
			?>
			
			
	<div id="bo_ser">
		<ul>
			<li><a href="board.php">[목록으로]</a></li>
			<li><a href="ck_modify.php?idx=<?php echo $board['idx']; ?>">[수정]</a></li>
			<li><a href="ck_delete.php?idx=<?php echo $board['idx']; ?>">[삭제]</a></li>
		</ul>
	</div>
</div>
<div class="reply_view">
	<h3>댓글목록</h3>
		<?php
			$sql3 = mysqli_query($conn, "select * from reply where con_num='$bno' order by idx desc");
			while($reply = $sql3->fetch_array()){ 
		?>
			<div><b><?php echo $reply['name'];?></b></div>
			<div><?php echo nl2br("$reply[content]"); ?></div>
			<div><?php echo $reply['date']; ?></div>
			<div>
				<a href="reply/reply_modify.php?bno=<?php echo $reply['con_num']; ?>&rno=<?php echo $reply['idx']; ?>">수정</a>
				<a href="reply/reply_delete.php?bno=<?php echo $reply['con_num']; ?>&rno=<?php echo $reply['idx']; ?>">삭제</a>
			</div>
			
		</div>
	<?php } ?>

	<!--- 댓글 입력 폼 -->
	<div>
		<form action="reply/reply_ok.php?idx=<?php echo $bno; ?>" method="post">
			<input type="text" name="dat_user" id="dat_user" class="dat_user" size="15" placeholder="아이디">
			<input type="password" name="dat_pw" id="dat_pw" class="dat_pw" size="15" placeholder="비밀번호">
			<div style="margin-top:10px; ">
				<textarea name="content" class="reply_content" id="re_content" ></textarea>
				<button id="rep_bt" class="re_bt">댓글 달기</button>
			</div>
		</form>
	</div>
</div><!--- 댓글 불러오기 끝 -->
<div id="foot_box"></div>
</div>
</body>
</html>
