# Lab 3
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- Linus Lei
- Way Zheng

## Lab Question Answers

Answer for Question 1: 

RESTful APIs are scalable because they use a stateless architecture which means that no client context is stored on the server between requests. This means that any incoming request from any client can be handled by any server, making it easier to distribute requests and scale out the system horizontally. Additionally, RESTful APIs use standard HTTP methods, making them easier to cache and leading to improved performance at scale.

reference from https://aws.amazon.com/what-is/restful-api/.
Systems that implement REST APIs can scale efficiently because REST optimizes client-server interactions. Statelessness removes server load because the server does not have to retain past client request information. Well-managed caching partially or completely eliminates some client-server interactions. All these features support scalability without causing communication bottlenecks that reduce performance.


Answer for Question 2:

 The definition of "resources" in the context of RESTful APIs refers to the distinct pieces of information or data that can be accessed or manipulated through the API. The specific resources provided by a mail server would depend on the specific implementation and functionality of that mail server.

reference from https://aws.amazon.com/what-is/restful-api/.
Resources are the information that different applications provide to their clients. Resources can be images, videos, text, numbers, or any type of data. The machine that gives the resource to the client is also called the server. Organizations use APIs to share resources and provide web services while maintaining security, control, and authentication. In addition, APIs help them to determine which clients get access to specific internal resources.



Answer for Question 3:  


...