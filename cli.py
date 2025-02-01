import logging
import sys
from dataclasses import dataclass

import click
import os
import yaml

from cli_commands.deploy import deploy_app
from cli_commands.update import update_app
from cli_commands.rollback import rollback_app
from cli_utils.input_validation import (
    validate_secret,
    validate_config_path,
    validate_config_data,
)
from cli_utils.logger import setup_logging


@dataclass
class Config:
    docker_image: str = "flask-multistage"
    docker_tag: str = "latest"
    host_port: int = 5001
    container_port: int = 5001
    ansible_inventory: str = "ansible/inventory.ini"
    log_file: str = "logs/deploy.log"


def load_config(config_path: str = None):
    """Load YAML config file and return as a dataclass instance."""
    user_config = {}

    if config_path and os.path.exists(config_path):
        with open(config_path, "r") as file:
            user_config = yaml.safe_load(file) or {}
    else:
        click.echo(f"Config file not found: {config_path}, using defaults.")

    config = Config(**user_config)

    return validate_config_data(config)


@click.command()
@click.option(
    "--config", callback=validate_config_path, help="Path to configuration file"
)
@click.option(
    "--env",
    type=click.Choice(["development", "staging", "production"]),
    default="development",
    help="Deployment environment",
)
@click.option("--verbose", is_flag=True, help="Enable verbose output")
@click.option("--log", type=click.Path(), help="Path to log file")
@click.option(
    "--secret", callback=validate_secret, help="key for secret in hashicorp vault"
)
@click.option("--deploy", is_flag=True, help="Deploy the web application")
@click.option("--update", is_flag=True, help="Update the existing deployment")
@click.option("--rollback", is_flag=True, help="Rollback the deployment")
@click.pass_context
def cli_main(ctx, config, env, verbose, log, secret, deploy, update, rollback):
    """CLI tool for managing web application deployment."""
    ctx.ensure_object(dict)
    ctx.obj["CONFIG"] = load_config(config)
    ctx.obj["ENV"] = env
    ctx.obj["VERBOSE"] = verbose
    ctx.obj["LOG"] = log if log else None
    ctx.obj["SECRET"] = secret if secret else ""

    setup_logging(ctx.obj["LOG"], verbose)
    ctx.obj["LOGGER"] = logging.getLogger("deployment_logger")

    # Ensure only one action is selected
    actions = [deploy, update, rollback]
    selected_actions = sum(actions)

    if selected_actions > 1:
        click.echo(
            "Error: You can only specify one action: --deploy, --update, or --rollback.",
            err=True,
        )
        sys.exit(1)  # ✅ Exit the script with an error status

    if selected_actions == 0:
        click.echo(
            "Error: You must specify an action: --deploy, --update, or --rollback.",
            err=True,
        )
        sys.exit(1)

    if deploy:
        ctx.invoke(deploy_app)
    elif update:
        ctx.invoke(update_app)
    elif rollback:
        ctx.invoke(rollback_app)


if __name__ == "__main__":
    cli_main()
