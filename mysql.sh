sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE djangodb;"
mysql -uroot -e "GRANT ALL PRIVILEGES  ON *.* TO 'root'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"
