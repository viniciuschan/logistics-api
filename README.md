
[![Build Status](https://travis-ci.com/viniciuschan/logistics-api.svg?token=qNsGtqKDkkLPeR8hiGRz&branch=master)](https://travis-ci.com/viniciuschan/logistics-api)




Logistics API
=============
##### API Rest to deal with a logistics network and best routes
###### Author: Vinícius Chan


#### Before getting started, we must install some dependencies:

| Dependency | Download Link |
| ------ | ------ |
| Docker | https://www.docker.com/ |
| Docker-Compose | https://docs.docker.com/compose/ |
| Django Rest Framework 3.9 | http://www.django-rest-framework.org |
| Python3 | https://www.python.org/downloads/release/python-368/ |
| Django 2.1.8 | https://docs.djangoproject.com/en/2.1/releases/2.1/ |
| NetworkX | https://networkx.github.io/documentation/stable/install.html |


# Getting Started
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


=============


# About project: How it works
## Manipulating logistics networks
#### POST
Endpoint: **http://localhost:80001/v1/logistics/**
Body contract:
```
{
    "name": "sp",
    "path_data": [
        {
            "source": "A",
            "destination": "B",
            "distance": 10
        },
        {
            "source": "B",
            "destination": "D",
            "distance": 15
        }
    ]
}
```

#### LIST
Endpoint: **http://localhost:80001/v1/logistics/**
Response:
```
[
    {
        "id": 1,
        "name": "sp",
        "path_data": [
            {
                "source": "A",
                "destination": "B",
                "distance": 10
            },
            {
                "source": "B",
                "destination": "D",
                "distance": 15
            }
        ]
    },
    {
        "id": 2,
        "name": "mg",
        "path_data": [
            {
                "source": "X",
                "destination": "Y",
                "distance": 50
            }
        ]
    }
]
```

#### GET
Endpoint: **http://localhost:80001/v1/logistics/1/**
Response:
```
{
    "id": 1,
    "name": "sp",
    "path_data": [
        {
            "source": "A",
            "destination": "B",
            "distance": 10
        },
        {
            "source":"B",
            "destination":"D",
            "distance":15
        }
    ]
    "status_code": 200
}
```

## Consult best route through logistics networks
#### GET
Endpoint: **http://localhost:8000/v1/logistics/check-best-way/?name=sp&source=A&destination=D&autonomy=10&fuel_price=2.5**
Response content:
```
{
    "shortest_path": [
        "A",
        "B",
        "D"
    ],
    "best_cost": 6.25
}
```


=============


# About Tech

### Docker
I like to prepare my environment before start projects. It's helpful to avoid any S.O. dependency problem. And it's very useful to create containers with Docker + Docker-Compose to work with local environment.

### Docker-Compose
Docker + Docker compose is my favorite combination to work with isolated local environment. Makefile can also be very helpful during project development. It allows me to create a lot of alias to access and manipulate my containers.

### Travis
This is the continuous integration delivery tool that I have more affinity.
I strongly believe that tests were made to help us during the project development.
Because of that, it is very important to let test statuses available. It also creates a sense of urgency for all involved in the project. If tests are not passing, software health is at risk.

### Postgres
I have never worked with postgres. It was my first time and I pretty liked it.
My motivation with this database was because I would like to try it's [JSON Type field](https://www.postgresql.org/docs/10/datatype-json.html).
I had a good lesson working in this project. It was very helpful to me. =)

### Django
Well, it's my favorite python web framework. I've been working with Django since 2017, December. It brings us a lot of helpful tools and allows us to deliver projects and Rest API's very quickly with it's built-in modules.

### Django Rest Framework
I'm most used to work with Django Restless framework. But for sure I prefer DRF.
This is another framework which I insist on using whenever it's possible. Django + Django Rest Framework is a very powerful tool to bring productivity to the project. Also that, I am not a fan of reinventing the wheel. If there is a tool that works well, why not use it?


### NetworkX
This library literally saved my ass. rsrs
I almost did not have to worry about the meaning of graph theory and it's complexities.
It was another very good lesson to me in this project.
Again, if there is a tool that works fine, why not use it?

### Trello
I organized my workflow using Trello.
It is a good open source tool to deal with work flow.
I also know Asana and Jira, but Trello is my favorite, it's simple and works fine for small projects.


=============
