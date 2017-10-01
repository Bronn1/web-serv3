sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE djangodb;"
mysql -uroot -e "CREATE USER 'dj@localhost' IDENTIFIED BY 'qweasz';"
mysql -uroot -e "GRANT ALL ON djangodb.* TO 'dj@localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"
