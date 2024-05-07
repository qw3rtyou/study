
# 기본 우회
<table border="1">
    <tr>
        <th></th>
        <th>true</th>
        <th>false</th>
        <th>1</th>
        <th>0</th>
        <th>-1</th>
        <th>"1"</th>
        <th>"0"</th>
        <th>"-1"</th>
        <th>null</th>
        <th>[]</th>
        <th>"php"</th>
        <th>""</th>
    </tr>
    <tr>
        <td>true</td>
        <td>true</td>
        <td>false</td>
        <td>true</td>
        <td>false</td>
        <td>true</td>
        <td>true</td>
        <td>false</td>
        <td>true</td>
        <td>false</td>
        <td>false</td>
        <td>true</td>
        <td>false</td>
    </tr>
    <tr>
        <td>false</td>
        <td>false</td>
        <td>true</td>
        <td>false</td>
        <td>true</td>
        <td>false</td>
        <td>false</td>
        <td>true</td>
        <td>false</td>
        <td>true</td>
        <td>true</td>
        <td>false</td>
        <td>true</td>
    </tr>
    <tr>
        <td>1</td>
        <td>true</td>
        <td>false</td>
        <td>true</td>
        <td>false</td>
        <td>false</td>
        <td>true</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
    </tr>
    <tr>
        <td>0</td>
        <td>false</td>
        <td>true</td>
        <td>false</td>
        <td>true</td>
        <td>false</td>
        <td>false</td>
        <td>true</td>
        <td>false</td>
        <td>true</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
    </tr>
    <tr>
        <td>-1</td>
        <td>true</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
        <td>true</td>
        <td>false</td>
        <td>false</td>
        <td>true</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
    </tr>
    <tr>
        <td>"1"</td>
        <td>true</td>
        <td>false</td>
        <td>true</td>
        <td>false</td>
        <td>false</td>
        <td>true</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
    </tr>
    <tr>
        <td>"0"</td>
        <td>false</td>
        <td>true</td>
        <td>false</td>
        <td>true</td>
        <td>false</td>
        <td>false</td>
        <td>true</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
    </tr>
    <tr>
        <td>"-1"</td>
        <td>true</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
        <td>true</td>
        <td>false</td>
        <td>false</td>
        <td>true</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
    </tr>
    <tr>
        <td>null</td>
        <td>false</td>
        <td>true</td>
        <td>false</td>
        <td>true</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
        <td>true</td>
        <td>true</td>
        <td>false</td>
        <td>true</td>
    </tr>
    <tr>
        <td>[]</td>
        <td>false</td>
        <td>true</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
        <td>true</td>
        <td>true</td>
        <td>false</td>
        <td>false</td>
    </tr>
    <tr>
        <td>"php"</td>
        <td>true</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
        <td>true</td>
        <td>false</td>
    </tr>
    <tr>
        <td>""</td>
        <td>false</td>
        <td>true</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
        <td>false</td>
        <td>true</td>
        <td>false</td>
        <td>false</td>
        <td>true</td>
    </tr>
</table>
# strcmp
- 문자열과 배열을 비교하면 0을 반환함을 이용함
```php
!strcmp($cred['pw'], $GLOBALS['admin_pw'])
```

- `"pw":[]`로 strcmp를 우회할 수 있음
# switch문
- [공식문서](https://www.php.net/manual/en/control-structures.switch.php)를 확인해 보면 switch 문에서 느슨한 비교를 하는 것을 알 수 있음
- 이를 이용하여 username에 true를 넣어 우회를 할 수 있음