sudo apt-get install -y mysql-server
sudo ufw enable
sudo ufw allow mysql
sudo systemctl start mysql
sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
#update ip to 0.0.0.0
sudo systemctl restart mysql
sudo mysql -u root
sudo systemctl restart mysql
