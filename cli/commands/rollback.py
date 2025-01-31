import click
import subprocess
from utils.logger import logger

@click.command()
@click.pass_context
def rollback(ctx):
    """Rollback the deployment."""
    env = ctx.obj["ENV"]
    logger.info(f"Rolling back deployment in {env} environment...")

    try:
        subprocess.run(["ansible-playbook", "-i", "ansible/inventory.ini", "ansible/roles/webapp/tasks/rollback.yml", "--extra-vars", f"env={env}"], check=True)
        logger.info("Rollback successful!")
    except subprocess.CalledProcessError as e:
        logger.error(f"Rollback failed: {e}")
