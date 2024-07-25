from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):

    wait_time = between(0.5, 3.0)

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """


    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass

    @task(1)
    def hello_world(self):
        self.client.get("http://127.0.0.1:5000")

    @task(2)
    def index(self):
        self.client.get("http://127.0.0.1")