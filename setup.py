from setuptools import setup, find_packages

with open('metrics/requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='metrics',
    version='0.0.1',
    author='Artur Mkrtychian',
    author_email='',
    url='',
    description='metrics info',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.6',
)
