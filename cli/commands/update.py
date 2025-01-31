import click
import subprocess
from utils.logger import logger

@click.command()
@click.pass_context
def update(ctx):
    """Update the existing deployment."""
    env = ctx.obj["ENV"]
    logger.info(f"Updating web application in {env} environment...")

    try:
        subprocess.run(["ansible-playbook", "-i", "ansible/inventory.ini", "ansible/roles/webapp/tasks/update.yml", "--extra-vars", f"env={env}"], check=True)
        logger.info("Update successful!")
    except subprocess.CalledProcessError as e:
        logger.error(f"Update failed: {e}")
