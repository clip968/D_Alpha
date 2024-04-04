## CSRF

- 임의 사용자의 쿠키를 사용할 수 있다면, 이는 곧 임의 이용자의 권한으로 웹 서비스의 기능을 사용할 수 있는 것이다.
- CSRF는 임의 사용자의 권한으로 임의 주소에 HTTP 요청을 보낼 수 있는 취약점이다. 
- Ex) 이용자의 계정으로 임의 금액을 송금해 금전적인 이득을 취하거나 비밀번호를 변경해 계정을 탈취하고, 관리자 계정을 공격해 공지사항 작성 등으로 혼란을 야기할 수 있다.
```python
# 이용자가 /sendmoney에 접속했을때 아래와 같은 송금 기능을 웹 서비스가 실행함.
@app.route('/sendmoney')
def sendmoney(name): # 송금을 받는 사람과 금액을 입력받음. 
	to_user = request.args.get('to') 
	amount = int(request.args.get('amount')) # 송금 기능 실행 후, 결과 반환 
	
	success_status = send_money(to_user, amount) # 송금이 성공했을 때, 
	if success_status: # 성공 메시지 출력 
		return "Send success." # 송금이 실패했을 때, 
		
	else: # 실패 메시지 출력 
		return "Send fail."
```

## CSRF 동작

- CSRF 공격에 성공하기 위해서는 공격자가 작성한 악성 스크립트를 이용자가 실행해야 한다. 
- 이는 공격자가 이용자에게 메일을 보내거나 게시판에 글을 작성해 이용자가 이를 조회하도록 유도하는 방법이 있다.
- 여기서 보내는 악성 스크립트는 HTTP 요청을 보내는 코드이다.
- CSRF 공격 스크립트는 HTML 또는 Javascript를 통해 작성할 수 있다. 
- ---
**figure 3**
```HTML
<img src='http://bank.dreamhack.io/sendmoney?to=dreamhack&amount=1337' width=0px height=0px>
```

**CSRF 실습 코드**
```html
<img src="/sendmoney?to=dreamhack&amount=1337">

<img src=1 onerror="fetch('/sendmoney?to=dreamhack&amount=1337');">

<link rel="stylesheet" href="/sendmoney?to=dreamhack&amount=1337">
```

## XSS와 CSRF의 차이

### 공통점

- 두 개의 취약점은 모두 클라이언트를 대상으로 하는 공격이며, 이용자가 악성 스크립트가 포함된 페이지에 접속하도록 유도해야 한다.

### 차이점

- 두 개의 취약점은 공격에 있어 서로 다른 목적을 가진다. XSS는 인증 정보인 세션 및 쿠키 탈취를 목적으로 하는 공격이며 공격할 사이트의 오리진에서 스크립트를 실행시킨다.
- CSRF는 이용자가 임의 페이지에 HTTP 요청을 보내는 것을 목적으로 하는 공격이다. 또한, 공격자는 악성 스크립트가 포함된 페이지에 접근한 이용자의 권한으로 웹 서비스의 임의 기능을 실행할 수 있다.
- 