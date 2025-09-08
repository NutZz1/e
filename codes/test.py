import pandas as pd
from jobs import Job

Jobs = []

def test_job_creation():
    for i in range(10):
        machine = input("enter machine requried (example A->B->C)")
        Jobs.append(Job(i, machine.split(" ")))
    

if __name__ == "__main__":
    test_job_creation()
    df = pd.DataFrame(Jobs,columns=["ID","Priority","Machines","Machine Running Time", "Total Time per Job", 
                               "Temperature Reduction" , "Job failure rate" , "Status"])
