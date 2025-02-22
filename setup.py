from setuptools import find_packages, setup


with open('README.md', 'r') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    install_requires = f.readlines()

setup(
    name='pyswaggerclient',
    version='2.3.0',
    packages=find_packages(
        exclude=('*.egg-info', 'build', 'dist', 'docs', 'deploy',),
    ),
    license='Apache-2.0',
    long_description=long_description,
    install_requires=install_requires,
)
