import click

from utils.execute import execute_and_log


@click.command()
@click.pass_context
def rollback(ctx):
    """Rollback the deployment."""
    logger = ctx.obj["LOGGER"]

    env = ctx.obj["ENV"]
    config = ctx.obj["CONFIG"]

    logger.info(f"Rolling back deployment in {env} environment...")
    logger.info(
        f"Using previous image: {config.docker_image}:{config.docker_tag} on ports {config.host_port}:{config.container_port}"
    )

    ansible_verbosity = "-vvv" if ctx.obj["VERBOSE"] else ""

    command = [
        "ansible-playbook",
        "-i",
        config.ansible_inventory,
        "ansible/playbook.yml",
        "--limit",
        env,
        "--extra-vars",
        f"action=rollback docker_image={config.docker_image} docker_tag={config.docker_tag} "
        f"host_port={config.host_port} container_port={config.container_port}",
    ]
    if ansible_verbosity:
        command.append(ansible_verbosity)

    result = execute_and_log(command, logger)
    if result:
        logger.info("Rollback successful!")
    else:
        logger.error("Rollback failed")
