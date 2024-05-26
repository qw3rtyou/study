```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        * {
            font-family: 'Lucida Sans';
            text-align: center;
            position: relative;
            top: 50px;
        }

        body {
            background-color: rgb(61, 61, 61);
            /* 회색 */
        }

        .date {
            font-size: 45px;
            color: rgb(255, 255, 255);
            /* 흰색 */
        }

        .time {
            font-size: 100px;
            font-weight: bold;
            color: rgb(179, 21, 171);
            /*보라색 */
        }
    </style>
</head>

<body>

    <div id="time" class="time"></div>
    <div id="date" class="date"></div>

</body>

<script>
    // 변수를 선언합니다.
    let date = new Date();
    let hours = date.getHours();
    // 조건문
    if (hours < 12) {
        // 표현식 "hours < 12"가 참일 때 실행합니다.
        alert('오전입니다.');
    }
    if (12 <= hours) {
        // 표현식 "12 <= hours"가 참일 때 실행합니다.
        alert('오후입니다.');
    }

    function setClock() {
        var dateInfo = new Date();
        var hour = modifyNumber(dateInfo.getHours());
        var min = modifyNumber(dateInfo.getMinutes());
        var sec = modifyNumber(dateInfo.getSeconds());
        var year = dateInfo.getFullYear();
        var month = dateInfo.getMonth() + 1; //monthIndex를 반환해주기 때문에 1을 더해준다.
        var date = dateInfo.getDate();
        document.getElementById("time").innerHTML = hour + ":" + min + ":" + sec;
        document.getElementById("date").innerHTML = year + "년 " + month + "월 " + date + "일";
    }
    function modifyNumber(time) {
        if (parseInt(time) < 10) {
            return "0" + time;
        }
        else
            return time;
    }
    window.onload = function () {
        setClock();
        setInterval(setClock, 1000); //1초마다 setClock 함수 실행
    }
</script>

</html>
```