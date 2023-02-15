
# create user
CREATE USER 'vis'@'117.99.103.84' IDENTIFIED BY 'vn@admin'; # use localhost and not ip

# grant all permissions
GRANT ALL ON *.* to vis@'117.99.103.84' IDENTIFIED BY 'vn@admin'; 


flush privileges;



mysql> SELECT User, Host, plugin FROM mysql.user;
+------------------+-----------+-----------------------+
| User             | Host      | plugin                |
+------------------+-----------+-----------------------+
| root             | localhost | auth_socket           |
| mysql.session    | localhost | mysql_native_password |
| mysql.sys        | localhost | mysql_native_password |
| debian-sys-maint | localhost | mysql_native_password |
| Vnurt123         | localhost | mysql_native_password |
| jainsangh        | localhost | mysql_native_password |
| xr1ew6fi_jainsan | localhost | mysql_native_password |
| vishvajeet       | localhost | mysql_native_password |
| vis              | localhost | mysql_native_password |	# local host and plugin should be same
+------------------+-----------+-----------------------+

# export database from sql
mysqldump -u vis -p jainsangh --single-transaction > jainsangh.sql

# copy file from server
scp -P 22 practice@31.220.55.70:/home/practice/jainsangh.sql /home/vnurture/test/