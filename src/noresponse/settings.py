from .basesdk import BaseSDK
from noresponse import models, utils
from noresponse._hooks import AfterParseErrorContext, HookContext, ResponseContext
from noresponse.types import OptionalNullable, UNSET
from noresponse.utils import get_security_from_env, response_helpers
from noresponse.utils.unmarshal_json_response import unmarshal_json_response
from typing import Any, Iterable, List, Mapping, Optional, Union, cast


class Settings(BaseSDK):
    r"""Environment policy, history and previews."""

    @property
    def with_raw_response(self):
        return SettingsWithRawResponse(self)

    @property
    def with_streaming_response(self):
        return SettingsWithStreamingResponse(self)

    def get(
        self,
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.GetSettingsResponse:
        r"""Read an environment's settings.

        Read this environment retention, source selection and effective flow policies. A flow without its own thresholds inherits account_creation. Requires settings or management. Another environment answers404. Read-only and safe to retry.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
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

        request = models.operations.GetSettingsRequest(
            workspace_id=workspace_id,
            environment=environment,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="GET",
            path="/v1/workspaces/{workspace_id}/settings/{environment}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
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
                return models.operations.GetSettingsResponse(
                    result=unmarshal_json_response(models.shared.Settings, http_res),
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
            operation_id="getSettings",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["settings"],
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

    async def get_async(
        self,
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.GetSettingsResponse:
        r"""Read an environment's settings.

        Read this environment retention, source selection and effective flow policies. A flow without its own thresholds inherits account_creation. Requires settings or management. Another environment answers404. Read-only and safe to retry.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
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

        request = models.operations.GetSettingsRequest(
            workspace_id=workspace_id,
            environment=environment,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="GET",
            path="/v1/workspaces/{workspace_id}/settings/{environment}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
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
                return models.operations.GetSettingsResponse(
                    result=unmarshal_json_response(models.shared.Settings, http_res),
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
            operation_id="getSettings",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["settings"],
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

    def update(
        self,
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        *,
        retention_days: Optional[int] = None,
        refused_sources: Optional[Iterable[models.shared.SourceID]] = None,
        flows: Optional[
            Union[
                models.shared.SettingsRequestFlows,
                models.shared.SettingsRequestFlowsTypedDict,
            ]
        ] = None,
        expected_policy_version: Optional[int] = None,
        change_reason: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.UpdateSettingsResponse:
        r"""Change an environment's settings.

        Change named retention, source or flow settings in one transaction. Requires settings or management; changes to active policy also require policy_publish, which legacy management includes. Use expected_policy_version to reject concurrent changes and record a change_reason. Each accepted change creates a fresh version and an atomic audit event. Retention-only edits do not require policy publication authority. Flow thresholds preserve their declared ordering and bounds.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param retention_days:
        :param refused_sources: Replaces the refused sources; [] refuses none. A change applies to new assessments within a minute.
        :param flows: Use account_creation or its deprecated alias signup, not both.
        :param expected_policy_version: Compare-and-set guard. A stale version returns 409 policy_version_conflict before any change; every settings write including retention advances the version.
        :param change_reason:
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

        request = models.operations.UpdateSettingsRequest(
            workspace_id=workspace_id,
            environment=environment,
            body=models.shared.SettingsRequest(
                retention_days=retention_days,
                refused_sources=utils.unmarshal(
                    refused_sources, Optional[List[models.shared.SourceID]]
                ),
                flows=utils.get_pydantic_model(
                    flows, Optional[models.shared.SettingsRequestFlows]
                ),
                expected_policy_version=expected_policy_version,
                change_reason=change_reason,
            ),
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="PATCH",
            path="/v1/workspaces/{workspace_id}/settings/{environment}",
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
                request.body, False, False, "json", models.shared.SettingsRequest
            ),
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
                return models.operations.UpdateSettingsResponse(
                    result=unmarshal_json_response(models.shared.Settings, http_res),
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
            operation_id="updateSettings",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["settings"],
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

    async def update_async(
        self,
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        *,
        retention_days: Optional[int] = None,
        refused_sources: Optional[Iterable[models.shared.SourceID]] = None,
        flows: Optional[
            Union[
                models.shared.SettingsRequestFlows,
                models.shared.SettingsRequestFlowsTypedDict,
            ]
        ] = None,
        expected_policy_version: Optional[int] = None,
        change_reason: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.UpdateSettingsResponse:
        r"""Change an environment's settings.

        Change named retention, source or flow settings in one transaction. Requires settings or management; changes to active policy also require policy_publish, which legacy management includes. Use expected_policy_version to reject concurrent changes and record a change_reason. Each accepted change creates a fresh version and an atomic audit event. Retention-only edits do not require policy publication authority. Flow thresholds preserve their declared ordering and bounds.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param retention_days:
        :param refused_sources: Replaces the refused sources; [] refuses none. A change applies to new assessments within a minute.
        :param flows: Use account_creation or its deprecated alias signup, not both.
        :param expected_policy_version: Compare-and-set guard. A stale version returns 409 policy_version_conflict before any change; every settings write including retention advances the version.
        :param change_reason:
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

        request = models.operations.UpdateSettingsRequest(
            workspace_id=workspace_id,
            environment=environment,
            body=models.shared.SettingsRequest(
                retention_days=retention_days,
                refused_sources=utils.unmarshal(
                    refused_sources, Optional[List[models.shared.SourceID]]
                ),
                flows=utils.get_pydantic_model(
                    flows, Optional[models.shared.SettingsRequestFlows]
                ),
                expected_policy_version=expected_policy_version,
                change_reason=change_reason,
            ),
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="PATCH",
            path="/v1/workspaces/{workspace_id}/settings/{environment}",
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
                request.body, False, False, "json", models.shared.SettingsRequest
            ),
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
                return models.operations.UpdateSettingsResponse(
                    result=unmarshal_json_response(models.shared.Settings, http_res),
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
            operation_id="updateSettings",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["settings"],
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

    def list_history(
        self,
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        *,
        before_version: Optional[int] = None,
        limit: Optional[int] = 50,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.ListPolicyHistoryResponse:
        r"""Read immutable configuration versions.

        Read immutable configuration versions in one environment with settings or management. Follow before_version for older records.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param before_version:
        :param limit:
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

        request = models.operations.ListPolicyHistoryRequest(
            workspace_id=workspace_id,
            environment=environment,
            before_version=before_version,
            limit=limit,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="GET",
            path="/v1/workspaces/{workspace_id}/settings/{environment}/history",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
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
                return models.operations.ListPolicyHistoryResponse(
                    result=unmarshal_json_response(
                        models.shared.PolicyHistory, http_res
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
            operation_id="listPolicyHistory",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["settings"],
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

    async def list_history_async(
        self,
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        *,
        before_version: Optional[int] = None,
        limit: Optional[int] = 50,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.ListPolicyHistoryResponse:
        r"""Read immutable configuration versions.

        Read immutable configuration versions in one environment with settings or management. Follow before_version for older records.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param before_version:
        :param limit:
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

        request = models.operations.ListPolicyHistoryRequest(
            workspace_id=workspace_id,
            environment=environment,
            before_version=before_version,
            limit=limit,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="GET",
            path="/v1/workspaces/{workspace_id}/settings/{environment}/history",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
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
                return models.operations.ListPolicyHistoryResponse(
                    result=unmarshal_json_response(
                        models.shared.PolicyHistory, http_res
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
            operation_id="listPolicyHistory",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["settings"],
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

    def restore(
        self,
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        *,
        version: int,
        expected_policy_version: int,
        change_reason: str,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.RestorePolicyResponse:
        r"""Restore captured settings as a new guarded version.

        Restore a retained configuration as a fresh version with the expected current version and a change reason. Requires settings plus policy_publish, or legacy management. Restore preserves the historical record and does not undo customer enforcement.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param version:
        :param expected_policy_version:
        :param change_reason:
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

        request = models.operations.RestorePolicyRequest(
            workspace_id=workspace_id,
            environment=environment,
            body=models.shared.PolicyRestoreRequest(
                version=version,
                expected_policy_version=expected_policy_version,
                change_reason=change_reason,
            ),
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="POST",
            path="/v1/workspaces/{workspace_id}/settings/{environment}/restore",
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
                request.body, False, False, "json", models.shared.PolicyRestoreRequest
            ),
            allow_empty_value=None,
            timeout_ms=timeout_ms,
        )

        def _noresponse_parse_response(http_res):
            response_data: Any = None
            if utils.match_response(http_res, "200", "application/json"):
                return models.operations.RestorePolicyResponse(
                    result=unmarshal_json_response(models.shared.Settings, http_res),
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
            operation_id="restorePolicy",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["settings"],
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

    async def restore_async(
        self,
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        *,
        version: int,
        expected_policy_version: int,
        change_reason: str,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.RestorePolicyResponse:
        r"""Restore captured settings as a new guarded version.

        Restore a retained configuration as a fresh version with the expected current version and a change reason. Requires settings plus policy_publish, or legacy management. Restore preserves the historical record and does not undo customer enforcement.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param version:
        :param expected_policy_version:
        :param change_reason:
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

        request = models.operations.RestorePolicyRequest(
            workspace_id=workspace_id,
            environment=environment,
            body=models.shared.PolicyRestoreRequest(
                version=version,
                expected_policy_version=expected_policy_version,
                change_reason=change_reason,
            ),
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="POST",
            path="/v1/workspaces/{workspace_id}/settings/{environment}/restore",
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
                request.body, False, False, "json", models.shared.PolicyRestoreRequest
            ),
            allow_empty_value=None,
            timeout_ms=timeout_ms,
        )

        async def _noresponse_parse_response(http_res):
            response_data: Any = None
            if utils.match_response(http_res, "200", "application/json"):
                return models.operations.RestorePolicyResponse(
                    result=unmarshal_json_response(models.shared.Settings, http_res),
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
            operation_id="restorePolicy",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["settings"],
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

    def preview(
        self,
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        *,
        expected_policy_version: int,
        from_: str,
        to: str,
        flows: Union[
            models.shared.PolicyPreviewRequestFlows,
            models.shared.PolicyPreviewRequestFlowsTypedDict,
        ],
        limit: Optional[int] = 1000,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.PreviewPolicyResponse:
        r"""Preview exact retained-score threshold transitions without side effects.

        Compare proposed policy with bounded retained first answers, including baseline, coverage and uncertainty. Requires settings or management. This read starts no provider work and publishes no changes.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param expected_policy_version:
        :param from_:
        :param to:
        :param flows:
        :param limit:
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

        request = models.operations.PreviewPolicyRequest(
            workspace_id=workspace_id,
            environment=environment,
            body=models.shared.PolicyPreviewRequest(
                expected_policy_version=expected_policy_version,
                from_=from_,
                to=to,
                limit=limit,
                flows=utils.get_pydantic_model(
                    flows, models.shared.PolicyPreviewRequestFlows
                ),
            ),
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="POST",
            path="/v1/workspaces/{workspace_id}/settings/{environment}/preview",
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
                request.body, False, False, "json", models.shared.PolicyPreviewRequest
            ),
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
                return models.operations.PreviewPolicyResponse(
                    result=unmarshal_json_response(
                        models.shared.PolicyPreview, http_res
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
            operation_id="previewPolicy",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["settings"],
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

    async def preview_async(
        self,
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        *,
        expected_policy_version: int,
        from_: str,
        to: str,
        flows: Union[
            models.shared.PolicyPreviewRequestFlows,
            models.shared.PolicyPreviewRequestFlowsTypedDict,
        ],
        limit: Optional[int] = 1000,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.PreviewPolicyResponse:
        r"""Preview exact retained-score threshold transitions without side effects.

        Compare proposed policy with bounded retained first answers, including baseline, coverage and uncertainty. Requires settings or management. This read starts no provider work and publishes no changes.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param expected_policy_version:
        :param from_:
        :param to:
        :param flows:
        :param limit:
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

        request = models.operations.PreviewPolicyRequest(
            workspace_id=workspace_id,
            environment=environment,
            body=models.shared.PolicyPreviewRequest(
                expected_policy_version=expected_policy_version,
                from_=from_,
                to=to,
                limit=limit,
                flows=utils.get_pydantic_model(
                    flows, models.shared.PolicyPreviewRequestFlows
                ),
            ),
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="POST",
            path="/v1/workspaces/{workspace_id}/settings/{environment}/preview",
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
                request.body, False, False, "json", models.shared.PolicyPreviewRequest
            ),
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
                return models.operations.PreviewPolicyResponse(
                    result=unmarshal_json_response(
                        models.shared.PolicyPreview, http_res
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
            operation_id="previewPolicy",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["settings"],
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


class SettingsWithRawResponse:
    def __init__(self, sdk: Settings) -> None:
        self._sdk = sdk
        self.get = response_helpers.to_raw_response_wrapper(sdk.get, "http_headers")
        self.get_async = response_helpers.async_to_raw_response_wrapper(
            sdk.get_async, "http_headers"
        )
        self.update = response_helpers.to_raw_response_wrapper(
            sdk.update, "http_headers"
        )
        self.update_async = response_helpers.async_to_raw_response_wrapper(
            sdk.update_async, "http_headers"
        )
        self.list_history = response_helpers.to_raw_response_wrapper(
            sdk.list_history, "http_headers"
        )
        self.list_history_async = response_helpers.async_to_raw_response_wrapper(
            sdk.list_history_async, "http_headers"
        )
        self.restore = response_helpers.to_raw_response_wrapper(
            sdk.restore, "http_headers"
        )
        self.restore_async = response_helpers.async_to_raw_response_wrapper(
            sdk.restore_async, "http_headers"
        )
        self.preview = response_helpers.to_raw_response_wrapper(
            sdk.preview, "http_headers"
        )
        self.preview_async = response_helpers.async_to_raw_response_wrapper(
            sdk.preview_async, "http_headers"
        )


class SettingsWithStreamingResponse:
    def __init__(self, sdk: Settings) -> None:
        self._sdk = sdk
        self.get = response_helpers.to_streamed_response_wrapper(
            sdk.get, "http_headers"
        )
        self.get_async = response_helpers.async_to_streamed_response_wrapper(
            sdk.get_async, "http_headers"
        )
        self.update = response_helpers.to_streamed_response_wrapper(
            sdk.update, "http_headers"
        )
        self.update_async = response_helpers.async_to_streamed_response_wrapper(
            sdk.update_async, "http_headers"
        )
        self.list_history = response_helpers.to_streamed_response_wrapper(
            sdk.list_history, "http_headers"
        )
        self.list_history_async = response_helpers.async_to_streamed_response_wrapper(
            sdk.list_history_async, "http_headers"
        )
        self.restore = response_helpers.to_streamed_response_wrapper(
            sdk.restore, "http_headers"
        )
        self.restore_async = response_helpers.async_to_streamed_response_wrapper(
            sdk.restore_async, "http_headers"
        )
        self.preview = response_helpers.to_streamed_response_wrapper(
            sdk.preview, "http_headers"
        )
        self.preview_async = response_helpers.async_to_streamed_response_wrapper(
            sdk.preview_async, "http_headers"
        )
