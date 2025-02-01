# Updated Module: actions/action_manager.py

import subprocess
import shlex

class ActionManager:
    def __init__(self, logger, tasks):
        self.logger = logger
        self.last_pid = None

    def execute_command(self, command):
        """Execute a user-defined command."""
        try:
            # 1. Command 파싱
            parsed_commnad = shlex.split(command)
            self.logger.log(f"Executing command: {command}")

            # 2. 프로세스 실행: Popen을 사용하여 프로세스를 실행하고 프로세스 id를 가져옴
            proc = subprocess.Popen(parsed_commnad)
            self.last_pid = proc.pid
            self.logger.log(f"Process started with PID: {proc.pid}")

            # 3. 프로세스가 완료될 때가지 대기 (동기 실행)
            proc.wait()

            # 4. 반환 코드 확인하여 성공 여부 로깅
            if proc.returncode == 0:
                self.logger.log(f"Command executed successfully: {command}")
            else:
                self.logger.log(f"Command failed with return code {proc.returncode}: {command}")

            # Deprecated
            # subprocess.run(command, shell=True, check=True)
            # self.logger.log(f"Command executed successfully: {command}")
        except subprocess.CalledProcessError as e:
            error_message = f"Error executing command: {e}"
            self.logger.log(error_message)