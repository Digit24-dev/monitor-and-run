# Updated Module: monitor/task_monitor.py

import psutil
import threading

class TaskMonitor:
    def __init__(self, logger):
        self.tasks = {}
        self.logger = logger

    def add_task(self, pid, on_complete):
        """Monitor a task by its PID and execute a callback when it completes."""
        if pid in self.tasks:
            self.logger.log(f"Task {pid} is already being monitored.")
            return False

        thread = threading.Thread(target=self._monitor_task, args=(pid, on_complete), daemon=True)
        self.tasks[pid] = thread
        thread.start()
        self.logger.log(f"Started monitoring task {pid}.")
        return True

    def _monitor_task(self, pid, on_complete):
        try:
            process = psutil.Process(pid)
            process.wait()  # Block until process ends
            on_complete()
        except psutil.NoSuchProcess:
            self.logger.log(f"Task {pid} does not exist or has already terminated.")
        finally:
            del self.tasks[pid]