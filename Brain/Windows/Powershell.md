# Powershell
- Microsoft가 개발한 강력한 명령줄 쉘 및 스크립팅 언어
- 주로 Windows 환경에서 사용
- PowerShell은 텍스트가 아닌 객체를 출력합니다. 이는 데이터를 처리할 때 더 많은 유연성과 강력한 기능을 제공
- 명령어의 결과를 직접 조작하고 다른 명령어로 파이프할 수 있음
- .NET Framework와 긴밀하게 통합되어 있어, .NET 객체와 클래스를 직접 사용할 수 있음
- `cmdlet`라고 불리는 PowerShell의 명령어를 사용

# cmdlet
- 일관된 '동사-명사' 형식
- Get-Command, Set-Item 등

```gpt
Get-Command: 사용할 수 있는 모든 cmdlet, 함수, 스크립트 파일을 나열합니다.
Get-Help: cmdlet의 도움말 정보를 제공합니다. 예를 들어 Get-Help Get-Item은 Get-Item cmdlet에 대한 정보를 보여줍니다.
Get-Item: 파일 시스템의 위치에서 항목을 가져옵니다.
Set-Item: 항목의 값을 변경합니다.
Get-Process: 현재 실행 중인 프로세스 목록을 보여줍니다.
Stop-Process: 프로세스를 중단합니다 (예: Stop-Process -Name notepad).
Copy-Item: 파일이나 폴더를 복사합니다.
Get-ChildItem: 지정된 위치의 디렉토리 내용을 나열합니다 (Unix의 ls와 비슷).
Select-Object: 객체의 특정 속성을 선택합니다.
```


- 루트에서 특정 단어를 포함한 디렉토리 찾기
```powershell
Get-ChildItem -Path C:\ -Recurse -ErrorAction SilentlyContinue -Force | Where-Object { $_.Name -eq 'Desktop' }
```

- 환경변수 출력
```powershell
echo $HOME
```

- 특정 경로 있는지 확인
```powershell
Test-Path $env:USERPROFILE\Desktop
```

- `rm -rf`
```powershell
Remove-Item -Path ".\project-9-" -Recurse -Force
```


# netsh
- 주변 네트워크 장비에 쉽게 접근하고 제어하는 역할인 듯 공부 필