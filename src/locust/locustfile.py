from locust import HttpUser ,task,between
import random
import string

class QuickStartUser(HttpUser):
    wait_time = between(1,2)
    
    
    
    def on_start(self):
        """ Create user and login with JWT before running tasks """ 
        self.username = self.generate_username() 
        self.password = "password123"
    
    def random_username(self):
        return "user_" + ''.join(random.choices(string.ascii_lowercase, k=5))

    def random_password(self):
        return "password123"

    @task(2)
    def register(self):
        username = self.random_username()
        password = self.random_password()

        self.client.post(
            "/register",
            json={
                "username": username,
                "password": password
            }
        )

    @task(3)
    def login(self):
        username = self.random_username()
        password = self.random_password()

        # register first
        self.client.post(
            "/register",
            json={
                "username": username,
                "password": password
            }
        )

        # login
        self.client.post(
            "/login",
            json={
                "username": username,
                "password": password
            }
        )

    @task(5)
    def login_jwt(self):
        username = self.random_username()
        password = self.random_password()

        # register first
        self.client.post(
            "/register",
            json={
                "username": username,
                "password": password
            }
        )

        # jwt login
        response = self.client.post(
            "/login/jwt",
            json={
                "username": username,
                "password": password
            }
        )

        if response.status_code == 200:
            data = response.json()
            refresh_token = data.get("refresh token")

            if refresh_token:
                self.client.post(
                    "/refresh_token",
                    json={
                        "token": refresh_token
                    }
                )

    @task(1)
    def send_test_email(self):
        self.client.post("/send-test-email")
        

    
    def generate_task_title(self):
        return "task_" + ''.join(
            random.choices(string.ascii_lowercase, k=5)
        )

    @task(5)
    def create_task(self):

        response = self.client.post(
            "/task/create",
            headers=self.headers,
            json={
                "title": self.generate_task_title(),
                "description": "locust performance testing",
                "is_complated": False
            }
        )

        if response.status_code == 200:
            task = response.json()
            self.task_id = task.get("id")

    @task(3)
    def get_all_tasks(self):

        self.client.get(
            "/tasks/?limit=10&offset=0",
            headers=self.headers
        )

    @task(2)
    def task_detail(self):

        if hasattr(self, "task_id"):

            self.client.get(
                f"/task/detail/{self.task_id}",
                headers=self.headers
            )

    @task(2)
    def update_task(self):

        if hasattr(self, "task_id"):

            self.client.put(
                f"/task/{self.task_id}",
                headers=self.headers,
                json={
                    "title": "updated task",
                    "description": "updated by locust",
                    "is_complated": True
                }
            )

    @task(1)
    def delete_task(self):

        if hasattr(self, "task_id"):

            self.client.delete(
                f"/delete/task/{self.task_id}",
                headers=self.headers
            )



    
    

    
    

