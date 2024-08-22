# Task Tracker

Solution for the [task-tracker](https://roadmap.sh/projects/task-tracker) challenge from [roadmap.sh](https://roadmap.sh/).

## How to run

Clone the repository and run the following command:

```bash
git clone https://github.com/vuong-ng/roadmap_project.git
cd todocli
```

Run the following command to build and run the project:

```bash
python main.py -a [task-details]
python main.py --help # To see the list of available commands

# To add a task
python main.py --add "Buy groceries" || python main.py -a "Buy groceries"

# To mark a task as done
python main.py --mkdone 1 

# To delete a task
python main.py -rm 1 || python main.py

# To mark a task as in progress/done/todo
python main.py --mkdoing 1
python main.py --mkdone 1


# To list all tasks
python main.py --list || python main.py -ls

```
