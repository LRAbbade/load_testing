from locust import HttpLocust, TaskSet, task
import json
import os
import gevent

PARAMS = int(os.getenv("LOCUST_PARAMS", "1"))
print(f'Starting locust with {PARAMS} params')

# Pre-initialize request data
JWT_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIwZGFhMjU1Ny04NThlLTQ2MWYtYjQwZC1hMDkyM2ExNGFhNTgiLCJpc3MiOiI1YmU0LTlkYTAtY2E3Yy03ZDBmLWQ3ZjAtNTMwZiIsImV4cCI6MTU1OTI1MzkyMH0.CZybRCZycd0Y4LysOzPFoDNtoXFseYgMzzrxFNjcJ4w"
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
    min_wait = 1
    max_wait = 1
    task_set = UserBehavior

    def __init__(self):
        print(f'Starting locust aimed at host: {self.host}')
        super(WebsiteUser, self).__init__()
