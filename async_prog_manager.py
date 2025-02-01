# Updated Code for main.py

import argparse
import sys
import tkinter as tk
from gui.app_gui import AppGUI
from monitor.task_monitor import TaskMonitor
from actions.action_manager import ActionManager
from utils.logger import Logger

VERSION = "1.0.0"

def parse_arguments():
    parser = argparse.ArgumentParser(description="Task Monitoring and Management Program")
    parser.add_argument("-p", "--pid", type=int, help="PID of the process to monitor")
    parser.add_argument("-e", "--execute", type=str, help="Command to execute after process completion")
    parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}", help="Show program version")
    return parser.parse_args()

def run_cui_mode(pid, command, logger):
    logger.log(f"CUI mode: Monitoring PID {pid} and executing '{command}' on completion.")
    task_monitor = TaskMonitor(logger)

    def on_complete():
        action_manager = ActionManager(logger)
        action_manager.execute_command(command)
        logger.log(f"Command executed after PID {pid} completed: {command}")

    if task_monitor.add_task(pid, on_complete):
        logger.log(f"Started monitoring PID {pid}. Waiting for it to complete...")
    else:
        logger.log(f"Failed to monitor PID {pid}. It may already be monitored or invalid.")


def run_gui_mode():
    root = tk.Tk()
    root.title("Task Monitoring and Management")

    # Instantiate core components
    tasks = []
    logger = Logger()
    task_monitor = TaskMonitor(logger)
    action_manager = ActionManager(logger, tasks=tasks)

    # Instantiate and launch the GUI
    app = AppGUI(root, task_monitor, action_manager, logger, tasks=tasks)
    sys.stdout = app.console
    app.pack(fill="both", expand=True)

    root.mainloop()

def main():
    # Check if running in shell or double-click
    if len(sys.argv) > 1:
        # Command-line arguments detected, run CUI mode
        args = parse_arguments()
        logger = Logger()

        if args.pid and args.execute:
            run_cui_mode(args.pid, args.execute, logger)
        else:
            print("Invalid arguments. Use --help for usage information.")
    else:
        # No command-line arguments, run GUI mode
        run_gui_mode()

if __name__ == "__main__":
    main()