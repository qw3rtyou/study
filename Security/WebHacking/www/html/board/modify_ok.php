<?php
$bno = $_GET['idx'];
$username = $_POST['name'];
$userpw = $_POST['pw'];
$title = $_POST['title'];
$content = $_POST['content'];
$conn= mysqli_connect('localhost', 'tmproot', 'rootword', 'db000');
$sql = mysqli_query($conn, "update board set name='$username',pw='$userpw',title='$title',content='$content' where idx='$bno'"); ?>

<script type="text/javascript">alert("수정되었습니다."); </script>
<meta http-equiv="refresh" content="0 url=read.php?idx=<?php echo $bno; ?>">
