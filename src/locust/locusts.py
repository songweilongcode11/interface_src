from locust import clients,HttpLocust,task,TaskSet
from src.testcase.login import login
import subprocess
import json

class UserBehaver(TaskSet):
    def start(self):
        pass
    def end(self):
        pass
    @task(1)
    def loginMethod(self):
        login()



class WebUserLocust(HttpLocust):
    weight = 1
    task_set = UserBehaver
    max_wait = 3000
    min_wait = 5000
