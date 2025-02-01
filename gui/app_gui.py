# Updated Module: gui/app_gui.py

import tkinter as tk
from tkinter import ttk
from gui.console_text import ConsoleText

class AppGUI(tk.Frame):
    def __init__(self, parent, task_monitor, action_manager, logger, tasks):
        super().__init__(parent)
        self.task_monitor = task_monitor
        self.action_manager = action_manager
        self.logger = logger
        self.task_num = 1
        
        self.console = ConsoleText(self, wrap='word', height=15, width=80)
        self.console.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.tasks = tasks
        self._create_widgets()

    def _create_widgets(self):
        """Create the main GUI layout."""
        self.label = tk.Label(self, text="Task Monitoring and Management", font=("Arial", 16))
        self.label.pack(pady=10)

        # Task PID input
        self.pid_label = tk.Label(self, text="Enter Task PID:")
        self.pid_label.pack(pady=5)
        self.pid_entry = ttk.Entry(self)
        self.pid_entry.pack(pady=5)

        self.status_label = tk.Label(self, text="", font=("Arial", 12))
        self.status_label.pack(pady=5)

        # DEBUG
        # self.debug_bt = ttk.Button(self, text="Go DEBUG", command=self._debug)
        # self.debug_bt.pack(pady=5)

        # User-defined process input
        self.process_label = tk.Label(self, text="Enter Command to Execute on Completion:")
        self.process_label.pack(pady=5)
        self.process_entry = ttk.Entry(self, width=50)
        self.process_entry.pack(pady=5)

        # Monitor task button
        self.monitor_task_button = ttk.Button(self, text="Monitor Task", command=self._monitor_task)
        self.monitor_task_button.pack(pady=5)

        # Add More tasks button
        # self.add_task_button = ttk.Button(self, text="Add Task", command=self._add_task)
        # self.add_task_button.pack(pady=5)

    def _monitor_task(self):
        """Handle adding a new task to monitor."""
        pid = self.pid_entry.get()
        command = self.process_entry.get()
        if not pid.isdigit():
            self.logger.log("Invalid PID entered.")
            self.status_label.config(text="Invalid PID", fg="red")
            return

        def on_complete():
            self.action_manager.execute_command(command)
            self.status_label.config(text=f"Task {pid} completed. Command executed: {command}", fg="green")
            self.logger.log(f"Task {pid} completed. Executed command: {command}")

        if self.task_monitor.add_task(int(pid), on_complete):
            self.status_label.config(text=f"Monitoring task {pid}...", fg="blue")
            self.logger.log(f"Started monitoring task {pid}.")
        else:
            self.status_label.config(text=f"Task {pid} is already being monitored.", fg="orange")

    def _add_task(self):
        """Add more tasks."""
        self.task_num = self.task_num + 1
        self.task_label = tk.Label(self, text=f"Task {self.task_num} >")
        self.task_label.pack(pady=10)
        self.add_entry = tk.Entry(self, width=50)
        self.add_entry.pack(pady=2)
        self.tasks.append(self.add_entry)

    def _debug(self):
        # print(self.tasks)
        for entry in self.tasks :
            if (type(entry) == str):
                print(entry)
            else:
                print(entry.get())
