from .apierror import APIError
from typing import Any, TYPE_CHECKING

from noresponse.utils.dynamic_imports import lazy_getattr, lazy_dir

if TYPE_CHECKING:
    from .apistatuserror import APIStatusError
    from .authenticationerror import AuthenticationError, AuthenticationErrorData
    from .badrequesterror import BadRequestError, BadRequestErrorData
    from .conflicterror import ConflictError, ConflictErrorData
    from .no_response_error import NoResponseError
    from .notfounderror import NotFoundError, NotFoundErrorData
    from .permissiondeniederror import PermissionDeniedError, PermissionDeniedErrorData
    from .ratelimiterror import RateLimitError, RateLimitErrorData
    from .responsevalidationerror import ResponseValidationError

__all__ = [
    "APIError",
    "APIStatusError",
    "AuthenticationError",
    "AuthenticationErrorData",
    "BadRequestError",
    "BadRequestErrorData",
    "ConflictError",
    "ConflictErrorData",
    "NoResponseError",
    "NotFoundError",
    "NotFoundErrorData",
    "PermissionDeniedError",
    "PermissionDeniedErrorData",
    "RateLimitError",
    "RateLimitErrorData",
    "ResponseValidationError",
]

_dynamic_imports: dict[str, str] = {
    "APIStatusError": ".apistatuserror",
    "AuthenticationError": ".authenticationerror",
    "AuthenticationErrorData": ".authenticationerror",
    "BadRequestError": ".badrequesterror",
    "BadRequestErrorData": ".badrequesterror",
    "ConflictError": ".conflicterror",
    "ConflictErrorData": ".conflicterror",
    "NoResponseError": ".no_response_error",
    "NotFoundError": ".notfounderror",
    "NotFoundErrorData": ".notfounderror",
    "PermissionDeniedError": ".permissiondeniederror",
    "PermissionDeniedErrorData": ".permissiondeniederror",
    "RateLimitError": ".ratelimiterror",
    "RateLimitErrorData": ".ratelimiterror",
    "ResponseValidationError": ".responsevalidationerror",
}


def __getattr__(attr_name: str) -> Any:
    return lazy_getattr(
        attr_name, package=__package__, dynamic_imports=_dynamic_imports
    )


def __dir__():
    return lazy_dir(dynamic_imports=_dynamic_imports)
