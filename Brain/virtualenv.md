# 현재 설정된 파이썬 버전
global 3.9
Security/Pwnable/pwnable_env 3.6

# pip 커맨드
pip install --upgrade pip	pip 최신버전 업그레이드
pip install some_package	패키지 다운
pip install some_package==x.y.z		패키지 특정버전으로 다운
pip list			다운로드된 패키지 확인
pip uninstall some_package			패키지 삭제

# virtualenv 커맨드
pip install virtualenv
virtualenv --python=usr/bin/python경로 가상환경이름		가상환경 사용하고 싶다 
source activate경로		가상환경 내부의 버전으로 파이썬 사용하고 싶다 
deactivate			가상환경 글로벌 버전으로 변경하고 싶다 
pip freeze > requirements.txt			가상환경 버전공유하고 싶다 
pip install -r ./requirements.txt		가상환경 공유받고 싶다 

# alternative(파이썬 버전 변경)
update-alternatives --config python			등록된 파이썬 버전 확인
update-alternatives --install [symbolic link path] python [real path] number\
파이썬 실행파일 등록
ex) update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1


# conda 사용법
conda create -n 가상환경_이름 python=파이썬_버전	가상환경 생성

conda activate 가상환경_이름	가상환경 활성화
conda deactivate	가상환경 비활성