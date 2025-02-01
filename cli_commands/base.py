import subprocess


class AnsibleCommand:
    """Base class for executing Ansible playbooks."""

    def __init__(self, ctx, action):
        self.logger = ctx.obj["LOGGER"]
        self.env = ctx.obj["ENV"]
        self.config = ctx.obj["CONFIG"]
        self.secret = ctx.obj["SECRET"]
        self.action = action
        self.verbosity = "-vvv" if ctx.obj["VERBOSE"] else ""

    def generate_ansible_command(self):
        """Generate the Ansible command with correct parameters."""
        command = [
            "ansible-playbook",
            "-i",
            self.config.ansible_inventory,
            "ansible/playbook.yml",
            "--limit",
            self.env,  # Limit to the specified environment
            "--extra-vars",
            f"action={self.action} docker_image={self.config.docker_image} docker_tag={self.config.docker_tag} "
            f"host_port={self.config.host_port} container_port={self.config.container_port} secret_key={self.secret}",
        ]
        if self.verbosity:
            command.append(self.verbosity)

        return command

    def execute_and_log(self, command):
        """Execute the Ansible command and log results."""
        try:
            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
            )

            # Capture Ansible output in real-time
            for line in iter(process.stdout.readline, ""):
                self.logger.info(line.strip())

            for line in iter(process.stderr.readline, ""):
                self.logger.error(line.strip())

            process.stdout.close()
            process.stderr.close()
            return_code = process.wait()

            if return_code != 0:
                raise subprocess.CalledProcessError(return_code, "ansible-playbook")

            return True

        except subprocess.CalledProcessError as e:
            self.logger.error(f"Command failed: {e}")
            return False

    def execute(self):
        """Execute the Ansible command and log results."""
        self.logger.info(f"Starting {self.action} for {self.env} environment...")
        command = self.generate_ansible_command()

        result = self.execute_and_log(command)
        if result:
            self.logger.info(f"{self.action.capitalize()} successful!")
        else:
            self.logger.error(f"{self.action.capitalize()} failed!")
