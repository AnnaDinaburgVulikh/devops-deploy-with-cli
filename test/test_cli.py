import pytest
from click.testing import CliRunner
from cli.cli import cli

@pytest.fixture
def runner():
    """Returns a Click test runner."""
    return CliRunner()

def test_cli_help(runner):
    """Test CLI help command."""
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "CLI tool for managing web application deployment" in result.output

def test_deploy_command(runner, mocker):
    """Test the deploy command with a mock Ansible call."""
    mock_subprocess = mocker.patch("subprocess.run")
    result = runner.invoke(cli, ["--deploy", "--env", "staging"])
    assert result.exit_code == 0
    assert "Deploying web application to staging environment..." in result.output
    mock_subprocess.assert_called_once()

def test_update_command(runner, mocker):
    """Test the update command."""
    mock_subprocess = mocker.patch("subprocess.run")
    result = runner.invoke(cli, ["--update", "--env", "production"])
    assert result.exit_code == 0
    assert "Updating web application in production environment..." in result.output
    mock_subprocess.assert_called_once()

def test_rollback_command(runner, mocker):
    """Test the rollback command."""
    mock_subprocess = mocker.patch("subprocess.run")
    result = runner.invoke(cli, ["--rollback", "--env", "staging"])
    assert result.exit_code == 0
    assert "Rolling back deployment in staging environment..." in result.output
    mock_subprocess.assert_called_once()

def test_invalid_env(runner):
    """Test invalid environment input."""
    result = runner.invoke(cli, ["--deploy", "--env", "invalid-env"])
    assert result.exit_code != 0
    assert "Invalid value for '--env'" in result.output
