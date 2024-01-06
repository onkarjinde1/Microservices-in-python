from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def numerical_integration_task(self):
        lower = 0
        upper = 3.14

        response = self.client.get(f"/numericalintegralservice/{lower}/{upper}")

        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            # You can parse the response content if needed
            integration_results = response.json()
        else:
            # Handle non-successful responses as needed
            print(f"Error: {response.status_code}, {response.text}")

    @task
    def details_task(self):
        lower = 0
        upper = 3.14

        response = self.client.get(f"/numericalintegralservice/{lower}/{upper}/details")

        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            # You can parse the response content if needed
            details_data = response.text
        else:
            # Handle non-successful responses as needed
            print(f"Error: {response.status_code}, {response.text}")

