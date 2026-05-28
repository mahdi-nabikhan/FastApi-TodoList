from locust import HttpUser ,task,between

class QuickStartUser(HttpUser):
    wait_time = between(1,2)
    
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



    
    
    

