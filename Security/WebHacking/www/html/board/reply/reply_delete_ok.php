<?php
$conn= mysqli_connect('localhost', 'tmproot', 'rootword', 'db000');
$rno = $_POST['rno']; 
$sql = mysqli_query($conn, "select * from reply where idx='".$rno."'");
$reply = $sql->fetch_array();

$bno = $_POST['bno'];
$sql2 = mysqli_query($conn, "select * from board where idx='".$bno."'");
$board = $sql2->fetch_array();

$pwk = $_POST['pw'];
$bpw = $reply['pw'];

echo 1;
echo $pwk;
echo 1;
echo $bpw;
echo 1;

if($pwk==$bpw) 
	{
		$sql = mysqli_query($conn, "delete from reply where idx='".$rno."'"); ?>
	<script type="text/javascript">alert('댓글이 삭제되었습니다.'); location.replace("../read.php?idx=<?php echo $board["idx"]; ?>");</script>
	<?php
	  $sql = mysqli_query($conn,"ALTER TABLE reply AUTO_INCREMENT=1");
          $sql = mysqli_query($conn,"SET @COUNT = 0");
          $sql = mysqli_query($conn,"UPDATE reply SET reply.idx = @COUNT:=@COUNT+1");
        ?>
	<?php 
	}else{ ?>
		<script type="text/javascript">alert('비밀번호가 틀립니다');history.back();</script>
	<?php } ?>
