This is real world project to showcase the migration of on-premises resources and application to AWS cloud with minimal changes that is rehosting method also known as lift and shift method.

Steps of migration process:
1. Plan: Sizing, prerequisites
2. Implementation: Deployment, best practices
3. Go Live: Validation, final migration
4. post go-live: Stability, ongoing support


Project: On premises migration to AWS cloud steps

1. Created subnets Public, and 2 private subnets because RDS has a prerequisite(atleast 2 subnet)
2. Created internet gateway and attach our vpc
3. Created route table for internet gateway to route to public internet.
4. Launch EC2 instance, 
	size t2.micro and Ubuntu Server 22.04 OS as required
	create new key pair download and save
	setup network seetings 
		with our vpc, 
		under public subnet and enable auto assign public IP, 
		Firewall (security groups): app01-sg [ inbound rules: Ports: 22 and 8080 ]
		
5. Create RDS MySQl
	version 8.0.
	DB instance identifier awsuse1db01
	credentials username and password( admin, admin123456)
	instance class (db.t3.micro)
	storage General Purpose SSD gp2
	VPC set to our vpc
	note:(never expose your DB to whole public internet)
	VPC security group: create new> sec-group-db-01 with us-east-1a AZ
	
6.  Use the EC2 public IP in git bash and the private key 
	ssh ubuntu@54.210.171.175 -i ssh-key.pem
	sudo apt-get update
	
	
7. run git commands to install resources 


	sudo apt update
	sudo apt install python3-dev -y
	sudo apt install python3-pip -y

	sudo apt install build-essential libssl-dev libffi-dev -y
	sudo apt install libmysqlclient-dev -y
	sudo apt install unzip -y
	sudo apt install libpq-dev libxml2-dev libxslt1-dev libldap2-dev -y
	sudo apt install libsasl2-dev libffi-dev -y

	pip install Flask==2.3.3

	export PATH=$PATH:/home/ubuntu/.local/bin/

	pip3 install wtforms
	sudo apt install pkg-config
	pip3 install flask_mysqldb
	pip3 install passlib


	### **MySql Client Installation:**


	sudo apt-get install mysql-client -y


8. Edit IB rules of VPC
	IB rule of sec-group-db-01, reset source to 0.0.0.0/0 just to make it easy but don't provide this in production environment.

9. In GIT BASH
	download application documents
	
	wget https://tcb-bootcamps.s3.amazonaws.com/bootcamp-aws/en/wikiapp-en.zip
	wget https://tcb-bootcamps.s3.amazonaws.com/bootcamp-aws/en/module3/dump-en.sql
	
10. MySQL CMD to allow us to connect remotly to MySQl in AWS
	mysql -h <rds_endpoint> -P 3306 -u admin -p
	(
		RD End point
		awsuse1db01.c3u8gcoo6cvm.us-east-1.rds.amazonaws.com
	)
	run sql queries
		create database wikidb;
		use wikidb;
		source dump-en.sql
		show tables;
		
	- REATE USER wiki@'%' IDENTIFIED BY 'admin123456';
	- GRANT ALL PRIVILEGES ON wikidb.* TO wiki@'%';
	- FLUSH PRIVILEGES;
	- EXIT;
			

	

11. In git bash modify app to connect with AWS application
	unzip wikiapp-en.zip
	
	cd wikiapp/
	vi wiki.py
	host ='awsuse1db01.c3u8gcoo6cvm.us-east-1.rds.amazonaws.com'
	user = 'wiki'
	password = 'admin123456'
	
	
12. run app
	python3 wiki.py
	access the application using the public IP of EC2 instance and port number 8080 we provided.
  example: http://54.210.171.175:8080/
