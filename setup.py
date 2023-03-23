from setuptools import setup, find_packages


setup(
    name="proxy_manager",
    version="0.1",
    description="Package for take current proxy from my API",
    packages=find_packages(),
    install_requires=[
        'requests',
        'pandas',
        'pydantic',
        'loguru'
    ]
)