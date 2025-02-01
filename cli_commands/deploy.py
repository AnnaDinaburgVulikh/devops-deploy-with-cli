import click

from cli_utils.execute import execute_and_log


@click.command()
@click.pass_context
def deploy_app(ctx):
    """Deploy the web application."""
    logger = ctx.obj["LOGGER"]

    env = ctx.obj["ENV"]
    config = ctx.obj["CONFIG"]
    secret = ctx.obj["SECRET"]

    logger.info(f"Deploying web application to {env} environment...")
    logger.info(
        f"Using Docker image: {config.docker_image}:{config.docker_tag} on ports {config.host_port}:{config.container_port}"
    )

    ansible_verbosity = "-vvv" if ctx.obj["VERBOSE"] else ""

    command = [
        "ansible-playbook",
        "-i",
        config.ansible_inventory,
        "ansible/playbook.yml",
        "--limit",
        env,  # Limit to the specified environment
        "--extra-vars",
        f"action=deploy docker_image={config.docker_image} docker_tag={config.docker_tag} "
        f"host_port={config.host_port} container_port={config.container_port} secret_key={secret}",
    ]
    if ansible_verbosity:
        command.append(ansible_verbosity)

    result = execute_and_log(command, logger)
    if result:
        logger.info("Deployment successful!")
    else:
        logger.error("Deployment failed")
