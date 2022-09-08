# this is the .env file template that will be put into the bot directory before running it.
DOT_ENV_TEMPLATE = """
BOT_TOKEN={BOT_TOKEN}
ADMINS={BOT_ADMIN_ID}
ip=localhost
"""

SUPERVISOR_TEMPLATE = """
[program:{deployment_id}]
command={python_path} {script_path}/app.py
numprocs=1
directory={script_path}
autostart=true
startretries=3
user={username}
redirect_stderr=false
stdout_logfile={log_path}/stdout.log
stderr_logfile={log_path}/stderr.log
"""
