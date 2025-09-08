import pandas as pd
from jobs import Job

Jobs = []

def test_job_creation_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        machine_list = line.strip().split()  # Split space-separated machine IDs
        job = Job(job_id=i, machine_requirement=machine_list)

        Jobs.append([
            job.job_id,
            job.job_priority,
            job.machine_requirement,
            job.machine_processing_time,
            job.total_processing_time,
            round(job.threshold_temperature_reduction, 3),
            round(job.job_failure_rate, 3),
            job.status
        ])

if __name__ == "__main__":
    test_job_creation_from_file(r"C:\Users\sreep\OneDrive\Desktop\Edge\codes\estcases.txt")  # Path to your text file
    
    df = pd.DataFrame(Jobs, columns=[
        "ID", "Priority", "Machines", "Machine Running Time",
        "Total Time per Job", "Temperature Reduction",
        "Job failure rate", "Status"
    ])
    
    print(df.head(10))
