import sys
import configparser
from setuptools import setup

def update_ansible_cfg():
    python_executable = sys.executable
    config = configparser.ConfigParser()
    config.read('ansible.cfg')

    if 'defaults' not in config:
        config['defaults'] = {}

    config['defaults']['interpreter_python'] = python_executable

    with open('ansible.cfg', 'w') as configfile:
        config.write(configfile)

if __name__ == '__main__':
    update_ansible_cfg()
    setup()