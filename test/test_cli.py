import pytest
from click.testing import CliRunner

from cli import cli_main


@pytest.fixture
def runner():
    return CliRunner()


def test_cli_help(runner):
    result = runner.invoke(cli_main, ["--help"])
    assert result.exit_code == 0
    assert "Usage:" in result.output
    assert "--deploy" in result.output
    assert "--update" in result.output
    assert "--rollback" in result.output
    assert "--env" in result.output


def test_deploy_command(runner):
    result = runner.invoke(cli_main, ["--deploy", "--env", "development"])
    assert result.exit_code == 0
    assert "Deploy successful!" in result.output


def test_update_command(runner):
    result = runner.invoke(cli_main, ["--update", "--env", "development"])
    assert result.exit_code == 0
    assert "Update successful!" in result.output


def test_rollback_command(runner):
    result = runner.invoke(cli_main, ["--rollback", "--env", "development"])
    assert result.exit_code == 0
    assert "Rollback successful!" in result.output


def test_invalid_env(runner):
    result = runner.invoke(cli_main, ["--deploy", "--env", "invalid"])
    assert result.exit_code != 0
    assert "Error: Invalid value for '--env'" in result.output


def test_multiple_commands(runner):
    result = runner.invoke(cli_main, ["--deploy", "--update", "--env", "development"])
    assert result.exit_code != 0
    assert "Error: You can only specify one action" in result.output


def test_no_command(runner):
    result = runner.invoke(cli_main)
    assert result.exit_code != 0
    assert "Error: You must specify an action" in result.output
