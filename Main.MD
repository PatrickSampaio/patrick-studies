##Lambda

Lamba is the invetion of the servless. Lambda can let the Developer only care about code. Amazon does all the heavy lifting in managing the servers.

- Event-driven compute
- API

What Languages

- NodeJS
- Python
- C#
- Java

How is Lambda Priced

If two user access an Lambda Function in the same time. It will be used two Lambda Instances instead of one

- Number of requests. 0.20$ per 1 million requests
- Duration, cost variafies according to the quantity of memory that you use. Your function can't last more then 5 minutes
- NO SERVERS!
- Continuous Scalling
- Very cheap

Lambda scales out(not up) automatically
Lambda functions are independents, 1 event = 1 function
Lambda is serverless
Know what services are serveless
Lambda functions can trigger other lambda functions, 1 event can =  x functions if functions trigger other functions
Architectures can get extremely complicated, you can user AWS X-ray when necessary to debug
Lambda can do things globally, you can use Lambda functions to back up S3 Buckets
Know your triggers
