# PySwaggerClient v2.0

[![Supported Versions](https://img.shields.io/pypi/pyversions/requests.svg)](https://pypi.org/project/requests)

A pyswagger wrapper for pythonic swagger client bindings. Exposes the API to python complete with tab-completion,
documentation, and seamless programmatic access.

## Installation

```bash
# stable
pip install https://github.com/soltanoff/PySwaggerClient/archive/v1.0.zip
# optional for openapi-3 version handling
npm install -g api-spec-converter
```

### Edge

```bash
pip install --upgrade https://github.com/soltanoff/PySwaggerClient/archive/master.zip
```

### Usage

```python
from pyswaggerclient import SwaggerClient


client = SwaggerClient(
    url='your_swagger_url',
    headers={
        'auth': 'whatever',
        'if': 'necessary',
    }
)
client.actions.your_op_id.call(your=params)
```

## Development

### Install dependencies

```bash
pip install -r requirements-dev.txt
```

`api-spec-converter` is an optional npm dependency for openapi 3-spec conversions. You can get it with:

```bash
npm install -g api-spec-converter
```

### flake8

[flake8](https://github.com/PyCQA/flake8) - a Python tool that combines pycodestyle, pyflakes, mccabe, and
third-party plugins to check the style and quality of Python code.

```shell
flake8 .
```

### pylint

[pylint](https://github.com/pylint-dev/pylint) - a static code analyzer for Python 2 or 3. It checks for
errors, enforces coding standards, attempts to find issues in the code, and can suggest code refactoring options.

```shell
pylint pyswaggerclient
```

### safety

[safety](https://pyup.io/safety/) - a tool designed to check installed dependencies for known vulnerabilities.

```shell
safety check
```