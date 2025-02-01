import subprocess


def execute_and_log(command, logger):
    try:
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
        )

        # Capture Ansible output in real-time
        for line in iter(process.stdout.readline, ''):
            logger.info(line.strip())

        for line in iter(process.stderr.readline, ''):
            logger.error(line.strip())

        process.stdout.close()
        process.stderr.close()
        return_code = process.wait()

        if return_code != 0:
            raise subprocess.CalledProcessError(return_code, "ansible-playbook")

        return True

    except subprocess.CalledProcessError as e:
        logger.error(f"Command failed: {e}")
        return False
