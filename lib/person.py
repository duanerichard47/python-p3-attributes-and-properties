#!/usr/bin/env python3

class Person:
        approved_jobs = ["Admin", "Customer Service", "Human Resources", "ITC", "Production", "Legal", "Finance", "Sales", "General Management", "Research & Development", "Marketing", "Purchasing"]
        def get_job(self):
            print("Retrieving the name of the dog")
            return self.job
    
    
        def set_job(self,job):
            if job in approved_job == true:
                print(f"Setting the name of the job to {job}.")
                self.job = job
            else:
                print("Job must be in list of apporved jobs.")
