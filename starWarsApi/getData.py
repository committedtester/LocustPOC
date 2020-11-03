import time
from locust import HttpUser, task, between

class starWarsApi_getData(HttpUser):
    host = "https://swapi.dev/api/"
    
    wait_time = between(1, 2)

    @task(3)
    def GetPlanetFromPerson(self):
        getPeopleResponse = self.client.get("people/1/")
        assert getPeopleResponse.status_code == 200, "Unexpected response code: " + getPeopleResponse.status_code
        getPeopleResponseJson = getPeopleResponse.json()
        homeworldUrl = getPeopleResponseJson['homeworld']

        getHomeworldResponse = self.client.get(homeworldUrl)
        assert getHomeworldResponse.status_code == 200, "Unexpected response code: " + getHomeworldResponse.status_code
        getHomeworldResponseJson = getHomeworldResponse.json()
        assert getHomeworldResponseJson["name"] == "Tatooine"
        pass

    @task
    # pylint: disable=function-redefined
    def GetDeathStar(self):
        getStarshipsResponse = self.client.get("starships/9/")
        assert getStarshipsResponse.status_code == 200, "Unexpected response code: " + getStarshipsResponse.status_code
        getStarshipResponseJson = getStarshipsResponse.json()
        assert getStarshipResponseJson["name"] == "Death Star"
        pass   
        

