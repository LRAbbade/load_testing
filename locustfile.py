from locust import HttpLocust, TaskSet, task
import json
import os

PARAMS = int(os.getenv("LOCUST_PARAMS", "1"))
print(f'Starting locust with {PARAMS} params')

# Pre-initialize request data
JWT_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI5NWRkNTliNy02NTUxLTRkOTUtYTAzZi1lZDRmNjZjZTlhNTkiLCJpc3MiOiI1YmUzLTNiOGQtOTVmZS1kZTEwLTM5NTEtMDg1YSIsImV4cCI6MTU1ODI2ODQ3Mn0.CkVC64YhDDDeJ2_qR9irU4MJqd8Na4jlyjPXjR7B_JA"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": JWT_TOKEN
}
PAYLOAD = json.dumps({f'data{i}': i for i in range(PARAMS)})

class UserBehavior(TaskSet):
    @task
    def post_data(self):
        self.client.post("/api/v1/message", data=PAYLOAD, headers=HEADERS)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior

    def __init__(self):
        print(f'Starting locust aimed at host: {self.host}')
        super(WebsiteUser, self).__init__()
