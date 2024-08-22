import os
from datetime import datetime
import json
# command line available
# add, delete, update, mk-done, mk-doing
actions_library = ["add", "delete", "update", "mk-done", "mk-doing"]

# sample json task
# task = {
#   id:
#   date:
#   details:
#   status:
# }
# with open("task/tasks.json","r") as f:

#     print(json_object)
        
class Task_tracker:
    def __init__(self, file="task/tasks.json"):
        self.file = file
        print(self.file)
        print(os.path.exists(file))
        
    def addTask(self, task_details):
        new_task = {
            "id":0,
            "details":task_details,
            "date": datetime.today().strftime('%Y-%m-%d'),
            "status":"not started",
        }
        print (new_task)
        with open(self.file, "r") as f:
            saved_tasks = json.load(f)
            new_task["id"]= "{id}".format(id = len(saved_tasks)+1)
            f.close()
        saved_tasks[new_task["id"]] = new_task
        file = open(self.file,"w")
        json.dump(saved_tasks,file)
        file.close()
    
    def updateStatus(self, id, newStatus):
        with open(self.file,"r") as f:
            saved_tasks = json.load(f)
            f.close()
        try:
            saved_tasks[id]["status"] = newStatus
            file = open(self.file,"w")
            json_object = json.dumps(saved_tasks)
            file.write(json_object)
            file.close()
        except:
            print('Task is not available')
    
    # def deleteTask(id):
    #     with open()
        
    def delete(self, id):
        with open(self.file,"r") as f:
            saved_tasks = json.load(f)
            f.close()
        try:
            del saved_tasks[id]
            file = open(self.file,"w")
            json_object = json.dumps(saved_tasks, indent=2)
            file.write(json_object)
            file.close()
        except:
            print('Task is not available')
    
    def list(self):
        f = open(self.file,"r")
        tasks= json.load(f)
        print(tasks)
