# DevOps Deploy CLI

DevOps Deploy CLI is a command-line interface tool for managing web application deployment. It provides functionality for deploying, updating, and rolling back applications using Docker and Ansible.

## Features

- Deploy web applications
- Update existing deployments
- Rollback deployments
- Configurable through YAML files
- Logging support
- Environment-specific configurations

## Prerequisites

- Python 3.9 or newer
- Docker
- Ansible

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/devops-deploy-cli.git
   cd devops-deploy-cli
   ```
2. Install the package:
    ```bash
    pip install .
    ```
   For development, install with extra dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

## Building the App Image
Before deploying, you need to build the Docker image for your application:
1. Navigate to the directory containing your Dockerfile:
   ```bash
   cd docker
   ```
2. Build the Docker image:
   ```bash
   docker build -t flask-multistage:latest .
   ```
3. Verify the image was created:
   ```bash
   docker images
   ```
   You should see your flask-multistage image in the list.

## Usage
The basic syntax for using the CLI is:
```bash
pyton cli.py [OPTIONS] COMMAND
```

Available commands:
- `--deploy`: Deploy the web application
- `--update`: Update the existing deployment 
- `--rollback`: Rollback the deployment
Options:
- `--config PATH`: Path to configuration file
- `--env TEXT`: Deployment environment (e.g., development, production)
- `--verbose`: Enable verbose output
- `--log PATH`: Path to log file
- `--secret TEXT`: Secret key for secure operations
Example:
```bash
deploy-cli --deploy --env development --config config.yml
```

## Configuration
Create a YAML configuration file with the following structure:
```yaml
docker_image: "flask-multistage"
docker_tag: "latest"
host_port: 5001
container_port: 5001
ansible_inventory: "ansible/inventory.ini"
log_file: "logs/deploy.log"
```

## Testing
All tests can be found in the tests folder
For test execution run (make sure to run from the project base folder):
```shell
pytest . -vvv
```
