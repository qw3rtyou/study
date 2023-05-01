<?php
$conn= mysqli_connect('localhost', 'tmproot', 'rootword', 'db000');
$username = $_POST['name'];
$userpw = $_POST['pw'];
$title = $_POST['title'];
$content = $_POST['content'];
$maxfilesize = (int)$_POST['MAX_FILE_SIZE']; 
$mycount = count($_FILES['b_file']['name']);




$special_pattern = "/[`~@#$%^&*|\\\'\";:\/?^=^+_()<>]/";
if( preg_match($special_pattern, $username)|preg_match($special_pattern, $userpw)|preg_match($special_pattern, $content)|preg_match($special_pattern, $title)|preg_match($special_pattern, $maxfilesize) ){ 

        $msg = "특수문자 사용"; 
        
        echo("<script>alert('$msg');history.back();");  
        
        exit; 
        
}


for($i=0;$i<$mycount;$i++){
$filename = $_FILES['b_file']['name'][$i];

$ext = explode(".", strtolower($filename),2);

if($ext[1]==null){}
else if(($ext[1]=="txt")||($ext[1]=="png")||($ext[1]=="jpg")){	
	
} else{
	echo "<script>
    		alert('error..');
    		history.back();</script>"; 
	exit;
}	
}





if($mycount>5){ 
               echo "<script>
    		alert('파일은 5개까지 첨부할 수 있습니다.');
    		history.back();</script>";
		exit;              
}
echo "모두 ".$mycount."개의 파일을 넘겨받았습니다.<br>";
echo "-----------------------------------<br>";


for($i=0;$i<$mycount;$i++){     
	if($_FILES['b_file']['size'][$i] > $maxfilesize){ 
               echo "<script>
    		alert(($i+1)+'번째 파일이 허용 파일용량을 초과하였습니다.');
    		history.back();</script>";
		exit;              
	}
}

mysqli_query($conn, "insert into board(idx,name,pw,title,content,date,hit) values(0,'$username','$userpw','$title','$content',now(),0)"); 

$sql=mysqli_query($conn, "select max(idx) from board");
$sql2=mysqli_fetch_row($sql);
$board_num=(int)$sql2[0];
echo $board_num;

for($i=0;$i<$mycount;$i++){   
	$tmpfile =  $_FILES['b_file']['tmp_name'][$i];
	$filename = $_FILES['b_file']['name'][$i];
	echo $filename;
	$folder = "../../upload/".$filename;
	move_uploaded_file($tmpfile,$folder);
	mysqli_query($conn, "insert into file(idx, board_num, file) values(0,'$board_num','$filename')");
	echo $i;
}
//iconv('UTF-8', 'EUC-KR', $_FILES['b_file']['name'][$i])
?>
<script type="text/javascript">alert("글쓰기 완료되었습니다.");</script>
<meta http-equiv="refresh" content="0 url=board.php" />























