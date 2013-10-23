Ubuntu下的MySQL配置
==================
#####默认配置文件路径
<pre>/etc/mysql/my.cnf</pre>

#####更改用户（root）密码
<pre>#命令行方式
mysqladmin -u USER -p password NEWPASSWORD
</pre>
<pre>#或者， 以root身份进入mysql
mysql -u root -p;
use mysql;
UPDATE user SET password=PASSWORD('NEWPASSWORD') WHERE user='root';
FLUSH PRIVILEGES; # 刷新系统权限表</pre>

#####创建用户
<pre>insert into mysql.user(Host,User,Password) values("localhost","username",password("pwd"));</pre>

#####授予权限
<pre>grant all privileges on db.* to user@localhost; #授予db的所有表的所有权限给user@localhost
grant select,update,insert on db.test to user@localhost; #授予db.test表的select,update和insert权限给user@localhost
FLUSH PRIVILEGES; # 刷新系统权限表</pre>

#####删除用户
<pre>DELETE FROM user WHERE User=user and Host="localhost";</pre>

#####创建数据库（设定字符集）
<pre>GBK: create database test2 DEFAULT CHARACTER SET gbk COLLATE gbk_chinese_ci;
UTF8: CREATE DATABASE test2 DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;</pre>

#####删除数据库
<pre>drop database dbname;</pre>

#####导出数据
<pre>mysqldump [OPTIONS] database [tables] > /tmp/dump.sql
[OPTIONS]
-P或--port          要连接的服务器端口,如果MySQL的端口不是3306,就要用到这个参数 
-d或--no-data       没有详细数据,仅仅导出数据的结构 
--add-drop-database 在创建数据库时,先drop掉已经存在的同名数据库[一般跟在-d参数后] 
--add-drop-table    在创建表时,先drop掉已经存在的同名表[一般跟在-d参数后]
[OPTIONS] <br/>
mysqldump -h localhost -u root -p --add-drop-database --add-drop-table test>/home/chuzj/daochu.sql #导出数据库test表结构和数据
mysqldump -h localhost -u root -p -d --add-drop-database --add-drop-table test>/home/chuzj/daochu.sql #导出数据库test表结构</pre>

#####导入数据
<pre>mysql -h localhost -u root -p test < /home/chuzj/daochu.sql –default-character-set=utf8; #导入数据并设置字符集 </pre>
