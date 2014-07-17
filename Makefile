install:
	pip install -r requirements.txt

mysql_install:
	sudo apt-get install python-mysqldb

test:
	curl -X POST http://127.0.0.1:3002/save -d "text=테스트&desc=asfasf&etc=123123"

daemon: install
	python hello.py --daemon

run: install
	python hello.py

kill:
	ps -ef | grep python | awk '{print $2}' | xargs kill -9