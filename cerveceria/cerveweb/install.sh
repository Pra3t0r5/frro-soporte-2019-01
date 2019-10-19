#!/bin/bash
if [ "$EUID" -ne 0 ]
then echo "Please run as root"
    exit
else (
        apt install python3
        apt install python3-pip
        source ../bin/activate
        pip3 install flask flask-sqlalchemy sqlalchemy wtforms flask-wtf mysql-connector-python flask-login
        mysql -e "create user 'cerveweb'@'localhost' identified by 'beerjesus'; grant all privileges on *.* to 'cerveweb'@'localhost'; flush privileges; create database cerveweb;"
        wget https://trello-attachments.s3.amazonaws.com/5d952a113b1ad84a91fb61a1/5d952f57131cda03c5780e94/077abeb91cd4bb2c1f997baa5d0680e2/cerveweb_dump_20191018.sql
        # wget https://trello-attachments.s3.amazonaws.com/5d952a113b1ad84a91fb61a1/5d952f57131cda03c5780e94/90e189b4b088da4f16c02171412836a3/cerveweb_dump_20191005.sql
        mysql -ucerveweb -pbeerjesus cerveweb < cerveweb_dump_20191018.sql
        echo "Instalacion completa"
    )
fi

exit