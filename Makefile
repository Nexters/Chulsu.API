install:
	pip install -r requirements.txt

mysql_install:
	sudo apt-get install python-mysqldb

test:
	curl -X POST http://127.0.0.1:3002/save -d "text=123&desc=asfasf&etc=123123"
