##Elastic Beanstalk

Elastic Beanstalk allows developers to upload their code easily. It is a GUI for AWS.
Amazon created this service, so developers that doesn't know AWS can deploy code on the AWS.

Architecture:
	
	The application is the high level strucutre in beanstalk(what that means?). Either your entire application, is one EB application, or each logical component of your application, can be a EB application or a EB enviroment application
	Applications can have multiple envirments, and versions. Environments are either single instance or scalable. Enviromnents either web server environments or worker environments
	Application versions are unique packages which represent version of apps. An applications is uploaded to Elastic Beanstalk as a applications bundle - .zip, each application have many version

Applications Supported:
- Apache Tomcat for Java applications
- Apache HTTP Server for PHP applications
- Apache HTTP Server for Python applications
- Nginx or Apache HTTP Server for Node.js applications
- Passengers or Puma for Ruby applications
- Microsoft IIS 7.5, 8.0, and 8.5 for .NET applications
- Java SE
- Docker
- Go

Key architecture Components:

- 

Exam Tips:

- You can have multiple versions of your applications
- Your applications can be split in to tiers (Web Tier/Application Tier/Database Tier)
- You can update your application
- You can update your configuration
- Updates can bd 1 instance at a time, a % of instance or an immutable update
- You pay for the resources that you use, but Elastic Beanstalk is FREE
- If elastic beanstalk creates your RDS database, then it will delete it when you delete your aplication. If no then the RDS instance stays
