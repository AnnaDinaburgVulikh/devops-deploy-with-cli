import click
from cli_commands.base import AnsibleCommand


@click.command()
@click.pass_context
def update_app(ctx):
    """Update the existing deployment."""
    UpdateCommand(ctx).execute()


class UpdateCommand(AnsibleCommand):
    def __init__(self, ctx):
        super().__init__(ctx, "update")
