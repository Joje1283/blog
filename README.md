# Simple blog
## 개발 환경
Python 3.7.7

## 실행 방법
```
$ pip install -r requirements.txt
$ python managy.py runserver
```

## 기능 요약
* 포스트 CRUD 및 페이징
* 태그 기반 그룹핑
* 제목, 내용 검색
* Contact 작성

## secret.py 작성하기
* settings.py에서는 django secret key와 email관련 설정을 secret.py에서 가져와서 실행한다.
* google 이메일 

### 작성 목록
```
# secret.py
secrets = {
  "BLOG_SECRET_KEY": "",
  "EMAIL_BACKEND": 'django.core.mail.backends.smtp.EmailBackend',
}
```
