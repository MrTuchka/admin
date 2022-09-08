import uuid
from typing import Dict
from fabric import Connection
from .templates import DOT_ENV_TEMPLATE, SUPERVISOR_TEMPLATE
import io


class BotDeployer:
    def __init__(self, connection_config: Dict) -> None:
        self._username = "botrunner"
        self._connection = Connection(**connection_config)

    def _exists(self, name: str) -> bool:
        result = self._connection.run(f"test -d {name}", hide=True, warn=True)
        return result.ok

    def _generate_deployment_id(self) -> str:
        while True:
            deployment_id = str(uuid.uuid4()).rsplit("-", 1)[1]
            if not self._exists(deployment_id):
                return deployment_id

    def deploy(self, github_repo: str, bot_token: str, admin_id: str) -> str:
        deployments_dir = "deployments"
        supervisor_dir = "supervisor"
        logs_dir = "logs"

        # make necessary directories if not exist
        for directory in (supervisor_dir, logs_dir, deployments_dir):
            if not self._exists(directory):
                self._connection.run(f"mkdir {directory}", hide=True)

        # go to the deployments' directory, generate a new deployment id,
        # and clone the bot template into the deployment id directory.
        with self._connection.cd(deployments_dir):
            deployment_id = self._generate_deployment_id()
            self._connection.run(f"git clone {github_repo} {deployment_id}", hide=True)

        # render .env template and place it in the new deployments' directory.
        dot_env = DOT_ENV_TEMPLATE.format(BOT_TOKEN=bot_token, BOT_ADMIN_ID=admin_id)
        self._connection.put(io.StringIO(dot_env), f"{deployments_dir}/{deployment_id}/.env")

        # create logs directory
        with self._connection.cd("logs"):
            self._connection.run(f"mkdir {deployment_id}")

        # prepare supervisor config
        base_path = f"/home/{self._username}"
        python_path = f"{base_path}/venv/bin/python"
        script_path = f"{base_path}/{deployments_dir}/{deployment_id}"
        log_path = f"{base_path}/{logs_dir}/{deployment_id}"
        conf_path = f"{base_path}/{supervisor_dir}/{deployment_id}.conf"
        supervisor_block = SUPERVISOR_TEMPLATE.format(
            username=self._username, python_path=python_path, deployment_id=deployment_id, script_path=script_path,
            log_path=log_path,
        )

        self._connection.put(io.StringIO(supervisor_block), conf_path)

        # start the process
        self._connection.sudo("supervisorctl reread", hide=True)
        self._connection.sudo("supervisorctl update", hide=True)

        return deployment_id

    def start(self, deployment_id: str) -> bool:
        result = self._connection.sudo(f"supervisorctl start {deployment_id}", hide=True, warn=True)
        return result.ok

    def stop(self, deployment_id: str) -> bool:
        result = self._connection.sudo(f"supervisorctl stop {deployment_id}", hide=True, warn=True)
        return result.ok

    def restart(self, deployment_id: str) -> bool:
        result = self._connection.sudo(f"supervisorctl restart {deployment_id}", hide=True, warn=True)
        return result.ok

    def remove(self, deployment_id: str) -> bool:
        result = True

        script_path = f"deployments/{deployment_id}"
        log_path = f"logs/{deployment_id}"
        conf_path = f"supervisor/{deployment_id}.conf"

        result = result and self._connection.run(f"rm {conf_path}", hide=True, warn=True).ok
        result = result and self._connection.run(f"rm -rf {log_path}", hide=True, warn=True).ok
        result = result and self._connection.run(f"rm -rf {script_path}", hide=True, warn=True).ok

        result = result and self._connection.sudo("supervisorctl reread", hide=True, warn=True)
        result = result and self._connection.sudo("supervisorctl update", hide=True, warn=True)

        return result
