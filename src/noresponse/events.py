from .basesdk import BaseSDK
from noresponse import models, utils
from noresponse._hooks import AfterParseErrorContext, HookContext, ResponseContext
from noresponse.types import OptionalNullable, UNSET
from noresponse.utils import get_security_from_env, response_helpers
from noresponse.utils.unmarshal_json_response import unmarshal_json_response
from typing import Any, Iterable, List, Mapping, Optional, Union, cast


class Events(BaseSDK):
    r"""Events, attendee lists, screenings and reviewer decisions."""

    @property
    def with_raw_response(self):
        return EventsWithRawResponse(self)

    @property
    def with_streaming_response(self):
        return EventsWithStreamingResponse(self)

    def list(
        self,
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        *,
        limit: Optional[int] = 20,
        before: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.ListEventsResponse:
        r"""List an environment's events.

        List this environment's events, newest first. Pass next_before back as before for the next page. Requires the events scope.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param limit: At most this many items.
        :param before: Read events older than this one.
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

        request = models.operations.ListEventsRequest(
            workspace_id=workspace_id,
            environment=environment,
            limit=limit,
            before=before,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="GET",
            path="/v1/workspaces/{workspace_id}/events/{environment}",
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
                return models.operations.ListEventsResponse(
                    result=unmarshal_json_response(models.shared.EventList, http_res),
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
            operation_id="listEvents",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["events"],
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
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        *,
        limit: Optional[int] = 20,
        before: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.ListEventsResponse:
        r"""List an environment's events.

        List this environment's events, newest first. Pass next_before back as before for the next page. Requires the events scope.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param limit: At most this many items.
        :param before: Read events older than this one.
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

        request = models.operations.ListEventsRequest(
            workspace_id=workspace_id,
            environment=environment,
            limit=limit,
            before=before,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="GET",
            path="/v1/workspaces/{workspace_id}/events/{environment}",
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
                return models.operations.ListEventsResponse(
                    result=unmarshal_json_response(models.shared.EventList, http_res),
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
            operation_id="listEvents",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["events"],
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

    def create(
        self,
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        *,
        name: str,
        starts_at: str,
        ends_at: Optional[str] = None,
        venue: Optional[str] = None,
        host: Optional[str] = None,
        principals: Optional[
            Union[
                Iterable[models.shared.Principal],
                Iterable[models.shared.PrincipalTypedDict],
            ]
        ] = None,
        topics: Optional[Iterable[str]] = None,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.CreateEventResponse:
        r"""Create an event to screen.

        Create an event to screen: its name, start, venue, host, the principals it protects and the sensitive topics posts are read against. An environment holds at most 1000 events.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param name: The event's name.
        :param starts_at: When the event starts.
        :param ends_at: When the event ends, at or after its start; the start when omitted.
        :param venue: Where the event is held.
        :param host: The organisation hosting the event.
        :param principals: The people the event protects, at most 20.
        :param topics: Sensitive topics the screening reads posts against, at most 50.
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

        request = models.operations.CreateEventRequest(
            workspace_id=workspace_id,
            environment=environment,
            body=models.shared.EventRequest(
                name=name,
                starts_at=starts_at,
                ends_at=ends_at,
                venue=venue,
                host=host,
                principals=utils.get_pydantic_model(
                    principals, Optional[List[models.shared.Principal]]
                ),
                topics=utils.unmarshal(topics, Optional[List[str]]),
            ),
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="POST",
            path="/v1/workspaces/{workspace_id}/events/{environment}",
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
                request.body, False, False, "json", models.shared.EventRequest
            ),
            allow_empty_value=None,
            timeout_ms=timeout_ms,
        )

        def _noresponse_parse_response(http_res):
            response_data: Any = None
            if utils.match_response(http_res, "201", "application/json"):
                return models.operations.CreateEventResponse(
                    result=unmarshal_json_response(models.shared.Event, http_res),
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
            operation_id="createEvent",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["events"],
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
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        *,
        name: str,
        starts_at: str,
        ends_at: Optional[str] = None,
        venue: Optional[str] = None,
        host: Optional[str] = None,
        principals: Optional[
            Union[
                Iterable[models.shared.Principal],
                Iterable[models.shared.PrincipalTypedDict],
            ]
        ] = None,
        topics: Optional[Iterable[str]] = None,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.CreateEventResponse:
        r"""Create an event to screen.

        Create an event to screen: its name, start, venue, host, the principals it protects and the sensitive topics posts are read against. An environment holds at most 1000 events.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param name: The event's name.
        :param starts_at: When the event starts.
        :param ends_at: When the event ends, at or after its start; the start when omitted.
        :param venue: Where the event is held.
        :param host: The organisation hosting the event.
        :param principals: The people the event protects, at most 20.
        :param topics: Sensitive topics the screening reads posts against, at most 50.
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

        request = models.operations.CreateEventRequest(
            workspace_id=workspace_id,
            environment=environment,
            body=models.shared.EventRequest(
                name=name,
                starts_at=starts_at,
                ends_at=ends_at,
                venue=venue,
                host=host,
                principals=utils.get_pydantic_model(
                    principals, Optional[List[models.shared.Principal]]
                ),
                topics=utils.unmarshal(topics, Optional[List[str]]),
            ),
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="POST",
            path="/v1/workspaces/{workspace_id}/events/{environment}",
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
                request.body, False, False, "json", models.shared.EventRequest
            ),
            allow_empty_value=None,
            timeout_ms=timeout_ms,
        )

        async def _noresponse_parse_response(http_res):
            response_data: Any = None
            if utils.match_response(http_res, "201", "application/json"):
                return models.operations.CreateEventResponse(
                    result=unmarshal_json_response(models.shared.Event, http_res),
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
            operation_id="createEvent",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["events"],
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

    def get(
        self,
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        event_id: str,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.GetEventResponse:
        r"""Read an event.

        Read an event and how many attendees it holds.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param event_id:
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

        request = models.operations.GetEventRequest(
            workspace_id=workspace_id,
            environment=environment,
            event_id=event_id,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="GET",
            path="/v1/workspaces/{workspace_id}/events/{environment}/{event_id}",
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
                return models.operations.GetEventResponse(
                    result=unmarshal_json_response(models.shared.Event, http_res),
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
            operation_id="getEvent",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["events"],
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
        event_id: str,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.GetEventResponse:
        r"""Read an event.

        Read an event and how many attendees it holds.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param event_id:
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

        request = models.operations.GetEventRequest(
            workspace_id=workspace_id,
            environment=environment,
            event_id=event_id,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="GET",
            path="/v1/workspaces/{workspace_id}/events/{environment}/{event_id}",
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
                return models.operations.GetEventResponse(
                    result=unmarshal_json_response(models.shared.Event, http_res),
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
            operation_id="getEvent",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["events"],
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
        event_id: str,
        *,
        name: Optional[str] = None,
        starts_at: Optional[str] = None,
        ends_at: Optional[str] = None,
        venue: Optional[str] = None,
        host: Optional[str] = None,
        principals: Optional[
            Union[
                Iterable[models.shared.Principal],
                Iterable[models.shared.PrincipalTypedDict],
            ]
        ] = None,
        topics: Optional[Iterable[str]] = None,
        expected_version: Optional[int] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.UpdateEventResponse:
        r"""Change an event.

        Change the fields you name. Send expected_version to apply the change only to that version.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param event_id:
        :param name: The event's name.
        :param starts_at: When the event starts.
        :param ends_at: When the event ends, at or after its start; the start when omitted.
        :param venue: Where the event is held.
        :param host: The organisation hosting the event.
        :param principals: The people the event protects, at most 20.
        :param topics: Sensitive topics the screening reads posts against, at most 50.
        :param expected_version: When present, the change applies only if the event is still at this version (409 event_conflict otherwise).
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

        request = models.operations.UpdateEventRequest(
            workspace_id=workspace_id,
            environment=environment,
            event_id=event_id,
            body=models.shared.EventUpdate(
                name=name,
                starts_at=starts_at,
                ends_at=ends_at,
                venue=venue,
                host=host,
                principals=utils.get_pydantic_model(
                    principals, Optional[List[models.shared.Principal]]
                ),
                topics=utils.unmarshal(topics, Optional[List[str]]),
                expected_version=expected_version,
            ),
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="PATCH",
            path="/v1/workspaces/{workspace_id}/events/{environment}/{event_id}",
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
                request.body, False, False, "json", models.shared.EventUpdate
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
                return models.operations.UpdateEventResponse(
                    result=unmarshal_json_response(models.shared.Event, http_res),
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
            operation_id="updateEvent",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["events"],
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
        event_id: str,
        *,
        name: Optional[str] = None,
        starts_at: Optional[str] = None,
        ends_at: Optional[str] = None,
        venue: Optional[str] = None,
        host: Optional[str] = None,
        principals: Optional[
            Union[
                Iterable[models.shared.Principal],
                Iterable[models.shared.PrincipalTypedDict],
            ]
        ] = None,
        topics: Optional[Iterable[str]] = None,
        expected_version: Optional[int] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.UpdateEventResponse:
        r"""Change an event.

        Change the fields you name. Send expected_version to apply the change only to that version.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param event_id:
        :param name: The event's name.
        :param starts_at: When the event starts.
        :param ends_at: When the event ends, at or after its start; the start when omitted.
        :param venue: Where the event is held.
        :param host: The organisation hosting the event.
        :param principals: The people the event protects, at most 20.
        :param topics: Sensitive topics the screening reads posts against, at most 50.
        :param expected_version: When present, the change applies only if the event is still at this version (409 event_conflict otherwise).
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

        request = models.operations.UpdateEventRequest(
            workspace_id=workspace_id,
            environment=environment,
            event_id=event_id,
            body=models.shared.EventUpdate(
                name=name,
                starts_at=starts_at,
                ends_at=ends_at,
                venue=venue,
                host=host,
                principals=utils.get_pydantic_model(
                    principals, Optional[List[models.shared.Principal]]
                ),
                topics=utils.unmarshal(topics, Optional[List[str]]),
                expected_version=expected_version,
            ),
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="PATCH",
            path="/v1/workspaces/{workspace_id}/events/{environment}/{event_id}",
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
                request.body, False, False, "json", models.shared.EventUpdate
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
                return models.operations.UpdateEventResponse(
                    result=unmarshal_json_response(models.shared.Event, http_res),
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
            operation_id="updateEvent",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["events"],
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
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        event_id: str,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.DeleteEventResponse:
        r"""Erase an event.

        Erase an event with its attendees, their decisions and its screenings, and stop any screening still running.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param event_id:
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

        request = models.operations.DeleteEventRequest(
            workspace_id=workspace_id,
            environment=environment,
            event_id=event_id,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="DELETE",
            path="/v1/workspaces/{workspace_id}/events/{environment}/{event_id}",
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
                return models.operations.DeleteEventResponse(
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
            operation_id="deleteEvent",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["events"],
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
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        event_id: str,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.DeleteEventResponse:
        r"""Erase an event.

        Erase an event with its attendees, their decisions and its screenings, and stop any screening still running.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param event_id:
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

        request = models.operations.DeleteEventRequest(
            workspace_id=workspace_id,
            environment=environment,
            event_id=event_id,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="DELETE",
            path="/v1/workspaces/{workspace_id}/events/{environment}/{event_id}",
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
                return models.operations.DeleteEventResponse(
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
            operation_id="deleteEvent",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["events"],
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

    def list_attendees(
        self,
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        event_id: str,
        *,
        limit: Optional[int] = 100,
        after: Optional[str] = None,
        band: Optional[models.shared.ListAttendeesBand] = None,
        decision: Optional[models.shared.ListAttendeesDecision] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.ListAttendeesResponse:
        r"""List an event's attendees.

        Read an event's roster in upload order, with each attendee's match state, highest finding band and decision. Filter by band or decision; pass next_after back as after.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param event_id:
        :param limit: At most this many attendees.
        :param after: Read attendees after this one.
        :param band: Only attendees whose highest finding has this band; none for attendees with no finding.
        :param decision: Only attendees with this decision; undecided for none yet.
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

        request = models.operations.ListAttendeesRequest(
            workspace_id=workspace_id,
            environment=environment,
            event_id=event_id,
            limit=limit,
            after=after,
            band=band,
            decision=decision,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="GET",
            path="/v1/workspaces/{workspace_id}/events/{environment}/{event_id}/attendees",
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
                return models.operations.ListAttendeesResponse(
                    result=unmarshal_json_response(
                        models.shared.AttendeeList, http_res
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
            operation_id="listAttendees",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["events"],
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

    async def list_attendees_async(
        self,
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        event_id: str,
        *,
        limit: Optional[int] = 100,
        after: Optional[str] = None,
        band: Optional[models.shared.ListAttendeesBand] = None,
        decision: Optional[models.shared.ListAttendeesDecision] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.ListAttendeesResponse:
        r"""List an event's attendees.

        Read an event's roster in upload order, with each attendee's match state, highest finding band and decision. Filter by band or decision; pass next_after back as after.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param event_id:
        :param limit: At most this many attendees.
        :param after: Read attendees after this one.
        :param band: Only attendees whose highest finding has this band; none for attendees with no finding.
        :param decision: Only attendees with this decision; undecided for none yet.
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

        request = models.operations.ListAttendeesRequest(
            workspace_id=workspace_id,
            environment=environment,
            event_id=event_id,
            limit=limit,
            after=after,
            band=band,
            decision=decision,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="GET",
            path="/v1/workspaces/{workspace_id}/events/{environment}/{event_id}/attendees",
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
                return models.operations.ListAttendeesResponse(
                    result=unmarshal_json_response(
                        models.shared.AttendeeList, http_res
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
            operation_id="listAttendees",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["events"],
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

    def add_attendees(
        self,
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        event_id: str,
        *,
        idempotency_key: str,
        attendees: Union[
            Iterable[models.shared.AttendeeIdentity],
            Iterable[models.shared.AttendeeIdentityTypedDict],
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.AddAttendeesResponse:
        r"""Add or update a batch of attendees.

        Add or update 1 to 500 attendees with an Idempotency-Key. A row with the same external_id, else email, else phone as an existing attendee updates it. Identities are stored encrypted.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param event_id:
        :param idempotency_key: Opaque client key, 16 to 128 characters of [A-Za-z0-9._:-] (a UUID or ULID fits). Scoped to the workspace principal and bound to the canonical body for 24 hours.
        :param attendees:
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

        request = models.operations.AddAttendeesRequest(
            workspace_id=workspace_id,
            environment=environment,
            event_id=event_id,
            idempotency_key=idempotency_key,
            body=models.shared.AttendeeBatchRequest(
                attendees=utils.get_pydantic_model(
                    attendees, List[models.shared.AttendeeIdentity]
                ),
            ),
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="POST",
            path="/v1/workspaces/{workspace_id}/events/{environment}/{event_id}/attendees",
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
                request.body, False, False, "json", models.shared.AttendeeBatchRequest
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
                return models.operations.AddAttendeesResponse(
                    result=unmarshal_json_response(
                        models.shared.AttendeeBatch, http_res
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
            operation_id="addAttendees",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["events"],
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

    async def add_attendees_async(
        self,
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        event_id: str,
        *,
        idempotency_key: str,
        attendees: Union[
            Iterable[models.shared.AttendeeIdentity],
            Iterable[models.shared.AttendeeIdentityTypedDict],
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.AddAttendeesResponse:
        r"""Add or update a batch of attendees.

        Add or update 1 to 500 attendees with an Idempotency-Key. A row with the same external_id, else email, else phone as an existing attendee updates it. Identities are stored encrypted.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param event_id:
        :param idempotency_key: Opaque client key, 16 to 128 characters of [A-Za-z0-9._:-] (a UUID or ULID fits). Scoped to the workspace principal and bound to the canonical body for 24 hours.
        :param attendees:
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

        request = models.operations.AddAttendeesRequest(
            workspace_id=workspace_id,
            environment=environment,
            event_id=event_id,
            idempotency_key=idempotency_key,
            body=models.shared.AttendeeBatchRequest(
                attendees=utils.get_pydantic_model(
                    attendees, List[models.shared.AttendeeIdentity]
                ),
            ),
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="POST",
            path="/v1/workspaces/{workspace_id}/events/{environment}/{event_id}/attendees",
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
                request.body, False, False, "json", models.shared.AttendeeBatchRequest
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
                return models.operations.AddAttendeesResponse(
                    result=unmarshal_json_response(
                        models.shared.AttendeeBatch, http_res
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
            operation_id="addAttendees",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["events"],
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

    def get_attendee(
        self,
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        event_id: str,
        attendee_id: str,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.GetAttendeeResponse:
        r"""Read an attendee's report.

        Read an attendee's report: matched profiles, findings with their evidence and every recorded decision.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param event_id:
        :param attendee_id:
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

        request = models.operations.GetAttendeeRequest(
            workspace_id=workspace_id,
            environment=environment,
            event_id=event_id,
            attendee_id=attendee_id,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="GET",
            path="/v1/workspaces/{workspace_id}/events/{environment}/{event_id}/attendees/{attendee_id}",
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
                return models.operations.GetAttendeeResponse(
                    result=unmarshal_json_response(
                        models.shared.AttendeeReport, http_res
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
            operation_id="getAttendee",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["events"],
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

    async def get_attendee_async(
        self,
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        event_id: str,
        attendee_id: str,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.GetAttendeeResponse:
        r"""Read an attendee's report.

        Read an attendee's report: matched profiles, findings with their evidence and every recorded decision.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param event_id:
        :param attendee_id:
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

        request = models.operations.GetAttendeeRequest(
            workspace_id=workspace_id,
            environment=environment,
            event_id=event_id,
            attendee_id=attendee_id,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="GET",
            path="/v1/workspaces/{workspace_id}/events/{environment}/{event_id}/attendees/{attendee_id}",
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
                return models.operations.GetAttendeeResponse(
                    result=unmarshal_json_response(
                        models.shared.AttendeeReport, http_res
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
            operation_id="getAttendee",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["events"],
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

    def review_attendee(
        self,
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        event_id: str,
        attendee_id: str,
        *,
        decision: models.shared.AttendeeDecision,
        note: Optional[str] = None,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.ReviewAttendeeResponse:
        r"""Record a decision on an attendee.

        Record a cleared, watch or escalated decision with a note. The latest decision is the attendee's; the next screening refreshes everyone on watch or escalated.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param event_id:
        :param attendee_id:
        :param decision:
        :param note: Why, for the venue team and later reviewers.
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

        request = models.operations.ReviewAttendeeRequest(
            workspace_id=workspace_id,
            environment=environment,
            event_id=event_id,
            attendee_id=attendee_id,
            body=models.shared.AttendeeReviewRequest(
                decision=decision,
                note=note,
            ),
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="POST",
            path="/v1/workspaces/{workspace_id}/events/{environment}/{event_id}/attendees/{attendee_id}/review",
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
                request.body, False, False, "json", models.shared.AttendeeReviewRequest
            ),
            allow_empty_value=None,
            timeout_ms=timeout_ms,
        )

        def _noresponse_parse_response(http_res):
            response_data: Any = None
            if utils.match_response(http_res, "200", "application/json"):
                return models.operations.ReviewAttendeeResponse(
                    result=unmarshal_json_response(models.shared.Attendee, http_res),
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
            operation_id="reviewAttendee",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["events"],
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

    async def review_attendee_async(
        self,
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        event_id: str,
        attendee_id: str,
        *,
        decision: models.shared.AttendeeDecision,
        note: Optional[str] = None,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.ReviewAttendeeResponse:
        r"""Record a decision on an attendee.

        Record a cleared, watch or escalated decision with a note. The latest decision is the attendee's; the next screening refreshes everyone on watch or escalated.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param event_id:
        :param attendee_id:
        :param decision:
        :param note: Why, for the venue team and later reviewers.
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

        request = models.operations.ReviewAttendeeRequest(
            workspace_id=workspace_id,
            environment=environment,
            event_id=event_id,
            attendee_id=attendee_id,
            body=models.shared.AttendeeReviewRequest(
                decision=decision,
                note=note,
            ),
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="POST",
            path="/v1/workspaces/{workspace_id}/events/{environment}/{event_id}/attendees/{attendee_id}/review",
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
                request.body, False, False, "json", models.shared.AttendeeReviewRequest
            ),
            allow_empty_value=None,
            timeout_ms=timeout_ms,
        )

        async def _noresponse_parse_response(http_res):
            response_data: Any = None
            if utils.match_response(http_res, "200", "application/json"):
                return models.operations.ReviewAttendeeResponse(
                    result=unmarshal_json_response(models.shared.Attendee, http_res),
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
            operation_id="reviewAttendee",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["events"],
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

    def list_screenings(
        self,
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        event_id: str,
        *,
        limit: Optional[int] = 20,
        before: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.ListScreeningsResponse:
        r"""List an event's screenings.

        List an event's screenings, newest first.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param event_id:
        :param limit: At most this many items.
        :param before: Read screenings older than this one.
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

        request = models.operations.ListScreeningsRequest(
            workspace_id=workspace_id,
            environment=environment,
            event_id=event_id,
            limit=limit,
            before=before,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="GET",
            path="/v1/workspaces/{workspace_id}/events/{environment}/{event_id}/screenings",
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
                return models.operations.ListScreeningsResponse(
                    result=unmarshal_json_response(
                        models.shared.ScreeningList, http_res
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
            operation_id="listScreenings",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["events"],
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

    async def list_screenings_async(
        self,
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        event_id: str,
        *,
        limit: Optional[int] = 20,
        before: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.ListScreeningsResponse:
        r"""List an event's screenings.

        List an event's screenings, newest first.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param event_id:
        :param limit: At most this many items.
        :param before: Read screenings older than this one.
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

        request = models.operations.ListScreeningsRequest(
            workspace_id=workspace_id,
            environment=environment,
            event_id=event_id,
            limit=limit,
            before=before,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="GET",
            path="/v1/workspaces/{workspace_id}/events/{environment}/{event_id}/screenings",
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
                return models.operations.ListScreeningsResponse(
                    result=unmarshal_json_response(
                        models.shared.ScreeningList, http_res
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
            operation_id="listScreenings",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["events"],
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

    def start_screening(
        self,
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        event_id: str,
        *,
        idempotency_key: str,
        depth: models.shared.ScreeningDepth,
        platforms: Iterable[models.shared.ScreeningRequestPlatform],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.StartScreeningResponse:
        r"""Start a screening.

        Start a screening of new attendees and everyone on watch or escalated, with an Idempotency-Key. It finishes completed, partial or failed minutes to hours later; poll it. The test environment screens with stand-ins that find no accounts.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param event_id:
        :param idempotency_key: Opaque client key, 16 to 128 characters of [A-Za-z0-9._:-] (a UUID or ULID fits). Scoped to the workspace principal and bound to the canonical body for 24 hours.
        :param depth:
        :param platforms:
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

        request = models.operations.StartScreeningRequest(
            workspace_id=workspace_id,
            environment=environment,
            event_id=event_id,
            idempotency_key=idempotency_key,
            body=models.shared.ScreeningRequest(
                depth=depth,
                platforms=utils.unmarshal(
                    platforms, List[models.shared.ScreeningRequestPlatform]
                ),
            ),
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="POST",
            path="/v1/workspaces/{workspace_id}/events/{environment}/{event_id}/screenings",
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
                request.body, False, False, "json", models.shared.ScreeningRequest
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
            if utils.match_response(http_res, "202", "application/json"):
                return models.operations.StartScreeningResponse(
                    result=unmarshal_json_response(models.shared.Screening, http_res),
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
            operation_id="startScreening",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["events"],
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

    async def start_screening_async(
        self,
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        event_id: str,
        *,
        idempotency_key: str,
        depth: models.shared.ScreeningDepth,
        platforms: Iterable[models.shared.ScreeningRequestPlatform],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.StartScreeningResponse:
        r"""Start a screening.

        Start a screening of new attendees and everyone on watch or escalated, with an Idempotency-Key. It finishes completed, partial or failed minutes to hours later; poll it. The test environment screens with stand-ins that find no accounts.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param event_id:
        :param idempotency_key: Opaque client key, 16 to 128 characters of [A-Za-z0-9._:-] (a UUID or ULID fits). Scoped to the workspace principal and bound to the canonical body for 24 hours.
        :param depth:
        :param platforms:
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

        request = models.operations.StartScreeningRequest(
            workspace_id=workspace_id,
            environment=environment,
            event_id=event_id,
            idempotency_key=idempotency_key,
            body=models.shared.ScreeningRequest(
                depth=depth,
                platforms=utils.unmarshal(
                    platforms, List[models.shared.ScreeningRequestPlatform]
                ),
            ),
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="POST",
            path="/v1/workspaces/{workspace_id}/events/{environment}/{event_id}/screenings",
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
                request.body, False, False, "json", models.shared.ScreeningRequest
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
            if utils.match_response(http_res, "202", "application/json"):
                return models.operations.StartScreeningResponse(
                    result=unmarshal_json_response(models.shared.Screening, http_res),
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
            operation_id="startScreening",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["events"],
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

    def get_screening(
        self,
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        event_id: str,
        screening_id: str,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.GetScreeningResponse:
        r"""Read a screening.

        Read a screening's status and progress.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param event_id:
        :param screening_id:
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

        request = models.operations.GetScreeningRequest(
            workspace_id=workspace_id,
            environment=environment,
            event_id=event_id,
            screening_id=screening_id,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="GET",
            path="/v1/workspaces/{workspace_id}/events/{environment}/{event_id}/screenings/{screening_id}",
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
                return models.operations.GetScreeningResponse(
                    result=unmarshal_json_response(models.shared.Screening, http_res),
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
            operation_id="getScreening",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["events"],
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

    async def get_screening_async(
        self,
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        event_id: str,
        screening_id: str,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.GetScreeningResponse:
        r"""Read a screening.

        Read a screening's status and progress.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param event_id:
        :param screening_id:
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

        request = models.operations.GetScreeningRequest(
            workspace_id=workspace_id,
            environment=environment,
            event_id=event_id,
            screening_id=screening_id,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="GET",
            path="/v1/workspaces/{workspace_id}/events/{environment}/{event_id}/screenings/{screening_id}",
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
                return models.operations.GetScreeningResponse(
                    result=unmarshal_json_response(models.shared.Screening, http_res),
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
            operation_id="getScreening",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["events"],
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

    def cancel_screening(
        self,
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        event_id: str,
        screening_id: str,
        *,
        body: Union[
            models.shared.ScreeningCancelRequest,
            models.shared.ScreeningCancelRequestTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.CancelScreeningResponse:
        r"""Cancel a screening.

        Stop a queued or running screening. Attendees already screened keep their results.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param event_id:
        :param screening_id:
        :param body:
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

        request = models.operations.CancelScreeningRequest(
            workspace_id=workspace_id,
            environment=environment,
            event_id=event_id,
            screening_id=screening_id,
            body=utils.get_pydantic_model(body, models.shared.ScreeningCancelRequest),
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="POST",
            path="/v1/workspaces/{workspace_id}/events/{environment}/{event_id}/screenings/{screening_id}/cancel",
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
                request.body, False, False, "json", models.shared.ScreeningCancelRequest
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
                return models.operations.CancelScreeningResponse(
                    result=unmarshal_json_response(models.shared.Screening, http_res),
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
            operation_id="cancelScreening",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["events"],
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

    async def cancel_screening_async(
        self,
        workspace_id: str,
        environment: models.shared.KeyEnvironment,
        event_id: str,
        screening_id: str,
        *,
        body: Union[
            models.shared.ScreeningCancelRequest,
            models.shared.ScreeningCancelRequestTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.CancelScreeningResponse:
        r"""Cancel a screening.

        Stop a queued or running screening. Attendees already screened keep their results.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param environment: The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404.
        :param event_id:
        :param screening_id:
        :param body:
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

        request = models.operations.CancelScreeningRequest(
            workspace_id=workspace_id,
            environment=environment,
            event_id=event_id,
            screening_id=screening_id,
            body=utils.get_pydantic_model(body, models.shared.ScreeningCancelRequest),
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="POST",
            path="/v1/workspaces/{workspace_id}/events/{environment}/{event_id}/screenings/{screening_id}/cancel",
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
                request.body, False, False, "json", models.shared.ScreeningCancelRequest
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
                return models.operations.CancelScreeningResponse(
                    result=unmarshal_json_response(models.shared.Screening, http_res),
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
            operation_id="cancelScreening",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["events"],
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


class EventsWithRawResponse:
    def __init__(self, sdk: Events) -> None:
        self._sdk = sdk
        self.list = response_helpers.to_raw_response_wrapper(sdk.list, "http_headers")
        self.list_async = response_helpers.async_to_raw_response_wrapper(
            sdk.list_async, "http_headers"
        )
        self.create = response_helpers.to_raw_response_wrapper(
            sdk.create, "http_headers"
        )
        self.create_async = response_helpers.async_to_raw_response_wrapper(
            sdk.create_async, "http_headers"
        )
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
        self.delete = response_helpers.to_raw_response_wrapper(
            sdk.delete, "http_headers"
        )
        self.delete_async = response_helpers.async_to_raw_response_wrapper(
            sdk.delete_async, "http_headers"
        )
        self.list_attendees = response_helpers.to_raw_response_wrapper(
            sdk.list_attendees, "http_headers"
        )
        self.list_attendees_async = response_helpers.async_to_raw_response_wrapper(
            sdk.list_attendees_async, "http_headers"
        )
        self.add_attendees = response_helpers.to_raw_response_wrapper(
            sdk.add_attendees, "http_headers"
        )
        self.add_attendees_async = response_helpers.async_to_raw_response_wrapper(
            sdk.add_attendees_async, "http_headers"
        )
        self.get_attendee = response_helpers.to_raw_response_wrapper(
            sdk.get_attendee, "http_headers"
        )
        self.get_attendee_async = response_helpers.async_to_raw_response_wrapper(
            sdk.get_attendee_async, "http_headers"
        )
        self.review_attendee = response_helpers.to_raw_response_wrapper(
            sdk.review_attendee, "http_headers"
        )
        self.review_attendee_async = response_helpers.async_to_raw_response_wrapper(
            sdk.review_attendee_async, "http_headers"
        )
        self.list_screenings = response_helpers.to_raw_response_wrapper(
            sdk.list_screenings, "http_headers"
        )
        self.list_screenings_async = response_helpers.async_to_raw_response_wrapper(
            sdk.list_screenings_async, "http_headers"
        )
        self.start_screening = response_helpers.to_raw_response_wrapper(
            sdk.start_screening, "http_headers"
        )
        self.start_screening_async = response_helpers.async_to_raw_response_wrapper(
            sdk.start_screening_async, "http_headers"
        )
        self.get_screening = response_helpers.to_raw_response_wrapper(
            sdk.get_screening, "http_headers"
        )
        self.get_screening_async = response_helpers.async_to_raw_response_wrapper(
            sdk.get_screening_async, "http_headers"
        )
        self.cancel_screening = response_helpers.to_raw_response_wrapper(
            sdk.cancel_screening, "http_headers"
        )
        self.cancel_screening_async = response_helpers.async_to_raw_response_wrapper(
            sdk.cancel_screening_async, "http_headers"
        )


class EventsWithStreamingResponse:
    def __init__(self, sdk: Events) -> None:
        self._sdk = sdk
        self.list = response_helpers.to_streamed_response_wrapper(
            sdk.list, "http_headers"
        )
        self.list_async = response_helpers.async_to_streamed_response_wrapper(
            sdk.list_async, "http_headers"
        )
        self.create = response_helpers.to_streamed_response_wrapper(
            sdk.create, "http_headers"
        )
        self.create_async = response_helpers.async_to_streamed_response_wrapper(
            sdk.create_async, "http_headers"
        )
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
        self.delete = response_helpers.to_streamed_response_wrapper(
            sdk.delete, "http_headers"
        )
        self.delete_async = response_helpers.async_to_streamed_response_wrapper(
            sdk.delete_async, "http_headers"
        )
        self.list_attendees = response_helpers.to_streamed_response_wrapper(
            sdk.list_attendees, "http_headers"
        )
        self.list_attendees_async = response_helpers.async_to_streamed_response_wrapper(
            sdk.list_attendees_async, "http_headers"
        )
        self.add_attendees = response_helpers.to_streamed_response_wrapper(
            sdk.add_attendees, "http_headers"
        )
        self.add_attendees_async = response_helpers.async_to_streamed_response_wrapper(
            sdk.add_attendees_async, "http_headers"
        )
        self.get_attendee = response_helpers.to_streamed_response_wrapper(
            sdk.get_attendee, "http_headers"
        )
        self.get_attendee_async = response_helpers.async_to_streamed_response_wrapper(
            sdk.get_attendee_async, "http_headers"
        )
        self.review_attendee = response_helpers.to_streamed_response_wrapper(
            sdk.review_attendee, "http_headers"
        )
        self.review_attendee_async = (
            response_helpers.async_to_streamed_response_wrapper(
                sdk.review_attendee_async, "http_headers"
            )
        )
        self.list_screenings = response_helpers.to_streamed_response_wrapper(
            sdk.list_screenings, "http_headers"
        )
        self.list_screenings_async = (
            response_helpers.async_to_streamed_response_wrapper(
                sdk.list_screenings_async, "http_headers"
            )
        )
        self.start_screening = response_helpers.to_streamed_response_wrapper(
            sdk.start_screening, "http_headers"
        )
        self.start_screening_async = (
            response_helpers.async_to_streamed_response_wrapper(
                sdk.start_screening_async, "http_headers"
            )
        )
        self.get_screening = response_helpers.to_streamed_response_wrapper(
            sdk.get_screening, "http_headers"
        )
        self.get_screening_async = response_helpers.async_to_streamed_response_wrapper(
            sdk.get_screening_async, "http_headers"
        )
        self.cancel_screening = response_helpers.to_streamed_response_wrapper(
            sdk.cancel_screening, "http_headers"
        )
        self.cancel_screening_async = (
            response_helpers.async_to_streamed_response_wrapper(
                sdk.cancel_screening_async, "http_headers"
            )
        )
