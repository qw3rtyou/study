# Shortcut
ctrl+p	파라미터 옵션,타입 확인
ctrl+shift+enter	자동완성함
ctrl+space	자동완성 추천 목록 보여줌
alt+insert	자동 generate(getter, setter, 생성자 등등을 자동 생성)
alt+enter	Quick Fix(리펙토링, 오류수정,코드수정 등등..)
shift+f6	이미 사용된 변수나 함수의 이름을 다같이 변경할 수 있음
ctrl+alt+v 	단순 변수로된 문장을 적당한 변수에 넣어줌
ctrl+alt+shift+t 	리펙토링 관련 단축키
ctrl+alt+m 	로직 함수로 분리
ctrl+shift+t 	테스트 클래스 자동 생성
shift+f10 		이전 실행조건으로 그대로 실행
ctrl+shift+t 	선택한 클래스 태스트 패키지에 태스트 코드 생성

soutv+tab	System.out.println("result = " + result);


# Static Import
자바에서 static import는 특정 클래스의 static 멤버(정적 멤버)를 직접적으로 사용할 수 있게 해주는 기능
import 문은 다른 패키지에 속한 클래스를 사용할 때 패키지명을 생략할 수 있게 해주는 역할
static import는 클래스의 static 멤버를 사용할 때 클래스 이름을 생략

아래의 코드를 다음과 같이 바꿀 수 있다.

	package hello.hellospring.repository;

	import hello.hellospring.domain.Member;
	import org.assertj.core.api.Assertions;
	import org.junit.jupiter.api.Test;

	class MemoryMemberRepositoryTest {
		MemoryMemberRepository repository = new MemoryMemberRepository();

		@Test
		public void saber(){
			Member member = new Member();
			member.setName("spring");

			repository.save(member);

			Member result = repository.findbyId(member.getId()).get();
			System.out.println("(result==member) = " + (result == member));
			Assertions.assertThat(member).isEqualTo(result);
			
		}
	}

	package hello.hellospring.repository;

	import hello.hellospring.domain.Member;
	import org.junit.jupiter.api.Test;

	import static org.assertj.core.api.Assertions.*;

	class MemoryMemberRepositoryTest {
		MemoryMemberRepository repository = new MemoryMemberRepository();

		@Test
		public void saber(){
			Member member = new Member();
			member.setName("spring");

			repository.save(member);

			Member result = repository.findbyId(member.getId()).get();
			System.out.println("(result==member) = " + (result == member));
			assertThat(member).isEqualTo(result);
			
		}
	}

단축키 alt+enter를 통해 자동으로 static import로 코드 수정이 가능하다.

