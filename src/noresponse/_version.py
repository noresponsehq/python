import importlib.metadata

__title__: str = "noresponse"
__version__: str = "3.0.0"
__response_mode_header__: str = "x-noresponse-response-mode"
__openapi_doc_version__: str = "1"
__gen_version__: str = "internal"
__user_agent__: str = "noresponse-sdk/python 3.0.0 internal 1 noresponse"

try:
    if __package__ is not None:
        __version__ = importlib.metadata.version(__package__)
except importlib.metadata.PackageNotFoundError:
    pass
