<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8" />
	<title>회원가입 폼</title>
</head>
<body>
	<form method="post" action="member_ok.php">
		<h1>회원가입</h1>
			<fieldset>
				<legend>입력사항</legend>
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

				<input type="submit" value="가입하기" />		
		</fieldset>
	</form>
</body>
</html>
