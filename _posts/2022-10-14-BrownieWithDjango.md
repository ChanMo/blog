---
layout: post
title: 在Django中使用Brownie
excerpt: how to integrate eth-brownie with django
tags: eth brownie django python web3 vyper solidity nft
---

## 什么是Django和Brownie

Django是基于Python的一个流行的web开发框架

Brownie是基于Python的一个以太坊合约开发框架

本文将介绍如何在Django中集成Brownie, 搭建基础的web3项目

## Create New Django Project

    $ mkdir demo_site
    $ virtualenv env
    $ source env/bin/activate
    $ pip install Django
    $ django-admin startproject server

## Create Brownie Directory

    $ cd server
    $ pip install eth-brownie
    $ brownie bake token

## Config Network

### Use Default Development Network

    $ ganache-cli -d

### Use Infura

    $ export WEB3_INFURA_PROJECT_ID=YourProjectID

## Import Account

If use development network, can skip this step.

    $ brownie accounts new master # master is your account nickname

## Update Django

open file `server/__init__.py`

``` {.python}
from brownie import project, network

p = project.load('token', name='MyProject')
p.load_config()

# if use live network
network.connect('rinkeby')
network.accounts.load('master', 'ACCOUNT_PASSWORD') # account nickname and password
```

## Run Django

    $ ./manage.py runserver

## Integrate With Contract

You do do this by \`./manage.py shell\` or in python file

``` {.python}
from brownie import project, accounts

erc721 = project.MyProject.ERC721 # Your contract name
tx = erc721.deploy({'from':accounts[0]})
```

## Use Celery

Because blockchain has high network delay, you should use celery do some
longtime tasks

## Use Next.js

Next.js is a very popular js framework.

## Use Docker

``` {.yaml}
version: '3'

services:
  client:
    build: ./client
    ports:
      - "3000:3000" 

  server: &base
    build: ./server
    volumes:
      - ./server:/app
      - ./server/static:/app/static
      - ./server/media:/app/media
      - ./.brownie:/root/.brownie
      - ./.solcx/:/root/.solcx
      - ./.vvm:/root/.vvm
    depends_on:
      - rabbitmq
      - postgres
    ports:
      - "8000:8000"
    environment:
      DJANGO_SETTINGS_MODULE: "server.production"
      WEB3_INFURA_PROJECT_ID: ""
    command: gunicorn server.wsgi:application -w 2 -b :8000

  postgres:
    image: postgres
    volumes:
      - ./db:/var/lib/postgresql/data
    environment:
      POSTGRES_PASSWORD: ""

  celery:
    <<: *base
    depends_on:
      - rabbitmq
    ports: []
    command: celery -A server worker -l INFO

  celery_beat:
    <<: *base
    depends_on:
      - rabbitmq
    ports: []
    command: celery -A server beat -l INFO


  rabbitmq:
    image: rabbitmq
    restart: always
    volumes:
      - ./mq:/var/lib/rabbitmq

```
