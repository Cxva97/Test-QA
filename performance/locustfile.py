import os
from locust import HttpUser, task, between
API_KEY = os.getenv("REQRES_API_KEY", "")

class ReqResUser(HttpUser):
    host = "https://reqres.in"
    wait_time = between(1, 3)

    def on_start(self):
        self.headers = {"x-api-key": API_KEY}

    @task(3)
    def list_users(self):
        self.client.get("/api/users?page=2", headers=self.headers, name="GET /api/users?page=2")

    @task(3)
    def get_single_user(self):
        self.client.get("/api/users/2", headers=self.headers, name="GET /api/users/2")

    @task(1)
    def create_user(self):
        payload = {"name": "Cesar Villacis", "job": "QA Automation Engineer"}
        self.client.post("/api/users", json=payload, headers=self.headers, name="POST /api/users")

    @task(1)
    def update_user(self):
        payload = {"name": "Cesar Villacis", "job": "Senior QA Automation Engineer"}
        self.client.put("/api/users/2", json=payload, headers=self.headers, name="PUT /api/users/2")

    @task(1)
    def delete_user(self):
        self.client.delete("/api/users/2", headers=self.headers, name="DELETE /api/users/2")