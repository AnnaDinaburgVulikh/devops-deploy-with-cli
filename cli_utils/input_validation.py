import os
import re
import click


def validate_port(value):
    """Validate if the given port is a number and within the valid range (1-65535)."""
    try:
        port = int(value)
        if not (1 <= port <= 65535):
            raise ValueError
        return port
    except ValueError:
        raise ValueError(
            f"Invalid port '{value}'. Port must be a number between 1 and 65535."
        )


def validate_docker_image(value):
    """Validate Docker image/tag format to prevent command injection."""
    docker_pattern = r"^[a-zA-Z0-9\-_]+(/[a-zA-Z0-9\-_]+)*(:[a-zA-Z0-9\-_\.]+)?$"
    if not re.match(docker_pattern, value):
        raise ValueError(
            f"Invalid Docker image format: '{value}'. Expected format: 'repository/name:tag'"
        )


def validate_config_path(ctx, param, value):
    """Ensure the config file path is valid and exists."""
    if value:
        if not os.path.exists(value):
            raise click.BadParameter(f"Config file '{value}' not found.")
        if not value.endswith((".yml", ".yaml")):
            raise click.BadParameter("Config file must be a YAML file (.yml or .yaml).")
        if not os.access(value, os.R_OK):
            raise click.BadParameter(f"Config file '{value}' is not readable.")
    return value


def validate_secret(ctx, param, value):
    """Validate secret name is a valid string."""
    if not value:
        return None  # Allow empty secret values

        # Ensure secret key follows a valid HashiCorp Vault path format
    vault_pattern = r"^secret(/[a-zA-Z0-9_\-]+)+$"
    if not re.match(vault_pattern, value):
        raise click.BadParameter(
            "Secret name must be a valid HashiCorp Vault path (e.g., 'secret/data/my-secret')."
        )

    return value


def validate_config_data(config):
    """Validate required fields in the config file."""
    # Validate specific values
    validate_docker_image(config.docker_image)
    validate_port(config.host_port)
    validate_port(config.container_port)

    return config
