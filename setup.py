from setuptools import setup, find_packages

setup(
    name="devops-deploy-cli",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.9",
    install_requires=[
        "Click",
        "PyYAML",
        "ansible",
    ],
    entry_points="""
        [console_scripts]
        deploy-cli=cli:cli
    """,
    extras_require={
        "dev": [
            "pytest>=8.3.4,<9.0",
            "ruff>=0.9.4,<1.0",
        ],
    },
)
