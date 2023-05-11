<?php
    $conn= mysqli_connect('localhost', 'tmproot', 'rootword', 'db000');
    $bno = $_GET['idx'];
    $userpw = $_POST['dat_pw'];
    
    if($bno && $_POST['dat_user'] && $userpw && $_POST['content']){
        $sql = mysqli_query($conn, "insert into reply(con_num,name,pw,content) values('".$bno."','".$_POST['dat_user']."','".$userpw."','".$_POST['content']."')");
        echo "<script>alert('댓글이 작성되었습니다.'); 
        location.href='../read.php?idx=$bno';</script>";
    }else{
        echo "<script>alert('댓글 작성에 실패했습니다.'); 
        history.back();</script>";
    }
	
?>
