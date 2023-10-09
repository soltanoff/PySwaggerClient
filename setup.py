from setuptools import setup


with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pyswaggerclient',
    version='2.0',
    packages=['pyswaggerclient'],
    license='Apache-2.0',
    long_description=long_description,
    install_requires=[
        'pyaml',
        'pyswagger',
        'requests',
    ],
)
