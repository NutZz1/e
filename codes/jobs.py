import random

class Job:
    def __init__(self, job_id,machine_requirement,):
        self.job_id = job_id                      # Unique identifier for the job
        self.job_priority = 0
        self.machine_requirement = machine_requirement  # Specific machine or None
        self.machine_processing_time = [random.randint(1,5) for i in self.machine_requirement]
        self.total_processing_time = sum(self.machine_processing_time)  # Time required to execute the job
        self.threshold_temperature_reduction = random.uniform(0.1, 0.5)
        if random.random() < 0.1:
            self.job_failure_rate = random.uniform(0.4,0.8)
        else:
            self.job_failure_rate = random.uniform(0.1,0.3)
        self.status = 'Not Started'             # Job status: Not Started / Running / Completed

    def start(self):
        self.status = 'Running'

    def complete(self):
        self.status = 'Completed'
        
    def fail(self):
        self.status = 'fail'
