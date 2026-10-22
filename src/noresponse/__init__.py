"""The NoResponse client for Python. Hand-written; not generated.

The generated modules live beside this file. Everything a caller needs is
imported here: ``from noresponse import NoResponse``.
"""

from ._version import (
    __title__,
    __version__,
    __openapi_doc_version__,
    __gen_version__,
    __user_agent__,
)
from ._public import *  # noqa: F401,F403
from .sdkconfiguration import *  # noqa: F401,F403

VERSION: str = __version__
OPENAPI_DOC_VERSION = __openapi_doc_version__
GENERATOR_VERSION = __gen_version__
USER_AGENT = __user_agent__

# NoResponse hand-written public helpers
from ._public import *  # noqa: F401,F403
