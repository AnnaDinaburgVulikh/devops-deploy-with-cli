import click
from cli_commands.base import AnsibleCommand


@click.command()
@click.pass_context
def deploy_app(ctx):
    """Deploy the web application."""
    DeployCommand(ctx).execute()


class DeployCommand(AnsibleCommand):
    def __init__(self, ctx):
        super().__init__(ctx, "deploy")
