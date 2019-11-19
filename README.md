타 프로젝트에서 발생 시키는 HTTP Request 를 확인하기 위한 간단한 Flask 기반 프로젝트.

### 실행

```
$ python run.py
```

### Example
테스트를 위한 호출 예.

```
$ curl -XPOST -H "Content-Type: application/json" 'http://127.0.0.1:5000/?param=1' -d '{"body-key":2}'
```

위와 같은 호출에 따른 결과
```
=== Header ===
Host: 127.0.0.1:5000
User-Agent: curl/7.60.0
Accept: */*
Content-Type: application/json
Content-Length: 12


=== Parameter ===
b'param=1'
=== Body ===
{'body-key': 2}
```