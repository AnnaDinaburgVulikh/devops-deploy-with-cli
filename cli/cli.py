import click
import os
from cli.commands.deploy import deploy
from cli.commands.update import update
from cli.commands.rollback import rollback
from utils.logger import setup_logging

@click.group()
@click.option("--config", type=click.Path(exists=True), help="Path to configuration file")
@click.option("--env", type=click.Choice(["development", "staging", "production"]), default="development", help="Deployment environment")
@click.option("--verbose", is_flag=True, help="Enable verbose output")
@click.option("--log", type=click.Path(), help="Path to log file")
@click.option("--secret", envvar="DEPLOY_SECRET", help="Secret key/token for operations")
@click.pass_context
def cli(ctx, config, env, verbose, log, secret):
    """CLI tool for managing web application deployment."""
    ctx.ensure_object(dict)
    ctx.obj["CONFIG"] = config
    ctx.obj["ENV"] = env
    ctx.obj["VERBOSE"] = verbose
    ctx.obj["LOG"] = log
    ctx.obj["SECRET"] = secret
    setup_logging(log, verbose)

cli.add_command(deploy)
cli.add_command(update)
cli.add_command(rollback)

if __name__ == "__main__":
    cli()
