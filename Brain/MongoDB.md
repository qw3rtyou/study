
MongoDB는 JSON 형태인 도큐먼트(Document)를 저장하며
스키마를 따로 정의하지 않아 각 콜렉션(Collection)에 대한 정의가 필요하지 않음
JSON 형식으로 쿼리를 작성할 수 있음
_id 필드가 Primary Key 역할을 함
다음은 같은 역할을 함

```sql
SELECT * FROM inventory WHERE status = "A" and qty < 30;

db.inventory.find( { $and: [ { status: "A" }, { qty: { $lt: 30 } } ] } )
```

# 연산자

### Comparison

	$eq
	지정된 값과 같은 값을 찾음 (equal)

	$in
	배열 안의 값들과 일치하는 값을 찾음 (in)

	$ne
	지정된 값과 같지 않은 값을 찾음 (not equal)

	$nin
	배열 안의 값들과 일치하지 않는 값을 찾음 (not in)

### Logical

	$and
	논리적 AND, 각각의 쿼리를 모두 만족하는 문서가 반환

	$not
	쿼리 식의 효과를 반전. 쿼리 식과 일치하지 않는 문서를 반환

	$nor
	논리적 NOR, 각각의 쿼리를 모두 만족하지 않는 문서가 반환

	$or
	논리적 OR, 각각의 쿼리 중 하나 이상 만족하는 문서가 반환

### Element
	$exists
	지정된 필드가 있는 문서를 찾음

	$type
	지정된 필드가 지정된 유형인 문서를 선택

### Evaluation
	$expr
	쿼리 언어 내에서 집계 식을 사용할 수 있음

	$regex
	지정된 정규식과 일치하는 문서를 선택

	$text
	지정된 텍스트를 검색합니다.


# RDBMS와 MongoDB 구문을 서로 비교하기

### SELECT

```sql
SELECT * FROM account;
db.account.find()

SELECT * FROM account WHERE user_id="admin";
db.account.find(
{user_id: "admin"}
)

SELECT user_idx FROM account WHERE user_id="admin";
db.account.find(
{ user_id: "admin" },
{ user_idx:1, _id:0 }
)
```
### INSERT

```sql
INSERT INTO account(
user_id,
user_pw,
) VALUES ("guest", "guest");
db.account.insert({
user_id: "guest",
user_pw: "guest"
})
```
### DELETE

```sql
DELETE FROM account;
db.account.remove()
DELETE FROM account WHERE user_id="guest";
db.account.remove( {user_id: "guest"} )
```
### UPDATE

```sql
UPDATE account SET user_id="guest2" WHERE user_idx=2;
db.account.update(
{user_idx: 2},
{ $set: { user_id: "guest2" } }
)
```