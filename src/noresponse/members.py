from .basesdk import BaseSDK
from noresponse import models, utils
from noresponse._hooks import AfterParseErrorContext, HookContext, ResponseContext
from noresponse.types import OptionalNullable, UNSET
from noresponse.utils import get_security_from_env, response_helpers
from noresponse.utils.unmarshal_json_response import unmarshal_json_response
from typing import Any, Iterable, List, Mapping, Optional, cast


class Members(BaseSDK):
    r"""Scoped workspace membership automation."""

    @property
    def with_raw_response(self):
        return MembersWithRawResponse(self)

    @property
    def with_streaming_response(self):
        return MembersWithStreamingResponse(self)

    def list(
        self,
        workspace_id: str,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.ListMembersResponse:
        r"""List a workspace's members.

        Read the workspace directory with a live key carrying members or members_manage. Member identities and grants belong to this workspace. Owner-controlled issuance limits team automation to authorised service credentials.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
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

        request = models.operations.ListMembersRequest(
            workspace_id=workspace_id,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="GET",
            path="/v1/workspaces/{workspace_id}/members",
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
                return models.operations.ListMembersResponse(
                    result=unmarshal_json_response(models.shared.MemberList, http_res),
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
            operation_id="listMembers",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["members"],
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
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.ListMembersResponse:
        r"""List a workspace's members.

        Read the workspace directory with a live key carrying members or members_manage. Member identities and grants belong to this workspace. Owner-controlled issuance limits team automation to authorised service credentials.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
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

        request = models.operations.ListMembersRequest(
            workspace_id=workspace_id,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="GET",
            path="/v1/workspaces/{workspace_id}/members",
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
                return models.operations.ListMembersResponse(
                    result=unmarshal_json_response(models.shared.MemberList, http_res),
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
            operation_id="listMembers",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["members"],
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
        member_id: str,
        *,
        role: models.shared.Role,
        environments: Optional[
            Iterable[models.shared.MemberUpdateRequestEnvironment]
        ] = None,
        denied_actions: Optional[
            Iterable[models.shared.MemberUpdateRequestDeniedAction]
        ] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.UpdateMemberResponse:
        r"""Change a member's role.

        Update a non-owner member role, environment access or sensitive permission exclusions with a live members_manage key. Owner changes, identity binding and support access remain outside this scope. The current delegation ceiling is checked within the change transaction.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param member_id: The member's mem_ id. A member of another workspace, or a removed one, answers 404.
        :param role: A built-in capability set. Specialist roles are independent; effective access is returned by GET /v1/workspaces/{workspace_id}/capabilities.
        :param environments: Allowed data environments. Invites default to both. Omitted on member PATCH preserves the current grants; owners retain both.
        :param denied_actions: Independent removals from a built-in preset: sensitive evidence, exports, or active policy publication. Owners retain full authority. Omitted member updates preserve exclusions.
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

        request = models.operations.UpdateMemberRequest(
            workspace_id=workspace_id,
            member_id=member_id,
            body=models.shared.MemberUpdateRequest(
                role=role,
                environments=utils.unmarshal(
                    environments,
                    Optional[List[models.shared.MemberUpdateRequestEnvironment]],
                ),
                denied_actions=utils.unmarshal(
                    denied_actions,
                    Optional[List[models.shared.MemberUpdateRequestDeniedAction]],
                ),
            ),
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="PATCH",
            path="/v1/workspaces/{workspace_id}/members/{member_id}",
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
                request.body, False, False, "json", models.shared.MemberUpdateRequest
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
                return models.operations.UpdateMemberResponse(
                    result=unmarshal_json_response(models.shared.Member, http_res),
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
            operation_id="updateMember",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["members"],
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
        member_id: str,
        *,
        role: models.shared.Role,
        environments: Optional[
            Iterable[models.shared.MemberUpdateRequestEnvironment]
        ] = None,
        denied_actions: Optional[
            Iterable[models.shared.MemberUpdateRequestDeniedAction]
        ] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.UpdateMemberResponse:
        r"""Change a member's role.

        Update a non-owner member role, environment access or sensitive permission exclusions with a live members_manage key. Owner changes, identity binding and support access remain outside this scope. The current delegation ceiling is checked within the change transaction.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param member_id: The member's mem_ id. A member of another workspace, or a removed one, answers 404.
        :param role: A built-in capability set. Specialist roles are independent; effective access is returned by GET /v1/workspaces/{workspace_id}/capabilities.
        :param environments: Allowed data environments. Invites default to both. Omitted on member PATCH preserves the current grants; owners retain both.
        :param denied_actions: Independent removals from a built-in preset: sensitive evidence, exports, or active policy publication. Owners retain full authority. Omitted member updates preserve exclusions.
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

        request = models.operations.UpdateMemberRequest(
            workspace_id=workspace_id,
            member_id=member_id,
            body=models.shared.MemberUpdateRequest(
                role=role,
                environments=utils.unmarshal(
                    environments,
                    Optional[List[models.shared.MemberUpdateRequestEnvironment]],
                ),
                denied_actions=utils.unmarshal(
                    denied_actions,
                    Optional[List[models.shared.MemberUpdateRequestDeniedAction]],
                ),
            ),
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="PATCH",
            path="/v1/workspaces/{workspace_id}/members/{member_id}",
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
                request.body, False, False, "json", models.shared.MemberUpdateRequest
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
                return models.operations.UpdateMemberResponse(
                    result=unmarshal_json_response(models.shared.Member, http_res),
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
            operation_id="updateMember",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["members"],
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

    def remove(
        self,
        workspace_id: str,
        member_id: str,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.RemoveMemberResponse:
        r"""Remove a member.

        Remove a non-owner member with a live members_manage key. Subsequent access is refused and personal credentials are revoked. Independently owned service credentials follow their own lifecycle.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param member_id: The member's mem_ id. A member of another workspace, or a removed one, answers 404.
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

        request = models.operations.RemoveMemberRequest(
            workspace_id=workspace_id,
            member_id=member_id,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="DELETE",
            path="/v1/workspaces/{workspace_id}/members/{member_id}",
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
                return models.operations.RemoveMemberResponse(
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
            operation_id="removeMember",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["members"],
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

    async def remove_async(
        self,
        workspace_id: str,
        member_id: str,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.RemoveMemberResponse:
        r"""Remove a member.

        Remove a non-owner member with a live members_manage key. Subsequent access is refused and personal credentials are revoked. Independently owned service credentials follow their own lifecycle.

        :param workspace_id: Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404.
        :param member_id: The member's mem_ id. A member of another workspace, or a removed one, answers 404.
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

        request = models.operations.RemoveMemberRequest(
            workspace_id=workspace_id,
            member_id=member_id,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="DELETE",
            path="/v1/workspaces/{workspace_id}/members/{member_id}",
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
                return models.operations.RemoveMemberResponse(
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
            operation_id="removeMember",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["members"],
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


class MembersWithRawResponse:
    def __init__(self, sdk: Members) -> None:
        self._sdk = sdk
        self.list = response_helpers.to_raw_response_wrapper(sdk.list, "http_headers")
        self.list_async = response_helpers.async_to_raw_response_wrapper(
            sdk.list_async, "http_headers"
        )
        self.update = response_helpers.to_raw_response_wrapper(
            sdk.update, "http_headers"
        )
        self.update_async = response_helpers.async_to_raw_response_wrapper(
            sdk.update_async, "http_headers"
        )
        self.remove = response_helpers.to_raw_response_wrapper(
            sdk.remove, "http_headers"
        )
        self.remove_async = response_helpers.async_to_raw_response_wrapper(
            sdk.remove_async, "http_headers"
        )


class MembersWithStreamingResponse:
    def __init__(self, sdk: Members) -> None:
        self._sdk = sdk
        self.list = response_helpers.to_streamed_response_wrapper(
            sdk.list, "http_headers"
        )
        self.list_async = response_helpers.async_to_streamed_response_wrapper(
            sdk.list_async, "http_headers"
        )
        self.update = response_helpers.to_streamed_response_wrapper(
            sdk.update, "http_headers"
        )
        self.update_async = response_helpers.async_to_streamed_response_wrapper(
            sdk.update_async, "http_headers"
        )
        self.remove = response_helpers.to_streamed_response_wrapper(
            sdk.remove, "http_headers"
        )
        self.remove_async = response_helpers.async_to_streamed_response_wrapper(
            sdk.remove_async, "http_headers"
        )
