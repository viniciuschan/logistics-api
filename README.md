
[![Build Status](https://travis-ci.com/viniciuschan/logistics-api.svg?token=qNsGtqKDkkLPeR8hiGRz&branch=master)](https://travis-ci.com/viniciuschan/logistics-api)




Logistics API
=============
API Rest to deal with a logistics network and best routes
Author: Vinícius Chan

Before getting started, we must install some dependencies:

| Dependency | Download Link |
| ------ | ------ |
| Docker | https://www.docker.com/ |
| Docker-Compose | https://docs.docker.com/compose/ |
| Django Rest Framework 3.9 | http://www.django-rest-framework.org |
| Python3 | https://www.python.org/download/releases/3.0/ |
| Django 2.1.8 | https://docs.djangoproject.com/en/2.1/releases/2.1/ |
| NetworkX | https://networkx.github.io/documentation/stable/install.html |

#Getting Started
I've prepared an easy way to run this project locally:

1. Clone this repository:
```
$ git@github.com:viniciuschan/logistics-api.git
```
2. In the working directory, you can enjoy a bunch of Makefile useful commands:
```
$ make run
```
3. As soon as you get your containers ON, you must migrate the data structure:
```
$ make migrate
```
4. I've prepared a fixture file to load initial items for test purposes:
```
$ make loaddata
```
5. Finally, you can check test cases by running the following command:
```
$ make test
```

### About Tech

### Docker
About Docker

### Docker-Compose
About Docker-Compose

### Travis
About Travis

### Postgres
About Postgres

### Django
About Django

### Django Rest Framework
About Rest Framework

### NetworkX
About NetworkX
