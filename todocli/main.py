from tracker import Task_tracker
import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-ls", "--list",action="store_true", help="List all tasks stored")
    parser.add_argument("-a","--add", help="Add a new task to list")
    parser.add_argument("-d", "--mkdone", help="Mark a task as done")
    parser.add_argument("-i","--mkdoing", help="Mark a task as in progress")
    parser.add_argument("-rm", "--remove", help="Delete a task")
    return parser

def main():
    tracker = Task_tracker()
    parser = create_parser()
    args=parser.parse_args()
    print(args.add)
    if args.add:
        tracker.addTask(args.add)
    elif args.mkdone:
        tracker.updateStatus(args.mkdone,"done")
    elif args.mkdoing:
        tracker.updateStatus(args.mkdoing,"doing")
    elif args.list:
        tracker.list()
    elif args.remove:
        tracker.delete(args.remove)
if __name__ == "__main__":
    main()
