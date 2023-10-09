__version__ = '2.0.0'

from .getter import Getter
from .core import App, Security

# backward compatible
SwaggerApp = App
SwaggerSecurity = Security
SwaggerAuth = SwaggerSecurity

