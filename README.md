创建数据库
```
use mysql;
create user 'bluelog'@'%' identified by 'A34kji;0B';
create database my_bluelog;
grant all privileges on my_bluelog.* to "bluelog"@'%';
```


启动应用
```
poetry install
poetry shell
flask forge
flask run
```