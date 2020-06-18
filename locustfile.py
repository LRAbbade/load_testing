from locust import task
from locust import HttpUser
# from locust.contrib.fasthttp import FastHttpUser
import json
import os


class WebsiteUser(HttpUser):
    min_wait = 1
    max_wait = 1
    
    @task
    def index(self):
        self.client.get('/')
