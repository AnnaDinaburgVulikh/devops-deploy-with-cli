import click
from cli_commands.base import AnsibleCommand


@click.command()
@click.pass_context
def rollback_app(ctx):
    """Rollback the deployment."""
    RollbackCommand(ctx).execute()


class RollbackCommand(AnsibleCommand):
    def __init__(self, ctx):
        super().__init__(ctx, "rollback")
