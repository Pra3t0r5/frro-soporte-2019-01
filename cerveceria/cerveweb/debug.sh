#!/bin/bash
echo "Sale birra bien fria!"
source ../bin/activate
export FLASK_APP=cerveweb
export FLASK_DEBUG=1
flask run
