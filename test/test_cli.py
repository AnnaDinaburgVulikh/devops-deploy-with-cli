import pytest
from click.testing import CliRunner

from cli import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_cli_help(runner):
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "Usage:" in result.output
    assert "--deploy" in result.output
    assert "--update" in result.output
    assert "--rollback" in result.output
    assert "--env" in result.output


def test_deploy_command(runner):
    result = runner.invoke(cli, ["--deploy", "--env", "development"])
    assert result.exit_code == 0
    assert "Deploy successful!" in result.output


def test_update_command(runner):
    result = runner.invoke(cli, ["--update", "--env", "development"])
    assert result.exit_code == 0
    assert "Update successful!" in result.output


def test_rollback_command(runner):
    result = runner.invoke(cli, ["--rollback", "--env", "development"])
    assert result.exit_code == 0
    assert "Rollback successful!" in result.output


def test_invalid_env(runner):
    result = runner.invoke(cli, ["--deploy", "--env", "invalid"])
    assert result.exit_code != 0
    assert "Error: Invalid value for '--env'" in result.output


def test_multiple_commands(runner):
    result = runner.invoke(cli, ["--deploy", "--update", "--env", "development"])
    assert result.exit_code != 0
    assert "Error: You can only specify one action" in result.output


def test_no_command(runner):
    result = runner.invoke(cli)
    assert result.exit_code != 0
    assert "Error: You must specify an action" in result.output
