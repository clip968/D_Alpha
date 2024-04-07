- 공격자는 데이터베이스 파일 탈취, SQL Injection 등과 같은 공격으로 정보를 확보하고 악용하여 금전적인 이익을 얻을 수 있다. 따라서 임의 정보 소유자 이외에 이용자에게 정보가 노출되지 않도록 해야 한다.
- SQL을 들어가기 앞서 **Injection**이란 무엇인지 알고 있어야 한다.
- 인젝션은 주입이라는 의미를 가진 영단어로, 인젝션 공격은 이용자의 입력값이 애플리케이션의 처리 과정에서 구조나 문법적인 데이터로 해석되어 발생하는 취약점을 의미한다.
![[Pasted image 20240407203419.png]]
- 위 그림은 드림이가 공장에 생산을 요청하는 그림으로, 위의 그림에서 드림이가 부품 생성 중에 임의의 요청을 보내 제품의 색깔을 지정한다. 그러나 아래 그림에서 드림이가 올바르지 않은 요청을 보내 공장 운영자가 의도하지 않은 행위를 일으키는 것을 확인할 수 있다. 
- 이와 같이 악의적인 입력 값을 주입해, 의도하지 않은 행위를 일으키는 것을 **인젝션**이라고 부른다.
- Ex) 만약에 드림이가 로그인을 하기 위해 "아이디가 DreamHack이고 패스워드가 Password인 계정으로 로그인 하겠습니다." 요청을 보내면 DBMS는 이에 해당하는 정보를 찾고 로그인 성공 여부를 결정한다.
- 그러나 만약 "아이디가 admin인 계정으로 로그인하겠습니다." 요청을 보내면 DBMS는 비밀번호 일치 여부를 검사하지 않고 아이디가 admin인 계정을 조회한 후 이용자에게 로그인 결과를 반환한다.
---
- SQL은 DBMS에 데이터를 질의하는 언어이다. 웹 서비스는 이용자의 입력을 sql 구문에 포함해 요청하는 경우가 있다.
- ex) 로그인 시에 id/pw를 포함하거나 게시글의 제목과 내용을 sql 구문에 포함한다
```sql
/*아래 쿼리 질의는 다음과 같은 의미를 가지고 있습니다.
- SELECT: 조회 명령어
- *: 테이블의 모든 컬럼 조회
- FROM accounts: accounts 테이블 에서 데이터를 조회할 것이라고 지정
- WHERE user_id='dreamhack' and user_pw='password': 
user_id 컬럼이 dreamhack이고, user_pw 컬럼이 password인 데이터로 범위 지정즉, 
이를 해석하면 DBMS에 저장된 accounts 테이블에서 이용자의 아이디가 dreamhack이고, 
비밀번호가 password인 데이터를 조회*/

SELECT * FROM accounts WHERE user_id='dreamhack' and user_pw='password'
```
- 윗 코드는 로그인 할 때 애플리케이션이 DBMS에 질의하는 예시 쿼리이다. 보면 이용자가 입력한 "dreamhack"과 "password"문자열을 삽입하는 행위를 sql injection이라고 부른다.

```sql
/*아래 쿼리 질의는 다음과 같은 의미를 가지고 있습니다.
- SELECT: 조회 명령어
- *: 테이블의 모든 컬럼 조회
- FROM accounts: accounts 테이블 에서 데이터를 조회할 것이라고 지정
- WHERE user_id='admin': user_id 컬럼이 admin인 데이터로 범위 지정즉, 
- 이를 해석하면 DBMS에 저장된 accounts 테이블에서 이용자의 아이디가 admin인 데이터를 조회*/

SELECT * FROM accounts WHERE user_id='admin'
```
- 윗 코드는 SQL Injection으로 조작한 쿼리문의 예시이다. 살펴보면 user_pw 조건문이 사라진 것을 확인할 수 있다.

