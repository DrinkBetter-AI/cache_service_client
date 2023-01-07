from pathlib import Path
from setuptools import find_packages, setup


def get_requirements(file_name):
    with open(Path(__file__).parent / file_name, "r") as f:
        content = f.read()
    return content.splitlines()


setup(
    name="cache_service",
    description="Client for cache service",
    version="1.0.1",
    include_package_data=False,
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    python_require=">=3.9",
)
