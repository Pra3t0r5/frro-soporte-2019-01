#!/bin/bash
if [ "$EUID" -ne 0 ]
then echo "Please run as root"
    exit
else (
        apt install python3
        apt install python3-pip
        source bin/activate
        pip3 install flask flask-sqlalchemy sqlalchemy wtforms flask-wtf mysql-connector-python flask-login
        mysql -e "create user 'cerveweb'@'localhost' identified by 'beerjesus'; grant all privileges on *.* to 'cerveweb'@'localhost'; flush privileges; drop database if exists cerveweb; create database cerveweb;"
        wget https://trello-attachments.s3.amazonaws.com/5d952a113b1ad84a91fb61a1/5d952f57131cda03c5780e94/ad4f57509c4a8ee9a5f225c5d8683ae0/cerveweb.sql
        # wget https://trello-attachments.s3.amazonaws.com/5d952a113b1ad84a91fb61a1/5d952f57131cda03c5780e94/077abeb91cd4bb2c1f997baa5d0680e2/cerveweb_dump_20191018.sql
        # wget https://trello-attachments.s3.amazonaws.com/5d952a113b1ad84a91fb61a1/5d952f57131cda03c5780e94/90e189b4b088da4f16c02171412836a3/cerveweb_dump_20191005.sql
        mysql -ucerveweb -pbeerjesus cerveweb < cerveweb.sql
        #rm cerveweb.sql
        echo "Instalacion completa"

    )
fi

exit