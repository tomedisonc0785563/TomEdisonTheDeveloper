This project is about the deployment of autoscaling webapplication using Amazon Elastic Beanstalk and caching in edge locations using Amazon CloudFront.

Steps

1. Created Dynamo DB table with email as primary key
2. Create EBS
3. You wil see 2 instances running
4. Access the domain website and see the app running
5. Error while trying to register
6. Finding errors logged
7. Fix error by adding permission to IAM role DynamoDB Access
8. Succesfully register an email
9. Create Cloudfront with allowed HHTP methods GET, HEAD, OPTIONS, PUT, POST, PATCH, DELETE , with cache policy : cachingoptimized and WAF enabled
https://d1w5t49ly6j1rt.cloudfront.net/
access through cloudfront

10. using public ip of any instance, connect to instance with key
ssh ec2-user@3.236.12.36 -i ssh-key.pem

11.  Installing and running “Stress” tool in GitBash
sudo amazon-linux-extras install epel -y
sudo yum install stress -y
stress -c 4

12. CPU reaches 100% utilization and health goes to warning mode. Auto increment of an instance and gets added to load balancer

13. remove stress

14. health checks becomes OK and intances auto decrement. 

