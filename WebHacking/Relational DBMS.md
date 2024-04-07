
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
