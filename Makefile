build:
	docker-compose build
run:
	docker-compose up
db:
	mysql -u tarantula -h 172.17.0.2 -ptarantula tarantula
runprod:	
	nohup docker run -p 5000:5000 -e "APP_ENV=prod" pabloncio/proxy-resource-server:latest > /var/log/proxy-resource-server.log &