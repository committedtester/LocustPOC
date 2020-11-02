import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    host = "https://swapi.dev/api/"
    
    wait_time = between(1, 2)

    @task
    def index_page(self):
        self.client.get("/people/1/")
        self.client.get("/planets/3/")
        self.client.get("starships/9/")

