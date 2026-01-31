from setuptools import setup, find_packages

setup(
    name="debug-ai",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "fix=debug_ai.cli:main"
        ]
    }
)
