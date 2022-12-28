<?php	
	$bno = $_GET['idx'];
	$conn= mysqli_connect('localhost', 'tmproot', 'rootword', 'db000');
	$sql = mysqli_query($conn, "delete from board where idx='$bno';");
	$sql2 = mysqli_query($conn, "delete from reply where con_num='$bno';");
?>
<script type="text/javascript">alert("삭제되었습니다.");</script>
<meta http-equiv="refresh" content="0 url=board.php" />
