# 배경
Javascript에서의 DOM 처리 방식을 이용한 공격 기법
Clobbering은 소프트웨어 공학에서 의도적,비의도적으로 특정 메모리나 레지스터를 완전히 덮어쓰는 현상을 의미
DOM을 덮어쓴다는 의미

HTML 태그 중 id 속성으로 명시된 Object는 window object에서도 호출이 가능  이를 이용한 공격이 DOM Clobbering