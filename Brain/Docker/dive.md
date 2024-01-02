Docker 이미지를 자세히 분석하게 만들어주는 툴
https://github.com/wagoodman/dive
# 설치
일반 계정으로 설치가 잘 안 됨
```sh
export DIVE_VERSION=$(curl -sL "https://api.github.com/repos/wagoodman/dive/releases/latest" | grep '"tag_name":' | sed -E 's/.*"v([^"]+)".*/\1/')
curl -OL https://github.com/wagoodman/dive/releases/download/v${DIVE_VERSION}/dive_${DIVE_VERSION}_linux_amd64.deb
sudo apt install ./dive_${DIVE_VERSION}_linux_amd64.deb
```

# 사용법
```sh
root@foo1-virtual-machine:~/tmp# dive dreamhackofficial/blue-whale:1
Image Source: docker://dreamhackofficial/blue-whale:1
Fetching image... (this can take a while for large images)
Analyzing image...
Building cache...
```