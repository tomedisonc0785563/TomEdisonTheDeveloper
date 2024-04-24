provider "aws" {
    region = "us-east-1"
}

resource "aws_s3_bucket" "tcb-bucket" {
  bucket = "startup-tech-storage-tome"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}

resource "aws_instance" "tcb_ec2"{
  ami = "ami-04e5276ebb8451442"
  instance_type = "t2.micro"
  key_name = "tcb-ssh-key"
  tags = {
    Name = "WebServer"
    Environment = "Dev"
  }
}

resource "aws_db_instance" "tcb_db" {
  allocated_storage    = 10
  db_name              = "mydb"
  engine               = "mysql"
  engine_version       = "8.0.35"
  instance_class       = "db.t3.micro"
  username             = "admin"
  password             = "admin123456!"
  parameter_group_name = "default.mysql8.0"
  skip_final_snapshot  = true
}
