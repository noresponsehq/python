from .basesdk import BaseSDK
from noresponse import models, utils
from noresponse._hooks import AfterParseErrorContext, HookContext, ResponseContext
from noresponse.types import OptionalNullable, UNSET
from noresponse.utils import get_security_from_env, response_helpers
from noresponse.utils.unmarshal_json_response import unmarshal_json_response
from typing import Any, Iterable, List, Mapping, Optional, cast


class Integrations(BaseSDK):
    r"""Hosted endpoints that answer your sign-up and sign-in hooks."""

    @property
    def with_raw_response(self):
        return IntegrationsWithRawResponse(self)

    @property
    def with_streaming_response(self):
        return IntegrationsWithStreamingResponse(self)

    def create(
        self,
        *,
        platform: models.shared.IntegrationPlatform,
        hook_points: Optional[Iterable[models.shared.IntegrationHookPoint]] = None,
        signing_secret: Optional[str] = None,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.CreateIntegrationResponse:
        r"""Register a hosted provider integration.

        Registers a WorkOS or Auth0 integration and returns its hosted endpoint, url, so a sign-up or sign-in is scored with no server of your own. For WorkOS, send the Actions signing secret from the WorkOS dashboard and point the user registration and authentication Actions at url. For Auth0, the answer's secret is the shared secret of the NoResponse Auth0 Action, shown once: store it as an Action secret. hook_points defaults to both pre_registration and post_login; an event that is not listed is allowed without an assessment. The endpoint waits for the full assessment for at most 2.5 seconds (WorkOS) or 4.5 seconds (Auth0), denies only when risk.block is true and allows on any failure. Requires the integrations scope; at most 10 per account. Not idempotent: a retry after a lost answer registers another integration.

        :param platform: The authentication provider that calls the endpoint.
        :param hook_points: The provider events the endpoint scores. Default both: pre_registration (WorkOS user registration Action, Auth0 pre-user-registration trigger) and post_login (WorkOS authentication Action, Auth0 post-login trigger). An event that is not listed is answered allow without an assessment.
        :param signing_secret: The WorkOS Actions signing secret, as the WorkOS dashboard shows it: 16 to 256 printable ASCII characters with no spaces. It is stored sealed and is not returned.
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.shared.IntegrationRequest(
            platform=platform,
            hook_points=utils.unmarshal(
                hook_points, Optional[List[models.shared.IntegrationHookPoint]]
            ),
            signing_secret=signing_secret,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="POST",
            path="/v1/integrations",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "json", models.shared.IntegrationRequest
            ),
            allow_empty_value=None,
            timeout_ms=timeout_ms,
        )

        def _noresponse_parse_response(http_res):
            response_data: Any = None
            if utils.match_response(http_res, "201", "application/json"):
                return models.operations.CreateIntegrationResponse(
                    result=unmarshal_json_response(models.shared.Integration, http_res),
                    headers=utils.get_response_headers(http_res.headers),
                )
            if utils.match_response(http_res, "400", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.BadRequestErrorData, http_res
                )
                raise models.errors.BadRequestError(response_data, http_res)
            if utils.match_response(http_res, "401", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.AuthenticationErrorData, http_res
                )
                raise models.errors.AuthenticationError(response_data, http_res)
            if utils.match_response(http_res, "403", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.PermissionDeniedErrorData, http_res
                )
                raise models.errors.PermissionDeniedError(response_data, http_res)
            if utils.match_response(http_res, "404", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.NotFoundErrorData, http_res
                )
                raise models.errors.NotFoundError(response_data, http_res)
            if utils.match_response(http_res, "409", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.ConflictErrorData, http_res
                )
                raise models.errors.ConflictError(response_data, http_res)
            if utils.match_response(http_res, "429", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.RateLimitErrorData, http_res
                )
                raise models.errors.RateLimitError(response_data, http_res)
            if utils.match_response(http_res, "4XX", "*"):
                http_res_text = utils.stream_to_text(http_res)
                raise models.errors.APIStatusError(
                    "API error occurred", http_res, http_res_text
                )
            if utils.match_response(http_res, "5XX", "*"):
                http_res_text = utils.stream_to_text(http_res)
                raise models.errors.APIStatusError(
                    "API error occurred", http_res, http_res_text
                )

            raise models.errors.APIStatusError("Unexpected response received", http_res)

        _noresponse_hook_ctx = HookContext(
            config=self.sdk_configuration,
            base_url=base_url or "",
            operation_id="createIntegration",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["integrations"],
            extensions=None,
            response=ResponseContext(mode=_noresponse_response_mode, execution="sync"),
        )
        http_res = self.do_request(
            hook_ctx=_noresponse_hook_ctx,
            request=req,
            is_error_status_code=lambda c: utils.match_status_codes(["4XX", "5XX"], c),
            stream=_noresponse_response_mode == "streaming",
        )
        if _noresponse_response_mode != "parsed":
            if utils.match_status_codes(["4XX", "5XX"], http_res.status_code):
                http_res.read()
                try:
                    _noresponse_parse_response(http_res)
                except Exception as parse_exc_:
                    response_helpers.raise_parse_error(
                        self.sdk_configuration.__dict__["_hooks"],
                        AfterParseErrorContext(_noresponse_hook_ctx),
                        http_res,
                        parse_exc_,
                    )
            _noresponse_response_cls = (
                response_helpers.StreamedAPIResponse
                if _noresponse_response_mode == "streaming"
                else response_helpers.APIResponse
            )
            return cast(
                Any,
                _noresponse_response_cls(
                    raw=http_res,
                    parser=_noresponse_parse_response,
                    mode="buffered",
                    client_ref=self,
                    hook_ctx=AfterParseErrorContext(_noresponse_hook_ctx),
                    hooks=self.sdk_configuration.__dict__.get("_hooks"),
                ),
            )
        try:
            return _noresponse_parse_response(http_res)
        except Exception as parse_exc_:
            response_helpers.raise_parse_error(
                self.sdk_configuration.__dict__["_hooks"],
                AfterParseErrorContext(_noresponse_hook_ctx),
                http_res,
                parse_exc_,
            )

    async def create_async(
        self,
        *,
        platform: models.shared.IntegrationPlatform,
        hook_points: Optional[Iterable[models.shared.IntegrationHookPoint]] = None,
        signing_secret: Optional[str] = None,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.CreateIntegrationResponse:
        r"""Register a hosted provider integration.

        Registers a WorkOS or Auth0 integration and returns its hosted endpoint, url, so a sign-up or sign-in is scored with no server of your own. For WorkOS, send the Actions signing secret from the WorkOS dashboard and point the user registration and authentication Actions at url. For Auth0, the answer's secret is the shared secret of the NoResponse Auth0 Action, shown once: store it as an Action secret. hook_points defaults to both pre_registration and post_login; an event that is not listed is allowed without an assessment. The endpoint waits for the full assessment for at most 2.5 seconds (WorkOS) or 4.5 seconds (Auth0), denies only when risk.block is true and allows on any failure. Requires the integrations scope; at most 10 per account. Not idempotent: a retry after a lost answer registers another integration.

        :param platform: The authentication provider that calls the endpoint.
        :param hook_points: The provider events the endpoint scores. Default both: pre_registration (WorkOS user registration Action, Auth0 pre-user-registration trigger) and post_login (WorkOS authentication Action, Auth0 post-login trigger). An event that is not listed is answered allow without an assessment.
        :param signing_secret: The WorkOS Actions signing secret, as the WorkOS dashboard shows it: 16 to 256 printable ASCII characters with no spaces. It is stored sealed and is not returned.
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.shared.IntegrationRequest(
            platform=platform,
            hook_points=utils.unmarshal(
                hook_points, Optional[List[models.shared.IntegrationHookPoint]]
            ),
            signing_secret=signing_secret,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="POST",
            path="/v1/integrations",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "json", models.shared.IntegrationRequest
            ),
            allow_empty_value=None,
            timeout_ms=timeout_ms,
        )

        async def _noresponse_parse_response(http_res):
            response_data: Any = None
            if utils.match_response(http_res, "201", "application/json"):
                return models.operations.CreateIntegrationResponse(
                    result=unmarshal_json_response(models.shared.Integration, http_res),
                    headers=utils.get_response_headers(http_res.headers),
                )
            if utils.match_response(http_res, "400", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.BadRequestErrorData, http_res
                )
                raise models.errors.BadRequestError(response_data, http_res)
            if utils.match_response(http_res, "401", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.AuthenticationErrorData, http_res
                )
                raise models.errors.AuthenticationError(response_data, http_res)
            if utils.match_response(http_res, "403", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.PermissionDeniedErrorData, http_res
                )
                raise models.errors.PermissionDeniedError(response_data, http_res)
            if utils.match_response(http_res, "404", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.NotFoundErrorData, http_res
                )
                raise models.errors.NotFoundError(response_data, http_res)
            if utils.match_response(http_res, "409", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.ConflictErrorData, http_res
                )
                raise models.errors.ConflictError(response_data, http_res)
            if utils.match_response(http_res, "429", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.RateLimitErrorData, http_res
                )
                raise models.errors.RateLimitError(response_data, http_res)
            if utils.match_response(http_res, "4XX", "*"):
                http_res_text = await utils.stream_to_text_async(http_res)
                raise models.errors.APIStatusError(
                    "API error occurred", http_res, http_res_text
                )
            if utils.match_response(http_res, "5XX", "*"):
                http_res_text = await utils.stream_to_text_async(http_res)
                raise models.errors.APIStatusError(
                    "API error occurred", http_res, http_res_text
                )

            raise models.errors.APIStatusError("Unexpected response received", http_res)

        _noresponse_hook_ctx = HookContext(
            config=self.sdk_configuration,
            base_url=base_url or "",
            operation_id="createIntegration",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["integrations"],
            extensions=None,
            response=ResponseContext(mode=_noresponse_response_mode, execution="async"),
        )
        http_res = await self.do_request_async(
            hook_ctx=_noresponse_hook_ctx,
            request=req,
            is_error_status_code=lambda c: utils.match_status_codes(["4XX", "5XX"], c),
            stream=_noresponse_response_mode == "streaming",
        )
        if _noresponse_response_mode != "parsed":
            if utils.match_status_codes(["4XX", "5XX"], http_res.status_code):
                await http_res.aread()
                try:
                    await _noresponse_parse_response(http_res)
                except Exception as parse_exc_:
                    await response_helpers.raise_parse_error_async(
                        self.sdk_configuration.__dict__.get("_async_hooks"),
                        self.sdk_configuration.__dict__.get("_hooks"),
                        AfterParseErrorContext(_noresponse_hook_ctx),
                        http_res,
                        parse_exc_,
                    )
            _noresponse_response_cls = (
                response_helpers.AsyncStreamedAPIResponse
                if _noresponse_response_mode == "streaming"
                else response_helpers.AsyncAPIResponse
            )
            return cast(
                Any,
                _noresponse_response_cls(
                    raw=http_res,
                    parser=_noresponse_parse_response,
                    mode="buffered",
                    client_ref=self,
                    hook_ctx=AfterParseErrorContext(_noresponse_hook_ctx),
                    hooks=self.sdk_configuration.__dict__.get("_hooks"),
                    async_hooks=self.sdk_configuration.__dict__.get("_async_hooks"),
                ),
            )
        try:
            return await _noresponse_parse_response(http_res)
        except Exception as parse_exc_:
            await response_helpers.raise_parse_error_async(
                self.sdk_configuration.__dict__.get("_async_hooks"),
                self.sdk_configuration.__dict__.get("_hooks"),
                AfterParseErrorContext(_noresponse_hook_ctx),
                http_res,
                parse_exc_,
            )

    def list(
        self,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.ListIntegrationsResponse:
        r"""List the tenant's integrations.

        Every integration, oldest first. Listings carry no secrets. Requires the integrations scope.

        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)
        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="GET",
            path="/v1/integrations",
            base_url=base_url,
            url_variables=url_variables,
            request=None,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            allow_empty_value=None,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(500, 8000, 2, 30000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["408", "429", "5XX"])

        def _noresponse_parse_response(http_res):
            response_data: Any = None
            if utils.match_response(http_res, "200", "application/json"):
                return models.operations.ListIntegrationsResponse(
                    result=unmarshal_json_response(
                        models.shared.IntegrationList, http_res
                    ),
                    headers=utils.get_response_headers(http_res.headers),
                )
            if utils.match_response(http_res, "400", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.BadRequestErrorData, http_res
                )
                raise models.errors.BadRequestError(response_data, http_res)
            if utils.match_response(http_res, "401", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.AuthenticationErrorData, http_res
                )
                raise models.errors.AuthenticationError(response_data, http_res)
            if utils.match_response(http_res, "403", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.PermissionDeniedErrorData, http_res
                )
                raise models.errors.PermissionDeniedError(response_data, http_res)
            if utils.match_response(http_res, "404", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.NotFoundErrorData, http_res
                )
                raise models.errors.NotFoundError(response_data, http_res)
            if utils.match_response(http_res, "409", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.ConflictErrorData, http_res
                )
                raise models.errors.ConflictError(response_data, http_res)
            if utils.match_response(http_res, "429", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.RateLimitErrorData, http_res
                )
                raise models.errors.RateLimitError(response_data, http_res)
            if utils.match_response(http_res, "4XX", "*"):
                http_res_text = utils.stream_to_text(http_res)
                raise models.errors.APIStatusError(
                    "API error occurred", http_res, http_res_text
                )
            if utils.match_response(http_res, "5XX", "*"):
                http_res_text = utils.stream_to_text(http_res)
                raise models.errors.APIStatusError(
                    "API error occurred", http_res, http_res_text
                )

            raise models.errors.APIStatusError("Unexpected response received", http_res)

        _noresponse_hook_ctx = HookContext(
            config=self.sdk_configuration,
            base_url=base_url or "",
            operation_id="listIntegrations",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["integrations"],
            extensions=None,
            response=ResponseContext(mode=_noresponse_response_mode, execution="sync"),
        )
        http_res = self.do_request(
            hook_ctx=_noresponse_hook_ctx,
            request=req,
            is_error_status_code=lambda c: utils.match_status_codes(["4XX", "5XX"], c),
            stream=_noresponse_response_mode == "streaming",
            retry_config=retry_config,
        )
        if _noresponse_response_mode != "parsed":
            if utils.match_status_codes(["4XX", "5XX"], http_res.status_code):
                http_res.read()
                try:
                    _noresponse_parse_response(http_res)
                except Exception as parse_exc_:
                    response_helpers.raise_parse_error(
                        self.sdk_configuration.__dict__["_hooks"],
                        AfterParseErrorContext(_noresponse_hook_ctx),
                        http_res,
                        parse_exc_,
                    )
            _noresponse_response_cls = (
                response_helpers.StreamedAPIResponse
                if _noresponse_response_mode == "streaming"
                else response_helpers.APIResponse
            )
            return cast(
                Any,
                _noresponse_response_cls(
                    raw=http_res,
                    parser=_noresponse_parse_response,
                    mode="buffered",
                    client_ref=self,
                    hook_ctx=AfterParseErrorContext(_noresponse_hook_ctx),
                    hooks=self.sdk_configuration.__dict__.get("_hooks"),
                ),
            )
        try:
            return _noresponse_parse_response(http_res)
        except Exception as parse_exc_:
            response_helpers.raise_parse_error(
                self.sdk_configuration.__dict__["_hooks"],
                AfterParseErrorContext(_noresponse_hook_ctx),
                http_res,
                parse_exc_,
            )

    async def list_async(
        self,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.ListIntegrationsResponse:
        r"""List the tenant's integrations.

        Every integration, oldest first. Listings carry no secrets. Requires the integrations scope.

        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)
        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="GET",
            path="/v1/integrations",
            base_url=base_url,
            url_variables=url_variables,
            request=None,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            allow_empty_value=None,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(500, 8000, 2, 30000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["408", "429", "5XX"])

        async def _noresponse_parse_response(http_res):
            response_data: Any = None
            if utils.match_response(http_res, "200", "application/json"):
                return models.operations.ListIntegrationsResponse(
                    result=unmarshal_json_response(
                        models.shared.IntegrationList, http_res
                    ),
                    headers=utils.get_response_headers(http_res.headers),
                )
            if utils.match_response(http_res, "400", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.BadRequestErrorData, http_res
                )
                raise models.errors.BadRequestError(response_data, http_res)
            if utils.match_response(http_res, "401", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.AuthenticationErrorData, http_res
                )
                raise models.errors.AuthenticationError(response_data, http_res)
            if utils.match_response(http_res, "403", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.PermissionDeniedErrorData, http_res
                )
                raise models.errors.PermissionDeniedError(response_data, http_res)
            if utils.match_response(http_res, "404", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.NotFoundErrorData, http_res
                )
                raise models.errors.NotFoundError(response_data, http_res)
            if utils.match_response(http_res, "409", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.ConflictErrorData, http_res
                )
                raise models.errors.ConflictError(response_data, http_res)
            if utils.match_response(http_res, "429", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.RateLimitErrorData, http_res
                )
                raise models.errors.RateLimitError(response_data, http_res)
            if utils.match_response(http_res, "4XX", "*"):
                http_res_text = await utils.stream_to_text_async(http_res)
                raise models.errors.APIStatusError(
                    "API error occurred", http_res, http_res_text
                )
            if utils.match_response(http_res, "5XX", "*"):
                http_res_text = await utils.stream_to_text_async(http_res)
                raise models.errors.APIStatusError(
                    "API error occurred", http_res, http_res_text
                )

            raise models.errors.APIStatusError("Unexpected response received", http_res)

        _noresponse_hook_ctx = HookContext(
            config=self.sdk_configuration,
            base_url=base_url or "",
            operation_id="listIntegrations",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["integrations"],
            extensions=None,
            response=ResponseContext(mode=_noresponse_response_mode, execution="async"),
        )
        http_res = await self.do_request_async(
            hook_ctx=_noresponse_hook_ctx,
            request=req,
            is_error_status_code=lambda c: utils.match_status_codes(["4XX", "5XX"], c),
            stream=_noresponse_response_mode == "streaming",
            retry_config=retry_config,
        )
        if _noresponse_response_mode != "parsed":
            if utils.match_status_codes(["4XX", "5XX"], http_res.status_code):
                await http_res.aread()
                try:
                    await _noresponse_parse_response(http_res)
                except Exception as parse_exc_:
                    await response_helpers.raise_parse_error_async(
                        self.sdk_configuration.__dict__.get("_async_hooks"),
                        self.sdk_configuration.__dict__.get("_hooks"),
                        AfterParseErrorContext(_noresponse_hook_ctx),
                        http_res,
                        parse_exc_,
                    )
            _noresponse_response_cls = (
                response_helpers.AsyncStreamedAPIResponse
                if _noresponse_response_mode == "streaming"
                else response_helpers.AsyncAPIResponse
            )
            return cast(
                Any,
                _noresponse_response_cls(
                    raw=http_res,
                    parser=_noresponse_parse_response,
                    mode="buffered",
                    client_ref=self,
                    hook_ctx=AfterParseErrorContext(_noresponse_hook_ctx),
                    hooks=self.sdk_configuration.__dict__.get("_hooks"),
                    async_hooks=self.sdk_configuration.__dict__.get("_async_hooks"),
                ),
            )
        try:
            return await _noresponse_parse_response(http_res)
        except Exception as parse_exc_:
            await response_helpers.raise_parse_error_async(
                self.sdk_configuration.__dict__.get("_async_hooks"),
                self.sdk_configuration.__dict__.get("_hooks"),
                AfterParseErrorContext(_noresponse_hook_ctx),
                http_res,
                parse_exc_,
            )

    def delete(
        self,
        integration_id: str,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.DeleteIntegrationResponse:
        r"""Delete an integration.

        Removes the integration and its secrets; its endpoint answers 404 from then on, so remove the Action from the provider first. Requires the integrations scope. An unknown or already deleted integration answers 404.

        :param integration_id: Path segment, matched case-sensitively. A value that does not match the integration_id shape, or another tenant's id, answers 404.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.operations.DeleteIntegrationRequest(
            integration_id=integration_id,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="DELETE",
            path="/v1/integrations/{integration_id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/problem+json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            allow_empty_value=None,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(500, 8000, 2, 30000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["408", "429", "5XX"])

        def _noresponse_parse_response(http_res):
            response_data: Any = None
            if utils.match_response(http_res, "204", "*"):
                return models.operations.DeleteIntegrationResponse(
                    headers=utils.get_response_headers(http_res.headers)
                )
            if utils.match_response(http_res, "400", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.BadRequestErrorData, http_res
                )
                raise models.errors.BadRequestError(response_data, http_res)
            if utils.match_response(http_res, "401", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.AuthenticationErrorData, http_res
                )
                raise models.errors.AuthenticationError(response_data, http_res)
            if utils.match_response(http_res, "403", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.PermissionDeniedErrorData, http_res
                )
                raise models.errors.PermissionDeniedError(response_data, http_res)
            if utils.match_response(http_res, "404", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.NotFoundErrorData, http_res
                )
                raise models.errors.NotFoundError(response_data, http_res)
            if utils.match_response(http_res, "409", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.ConflictErrorData, http_res
                )
                raise models.errors.ConflictError(response_data, http_res)
            if utils.match_response(http_res, "429", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.RateLimitErrorData, http_res
                )
                raise models.errors.RateLimitError(response_data, http_res)
            if utils.match_response(http_res, "4XX", "*"):
                http_res_text = utils.stream_to_text(http_res)
                raise models.errors.APIStatusError(
                    "API error occurred", http_res, http_res_text
                )
            if utils.match_response(http_res, "5XX", "*"):
                http_res_text = utils.stream_to_text(http_res)
                raise models.errors.APIStatusError(
                    "API error occurred", http_res, http_res_text
                )

            raise models.errors.APIStatusError("Unexpected response received", http_res)

        _noresponse_hook_ctx = HookContext(
            config=self.sdk_configuration,
            base_url=base_url or "",
            operation_id="deleteIntegration",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["integrations"],
            extensions=None,
            response=ResponseContext(mode=_noresponse_response_mode, execution="sync"),
        )
        http_res = self.do_request(
            hook_ctx=_noresponse_hook_ctx,
            request=req,
            is_error_status_code=lambda c: utils.match_status_codes(["4XX", "5XX"], c),
            stream=_noresponse_response_mode == "streaming",
            retry_config=retry_config,
        )
        if _noresponse_response_mode != "parsed":
            if utils.match_status_codes(["4XX", "5XX"], http_res.status_code):
                http_res.read()
                try:
                    _noresponse_parse_response(http_res)
                except Exception as parse_exc_:
                    response_helpers.raise_parse_error(
                        self.sdk_configuration.__dict__["_hooks"],
                        AfterParseErrorContext(_noresponse_hook_ctx),
                        http_res,
                        parse_exc_,
                    )
            _noresponse_response_cls = (
                response_helpers.StreamedAPIResponse
                if _noresponse_response_mode == "streaming"
                else response_helpers.APIResponse
            )
            return cast(
                Any,
                _noresponse_response_cls(
                    raw=http_res,
                    parser=_noresponse_parse_response,
                    mode="buffered",
                    client_ref=self,
                    hook_ctx=AfterParseErrorContext(_noresponse_hook_ctx),
                    hooks=self.sdk_configuration.__dict__.get("_hooks"),
                ),
            )
        try:
            return _noresponse_parse_response(http_res)
        except Exception as parse_exc_:
            response_helpers.raise_parse_error(
                self.sdk_configuration.__dict__["_hooks"],
                AfterParseErrorContext(_noresponse_hook_ctx),
                http_res,
                parse_exc_,
            )

    async def delete_async(
        self,
        integration_id: str,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.DeleteIntegrationResponse:
        r"""Delete an integration.

        Removes the integration and its secrets; its endpoint answers 404 from then on, so remove the Action from the provider first. Requires the integrations scope. An unknown or already deleted integration answers 404.

        :param integration_id: Path segment, matched case-sensitively. A value that does not match the integration_id shape, or another tenant's id, answers 404.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.operations.DeleteIntegrationRequest(
            integration_id=integration_id,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="DELETE",
            path="/v1/integrations/{integration_id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/problem+json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            allow_empty_value=None,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(500, 8000, 2, 30000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["408", "429", "5XX"])

        async def _noresponse_parse_response(http_res):
            response_data: Any = None
            if utils.match_response(http_res, "204", "*"):
                return models.operations.DeleteIntegrationResponse(
                    headers=utils.get_response_headers(http_res.headers)
                )
            if utils.match_response(http_res, "400", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.BadRequestErrorData, http_res
                )
                raise models.errors.BadRequestError(response_data, http_res)
            if utils.match_response(http_res, "401", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.AuthenticationErrorData, http_res
                )
                raise models.errors.AuthenticationError(response_data, http_res)
            if utils.match_response(http_res, "403", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.PermissionDeniedErrorData, http_res
                )
                raise models.errors.PermissionDeniedError(response_data, http_res)
            if utils.match_response(http_res, "404", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.NotFoundErrorData, http_res
                )
                raise models.errors.NotFoundError(response_data, http_res)
            if utils.match_response(http_res, "409", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.ConflictErrorData, http_res
                )
                raise models.errors.ConflictError(response_data, http_res)
            if utils.match_response(http_res, "429", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.RateLimitErrorData, http_res
                )
                raise models.errors.RateLimitError(response_data, http_res)
            if utils.match_response(http_res, "4XX", "*"):
                http_res_text = await utils.stream_to_text_async(http_res)
                raise models.errors.APIStatusError(
                    "API error occurred", http_res, http_res_text
                )
            if utils.match_response(http_res, "5XX", "*"):
                http_res_text = await utils.stream_to_text_async(http_res)
                raise models.errors.APIStatusError(
                    "API error occurred", http_res, http_res_text
                )

            raise models.errors.APIStatusError("Unexpected response received", http_res)

        _noresponse_hook_ctx = HookContext(
            config=self.sdk_configuration,
            base_url=base_url or "",
            operation_id="deleteIntegration",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["integrations"],
            extensions=None,
            response=ResponseContext(mode=_noresponse_response_mode, execution="async"),
        )
        http_res = await self.do_request_async(
            hook_ctx=_noresponse_hook_ctx,
            request=req,
            is_error_status_code=lambda c: utils.match_status_codes(["4XX", "5XX"], c),
            stream=_noresponse_response_mode == "streaming",
            retry_config=retry_config,
        )
        if _noresponse_response_mode != "parsed":
            if utils.match_status_codes(["4XX", "5XX"], http_res.status_code):
                await http_res.aread()
                try:
                    await _noresponse_parse_response(http_res)
                except Exception as parse_exc_:
                    await response_helpers.raise_parse_error_async(
                        self.sdk_configuration.__dict__.get("_async_hooks"),
                        self.sdk_configuration.__dict__.get("_hooks"),
                        AfterParseErrorContext(_noresponse_hook_ctx),
                        http_res,
                        parse_exc_,
                    )
            _noresponse_response_cls = (
                response_helpers.AsyncStreamedAPIResponse
                if _noresponse_response_mode == "streaming"
                else response_helpers.AsyncAPIResponse
            )
            return cast(
                Any,
                _noresponse_response_cls(
                    raw=http_res,
                    parser=_noresponse_parse_response,
                    mode="buffered",
                    client_ref=self,
                    hook_ctx=AfterParseErrorContext(_noresponse_hook_ctx),
                    hooks=self.sdk_configuration.__dict__.get("_hooks"),
                    async_hooks=self.sdk_configuration.__dict__.get("_async_hooks"),
                ),
            )
        try:
            return await _noresponse_parse_response(http_res)
        except Exception as parse_exc_:
            await response_helpers.raise_parse_error_async(
                self.sdk_configuration.__dict__.get("_async_hooks"),
                self.sdk_configuration.__dict__.get("_hooks"),
                AfterParseErrorContext(_noresponse_hook_ctx),
                http_res,
                parse_exc_,
            )

    def rotate(
        self,
        integration_id: str,
        *,
        signing_secret: Optional[str] = None,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.RotateIntegrationSecretResponse:
        r"""Replace an integration's secret.

        For Auth0, send {} and the answer's secret is the new shared secret, shown once. For WorkOS, regenerate the Actions secret in the WorkOS dashboard and send it as signing_secret. The replaced secret is still accepted for 24 hours (previous_secret_expires_at). Requires the integrations scope. Not idempotent: a retry after a lost answer rotates again.

        :param integration_id: Path segment, matched case-sensitively. A value that does not match the integration_id shape, or another tenant's id, answers 404.
        :param signing_secret: The WorkOS Actions signing secret, as the WorkOS dashboard shows it: 16 to 256 printable ASCII characters with no spaces. It is stored sealed and is not returned.
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.operations.RotateIntegrationSecretRequest(
            integration_id=integration_id,
            body=models.shared.IntegrationRotationRequest(
                signing_secret=signing_secret,
            ),
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="POST",
            path="/v1/integrations/{integration_id}/rotate",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.body,
                False,
                False,
                "json",
                models.shared.IntegrationRotationRequest,
            ),
            allow_empty_value=None,
            timeout_ms=timeout_ms,
        )

        def _noresponse_parse_response(http_res):
            response_data: Any = None
            if utils.match_response(http_res, "200", "application/json"):
                return models.operations.RotateIntegrationSecretResponse(
                    result=unmarshal_json_response(models.shared.Integration, http_res),
                    headers=utils.get_response_headers(http_res.headers),
                )
            if utils.match_response(http_res, "400", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.BadRequestErrorData, http_res
                )
                raise models.errors.BadRequestError(response_data, http_res)
            if utils.match_response(http_res, "401", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.AuthenticationErrorData, http_res
                )
                raise models.errors.AuthenticationError(response_data, http_res)
            if utils.match_response(http_res, "403", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.PermissionDeniedErrorData, http_res
                )
                raise models.errors.PermissionDeniedError(response_data, http_res)
            if utils.match_response(http_res, "404", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.NotFoundErrorData, http_res
                )
                raise models.errors.NotFoundError(response_data, http_res)
            if utils.match_response(http_res, "409", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.ConflictErrorData, http_res
                )
                raise models.errors.ConflictError(response_data, http_res)
            if utils.match_response(http_res, "429", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.RateLimitErrorData, http_res
                )
                raise models.errors.RateLimitError(response_data, http_res)
            if utils.match_response(http_res, "4XX", "*"):
                http_res_text = utils.stream_to_text(http_res)
                raise models.errors.APIStatusError(
                    "API error occurred", http_res, http_res_text
                )
            if utils.match_response(http_res, "5XX", "*"):
                http_res_text = utils.stream_to_text(http_res)
                raise models.errors.APIStatusError(
                    "API error occurred", http_res, http_res_text
                )

            raise models.errors.APIStatusError("Unexpected response received", http_res)

        _noresponse_hook_ctx = HookContext(
            config=self.sdk_configuration,
            base_url=base_url or "",
            operation_id="rotateIntegrationSecret",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["integrations"],
            extensions=None,
            response=ResponseContext(mode=_noresponse_response_mode, execution="sync"),
        )
        http_res = self.do_request(
            hook_ctx=_noresponse_hook_ctx,
            request=req,
            is_error_status_code=lambda c: utils.match_status_codes(["4XX", "5XX"], c),
            stream=_noresponse_response_mode == "streaming",
        )
        if _noresponse_response_mode != "parsed":
            if utils.match_status_codes(["4XX", "5XX"], http_res.status_code):
                http_res.read()
                try:
                    _noresponse_parse_response(http_res)
                except Exception as parse_exc_:
                    response_helpers.raise_parse_error(
                        self.sdk_configuration.__dict__["_hooks"],
                        AfterParseErrorContext(_noresponse_hook_ctx),
                        http_res,
                        parse_exc_,
                    )
            _noresponse_response_cls = (
                response_helpers.StreamedAPIResponse
                if _noresponse_response_mode == "streaming"
                else response_helpers.APIResponse
            )
            return cast(
                Any,
                _noresponse_response_cls(
                    raw=http_res,
                    parser=_noresponse_parse_response,
                    mode="buffered",
                    client_ref=self,
                    hook_ctx=AfterParseErrorContext(_noresponse_hook_ctx),
                    hooks=self.sdk_configuration.__dict__.get("_hooks"),
                ),
            )
        try:
            return _noresponse_parse_response(http_res)
        except Exception as parse_exc_:
            response_helpers.raise_parse_error(
                self.sdk_configuration.__dict__["_hooks"],
                AfterParseErrorContext(_noresponse_hook_ctx),
                http_res,
                parse_exc_,
            )

    async def rotate_async(
        self,
        integration_id: str,
        *,
        signing_secret: Optional[str] = None,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.RotateIntegrationSecretResponse:
        r"""Replace an integration's secret.

        For Auth0, send {} and the answer's secret is the new shared secret, shown once. For WorkOS, regenerate the Actions secret in the WorkOS dashboard and send it as signing_secret. The replaced secret is still accepted for 24 hours (previous_secret_expires_at). Requires the integrations scope. Not idempotent: a retry after a lost answer rotates again.

        :param integration_id: Path segment, matched case-sensitively. A value that does not match the integration_id shape, or another tenant's id, answers 404.
        :param signing_secret: The WorkOS Actions signing secret, as the WorkOS dashboard shows it: 16 to 256 printable ASCII characters with no spaces. It is stored sealed and is not returned.
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.operations.RotateIntegrationSecretRequest(
            integration_id=integration_id,
            body=models.shared.IntegrationRotationRequest(
                signing_secret=signing_secret,
            ),
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="POST",
            path="/v1/integrations/{integration_id}/rotate",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.body,
                False,
                False,
                "json",
                models.shared.IntegrationRotationRequest,
            ),
            allow_empty_value=None,
            timeout_ms=timeout_ms,
        )

        async def _noresponse_parse_response(http_res):
            response_data: Any = None
            if utils.match_response(http_res, "200", "application/json"):
                return models.operations.RotateIntegrationSecretResponse(
                    result=unmarshal_json_response(models.shared.Integration, http_res),
                    headers=utils.get_response_headers(http_res.headers),
                )
            if utils.match_response(http_res, "400", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.BadRequestErrorData, http_res
                )
                raise models.errors.BadRequestError(response_data, http_res)
            if utils.match_response(http_res, "401", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.AuthenticationErrorData, http_res
                )
                raise models.errors.AuthenticationError(response_data, http_res)
            if utils.match_response(http_res, "403", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.PermissionDeniedErrorData, http_res
                )
                raise models.errors.PermissionDeniedError(response_data, http_res)
            if utils.match_response(http_res, "404", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.NotFoundErrorData, http_res
                )
                raise models.errors.NotFoundError(response_data, http_res)
            if utils.match_response(http_res, "409", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.ConflictErrorData, http_res
                )
                raise models.errors.ConflictError(response_data, http_res)
            if utils.match_response(http_res, "429", "application/problem+json"):
                response_data = unmarshal_json_response(
                    models.errors.RateLimitErrorData, http_res
                )
                raise models.errors.RateLimitError(response_data, http_res)
            if utils.match_response(http_res, "4XX", "*"):
                http_res_text = await utils.stream_to_text_async(http_res)
                raise models.errors.APIStatusError(
                    "API error occurred", http_res, http_res_text
                )
            if utils.match_response(http_res, "5XX", "*"):
                http_res_text = await utils.stream_to_text_async(http_res)
                raise models.errors.APIStatusError(
                    "API error occurred", http_res, http_res_text
                )

            raise models.errors.APIStatusError("Unexpected response received", http_res)

        _noresponse_hook_ctx = HookContext(
            config=self.sdk_configuration,
            base_url=base_url or "",
            operation_id="rotateIntegrationSecret",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["integrations"],
            extensions=None,
            response=ResponseContext(mode=_noresponse_response_mode, execution="async"),
        )
        http_res = await self.do_request_async(
            hook_ctx=_noresponse_hook_ctx,
            request=req,
            is_error_status_code=lambda c: utils.match_status_codes(["4XX", "5XX"], c),
            stream=_noresponse_response_mode == "streaming",
        )
        if _noresponse_response_mode != "parsed":
            if utils.match_status_codes(["4XX", "5XX"], http_res.status_code):
                await http_res.aread()
                try:
                    await _noresponse_parse_response(http_res)
                except Exception as parse_exc_:
                    await response_helpers.raise_parse_error_async(
                        self.sdk_configuration.__dict__.get("_async_hooks"),
                        self.sdk_configuration.__dict__.get("_hooks"),
                        AfterParseErrorContext(_noresponse_hook_ctx),
                        http_res,
                        parse_exc_,
                    )
            _noresponse_response_cls = (
                response_helpers.AsyncStreamedAPIResponse
                if _noresponse_response_mode == "streaming"
                else response_helpers.AsyncAPIResponse
            )
            return cast(
                Any,
                _noresponse_response_cls(
                    raw=http_res,
                    parser=_noresponse_parse_response,
                    mode="buffered",
                    client_ref=self,
                    hook_ctx=AfterParseErrorContext(_noresponse_hook_ctx),
                    hooks=self.sdk_configuration.__dict__.get("_hooks"),
                    async_hooks=self.sdk_configuration.__dict__.get("_async_hooks"),
                ),
            )
        try:
            return await _noresponse_parse_response(http_res)
        except Exception as parse_exc_:
            await response_helpers.raise_parse_error_async(
                self.sdk_configuration.__dict__.get("_async_hooks"),
                self.sdk_configuration.__dict__.get("_hooks"),
                AfterParseErrorContext(_noresponse_hook_ctx),
                http_res,
                parse_exc_,
            )


class IntegrationsWithRawResponse:
    def __init__(self, sdk: Integrations) -> None:
        self._sdk = sdk
        self.create = response_helpers.to_raw_response_wrapper(
            sdk.create, "http_headers"
        )
        self.create_async = response_helpers.async_to_raw_response_wrapper(
            sdk.create_async, "http_headers"
        )
        self.list = response_helpers.to_raw_response_wrapper(sdk.list, "http_headers")
        self.list_async = response_helpers.async_to_raw_response_wrapper(
            sdk.list_async, "http_headers"
        )
        self.delete = response_helpers.to_raw_response_wrapper(
            sdk.delete, "http_headers"
        )
        self.delete_async = response_helpers.async_to_raw_response_wrapper(
            sdk.delete_async, "http_headers"
        )
        self.rotate = response_helpers.to_raw_response_wrapper(
            sdk.rotate, "http_headers"
        )
        self.rotate_async = response_helpers.async_to_raw_response_wrapper(
            sdk.rotate_async, "http_headers"
        )


class IntegrationsWithStreamingResponse:
    def __init__(self, sdk: Integrations) -> None:
        self._sdk = sdk
        self.create = response_helpers.to_streamed_response_wrapper(
            sdk.create, "http_headers"
        )
        self.create_async = response_helpers.async_to_streamed_response_wrapper(
            sdk.create_async, "http_headers"
        )
        self.list = response_helpers.to_streamed_response_wrapper(
            sdk.list, "http_headers"
        )
        self.list_async = response_helpers.async_to_streamed_response_wrapper(
            sdk.list_async, "http_headers"
        )
        self.delete = response_helpers.to_streamed_response_wrapper(
            sdk.delete, "http_headers"
        )
        self.delete_async = response_helpers.async_to_streamed_response_wrapper(
            sdk.delete_async, "http_headers"
        )
        self.rotate = response_helpers.to_streamed_response_wrapper(
            sdk.rotate, "http_headers"
        )
        self.rotate_async = response_helpers.async_to_streamed_response_wrapper(
            sdk.rotate_async, "http_headers"
        )
