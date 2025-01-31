import click
import subprocess
from utils.logger import logger

@click.command()
@click.pass_context
def deploy(ctx):
    """Deploy the web application."""
    env = ctx.obj["ENV"]
    logger.info(f"Deploying web application to {env} environment...")

    try:
        subprocess.run(["ansible-playbook", "-i", "ansible/inventory.ini", "ansible/playbook.yml", "--extra-vars", f"env={env}"], check=True)
        logger.info("Deployment successful!")
    except subprocess.CalledProcessError as e:
        logger.error(f"Deployment failed: {e}")
