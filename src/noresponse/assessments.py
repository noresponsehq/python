from .basesdk import BaseSDK
from jsonpath import JSONPath
from noresponse import models, utils
from noresponse._hooks import AfterParseErrorContext, HookContext, ResponseContext
from noresponse.types import OptionalNullable, UNSET
from noresponse.utils import get_security_from_env, response_helpers
from noresponse.utils.unmarshal_json_response import unmarshal_json_response
from typing import Any, Awaitable, Dict, Iterable, List, Mapping, Optional, Union, cast


class Assessments(BaseSDK):
    r"""Assessments of account creation, login and purchase."""

    @property
    def with_raw_response(self):
        return AssessmentsWithRawResponse(self)

    @property
    def with_streaming_response(self):
        return AssessmentsWithStreamingResponse(self)

    def create(
        self,
        *,
        idempotency_key: str,
        account_id: str,
        flow: models.shared.Flow,
        identifiers: Union[
            models.shared.AssessmentRequestIdentifiers,
            models.shared.AssessmentRequestIdentifiersTypedDict,
        ],
        depth: Optional[models.shared.Depth] = None,
        policy_context: Optional[
            Union[
                models.shared.AssessmentRequestPolicyContext,
                models.shared.AssessmentRequestPolicyContextTypedDict,
            ]
        ] = None,
        request_id: Optional[str] = None,
        deadline_ms: Optional[int] = None,
        response_mode: Optional[models.shared.ResponseMode] = None,
        client_context: Optional[
            Union[
                models.shared.AssessmentRequestClientContext,
                models.shared.AssessmentRequestClientContextTypedDict,
            ]
        ] = None,
        auth_context: Optional[
            Union[models.shared.AuthContext, models.shared.AuthContextTypedDict]
        ] = None,
        issued_credential: Optional[
            Union[
                models.shared.AssessmentRequestIssuedCredential,
                models.shared.AssessmentRequestIssuedCredentialTypedDict,
            ]
        ] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.CreateAssessmentResponse:
        r"""Assess identifiers for a signup or gateway decision.

        Assesses one account creation, login or purchase (flow) and answers with the account's one current risk: account.risk.decision is the decision for this flow (allow, step_up, review or block, where block means your block threshold was reached), and detail holds this assessment's own facts. depth sets how long the answer waits for sources: quick waits only for the fast ones (500 ms), full for the whole budget (3000 ms at most); it defaults to full for account_creation and purchase and quick for login. 200 carries complete or partial, 202 carries pending with Location and Retry-After. While the account's first assessment is pending, account is absent: apply your own fallback for that, 429, 503 or a timeout. NoResponse blocks nothing itself; you decide. Requires the assess scope. Idempotency-Key is required and is bound to the body for 24 hours: the same key with the same body replays the latest assessment with Idempotent-Replayed: true and starts no new work; the same key with a different body answers 409 idempotency_key_reused. response_mode defaults to standard; detailed needs the detailed scope. The answer leaves out detail.identifiers: you hold what you sent, and a key with the history scope gets them back with GET.

        :param idempotency_key: Opaque client key, 16 to 128 characters of [A-Za-z0-9._:-] (a UUID or ULID fits). Scoped to the workspace principal and bound to the canonical body for 24 hours.
        :param account_id: Your own opaque identifier for the account being checked, scoped to your workspace. Use an id you mint, with no direct identifier (email, phone, name or national id) in it. '|' is accepted so an Auth0 user id such as 'auth0|64abc' passes unchanged; '@', '+', '
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.operations.CreateAssessmentRequest(
            idempotency_key=idempotency_key,
            body=models.shared.AssessmentRequest(
                account_id=account_id,
                flow=flow,
                depth=depth,
                identifiers=utils.get_pydantic_model(identifiers, models.shared.AssessmentRequestIdentifiers),
                policy_context=utils.get_pydantic_model(policy_context, Optional[models.shared.AssessmentRequestPolicyContext]),
                request_id=request_id,
                deadline_ms=deadline_ms,
                response_mode=response_mode,
                client_context=utils.get_pydantic_model(client_context, Optional[models.shared.AssessmentRequestClientContext]),
                auth_context=utils.get_pydantic_model(auth_context, Optional[models.shared.AuthContext]),
                issued_credential=utils.get_pydantic_model(issued_credential, Optional[models.shared.AssessmentRequestIssuedCredential]),
            ),
        )

        _noresponse_response_mode, http_headers = response_helpers.consume_response_mode(http_headers)
        req = self._build_request(
            method="POST",
            path="/v1/assessments",
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
            get_serialized_body=lambda: utils.serialize_request_body(request.body, False, False, "json", models.shared.AssessmentRequest),
            allow_empty_value=None,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig("backoff", utils.BackoffStrategy(500, 8000, 2, 30000), True)

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "408",
                "429",
                "5XX"
            ])

        def _noresponse_parse_response(http_res):


            response_data: Any = None
            if utils.match_response(http_res, ["200","202"], "application/json"):
                return models.operations.CreateAssessmentResponse(result=unmarshal_json_response(models.shared.Assessment, http_res )
                , headers=utils.get_response_headers(http_res.headers))
            if utils.match_response(http_res, "400", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.BadRequestErrorData, http_res)
                raise models.errors.BadRequestError(response_data, http_res)
            if utils.match_response(http_res, "401", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.AuthenticationErrorData, http_res)
                raise models.errors.AuthenticationError(response_data, http_res)
            if utils.match_response(http_res, "403", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.PermissionDeniedErrorData, http_res)
                raise models.errors.PermissionDeniedError(response_data, http_res)
            if utils.match_response(http_res, "404", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.NotFoundErrorData, http_res)
                raise models.errors.NotFoundError(response_data, http_res)
            if utils.match_response(http_res, "409", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.ConflictErrorData, http_res)
                raise models.errors.ConflictError(response_data, http_res)
            if utils.match_response(http_res, "429", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.RateLimitErrorData, http_res)
                raise models.errors.RateLimitError(response_data, http_res)
            if utils.match_response(http_res, "4XX", "*"):
                http_res_text =  utils.stream_to_text(http_res)
                raise models.errors.APIStatusError("API error occurred", http_res, http_res_text)
            if utils.match_response(http_res, "5XX", "*"):
                http_res_text =  utils.stream_to_text(http_res)
                raise models.errors.APIStatusError("API error occurred", http_res, http_res_text)

            raise models.errors.APIStatusError("Unexpected response received", http_res)
        _noresponse_hook_ctx = HookContext(config=self.sdk_configuration, base_url=base_url or "", operation_id="createAssessment", oauth2_scopes=None, security_source=get_security_from_env(self.sdk_configuration.security, models.shared.Security), tags=["assessments"], extensions=None, response=ResponseContext(mode=_noresponse_response_mode, execution="sync"))
        http_res = self.do_request(
            hook_ctx=_noresponse_hook_ctx,
            request=req,
            is_error_status_code=lambda c: utils.match_status_codes(["4XX","5XX"], c),
            stream=_noresponse_response_mode == "streaming",
            retry_config=retry_config
        )
        if _noresponse_response_mode != "parsed":
            if utils.match_status_codes(["4XX","5XX"], http_res.status_code):
                http_res.read()
                try:
                    _noresponse_parse_response(http_res)
                except Exception as parse_exc_:
                    response_helpers.raise_parse_error(self.sdk_configuration.__dict__['_hooks'],
                        AfterParseErrorContext(_noresponse_hook_ctx),
                        http_res,
                        parse_exc_,
                    )
            _noresponse_response_cls = (
                response_helpers.StreamedAPIResponse
                if _noresponse_response_mode == "streaming"
                else response_helpers.APIResponse
            )
            return cast(Any, _noresponse_response_cls(
                raw=http_res,
                parser=_noresponse_parse_response,
                mode="buffered",
                client_ref=self,
                hook_ctx=AfterParseErrorContext(_noresponse_hook_ctx),
                hooks=self.sdk_configuration.__dict__.get("_hooks"),

            ))
        try:
            return _noresponse_parse_response(http_res)
        except Exception as parse_exc_:
            response_helpers.raise_parse_error(self.sdk_configuration.__dict__['_hooks'],
                AfterParseErrorContext(_noresponse_hook_ctx),
                http_res,
                parse_exc_,
            ) and whitespace are refused by the pattern, as is an exact-shape JWT; a hex digest such as a SHA-256 is allowed, because hashing an internal id is a common pseudonymous scheme. A value such as '07700900123' or 'jane.doe.gmail.com' cannot be told apart from an opaque id. It travels in bodies, and in a URL only as the path segment of GET /v1/accounts/{account_id}, its /assessments and its /linked_accounts. An assessment requested by a provider hook at pre_registration, which has no account yet, carries the server-issued account_id pre: followed by its assessment_id.
        :param flow: The event an assessment is made for: account_creation (a user creates an account), login (a user returns to an existing account) or purchase (a payment or a credit grant). The account's risk is reported with the decision for this flow.
        :param identifiers: At least one of email, username or phone. name and ip refine the match and travel beside a lookup identifier; a body with only name or ip is refused with 400.
        :param depth: How long the synchronous answer waits for sources. quick waits only for the fast sources, those that answer within 500 ms of ingress (or deadline_ms when lower); full waits for the whole budget, up to 3000 ms. Sources still running at the cut continue asynchronously and update the assessment either way.
        :param policy_context: Optional policy inputs: region.
        :param request_id: An optional provider correlation id, echoed back. It is not an idempotency key. Refuses an exact-shape JWT or a bare 40, 64 or 128 character hex digest; a UUID is accepted.
        :param deadline_ms: Optional tighter budget, 50 to 3000 ms, measured from the moment the request reaches NoResponse. Absent means the 3000 ms ceiling; a value above it is refused with 400 rather than clamped.
        :param response_mode: standard returns the consolidated risk response; detailed adds merged provider-neutral facts when the key has detailed scope. There is no raw mode.
        :param client_context: Optional context observed by the client of the user. The server parses these hints into coarse features, leaves raw user_agent and opaque ids out of every answer, and weighs a mismatch with the other evidence.
        :param auth_context: Normalised claims from a session your backend has already verified with WorkOS, Clerk, Auth0 or any OIDC provider. Pass the output of the SDK's auth adapters, not a raw token.
        :param issued_credential: Optional. When your platform issues an API key to the new account, send SHA-256 of that key, so later usage of the key, or a leaked copy, ties back to this assessment. Each SDK has a helper that computes it. Send only the hash: customer keys are high-entropy, so the hash reveals nothing about them. The assessment stores it, and no response, webhook or log carries it.
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

        request = models.operations.CreateAssessmentRequest(
            idempotency_key=idempotency_key,
            body=models.shared.AssessmentRequest(
                account_id=account_id,
                flow=flow,
                depth=depth,
                identifiers=utils.get_pydantic_model(
                    identifiers, models.shared.AssessmentRequestIdentifiers
                ),
                policy_context=utils.get_pydantic_model(
                    policy_context,
                    Optional[models.shared.AssessmentRequestPolicyContext],
                ),
                request_id=request_id,
                deadline_ms=deadline_ms,
                response_mode=response_mode,
                client_context=utils.get_pydantic_model(
                    client_context,
                    Optional[models.shared.AssessmentRequestClientContext],
                ),
                auth_context=utils.get_pydantic_model(
                    auth_context, Optional[models.shared.AuthContext]
                ),
                issued_credential=utils.get_pydantic_model(
                    issued_credential,
                    Optional[models.shared.AssessmentRequestIssuedCredential],
                ),
            ),
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="POST",
            path="/v1/assessments",
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
                request.body, False, False, "json", models.shared.AssessmentRequest
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
            if utils.match_response(http_res, ["200", "202"], "application/json"):
                return models.operations.CreateAssessmentResponse(
                    result=unmarshal_json_response(models.shared.Assessment, http_res),
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
            operation_id="createAssessment",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["assessments"],
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

    async def create_async(
        self,
        *,
        idempotency_key: str,
        account_id: str,
        flow: models.shared.Flow,
        identifiers: Union[
            models.shared.AssessmentRequestIdentifiers,
            models.shared.AssessmentRequestIdentifiersTypedDict,
        ],
        depth: Optional[models.shared.Depth] = None,
        policy_context: Optional[
            Union[
                models.shared.AssessmentRequestPolicyContext,
                models.shared.AssessmentRequestPolicyContextTypedDict,
            ]
        ] = None,
        request_id: Optional[str] = None,
        deadline_ms: Optional[int] = None,
        response_mode: Optional[models.shared.ResponseMode] = None,
        client_context: Optional[
            Union[
                models.shared.AssessmentRequestClientContext,
                models.shared.AssessmentRequestClientContextTypedDict,
            ]
        ] = None,
        auth_context: Optional[
            Union[models.shared.AuthContext, models.shared.AuthContextTypedDict]
        ] = None,
        issued_credential: Optional[
            Union[
                models.shared.AssessmentRequestIssuedCredential,
                models.shared.AssessmentRequestIssuedCredentialTypedDict,
            ]
        ] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.CreateAssessmentResponse:
        r"""Assess identifiers for a signup or gateway decision.

        Assesses one account creation, login or purchase (flow) and answers with the account's one current risk: account.risk.decision is the decision for this flow (allow, step_up, review or block, where block means your block threshold was reached), and detail holds this assessment's own facts. depth sets how long the answer waits for sources: quick waits only for the fast ones (500 ms), full for the whole budget (3000 ms at most); it defaults to full for account_creation and purchase and quick for login. 200 carries complete or partial, 202 carries pending with Location and Retry-After. While the account's first assessment is pending, account is absent: apply your own fallback for that, 429, 503 or a timeout. NoResponse blocks nothing itself; you decide. Requires the assess scope. Idempotency-Key is required and is bound to the body for 24 hours: the same key with the same body replays the latest assessment with Idempotent-Replayed: true and starts no new work; the same key with a different body answers 409 idempotency_key_reused. response_mode defaults to standard; detailed needs the detailed scope. The answer leaves out detail.identifiers: you hold what you sent, and a key with the history scope gets them back with GET.

        :param idempotency_key: Opaque client key, 16 to 128 characters of [A-Za-z0-9._:-] (a UUID or ULID fits). Scoped to the workspace principal and bound to the canonical body for 24 hours.
        :param account_id: Your own opaque identifier for the account being checked, scoped to your workspace. Use an id you mint, with no direct identifier (email, phone, name or national id) in it. '|' is accepted so an Auth0 user id such as 'auth0|64abc' passes unchanged; '@', '+', '
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.operations.CreateAssessmentRequest(
            idempotency_key=idempotency_key,
            body=models.shared.AssessmentRequest(
                account_id=account_id,
                flow=flow,
                depth=depth,
                identifiers=utils.get_pydantic_model(identifiers, models.shared.AssessmentRequestIdentifiers),
                policy_context=utils.get_pydantic_model(policy_context, Optional[models.shared.AssessmentRequestPolicyContext]),
                request_id=request_id,
                deadline_ms=deadline_ms,
                response_mode=response_mode,
                client_context=utils.get_pydantic_model(client_context, Optional[models.shared.AssessmentRequestClientContext]),
                auth_context=utils.get_pydantic_model(auth_context, Optional[models.shared.AuthContext]),
                issued_credential=utils.get_pydantic_model(issued_credential, Optional[models.shared.AssessmentRequestIssuedCredential]),
            ),
        )

        _noresponse_response_mode, http_headers = response_helpers.consume_response_mode(http_headers)
        req = self._build_request_async(
            method="POST",
            path="/v1/assessments",
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
            get_serialized_body=lambda: utils.serialize_request_body(request.body, False, False, "json", models.shared.AssessmentRequest),
            allow_empty_value=None,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig("backoff", utils.BackoffStrategy(500, 8000, 2, 30000), True)

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "408",
                "429",
                "5XX"
            ])

        async def _noresponse_parse_response(http_res):


            response_data: Any = None
            if utils.match_response(http_res, ["200","202"], "application/json"):
                return models.operations.CreateAssessmentResponse(result=unmarshal_json_response(models.shared.Assessment, http_res )
                , headers=utils.get_response_headers(http_res.headers))
            if utils.match_response(http_res, "400", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.BadRequestErrorData, http_res)
                raise models.errors.BadRequestError(response_data, http_res)
            if utils.match_response(http_res, "401", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.AuthenticationErrorData, http_res)
                raise models.errors.AuthenticationError(response_data, http_res)
            if utils.match_response(http_res, "403", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.PermissionDeniedErrorData, http_res)
                raise models.errors.PermissionDeniedError(response_data, http_res)
            if utils.match_response(http_res, "404", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.NotFoundErrorData, http_res)
                raise models.errors.NotFoundError(response_data, http_res)
            if utils.match_response(http_res, "409", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.ConflictErrorData, http_res)
                raise models.errors.ConflictError(response_data, http_res)
            if utils.match_response(http_res, "429", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.RateLimitErrorData, http_res)
                raise models.errors.RateLimitError(response_data, http_res)
            if utils.match_response(http_res, "4XX", "*"):
                http_res_text = await utils.stream_to_text_async(http_res)
                raise models.errors.APIStatusError("API error occurred", http_res, http_res_text)
            if utils.match_response(http_res, "5XX", "*"):
                http_res_text = await utils.stream_to_text_async(http_res)
                raise models.errors.APIStatusError("API error occurred", http_res, http_res_text)

            raise models.errors.APIStatusError("Unexpected response received", http_res)
        _noresponse_hook_ctx = HookContext(config=self.sdk_configuration, base_url=base_url or "", operation_id="createAssessment", oauth2_scopes=None, security_source=get_security_from_env(self.sdk_configuration.security, models.shared.Security), tags=["assessments"], extensions=None, response=ResponseContext(mode=_noresponse_response_mode, execution="async"))
        http_res = await self.do_request_async(
            hook_ctx=_noresponse_hook_ctx,
            request=req,
            is_error_status_code=lambda c: utils.match_status_codes(["4XX","5XX"], c),
            stream=_noresponse_response_mode == "streaming",
            retry_config=retry_config
        )
        if _noresponse_response_mode != "parsed":
            if utils.match_status_codes(["4XX","5XX"], http_res.status_code):
                await http_res.aread()
                try:
                    await _noresponse_parse_response(http_res)
                except Exception as parse_exc_:
                    await response_helpers.raise_parse_error_async(self.sdk_configuration.__dict__.get('_async_hooks'), self.sdk_configuration.__dict__.get('_hooks'),
                        AfterParseErrorContext(_noresponse_hook_ctx),
                        http_res,
                        parse_exc_,
                    )
            _noresponse_response_cls = (
                response_helpers.AsyncStreamedAPIResponse
                if _noresponse_response_mode == "streaming"
                else response_helpers.AsyncAPIResponse
            )
            return cast(Any, _noresponse_response_cls(
                raw=http_res,
                parser=_noresponse_parse_response,
                mode="buffered",
                client_ref=self,
                hook_ctx=AfterParseErrorContext(_noresponse_hook_ctx),
                hooks=self.sdk_configuration.__dict__.get("_hooks"),
                async_hooks=self.sdk_configuration.__dict__.get('_async_hooks'),
            ))
        try:
            return await _noresponse_parse_response(http_res)
        except Exception as parse_exc_:
            await response_helpers.raise_parse_error_async(self.sdk_configuration.__dict__.get('_async_hooks'), self.sdk_configuration.__dict__.get('_hooks'),
                AfterParseErrorContext(_noresponse_hook_ctx),
                http_res,
                parse_exc_,
            ) and whitespace are refused by the pattern, as is an exact-shape JWT; a hex digest such as a SHA-256 is allowed, because hashing an internal id is a common pseudonymous scheme. A value such as '07700900123' or 'jane.doe.gmail.com' cannot be told apart from an opaque id. It travels in bodies, and in a URL only as the path segment of GET /v1/accounts/{account_id}, its /assessments and its /linked_accounts. An assessment requested by a provider hook at pre_registration, which has no account yet, carries the server-issued account_id pre: followed by its assessment_id.
        :param flow: The event an assessment is made for: account_creation (a user creates an account), login (a user returns to an existing account) or purchase (a payment or a credit grant). The account's risk is reported with the decision for this flow.
        :param identifiers: At least one of email, username or phone. name and ip refine the match and travel beside a lookup identifier; a body with only name or ip is refused with 400.
        :param depth: How long the synchronous answer waits for sources. quick waits only for the fast sources, those that answer within 500 ms of ingress (or deadline_ms when lower); full waits for the whole budget, up to 3000 ms. Sources still running at the cut continue asynchronously and update the assessment either way.
        :param policy_context: Optional policy inputs: region.
        :param request_id: An optional provider correlation id, echoed back. It is not an idempotency key. Refuses an exact-shape JWT or a bare 40, 64 or 128 character hex digest; a UUID is accepted.
        :param deadline_ms: Optional tighter budget, 50 to 3000 ms, measured from the moment the request reaches NoResponse. Absent means the 3000 ms ceiling; a value above it is refused with 400 rather than clamped.
        :param response_mode: standard returns the consolidated risk response; detailed adds merged provider-neutral facts when the key has detailed scope. There is no raw mode.
        :param client_context: Optional context observed by the client of the user. The server parses these hints into coarse features, leaves raw user_agent and opaque ids out of every answer, and weighs a mismatch with the other evidence.
        :param auth_context: Normalised claims from a session your backend has already verified with WorkOS, Clerk, Auth0 or any OIDC provider. Pass the output of the SDK's auth adapters, not a raw token.
        :param issued_credential: Optional. When your platform issues an API key to the new account, send SHA-256 of that key, so later usage of the key, or a leaked copy, ties back to this assessment. Each SDK has a helper that computes it. Send only the hash: customer keys are high-entropy, so the hash reveals nothing about them. The assessment stores it, and no response, webhook or log carries it.
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

        request = models.operations.CreateAssessmentRequest(
            idempotency_key=idempotency_key,
            body=models.shared.AssessmentRequest(
                account_id=account_id,
                flow=flow,
                depth=depth,
                identifiers=utils.get_pydantic_model(
                    identifiers, models.shared.AssessmentRequestIdentifiers
                ),
                policy_context=utils.get_pydantic_model(
                    policy_context,
                    Optional[models.shared.AssessmentRequestPolicyContext],
                ),
                request_id=request_id,
                deadline_ms=deadline_ms,
                response_mode=response_mode,
                client_context=utils.get_pydantic_model(
                    client_context,
                    Optional[models.shared.AssessmentRequestClientContext],
                ),
                auth_context=utils.get_pydantic_model(
                    auth_context, Optional[models.shared.AuthContext]
                ),
                issued_credential=utils.get_pydantic_model(
                    issued_credential,
                    Optional[models.shared.AssessmentRequestIssuedCredential],
                ),
            ),
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="POST",
            path="/v1/assessments",
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
                request.body, False, False, "json", models.shared.AssessmentRequest
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
            if utils.match_response(http_res, ["200", "202"], "application/json"):
                return models.operations.CreateAssessmentResponse(
                    result=unmarshal_json_response(models.shared.Assessment, http_res),
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
            operation_id="createAssessment",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["assessments"],
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

    def get(
        self,
        assessment_id: str,
        *,
        response_mode: Optional[models.shared.ResponseMode] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.GetAssessmentResponse:
        r"""Poll the authoritative assessment of one assessment.

        Returns the highest assessment_version, with the account's current risk. Requires the assess or history scope. While status is pending, or partial with a source still running, the response carries Retry-After; poll no faster than it says. Another workspace's assessment, an unknown or expired assessment and a malformed assessment_id all answer 404 not_found. response_mode=detailed needs the detailed scope. A key with the history scope also gets detail.identifiers, the identifiers the assessment was sent, exactly as received.

        :param assessment_id: Path segment, matched case-sensitively. A value that does not match the assessment_id shape answers 404, not 400.
        :param response_mode: Optional standard or separately authorised detailed customer view; raw is rejected.
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

        request = models.operations.GetAssessmentRequest(
            assessment_id=assessment_id,
            response_mode=response_mode,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="GET",
            path="/v1/assessments/{assessment_id}",
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
                return models.operations.GetAssessmentResponse(
                    result=unmarshal_json_response(models.shared.Assessment, http_res),
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
            operation_id="getAssessment",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["assessments"],
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
        assessment_id: str,
        *,
        response_mode: Optional[models.shared.ResponseMode] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.GetAssessmentResponse:
        r"""Poll the authoritative assessment of one assessment.

        Returns the highest assessment_version, with the account's current risk. Requires the assess or history scope. While status is pending, or partial with a source still running, the response carries Retry-After; poll no faster than it says. Another workspace's assessment, an unknown or expired assessment and a malformed assessment_id all answer 404 not_found. response_mode=detailed needs the detailed scope. A key with the history scope also gets detail.identifiers, the identifiers the assessment was sent, exactly as received.

        :param assessment_id: Path segment, matched case-sensitively. A value that does not match the assessment_id shape answers 404, not 400.
        :param response_mode: Optional standard or separately authorised detailed customer view; raw is rejected.
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

        request = models.operations.GetAssessmentRequest(
            assessment_id=assessment_id,
            response_mode=response_mode,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="GET",
            path="/v1/assessments/{assessment_id}",
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
                return models.operations.GetAssessmentResponse(
                    result=unmarshal_json_response(models.shared.Assessment, http_res),
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
            operation_id="getAssessment",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["assessments"],
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
        assessment_id: str,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.DeleteAssessmentResponse:
        r"""Delete one assessment.

        Deletes one assessment in the environment of your key, with its versions, evidence and outcomes and the identity-graph marks its outcomes set, and scores its account again from what remains. Afterwards the assessment answers 404 and leaves the account's history. The answer names the account and the assessment its current risk now comes from; current_assessment_id is absent when the account has no assessment with a decision left. Requires the history scope. An unknown, expired or already deleted assessment answers 404, so a repeat answers 404; to erase a whole account idempotently, use accounts.delete.

        :param assessment_id: Path segment, matched case-sensitively. A value that does not match the assessment_id shape answers 404, not 400.
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

        request = models.operations.DeleteAssessmentRequest(
            assessment_id=assessment_id,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="DELETE",
            path="/v1/assessments/{assessment_id}",
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
                return models.operations.DeleteAssessmentResponse(
                    result=unmarshal_json_response(
                        models.shared.AssessmentDeletion, http_res
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
            operation_id="deleteAssessment",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["assessments"],
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
        assessment_id: str,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.DeleteAssessmentResponse:
        r"""Delete one assessment.

        Deletes one assessment in the environment of your key, with its versions, evidence and outcomes and the identity-graph marks its outcomes set, and scores its account again from what remains. Afterwards the assessment answers 404 and leaves the account's history. The answer names the account and the assessment its current risk now comes from; current_assessment_id is absent when the account has no assessment with a decision left. Requires the history scope. An unknown, expired or already deleted assessment answers 404, so a repeat answers 404; to erase a whole account idempotently, use accounts.delete.

        :param assessment_id: Path segment, matched case-sensitively. A value that does not match the assessment_id shape answers 404, not 400.
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

        request = models.operations.DeleteAssessmentRequest(
            assessment_id=assessment_id,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="DELETE",
            path="/v1/assessments/{assessment_id}",
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
                return models.operations.DeleteAssessmentResponse(
                    result=unmarshal_json_response(
                        models.shared.AssessmentDeletion, http_res
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
            operation_id="deleteAssessment",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["assessments"],
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

    def record_outcome(
        self,
        assessment_id: str,
        *,
        idempotency_key: str,
        outcome: models.shared.Outcome,
        observed_at: Optional[str] = None,
        external_ref: Optional[str] = None,
        notes: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.RecordAssessmentOutcomeResponse:
        r"""Report what was later learned about an assessed account.

        Records what you later learned about an assessed account: confirmed_abuse, account_takeover and chargeback report abuse; false_positive and legitimate withdraw your earlier report; unknown is recorded only. Outcomes are append-only and the latest one wins. Requires the assess scope. Idempotency-Key is required and handled as on POST /v1/assessments: a retry with the same key and body answers the same record with Idempotent-Replayed: true; a different body answers 409. An unknown, expired or foreign assessment answers 404 not_found.

        :param assessment_id: Path segment, matched case-sensitively. A value that does not match the assessment_id shape answers 404, not 400.
        :param idempotency_key: Opaque client key, 16 to 128 characters of [A-Za-z0-9._:-] (a UUID or ULID fits). Scoped to the workspace principal and bound to the canonical body for 24 hours.
        :param outcome: What the provider later learned about the assessed account. confirmed_abuse, account_takeover and chargeback report abuse; false_positive and legitimate withdraw an earlier abuse report of this workspace for the assessment; unknown is recorded only. Outcomes are append-only and the latest one recorded for an assessment wins.
        :param observed_at: When the provider observed the outcome. Defaults to when NoResponse received it.
        :param external_ref: Your own opaque reference for the outcome, such as a case or ticket id. Stored as given and not interpreted; keep direct identifiers out of it.
        :param notes: Free text for your own records, at most 500 characters. Stored only; it is left out of scoring and answers. Keep personal data out of it. Control characters other than tab and line breaks are refused.
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

        request = models.operations.RecordAssessmentOutcomeRequest(
            assessment_id=assessment_id,
            idempotency_key=idempotency_key,
            body=models.shared.AssessmentOutcomeRequest(
                outcome=outcome,
                observed_at=observed_at,
                external_ref=external_ref,
                notes=notes,
            ),
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="POST",
            path="/v1/assessments/{assessment_id}/outcomes",
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
                models.shared.AssessmentOutcomeRequest,
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
                return models.operations.RecordAssessmentOutcomeResponse(
                    result=unmarshal_json_response(
                        models.shared.AssessmentOutcome, http_res
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
            operation_id="recordAssessmentOutcome",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["assessments"],
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

    async def record_outcome_async(
        self,
        assessment_id: str,
        *,
        idempotency_key: str,
        outcome: models.shared.Outcome,
        observed_at: Optional[str] = None,
        external_ref: Optional[str] = None,
        notes: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.RecordAssessmentOutcomeResponse:
        r"""Report what was later learned about an assessed account.

        Records what you later learned about an assessed account: confirmed_abuse, account_takeover and chargeback report abuse; false_positive and legitimate withdraw your earlier report; unknown is recorded only. Outcomes are append-only and the latest one wins. Requires the assess scope. Idempotency-Key is required and handled as on POST /v1/assessments: a retry with the same key and body answers the same record with Idempotent-Replayed: true; a different body answers 409. An unknown, expired or foreign assessment answers 404 not_found.

        :param assessment_id: Path segment, matched case-sensitively. A value that does not match the assessment_id shape answers 404, not 400.
        :param idempotency_key: Opaque client key, 16 to 128 characters of [A-Za-z0-9._:-] (a UUID or ULID fits). Scoped to the workspace principal and bound to the canonical body for 24 hours.
        :param outcome: What the provider later learned about the assessed account. confirmed_abuse, account_takeover and chargeback report abuse; false_positive and legitimate withdraw an earlier abuse report of this workspace for the assessment; unknown is recorded only. Outcomes are append-only and the latest one recorded for an assessment wins.
        :param observed_at: When the provider observed the outcome. Defaults to when NoResponse received it.
        :param external_ref: Your own opaque reference for the outcome, such as a case or ticket id. Stored as given and not interpreted; keep direct identifiers out of it.
        :param notes: Free text for your own records, at most 500 characters. Stored only; it is left out of scoring and answers. Keep personal data out of it. Control characters other than tab and line breaks are refused.
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

        request = models.operations.RecordAssessmentOutcomeRequest(
            assessment_id=assessment_id,
            idempotency_key=idempotency_key,
            body=models.shared.AssessmentOutcomeRequest(
                outcome=outcome,
                observed_at=observed_at,
                external_ref=external_ref,
                notes=notes,
            ),
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="POST",
            path="/v1/assessments/{assessment_id}/outcomes",
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
                models.shared.AssessmentOutcomeRequest,
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
                return models.operations.RecordAssessmentOutcomeResponse(
                    result=unmarshal_json_response(
                        models.shared.AssessmentOutcome, http_res
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
            operation_id="recordAssessmentOutcome",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["assessments"],
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

    def query(
        self,
        *,
        account_id: str,
        limit: Optional[int] = 20,
        cursor: Optional[str] = None,
        response_mode: Optional[models.shared.ResponseMode] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Optional[models.operations.QueryAccountAssessmentsResponse]:
        r"""Page through one account's unexpired assessments.

        History is a POST with account_id in the body so an account identifier stays out of URLs and access logs. Requires the history scope. Read-only and safe to retry. Newest first, each at its latest assessment_version. An account with no assessments answers 200 with empty items. The cursor is opaque and bound to your workspace and the account; a tampered or expired cursor answers 400 invalid_cursor. response_mode=detailed needs the detailed scope. Each item's identifiers holds the identifiers its assessment was sent, exactly as received.

        :param account_id: Your own opaque identifier for the account being checked, scoped to your workspace. Use an id you mint, with no direct identifier (email, phone, name or national id) in it. '|' is accepted so an Auth0 user id such as 'auth0|64abc' passes unchanged; '@', '+', '
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.shared.AssessmentQuery(
            account_id=account_id,
            limit=limit,
            cursor=cursor,
            response_mode=response_mode,
        )

        _noresponse_response_mode, http_headers = response_helpers.consume_response_mode(http_headers)
        req = self._build_request(
            method="POST",
            path="/v1/assessments/query",
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
            get_serialized_body=lambda: utils.serialize_request_body(request, False, False, "json", models.shared.AssessmentQuery),
            allow_empty_value=None,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig("backoff", utils.BackoffStrategy(500, 8000, 2, 30000), True)

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "408",
                "429",
                "5XX"
            ])

        def _noresponse_parse_response(http_res):

            def next_func() -> Optional[models.operations.QueryAccountAssessmentsResponse]:
                body = utils.unmarshal_json(http_res.text, Union[Dict[Any, Any], List[Any]])



                next_cursor = JSONPath("$.next_cursor").parse(body)

                if len(next_cursor) == 0:
                    return None

                next_cursor = next_cursor[0]
                if next_cursor is None or str(next_cursor).strip() == "":
                    return None

                return self.query(
                    account_id=account_id,
                    limit=limit,
                    cursor=next_cursor,
                    response_mode=response_mode,
                    retries=retries,
                    server_url=server_url,
                    timeout_ms=timeout_ms,
                    http_headers=http_headers,
                )


            response_data: Any = None
            if utils.match_response(http_res, "200", "application/json"):
                return models.operations.QueryAccountAssessmentsResponse(result=unmarshal_json_response(models.shared.AssessmentList, http_res )
                , next=next_func, headers=utils.get_response_headers(http_res.headers))
            if utils.match_response(http_res, "400", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.BadRequestErrorData, http_res)
                raise models.errors.BadRequestError(response_data, http_res)
            if utils.match_response(http_res, "401", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.AuthenticationErrorData, http_res)
                raise models.errors.AuthenticationError(response_data, http_res)
            if utils.match_response(http_res, "403", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.PermissionDeniedErrorData, http_res)
                raise models.errors.PermissionDeniedError(response_data, http_res)
            if utils.match_response(http_res, "404", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.NotFoundErrorData, http_res)
                raise models.errors.NotFoundError(response_data, http_res)
            if utils.match_response(http_res, "409", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.ConflictErrorData, http_res)
                raise models.errors.ConflictError(response_data, http_res)
            if utils.match_response(http_res, "429", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.RateLimitErrorData, http_res)
                raise models.errors.RateLimitError(response_data, http_res)
            if utils.match_response(http_res, "4XX", "*"):
                http_res_text =  utils.stream_to_text(http_res)
                raise models.errors.APIStatusError("API error occurred", http_res, http_res_text)
            if utils.match_response(http_res, "5XX", "*"):
                http_res_text =  utils.stream_to_text(http_res)
                raise models.errors.APIStatusError("API error occurred", http_res, http_res_text)

            raise models.errors.APIStatusError("Unexpected response received", http_res)
        _noresponse_hook_ctx = HookContext(config=self.sdk_configuration, base_url=base_url or "", operation_id="queryAccountAssessments", oauth2_scopes=None, security_source=get_security_from_env(self.sdk_configuration.security, models.shared.Security), tags=["assessments"], extensions=None, response=ResponseContext(mode=_noresponse_response_mode, execution="sync"))
        http_res = self.do_request(
            hook_ctx=_noresponse_hook_ctx,
            request=req,
            is_error_status_code=lambda c: utils.match_status_codes(["4XX","5XX"], c),
            stream=_noresponse_response_mode == "streaming",
            retry_config=retry_config
        )
        if _noresponse_response_mode != "parsed":
            if utils.match_status_codes(["4XX","5XX"], http_res.status_code):
                http_res.read()
                try:
                    _noresponse_parse_response(http_res)
                except Exception as parse_exc_:
                    response_helpers.raise_parse_error(self.sdk_configuration.__dict__['_hooks'],
                        AfterParseErrorContext(_noresponse_hook_ctx),
                        http_res,
                        parse_exc_,
                    )
            _noresponse_response_cls = (
                response_helpers.StreamedAPIResponse
                if _noresponse_response_mode == "streaming"
                else response_helpers.APIResponse
            )
            return cast(Any, _noresponse_response_cls(
                raw=http_res,
                parser=_noresponse_parse_response,
                mode="buffered",
                client_ref=self,
                hook_ctx=AfterParseErrorContext(_noresponse_hook_ctx),
                hooks=self.sdk_configuration.__dict__.get("_hooks"),

            ))
        try:
            return _noresponse_parse_response(http_res)
        except Exception as parse_exc_:
            response_helpers.raise_parse_error(self.sdk_configuration.__dict__['_hooks'],
                AfterParseErrorContext(_noresponse_hook_ctx),
                http_res,
                parse_exc_,
            ) and whitespace are refused by the pattern, as is an exact-shape JWT; a hex digest such as a SHA-256 is allowed, because hashing an internal id is a common pseudonymous scheme. A value such as '07700900123' or 'jane.doe.gmail.com' cannot be told apart from an opaque id. It travels in bodies, and in a URL only as the path segment of GET /v1/accounts/{account_id}, its /assessments and its /linked_accounts. An assessment requested by a provider hook at pre_registration, which has no account yet, carries the server-issued account_id pre: followed by its assessment_id.
        :param limit:
        :param cursor: next_cursor from the previous page, unchanged. Opaque, MAC'd and bound to the workspace and account_id.
        :param response_mode: standard returns the consolidated risk response; detailed adds merged provider-neutral facts when the key has detailed scope. There is no raw mode.
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

        request = models.shared.AssessmentQuery(
            account_id=account_id,
            limit=limit,
            cursor=cursor,
            response_mode=response_mode,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="POST",
            path="/v1/assessments/query",
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
                request, False, False, "json", models.shared.AssessmentQuery
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
            def next_func() -> (
                Optional[models.operations.QueryAccountAssessmentsResponse]
            ):
                body = utils.unmarshal_json(
                    http_res.text, Union[Dict[Any, Any], List[Any]]
                )

                next_cursor = JSONPath("$.next_cursor").parse(body)

                if len(next_cursor) == 0:
                    return None

                next_cursor = next_cursor[0]
                if next_cursor is None or str(next_cursor).strip() == "":
                    return None

                return self.query(
                    account_id=account_id,
                    limit=limit,
                    cursor=next_cursor,
                    response_mode=response_mode,
                    retries=retries,
                    server_url=server_url,
                    timeout_ms=timeout_ms,
                    http_headers=http_headers,
                )

            response_data: Any = None
            if utils.match_response(http_res, "200", "application/json"):
                return models.operations.QueryAccountAssessmentsResponse(
                    result=unmarshal_json_response(
                        models.shared.AssessmentList, http_res
                    ),
                    next=next_func,
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
            operation_id="queryAccountAssessments",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["assessments"],
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

    async def query_async(
        self,
        *,
        account_id: str,
        limit: Optional[int] = 20,
        cursor: Optional[str] = None,
        response_mode: Optional[models.shared.ResponseMode] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Optional[models.operations.QueryAccountAssessmentsResponse]:
        r"""Page through one account's unexpired assessments.

        History is a POST with account_id in the body so an account identifier stays out of URLs and access logs. Requires the history scope. Read-only and safe to retry. Newest first, each at its latest assessment_version. An account with no assessments answers 200 with empty items. The cursor is opaque and bound to your workspace and the account; a tampered or expired cursor answers 400 invalid_cursor. response_mode=detailed needs the detailed scope. Each item's identifiers holds the identifiers its assessment was sent, exactly as received.

        :param account_id: Your own opaque identifier for the account being checked, scoped to your workspace. Use an id you mint, with no direct identifier (email, phone, name or national id) in it. '|' is accepted so an Auth0 user id such as 'auth0|64abc' passes unchanged; '@', '+', '
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.shared.AssessmentQuery(
            account_id=account_id,
            limit=limit,
            cursor=cursor,
            response_mode=response_mode,
        )

        _noresponse_response_mode, http_headers = response_helpers.consume_response_mode(http_headers)
        req = self._build_request_async(
            method="POST",
            path="/v1/assessments/query",
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
            get_serialized_body=lambda: utils.serialize_request_body(request, False, False, "json", models.shared.AssessmentQuery),
            allow_empty_value=None,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig("backoff", utils.BackoffStrategy(500, 8000, 2, 30000), True)

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "408",
                "429",
                "5XX"
            ])

        async def _noresponse_parse_response(http_res):

            def next_func() -> Awaitable[Optional[models.operations.QueryAccountAssessmentsResponse]]:
                body = utils.unmarshal_json(http_res.text, Union[Dict[Any, Any], List[Any]])
                async def empty_result(): return None


                next_cursor = JSONPath("$.next_cursor").parse(body)

                if len(next_cursor) == 0:
                    return empty_result()

                next_cursor = next_cursor[0]
                if next_cursor is None or str(next_cursor).strip() == "":
                    return empty_result()

                return self.query_async(
                    account_id=account_id,
                    limit=limit,
                    cursor=next_cursor,
                    response_mode=response_mode,
                    retries=retries,
                    server_url=server_url,
                    timeout_ms=timeout_ms,
                    http_headers=http_headers,
                )


            response_data: Any = None
            if utils.match_response(http_res, "200", "application/json"):
                return models.operations.QueryAccountAssessmentsResponse(result=unmarshal_json_response(models.shared.AssessmentList, http_res )
                , next=next_func, headers=utils.get_response_headers(http_res.headers))
            if utils.match_response(http_res, "400", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.BadRequestErrorData, http_res)
                raise models.errors.BadRequestError(response_data, http_res)
            if utils.match_response(http_res, "401", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.AuthenticationErrorData, http_res)
                raise models.errors.AuthenticationError(response_data, http_res)
            if utils.match_response(http_res, "403", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.PermissionDeniedErrorData, http_res)
                raise models.errors.PermissionDeniedError(response_data, http_res)
            if utils.match_response(http_res, "404", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.NotFoundErrorData, http_res)
                raise models.errors.NotFoundError(response_data, http_res)
            if utils.match_response(http_res, "409", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.ConflictErrorData, http_res)
                raise models.errors.ConflictError(response_data, http_res)
            if utils.match_response(http_res, "429", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.RateLimitErrorData, http_res)
                raise models.errors.RateLimitError(response_data, http_res)
            if utils.match_response(http_res, "4XX", "*"):
                http_res_text = await utils.stream_to_text_async(http_res)
                raise models.errors.APIStatusError("API error occurred", http_res, http_res_text)
            if utils.match_response(http_res, "5XX", "*"):
                http_res_text = await utils.stream_to_text_async(http_res)
                raise models.errors.APIStatusError("API error occurred", http_res, http_res_text)

            raise models.errors.APIStatusError("Unexpected response received", http_res)
        _noresponse_hook_ctx = HookContext(config=self.sdk_configuration, base_url=base_url or "", operation_id="queryAccountAssessments", oauth2_scopes=None, security_source=get_security_from_env(self.sdk_configuration.security, models.shared.Security), tags=["assessments"], extensions=None, response=ResponseContext(mode=_noresponse_response_mode, execution="async"))
        http_res = await self.do_request_async(
            hook_ctx=_noresponse_hook_ctx,
            request=req,
            is_error_status_code=lambda c: utils.match_status_codes(["4XX","5XX"], c),
            stream=_noresponse_response_mode == "streaming",
            retry_config=retry_config
        )
        if _noresponse_response_mode != "parsed":
            if utils.match_status_codes(["4XX","5XX"], http_res.status_code):
                await http_res.aread()
                try:
                    await _noresponse_parse_response(http_res)
                except Exception as parse_exc_:
                    await response_helpers.raise_parse_error_async(self.sdk_configuration.__dict__.get('_async_hooks'), self.sdk_configuration.__dict__.get('_hooks'),
                        AfterParseErrorContext(_noresponse_hook_ctx),
                        http_res,
                        parse_exc_,
                    )
            _noresponse_response_cls = (
                response_helpers.AsyncStreamedAPIResponse
                if _noresponse_response_mode == "streaming"
                else response_helpers.AsyncAPIResponse
            )
            return cast(Any, _noresponse_response_cls(
                raw=http_res,
                parser=_noresponse_parse_response,
                mode="buffered",
                client_ref=self,
                hook_ctx=AfterParseErrorContext(_noresponse_hook_ctx),
                hooks=self.sdk_configuration.__dict__.get("_hooks"),
                async_hooks=self.sdk_configuration.__dict__.get('_async_hooks'),
            ))
        try:
            return await _noresponse_parse_response(http_res)
        except Exception as parse_exc_:
            await response_helpers.raise_parse_error_async(self.sdk_configuration.__dict__.get('_async_hooks'), self.sdk_configuration.__dict__.get('_hooks'),
                AfterParseErrorContext(_noresponse_hook_ctx),
                http_res,
                parse_exc_,
            ) and whitespace are refused by the pattern, as is an exact-shape JWT; a hex digest such as a SHA-256 is allowed, because hashing an internal id is a common pseudonymous scheme. A value such as '07700900123' or 'jane.doe.gmail.com' cannot be told apart from an opaque id. It travels in bodies, and in a URL only as the path segment of GET /v1/accounts/{account_id}, its /assessments and its /linked_accounts. An assessment requested by a provider hook at pre_registration, which has no account yet, carries the server-issued account_id pre: followed by its assessment_id.
        :param limit:
        :param cursor: next_cursor from the previous page, unchanged. Opaque, MAC'd and bound to the workspace and account_id.
        :param response_mode: standard returns the consolidated risk response; detailed adds merged provider-neutral facts when the key has detailed scope. There is no raw mode.
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

        request = models.shared.AssessmentQuery(
            account_id=account_id,
            limit=limit,
            cursor=cursor,
            response_mode=response_mode,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="POST",
            path="/v1/assessments/query",
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
                request, False, False, "json", models.shared.AssessmentQuery
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
            def next_func() -> (
                Awaitable[Optional[models.operations.QueryAccountAssessmentsResponse]]
            ):
                body = utils.unmarshal_json(
                    http_res.text, Union[Dict[Any, Any], List[Any]]
                )

                async def empty_result():
                    return None

                next_cursor = JSONPath("$.next_cursor").parse(body)

                if len(next_cursor) == 0:
                    return empty_result()

                next_cursor = next_cursor[0]
                if next_cursor is None or str(next_cursor).strip() == "":
                    return empty_result()

                return self.query_async(
                    account_id=account_id,
                    limit=limit,
                    cursor=next_cursor,
                    response_mode=response_mode,
                    retries=retries,
                    server_url=server_url,
                    timeout_ms=timeout_ms,
                    http_headers=http_headers,
                )

            response_data: Any = None
            if utils.match_response(http_res, "200", "application/json"):
                return models.operations.QueryAccountAssessmentsResponse(
                    result=unmarshal_json_response(
                        models.shared.AssessmentList, http_res
                    ),
                    next=next_func,
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
            operation_id="queryAccountAssessments",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["assessments"],
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

    def aggregate(
        self,
        *,
        from_: str,
        to: str,
        bucket: models.shared.Bucket,
        time_zone: Optional[str] = "UTC",
        group_by: Optional[Iterable[models.shared.AggregateDimension]] = None,
        metrics: Optional[
            Iterable[models.shared.AssessmentAggregateRequestMetric]
        ] = None,
        limit: Optional[int] = 20,
        flow: Optional[models.shared.Flow] = None,
        status: Optional[models.shared.Status] = None,
        recommendation: Optional[models.shared.Recommendation] = None,
        decision: Optional[models.shared.Decision] = None,
        revision: Optional[models.shared.AnswerRevision] = None,
        population: Optional[models.shared.Population] = None,
        band: Optional[models.shared.Band] = None,
        reason: Optional[models.shared.ReasonCode] = None,
        impact: Optional[models.shared.Impact] = None,
        lane: Optional[models.shared.Lane] = None,
        country: Optional[str] = None,
        asn: Optional[int] = None,
        score_min: Optional[int] = None,
        score_max: Optional[int] = None,
        list_match: Optional[models.shared.ListMatch] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.AggregateAssessmentsResponse:
        r"""Count assessments by time, decision and reason

        Count this environment's assessments created in [from,to) by UTC hour, or by day or week from local midnight in time_zone (an IANA name, UTC by default; at most 92 days in a zone other than UTC), grouped by up to two of decision, flow, recommendation, band, reason, lane, country, asn and list_match. Each assessment counts once, by its first answer; late results do not count it again and appear in late_flips. Optional metrics add a score histogram per flow, that histogram by the latest reported outcome, and late account decision changes. from and to start a bucket and cover at most 366 days (31 for hour buckets) inside the retention period. The filters are search's and describe the first answer: send them to search with revision first to list a cell's assessments. Counts hold no identifier, stay when an assessment or account is deleted, and report reasons by code and impact band. No Idempotency-Key.

        :param from_: The first bucket's start.
        :param to: The end, excluded: the start of the bucket after the last.
        :param bucket: The period each count covers: an hour, or a day or a week (from Monday) in time_zone. Hour buckets are whole UTC hours in any time zone.
        :param time_zone: The IANA time zone whose local midnight starts each day and week bucket, such as Europe/London or Asia/Kolkata; daylight saving changes make those days 23 or 25 hours long. A name the zone database does not know is refused (400 invalid_request naming time_zone). Day and week buckets in a zone other than UTC cover at most 92 days (400 invalid_request naming to); a year of them reads too many hourly counts to answer in time. Hour buckets stay whole UTC hours. Bucket starts, from and to stay instants. With the default population, a zone whose local midnight falls inside a UTC hour (a half-hour offset such as Asia/Kolkata) is refused for day and week buckets, as those counts are kept by the hour; retained_first_answers counts it.
        :param group_by: At most two dimensions to count by, of which at most one is reason, lane, country or asn. An assessment counts once in each of its reasons and incomplete lanes, so those groups can add up to more than the bucket's count. With population retained_first_answers, both dimensions can be facets; counts cover retained first answers only.
        :param metrics: count: each bucket's count and groups. score_histogram: first answers by flow and 5-point score bucket. score_outcomes: the histogram's first answers that have a reported outcome, by flow, 5-point score bucket and the latest outcome reported for the assessment (POST /v1/assessments/{assessment_id}/outcomes); the rest of a bin has none reported. late_flips: changes of an assessment's account decision for its flow after its first answer, by from, to and delay.
        :param limit: The most groups answered: the largest over the whole range, then by value. groups_truncated says when there were more.
        :param flow: The event an assessment is made for: account_creation (a user creates an account), login (a user returns to an existing account) or purchase (a payment or a credit grant). The account's risk is reported with the decision for this flow.
        :param status: Processing state, separate from evidence coverage. complete: final; nothing is still running, but unsupported, failed or unanswered lanes remain in incomplete_sources. partial: a recommendation exists and evidence is incomplete; assessment_url identifies continuing work when present. pending: no recommendation yet; poll or wait for the webhook. Finished processing does not mean all sources answered.
        :param recommendation: The recommended action: allow, step_up or review. Your application applies it.
        :param decision: An assessment's own decision: block when its stored risk.block is true, otherwise its recommendation. It is not the account's decision or held-admission state.
        :param revision: Which answer of each assessment the filters describe: latest, the latest stored revision, or first, the first answer, as served when the assessment was first answered (POST /v1/assessments/aggregate counts first answers). A cell of an aggregate drills down to POST /v1/assessments/search with the same filters, revision first and the cell's bucket as from and to.
        :param population: first_answers uses anonymous counters that can include erased detail. retained_first_answers computes exact intersections over retained first answers within 31 days. Requests exceeding the 100000-record work budget are refused.
        :param band:
        :param reason: A stable reason code. New codes may appear; ignore any you do not know.
        :param impact: The selected reason's served impact band. Requires reason.
        :param lane: An evidence lane: accounts (account presence for email and username), phone, breach, domain (the email domain's registration) and ip.
        :param country:
        :param asn:
        :param score_min: Inclusive lower score bound. Pending answers without a score do not match.
        :param score_max: Inclusive upper score bound, at least score_min when both are supplied.
        :param list_match: The list action captured at the first answer. Requires revision first. Older answers without captured list state do not match, including none.
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

        request = models.shared.AssessmentAggregateRequest(
            from_=from_,
            to=to,
            bucket=bucket,
            time_zone=time_zone,
            group_by=utils.unmarshal(
                group_by, Optional[List[models.shared.AggregateDimension]]
            ),
            metrics=utils.unmarshal(
                metrics, Optional[List[models.shared.AssessmentAggregateRequestMetric]]
            ),
            limit=limit,
            flow=flow,
            status=status,
            recommendation=recommendation,
            decision=decision,
            revision=revision,
            population=population,
            band=band,
            reason=reason,
            impact=impact,
            lane=lane,
            country=country,
            asn=asn,
            score_min=score_min,
            score_max=score_max,
            list_match=list_match,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="POST",
            path="/v1/assessments/aggregate",
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
                request, False, False, "json", models.shared.AssessmentAggregateRequest
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
                return models.operations.AggregateAssessmentsResponse(
                    result=unmarshal_json_response(
                        models.shared.AssessmentAggregate, http_res
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
            operation_id="aggregateAssessments",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["assessments"],
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

    async def aggregate_async(
        self,
        *,
        from_: str,
        to: str,
        bucket: models.shared.Bucket,
        time_zone: Optional[str] = "UTC",
        group_by: Optional[Iterable[models.shared.AggregateDimension]] = None,
        metrics: Optional[
            Iterable[models.shared.AssessmentAggregateRequestMetric]
        ] = None,
        limit: Optional[int] = 20,
        flow: Optional[models.shared.Flow] = None,
        status: Optional[models.shared.Status] = None,
        recommendation: Optional[models.shared.Recommendation] = None,
        decision: Optional[models.shared.Decision] = None,
        revision: Optional[models.shared.AnswerRevision] = None,
        population: Optional[models.shared.Population] = None,
        band: Optional[models.shared.Band] = None,
        reason: Optional[models.shared.ReasonCode] = None,
        impact: Optional[models.shared.Impact] = None,
        lane: Optional[models.shared.Lane] = None,
        country: Optional[str] = None,
        asn: Optional[int] = None,
        score_min: Optional[int] = None,
        score_max: Optional[int] = None,
        list_match: Optional[models.shared.ListMatch] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.AggregateAssessmentsResponse:
        r"""Count assessments by time, decision and reason

        Count this environment's assessments created in [from,to) by UTC hour, or by day or week from local midnight in time_zone (an IANA name, UTC by default; at most 92 days in a zone other than UTC), grouped by up to two of decision, flow, recommendation, band, reason, lane, country, asn and list_match. Each assessment counts once, by its first answer; late results do not count it again and appear in late_flips. Optional metrics add a score histogram per flow, that histogram by the latest reported outcome, and late account decision changes. from and to start a bucket and cover at most 366 days (31 for hour buckets) inside the retention period. The filters are search's and describe the first answer: send them to search with revision first to list a cell's assessments. Counts hold no identifier, stay when an assessment or account is deleted, and report reasons by code and impact band. No Idempotency-Key.

        :param from_: The first bucket's start.
        :param to: The end, excluded: the start of the bucket after the last.
        :param bucket: The period each count covers: an hour, or a day or a week (from Monday) in time_zone. Hour buckets are whole UTC hours in any time zone.
        :param time_zone: The IANA time zone whose local midnight starts each day and week bucket, such as Europe/London or Asia/Kolkata; daylight saving changes make those days 23 or 25 hours long. A name the zone database does not know is refused (400 invalid_request naming time_zone). Day and week buckets in a zone other than UTC cover at most 92 days (400 invalid_request naming to); a year of them reads too many hourly counts to answer in time. Hour buckets stay whole UTC hours. Bucket starts, from and to stay instants. With the default population, a zone whose local midnight falls inside a UTC hour (a half-hour offset such as Asia/Kolkata) is refused for day and week buckets, as those counts are kept by the hour; retained_first_answers counts it.
        :param group_by: At most two dimensions to count by, of which at most one is reason, lane, country or asn. An assessment counts once in each of its reasons and incomplete lanes, so those groups can add up to more than the bucket's count. With population retained_first_answers, both dimensions can be facets; counts cover retained first answers only.
        :param metrics: count: each bucket's count and groups. score_histogram: first answers by flow and 5-point score bucket. score_outcomes: the histogram's first answers that have a reported outcome, by flow, 5-point score bucket and the latest outcome reported for the assessment (POST /v1/assessments/{assessment_id}/outcomes); the rest of a bin has none reported. late_flips: changes of an assessment's account decision for its flow after its first answer, by from, to and delay.
        :param limit: The most groups answered: the largest over the whole range, then by value. groups_truncated says when there were more.
        :param flow: The event an assessment is made for: account_creation (a user creates an account), login (a user returns to an existing account) or purchase (a payment or a credit grant). The account's risk is reported with the decision for this flow.
        :param status: Processing state, separate from evidence coverage. complete: final; nothing is still running, but unsupported, failed or unanswered lanes remain in incomplete_sources. partial: a recommendation exists and evidence is incomplete; assessment_url identifies continuing work when present. pending: no recommendation yet; poll or wait for the webhook. Finished processing does not mean all sources answered.
        :param recommendation: The recommended action: allow, step_up or review. Your application applies it.
        :param decision: An assessment's own decision: block when its stored risk.block is true, otherwise its recommendation. It is not the account's decision or held-admission state.
        :param revision: Which answer of each assessment the filters describe: latest, the latest stored revision, or first, the first answer, as served when the assessment was first answered (POST /v1/assessments/aggregate counts first answers). A cell of an aggregate drills down to POST /v1/assessments/search with the same filters, revision first and the cell's bucket as from and to.
        :param population: first_answers uses anonymous counters that can include erased detail. retained_first_answers computes exact intersections over retained first answers within 31 days. Requests exceeding the 100000-record work budget are refused.
        :param band:
        :param reason: A stable reason code. New codes may appear; ignore any you do not know.
        :param impact: The selected reason's served impact band. Requires reason.
        :param lane: An evidence lane: accounts (account presence for email and username), phone, breach, domain (the email domain's registration) and ip.
        :param country:
        :param asn:
        :param score_min: Inclusive lower score bound. Pending answers without a score do not match.
        :param score_max: Inclusive upper score bound, at least score_min when both are supplied.
        :param list_match: The list action captured at the first answer. Requires revision first. Older answers without captured list state do not match, including none.
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

        request = models.shared.AssessmentAggregateRequest(
            from_=from_,
            to=to,
            bucket=bucket,
            time_zone=time_zone,
            group_by=utils.unmarshal(
                group_by, Optional[List[models.shared.AggregateDimension]]
            ),
            metrics=utils.unmarshal(
                metrics, Optional[List[models.shared.AssessmentAggregateRequestMetric]]
            ),
            limit=limit,
            flow=flow,
            status=status,
            recommendation=recommendation,
            decision=decision,
            revision=revision,
            population=population,
            band=band,
            reason=reason,
            impact=impact,
            lane=lane,
            country=country,
            asn=asn,
            score_min=score_min,
            score_max=score_max,
            list_match=list_match,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="POST",
            path="/v1/assessments/aggregate",
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
                request, False, False, "json", models.shared.AssessmentAggregateRequest
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
                return models.operations.AggregateAssessmentsResponse(
                    result=unmarshal_json_response(
                        models.shared.AssessmentAggregate, http_res
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
            operation_id="aggregateAssessments",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["assessments"],
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

    def search(
        self,
        *,
        from_: str,
        to: str,
        account_id: Optional[str] = None,
        email: Optional[str] = None,
        flow: Optional[models.shared.Flow] = None,
        status: Optional[models.shared.Status] = None,
        recommendation: Optional[models.shared.Recommendation] = None,
        limit: Optional[int] = 20,
        cursor: Optional[str] = None,
        response_mode: Optional[models.shared.ResponseMode] = None,
        decision: Optional[models.shared.Decision] = None,
        revision: Optional[models.shared.AnswerRevision] = None,
        band: Optional[models.shared.Band] = None,
        reason: Optional[models.shared.ReasonCode] = None,
        impact: Optional[models.shared.Impact] = None,
        lane: Optional[models.shared.Lane] = None,
        country: Optional[str] = None,
        asn: Optional[int] = None,
        score_min: Optional[int] = None,
        score_max: Optional[int] = None,
        list_match: Optional[models.shared.ListMatch] = None,
        changed: Optional[bool] = None,
        identifier: Optional[
            Union[
                models.shared.IdentifierSearch, models.shared.IdentifierSearchTypedDict
            ]
        ] = None,
        identifier_expression: Optional[
            Union[
                models.shared.IdentifierExpression,
                models.shared.IdentifierExpressionTypedDict,
            ]
        ] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.SearchAssessmentsResponse:
        r"""Search assessments across this environment

        Search retained assessments created in [from,to), at most 366 days. identifier directly matches that assessment's submitted email, phone or customer-namespace username using exact, canonical or explicitly selected email mailbox matching. matched_identifier explains the original value and match basis. Legacy email keeps its account-wide mailbox semantics and cannot be combined with identifier. Other filters combine using AND and describe assessment decisions, separate from current account decisions. Each item carries the original submitted identifiers and its first_decision when available. Newest-created order has an assessment-ID tie break. Results are live across pages; each page's total and items use one database snapshot. Totals are exact below 10000 and capped at 10000. Requires history or investigate authority and identifier-read permission for identifier, identifier_expression or email filters; detailed mode also requires detailed permission. No Idempotency-Key. identifier_expression combines submitted terms with bounded AND/OR, at most 8 raw terms and 3 group levels. Each node selects exactly one of term, and, or. Groups have 2 to 8 operands. Duplicate normalized terms are idempotent and still count toward the limit. identifier_expression, identifier and email are mutually exclusive. Expression results use matched_identifiers with original submitted witnesses and zero-based depth-first term_index. All satisfied unique terms are returned in first-occurrence order. Cursors bind scope, ordered structure, original values, matching modes and all other filters; changing only page limit is allowed. Expression scope must be assessment: each returned assessment itself satisfies the complete expression. Scope account is rejected with 400 invalid_request; use account search for historical combinations.

        :param from_:
        :param to:
        :param account_id: Your own opaque identifier for the account being checked, scoped to your workspace. Use an id you mint, with no direct identifier (email, phone, name or national id) in it. '|' is accepted so an Auth0 user id such as 'auth0|64abc' passes unchanged; '@', '+', '
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.shared.AssessmentSearchRequest(
            from_=from_,
            to=to,
            account_id=account_id,
            email=email,
            flow=flow,
            status=status,
            recommendation=recommendation,
            limit=limit,
            cursor=cursor,
            response_mode=response_mode,
            decision=decision,
            revision=revision,
            band=band,
            reason=reason,
            impact=impact,
            lane=lane,
            country=country,
            asn=asn,
            score_min=score_min,
            score_max=score_max,
            list_match=list_match,
            changed=changed,
            identifier=utils.get_pydantic_model(identifier, Optional[models.shared.IdentifierSearch]),
            identifier_expression=utils.get_pydantic_model(identifier_expression, Optional[models.shared.IdentifierExpression]),
        )

        _noresponse_response_mode, http_headers = response_helpers.consume_response_mode(http_headers)
        req = self._build_request(
            method="POST",
            path="/v1/assessments/search",
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
            get_serialized_body=lambda: utils.serialize_request_body(request, False, False, "json", models.shared.AssessmentSearchRequest),
            allow_empty_value=None,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig("backoff", utils.BackoffStrategy(500, 8000, 2, 30000), True)

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "408",
                "429",
                "5XX"
            ])

        def _noresponse_parse_response(http_res):


            response_data: Any = None
            if utils.match_response(http_res, "200", "application/json"):
                return models.operations.SearchAssessmentsResponse(result=unmarshal_json_response(models.shared.AssessmentSearchPage, http_res )
                , headers=utils.get_response_headers(http_res.headers))
            if utils.match_response(http_res, "400", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.BadRequestErrorData, http_res)
                raise models.errors.BadRequestError(response_data, http_res)
            if utils.match_response(http_res, "401", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.AuthenticationErrorData, http_res)
                raise models.errors.AuthenticationError(response_data, http_res)
            if utils.match_response(http_res, "403", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.PermissionDeniedErrorData, http_res)
                raise models.errors.PermissionDeniedError(response_data, http_res)
            if utils.match_response(http_res, "404", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.NotFoundErrorData, http_res)
                raise models.errors.NotFoundError(response_data, http_res)
            if utils.match_response(http_res, "409", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.ConflictErrorData, http_res)
                raise models.errors.ConflictError(response_data, http_res)
            if utils.match_response(http_res, "429", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.RateLimitErrorData, http_res)
                raise models.errors.RateLimitError(response_data, http_res)
            if utils.match_response(http_res, "4XX", "*"):
                http_res_text =  utils.stream_to_text(http_res)
                raise models.errors.APIStatusError("API error occurred", http_res, http_res_text)
            if utils.match_response(http_res, "5XX", "*"):
                http_res_text =  utils.stream_to_text(http_res)
                raise models.errors.APIStatusError("API error occurred", http_res, http_res_text)

            raise models.errors.APIStatusError("Unexpected response received", http_res)
        _noresponse_hook_ctx = HookContext(config=self.sdk_configuration, base_url=base_url or "", operation_id="searchAssessments", oauth2_scopes=None, security_source=get_security_from_env(self.sdk_configuration.security, models.shared.Security), tags=["assessments"], extensions=None, response=ResponseContext(mode=_noresponse_response_mode, execution="sync"))
        http_res = self.do_request(
            hook_ctx=_noresponse_hook_ctx,
            request=req,
            is_error_status_code=lambda c: utils.match_status_codes(["4XX","5XX"], c),
            stream=_noresponse_response_mode == "streaming",
            retry_config=retry_config
        )
        if _noresponse_response_mode != "parsed":
            if utils.match_status_codes(["4XX","5XX"], http_res.status_code):
                http_res.read()
                try:
                    _noresponse_parse_response(http_res)
                except Exception as parse_exc_:
                    response_helpers.raise_parse_error(self.sdk_configuration.__dict__['_hooks'],
                        AfterParseErrorContext(_noresponse_hook_ctx),
                        http_res,
                        parse_exc_,
                    )
            _noresponse_response_cls = (
                response_helpers.StreamedAPIResponse
                if _noresponse_response_mode == "streaming"
                else response_helpers.APIResponse
            )
            return cast(Any, _noresponse_response_cls(
                raw=http_res,
                parser=_noresponse_parse_response,
                mode="buffered",
                client_ref=self,
                hook_ctx=AfterParseErrorContext(_noresponse_hook_ctx),
                hooks=self.sdk_configuration.__dict__.get("_hooks"),

            ))
        try:
            return _noresponse_parse_response(http_res)
        except Exception as parse_exc_:
            response_helpers.raise_parse_error(self.sdk_configuration.__dict__['_hooks'],
                AfterParseErrorContext(_noresponse_hook_ctx),
                http_res,
                parse_exc_,
            ) and whitespace are refused by the pattern, as is an exact-shape JWT; a hex digest such as a SHA-256 is allowed, because hashing an internal id is a common pseudonymous scheme. A value such as '07700900123' or 'jane.doe.gmail.com' cannot be told apart from an opaque id. It travels in bodies, and in a URL only as the path segment of GET /v1/accounts/{account_id}, its /assessments and its /linked_accounts. An assessment requested by a provider hook at pre_registration, which has no account yet, carries the server-issued account_id pre: followed by its assessment_id.
        :param email: Assessments of every account that one of its retained admitted assessments sent this mailbox as identifiers.email, matched as lists match an email entry: case-insensitive, a +tag removed and, at gmail.com and googlemail.com, the dots of the local part ignored. Only assessments stored since email list matching began carry the mailbox. An address that is not a valid mailbox is refused with 400.
        :param flow: The event an assessment is made for: account_creation (a user creates an account), login (a user returns to an existing account) or purchase (a payment or a credit grant). The account's risk is reported with the decision for this flow.
        :param status: Processing state, separate from evidence coverage. complete: final; nothing is still running, but unsupported, failed or unanswered lanes remain in incomplete_sources. partial: a recommendation exists and evidence is incomplete; assessment_url identifies continuing work when present. pending: no recommendation yet; poll or wait for the webhook. Finished processing does not mean all sources answered.
        :param recommendation: The recommended action: allow, step_up or review. Your application applies it.
        :param limit:
        :param cursor: Opaque, expiring cursor bound to workspace, environment, operation and all filters, including expression scope, ordered structure and original term values. Keep grouping, operand order, matching modes and values unchanged; an omitted match is equivalent to exact. The page limit may change.
        :param response_mode: standard returns the consolidated risk response; detailed adds merged provider-neutral facts when the key has detailed scope. There is no raw mode.
        :param decision: An assessment's own decision: block when its stored risk.block is true, otherwise its recommendation. It is not the account's decision or held-admission state.
        :param revision: Which answer of each assessment the filters describe: latest, the latest stored revision, or first, the first answer, as served when the assessment was first answered (POST /v1/assessments/aggregate counts first answers). A cell of an aggregate drills down to POST /v1/assessments/search with the same filters, revision first and the cell's bucket as from and to.
        :param band:
        :param reason: A stable reason code. New codes may appear; ignore any you do not know.
        :param impact: The selected reason's served impact band. Requires reason.
        :param lane: An evidence lane: accounts (account presence for email and username), phone, breach, domain (the email domain's registration) and ip.
        :param country:
        :param asn:
        :param score_min: Inclusive lower score bound. Pending answers without a score do not match.
        :param score_max: Inclusive upper score bound, at least score_min when both are supplied.
        :param list_match: The list action captured at the first answer. Requires revision first. Older answers without captured list state do not match, including none.
        :param changed: true returns only assessments whose latest stored revision's decision differs from their first answer's decision (see decision); false only the others. An assessment whose first answer or latest revision has no decision yet is not changed. Cannot be combined with revision first.
        :param identifier: One customer-submitted identifier. Defaults to exact comparison of the original submitted value. canonical uses the supported identifier normalisation without an ownership claim: email preserves local-part case, NFC-normalises it and lowercases the domain without removing dots or tags; phone uses international E.164 without extensions or an inferred region; username uses NFC and Unicode case folding within the customer namespace. mailbox is email-only and explicitly selects existing list rules: case-insensitive, remove +tag, and ignore local-part dots at gmail.com and googlemail.com; googlemail.com maps to gmail.com. Username requires namespace customer. Email and phone forbid namespace. Source-discovered identifiers and platform handles are not searched. Unsupported kinds, namespaces, modes and invalid values return 400. Search equality does not establish verified ownership or merge accounts.
        :param identifier_expression: A bounded AND/OR expression over submitted identifiers. Required scope assessment means the entire expression must match one retained assessment. Scope account permits each term to match a different retained assessment of the same account and is accepted only by account search. Exactly one of term, and or or is allowed at every node. Groups contain 2 to 8 operands, with at most 3 nested group levels and 8 raw term occurrences over the entire expression. A root term is allowed. Duplicate terms with the same kind, match rule, namespace and normalized comparison are idempotent, but count toward the raw limit. Match rules default to exact and preserve the existing identifier contract. Only retained submitted identifiers can satisfy a term. Unknown fields, unsupported scopes and malformed or oversized expressions return 400 invalid_request.
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

        request = models.shared.AssessmentSearchRequest(
            from_=from_,
            to=to,
            account_id=account_id,
            email=email,
            flow=flow,
            status=status,
            recommendation=recommendation,
            limit=limit,
            cursor=cursor,
            response_mode=response_mode,
            decision=decision,
            revision=revision,
            band=band,
            reason=reason,
            impact=impact,
            lane=lane,
            country=country,
            asn=asn,
            score_min=score_min,
            score_max=score_max,
            list_match=list_match,
            changed=changed,
            identifier=utils.get_pydantic_model(
                identifier, Optional[models.shared.IdentifierSearch]
            ),
            identifier_expression=utils.get_pydantic_model(
                identifier_expression, Optional[models.shared.IdentifierExpression]
            ),
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="POST",
            path="/v1/assessments/search",
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
                request, False, False, "json", models.shared.AssessmentSearchRequest
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
                return models.operations.SearchAssessmentsResponse(
                    result=unmarshal_json_response(
                        models.shared.AssessmentSearchPage, http_res
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
            operation_id="searchAssessments",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["assessments"],
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

    async def search_async(
        self,
        *,
        from_: str,
        to: str,
        account_id: Optional[str] = None,
        email: Optional[str] = None,
        flow: Optional[models.shared.Flow] = None,
        status: Optional[models.shared.Status] = None,
        recommendation: Optional[models.shared.Recommendation] = None,
        limit: Optional[int] = 20,
        cursor: Optional[str] = None,
        response_mode: Optional[models.shared.ResponseMode] = None,
        decision: Optional[models.shared.Decision] = None,
        revision: Optional[models.shared.AnswerRevision] = None,
        band: Optional[models.shared.Band] = None,
        reason: Optional[models.shared.ReasonCode] = None,
        impact: Optional[models.shared.Impact] = None,
        lane: Optional[models.shared.Lane] = None,
        country: Optional[str] = None,
        asn: Optional[int] = None,
        score_min: Optional[int] = None,
        score_max: Optional[int] = None,
        list_match: Optional[models.shared.ListMatch] = None,
        changed: Optional[bool] = None,
        identifier: Optional[
            Union[
                models.shared.IdentifierSearch, models.shared.IdentifierSearchTypedDict
            ]
        ] = None,
        identifier_expression: Optional[
            Union[
                models.shared.IdentifierExpression,
                models.shared.IdentifierExpressionTypedDict,
            ]
        ] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.SearchAssessmentsResponse:
        r"""Search assessments across this environment

        Search retained assessments created in [from,to), at most 366 days. identifier directly matches that assessment's submitted email, phone or customer-namespace username using exact, canonical or explicitly selected email mailbox matching. matched_identifier explains the original value and match basis. Legacy email keeps its account-wide mailbox semantics and cannot be combined with identifier. Other filters combine using AND and describe assessment decisions, separate from current account decisions. Each item carries the original submitted identifiers and its first_decision when available. Newest-created order has an assessment-ID tie break. Results are live across pages; each page's total and items use one database snapshot. Totals are exact below 10000 and capped at 10000. Requires history or investigate authority and identifier-read permission for identifier, identifier_expression or email filters; detailed mode also requires detailed permission. No Idempotency-Key. identifier_expression combines submitted terms with bounded AND/OR, at most 8 raw terms and 3 group levels. Each node selects exactly one of term, and, or. Groups have 2 to 8 operands. Duplicate normalized terms are idempotent and still count toward the limit. identifier_expression, identifier and email are mutually exclusive. Expression results use matched_identifiers with original submitted witnesses and zero-based depth-first term_index. All satisfied unique terms are returned in first-occurrence order. Cursors bind scope, ordered structure, original values, matching modes and all other filters; changing only page limit is allowed. Expression scope must be assessment: each returned assessment itself satisfies the complete expression. Scope account is rejected with 400 invalid_request; use account search for historical combinations.

        :param from_:
        :param to:
        :param account_id: Your own opaque identifier for the account being checked, scoped to your workspace. Use an id you mint, with no direct identifier (email, phone, name or national id) in it. '|' is accepted so an Auth0 user id such as 'auth0|64abc' passes unchanged; '@', '+', '
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.shared.AssessmentSearchRequest(
            from_=from_,
            to=to,
            account_id=account_id,
            email=email,
            flow=flow,
            status=status,
            recommendation=recommendation,
            limit=limit,
            cursor=cursor,
            response_mode=response_mode,
            decision=decision,
            revision=revision,
            band=band,
            reason=reason,
            impact=impact,
            lane=lane,
            country=country,
            asn=asn,
            score_min=score_min,
            score_max=score_max,
            list_match=list_match,
            changed=changed,
            identifier=utils.get_pydantic_model(identifier, Optional[models.shared.IdentifierSearch]),
            identifier_expression=utils.get_pydantic_model(identifier_expression, Optional[models.shared.IdentifierExpression]),
        )

        _noresponse_response_mode, http_headers = response_helpers.consume_response_mode(http_headers)
        req = self._build_request_async(
            method="POST",
            path="/v1/assessments/search",
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
            get_serialized_body=lambda: utils.serialize_request_body(request, False, False, "json", models.shared.AssessmentSearchRequest),
            allow_empty_value=None,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig("backoff", utils.BackoffStrategy(500, 8000, 2, 30000), True)

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "408",
                "429",
                "5XX"
            ])

        async def _noresponse_parse_response(http_res):


            response_data: Any = None
            if utils.match_response(http_res, "200", "application/json"):
                return models.operations.SearchAssessmentsResponse(result=unmarshal_json_response(models.shared.AssessmentSearchPage, http_res )
                , headers=utils.get_response_headers(http_res.headers))
            if utils.match_response(http_res, "400", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.BadRequestErrorData, http_res)
                raise models.errors.BadRequestError(response_data, http_res)
            if utils.match_response(http_res, "401", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.AuthenticationErrorData, http_res)
                raise models.errors.AuthenticationError(response_data, http_res)
            if utils.match_response(http_res, "403", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.PermissionDeniedErrorData, http_res)
                raise models.errors.PermissionDeniedError(response_data, http_res)
            if utils.match_response(http_res, "404", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.NotFoundErrorData, http_res)
                raise models.errors.NotFoundError(response_data, http_res)
            if utils.match_response(http_res, "409", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.ConflictErrorData, http_res)
                raise models.errors.ConflictError(response_data, http_res)
            if utils.match_response(http_res, "429", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.RateLimitErrorData, http_res)
                raise models.errors.RateLimitError(response_data, http_res)
            if utils.match_response(http_res, "4XX", "*"):
                http_res_text = await utils.stream_to_text_async(http_res)
                raise models.errors.APIStatusError("API error occurred", http_res, http_res_text)
            if utils.match_response(http_res, "5XX", "*"):
                http_res_text = await utils.stream_to_text_async(http_res)
                raise models.errors.APIStatusError("API error occurred", http_res, http_res_text)

            raise models.errors.APIStatusError("Unexpected response received", http_res)
        _noresponse_hook_ctx = HookContext(config=self.sdk_configuration, base_url=base_url or "", operation_id="searchAssessments", oauth2_scopes=None, security_source=get_security_from_env(self.sdk_configuration.security, models.shared.Security), tags=["assessments"], extensions=None, response=ResponseContext(mode=_noresponse_response_mode, execution="async"))
        http_res = await self.do_request_async(
            hook_ctx=_noresponse_hook_ctx,
            request=req,
            is_error_status_code=lambda c: utils.match_status_codes(["4XX","5XX"], c),
            stream=_noresponse_response_mode == "streaming",
            retry_config=retry_config
        )
        if _noresponse_response_mode != "parsed":
            if utils.match_status_codes(["4XX","5XX"], http_res.status_code):
                await http_res.aread()
                try:
                    await _noresponse_parse_response(http_res)
                except Exception as parse_exc_:
                    await response_helpers.raise_parse_error_async(self.sdk_configuration.__dict__.get('_async_hooks'), self.sdk_configuration.__dict__.get('_hooks'),
                        AfterParseErrorContext(_noresponse_hook_ctx),
                        http_res,
                        parse_exc_,
                    )
            _noresponse_response_cls = (
                response_helpers.AsyncStreamedAPIResponse
                if _noresponse_response_mode == "streaming"
                else response_helpers.AsyncAPIResponse
            )
            return cast(Any, _noresponse_response_cls(
                raw=http_res,
                parser=_noresponse_parse_response,
                mode="buffered",
                client_ref=self,
                hook_ctx=AfterParseErrorContext(_noresponse_hook_ctx),
                hooks=self.sdk_configuration.__dict__.get("_hooks"),
                async_hooks=self.sdk_configuration.__dict__.get('_async_hooks'),
            ))
        try:
            return await _noresponse_parse_response(http_res)
        except Exception as parse_exc_:
            await response_helpers.raise_parse_error_async(self.sdk_configuration.__dict__.get('_async_hooks'), self.sdk_configuration.__dict__.get('_hooks'),
                AfterParseErrorContext(_noresponse_hook_ctx),
                http_res,
                parse_exc_,
            ) and whitespace are refused by the pattern, as is an exact-shape JWT; a hex digest such as a SHA-256 is allowed, because hashing an internal id is a common pseudonymous scheme. A value such as '07700900123' or 'jane.doe.gmail.com' cannot be told apart from an opaque id. It travels in bodies, and in a URL only as the path segment of GET /v1/accounts/{account_id}, its /assessments and its /linked_accounts. An assessment requested by a provider hook at pre_registration, which has no account yet, carries the server-issued account_id pre: followed by its assessment_id.
        :param email: Assessments of every account that one of its retained admitted assessments sent this mailbox as identifiers.email, matched as lists match an email entry: case-insensitive, a +tag removed and, at gmail.com and googlemail.com, the dots of the local part ignored. Only assessments stored since email list matching began carry the mailbox. An address that is not a valid mailbox is refused with 400.
        :param flow: The event an assessment is made for: account_creation (a user creates an account), login (a user returns to an existing account) or purchase (a payment or a credit grant). The account's risk is reported with the decision for this flow.
        :param status: Processing state, separate from evidence coverage. complete: final; nothing is still running, but unsupported, failed or unanswered lanes remain in incomplete_sources. partial: a recommendation exists and evidence is incomplete; assessment_url identifies continuing work when present. pending: no recommendation yet; poll or wait for the webhook. Finished processing does not mean all sources answered.
        :param recommendation: The recommended action: allow, step_up or review. Your application applies it.
        :param limit:
        :param cursor: Opaque, expiring cursor bound to workspace, environment, operation and all filters, including expression scope, ordered structure and original term values. Keep grouping, operand order, matching modes and values unchanged; an omitted match is equivalent to exact. The page limit may change.
        :param response_mode: standard returns the consolidated risk response; detailed adds merged provider-neutral facts when the key has detailed scope. There is no raw mode.
        :param decision: An assessment's own decision: block when its stored risk.block is true, otherwise its recommendation. It is not the account's decision or held-admission state.
        :param revision: Which answer of each assessment the filters describe: latest, the latest stored revision, or first, the first answer, as served when the assessment was first answered (POST /v1/assessments/aggregate counts first answers). A cell of an aggregate drills down to POST /v1/assessments/search with the same filters, revision first and the cell's bucket as from and to.
        :param band:
        :param reason: A stable reason code. New codes may appear; ignore any you do not know.
        :param impact: The selected reason's served impact band. Requires reason.
        :param lane: An evidence lane: accounts (account presence for email and username), phone, breach, domain (the email domain's registration) and ip.
        :param country:
        :param asn:
        :param score_min: Inclusive lower score bound. Pending answers without a score do not match.
        :param score_max: Inclusive upper score bound, at least score_min when both are supplied.
        :param list_match: The list action captured at the first answer. Requires revision first. Older answers without captured list state do not match, including none.
        :param changed: true returns only assessments whose latest stored revision's decision differs from their first answer's decision (see decision); false only the others. An assessment whose first answer or latest revision has no decision yet is not changed. Cannot be combined with revision first.
        :param identifier: One customer-submitted identifier. Defaults to exact comparison of the original submitted value. canonical uses the supported identifier normalisation without an ownership claim: email preserves local-part case, NFC-normalises it and lowercases the domain without removing dots or tags; phone uses international E.164 without extensions or an inferred region; username uses NFC and Unicode case folding within the customer namespace. mailbox is email-only and explicitly selects existing list rules: case-insensitive, remove +tag, and ignore local-part dots at gmail.com and googlemail.com; googlemail.com maps to gmail.com. Username requires namespace customer. Email and phone forbid namespace. Source-discovered identifiers and platform handles are not searched. Unsupported kinds, namespaces, modes and invalid values return 400. Search equality does not establish verified ownership or merge accounts.
        :param identifier_expression: A bounded AND/OR expression over submitted identifiers. Required scope assessment means the entire expression must match one retained assessment. Scope account permits each term to match a different retained assessment of the same account and is accepted only by account search. Exactly one of term, and or or is allowed at every node. Groups contain 2 to 8 operands, with at most 3 nested group levels and 8 raw term occurrences over the entire expression. A root term is allowed. Duplicate terms with the same kind, match rule, namespace and normalized comparison are idempotent, but count toward the raw limit. Match rules default to exact and preserve the existing identifier contract. Only retained submitted identifiers can satisfy a term. Unknown fields, unsupported scopes and malformed or oversized expressions return 400 invalid_request.
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

        request = models.shared.AssessmentSearchRequest(
            from_=from_,
            to=to,
            account_id=account_id,
            email=email,
            flow=flow,
            status=status,
            recommendation=recommendation,
            limit=limit,
            cursor=cursor,
            response_mode=response_mode,
            decision=decision,
            revision=revision,
            band=band,
            reason=reason,
            impact=impact,
            lane=lane,
            country=country,
            asn=asn,
            score_min=score_min,
            score_max=score_max,
            list_match=list_match,
            changed=changed,
            identifier=utils.get_pydantic_model(
                identifier, Optional[models.shared.IdentifierSearch]
            ),
            identifier_expression=utils.get_pydantic_model(
                identifier_expression, Optional[models.shared.IdentifierExpression]
            ),
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="POST",
            path="/v1/assessments/search",
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
                request, False, False, "json", models.shared.AssessmentSearchRequest
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
                return models.operations.SearchAssessmentsResponse(
                    result=unmarshal_json_response(
                        models.shared.AssessmentSearchPage, http_res
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
            operation_id="searchAssessments",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["assessments"],
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

    def retrieve_version(
        self,
        assessment_id: str,
        version: int,
        *,
        response_mode: Optional[models.shared.ResponseMode] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.GetAssessmentVersionResponse:
        r"""Retrieve an exact assessment revision

        Retrieve a retained assessment version with its original decision, policy, flow and depth. This response excludes the current account decision. Current retention and response-mode permissions still apply. detail.identifiers holds the identifiers the assessment was sent, exactly as received.

        :param assessment_id: Path segment, matched case-sensitively. A value that does not match the assessment_id shape answers 404, not 400.
        :param version: The stored assessment_version, in canonical decimal form. An unavailable or malformed version answers 404.
        :param response_mode: Optional standard or separately authorised detailed customer view; raw is rejected.
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

        request = models.operations.GetAssessmentVersionRequest(
            assessment_id=assessment_id,
            response_mode=response_mode,
            version=version,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="GET",
            path="/v1/assessments/{assessment_id}/versions/{version}",
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
                return models.operations.GetAssessmentVersionResponse(
                    result=unmarshal_json_response(
                        models.shared.AssessmentRevision, http_res
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
            operation_id="getAssessmentVersion",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["assessments"],
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

    async def retrieve_version_async(
        self,
        assessment_id: str,
        version: int,
        *,
        response_mode: Optional[models.shared.ResponseMode] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.GetAssessmentVersionResponse:
        r"""Retrieve an exact assessment revision

        Retrieve a retained assessment version with its original decision, policy, flow and depth. This response excludes the current account decision. Current retention and response-mode permissions still apply. detail.identifiers holds the identifiers the assessment was sent, exactly as received.

        :param assessment_id: Path segment, matched case-sensitively. A value that does not match the assessment_id shape answers 404, not 400.
        :param version: The stored assessment_version, in canonical decimal form. An unavailable or malformed version answers 404.
        :param response_mode: Optional standard or separately authorised detailed customer view; raw is rejected.
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

        request = models.operations.GetAssessmentVersionRequest(
            assessment_id=assessment_id,
            response_mode=response_mode,
            version=version,
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="GET",
            path="/v1/assessments/{assessment_id}/versions/{version}",
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
                return models.operations.GetAssessmentVersionResponse(
                    result=unmarshal_json_response(
                        models.shared.AssessmentRevision, http_res
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
            operation_id="getAssessmentVersion",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["assessments"],
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

    def bind_account(
        self,
        assessment_id: str,
        *,
        account_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.BindProvisionalAccountResponse:
        r"""Bind a provisional signup account

        One-time association to an opaque stable customer account. The assessment is its natural idempotency key. Repeating the same binding returns its first receipt; a conflicting target is refused. No arbitrary account merging.

        :param assessment_id: Path segment, matched case-sensitively. A value that does not match the assessment_id shape answers 404, not 400.
        :param account_id: Your own opaque identifier for the account being checked, scoped to your workspace. Use an id you mint, with no direct identifier (email, phone, name or national id) in it. '|' is accepted so an Auth0 user id such as 'auth0|64abc' passes unchanged; '@', '+', '
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.operations.BindProvisionalAccountRequest(
            assessment_id=assessment_id,
            body=models.shared.AccountBindingRequest(
                account_id=account_id,
            ),
        )

        _noresponse_response_mode, http_headers = response_helpers.consume_response_mode(http_headers)
        req = self._build_request(
            method="POST",
            path="/v1/assessments/{assessment_id}/bind",
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
            get_serialized_body=lambda: utils.serialize_request_body(request.body, False, False, "json", models.shared.AccountBindingRequest),
            allow_empty_value=None,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig("backoff", utils.BackoffStrategy(500, 8000, 2, 30000), True)

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "408",
                "429",
                "5XX"
            ])

        def _noresponse_parse_response(http_res):


            response_data: Any = None
            if utils.match_response(http_res, ["200","201"], "application/json"):
                return models.operations.BindProvisionalAccountResponse(result=unmarshal_json_response(models.shared.AccountBinding, http_res )
                , headers=utils.get_response_headers(http_res.headers))
            if utils.match_response(http_res, "400", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.BadRequestErrorData, http_res)
                raise models.errors.BadRequestError(response_data, http_res)
            if utils.match_response(http_res, "401", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.AuthenticationErrorData, http_res)
                raise models.errors.AuthenticationError(response_data, http_res)
            if utils.match_response(http_res, "403", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.PermissionDeniedErrorData, http_res)
                raise models.errors.PermissionDeniedError(response_data, http_res)
            if utils.match_response(http_res, "404", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.NotFoundErrorData, http_res)
                raise models.errors.NotFoundError(response_data, http_res)
            if utils.match_response(http_res, "409", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.ConflictErrorData, http_res)
                raise models.errors.ConflictError(response_data, http_res)
            if utils.match_response(http_res, "429", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.RateLimitErrorData, http_res)
                raise models.errors.RateLimitError(response_data, http_res)
            if utils.match_response(http_res, "4XX", "*"):
                http_res_text =  utils.stream_to_text(http_res)
                raise models.errors.APIStatusError("API error occurred", http_res, http_res_text)
            if utils.match_response(http_res, "5XX", "*"):
                http_res_text =  utils.stream_to_text(http_res)
                raise models.errors.APIStatusError("API error occurred", http_res, http_res_text)

            raise models.errors.APIStatusError("Unexpected response received", http_res)
        _noresponse_hook_ctx = HookContext(config=self.sdk_configuration, base_url=base_url or "", operation_id="bindProvisionalAccount", oauth2_scopes=None, security_source=get_security_from_env(self.sdk_configuration.security, models.shared.Security), tags=["assessments"], extensions=None, response=ResponseContext(mode=_noresponse_response_mode, execution="sync"))
        http_res = self.do_request(
            hook_ctx=_noresponse_hook_ctx,
            request=req,
            is_error_status_code=lambda c: utils.match_status_codes(["4XX","5XX"], c),
            stream=_noresponse_response_mode == "streaming",
            retry_config=retry_config
        )
        if _noresponse_response_mode != "parsed":
            if utils.match_status_codes(["4XX","5XX"], http_res.status_code):
                http_res.read()
                try:
                    _noresponse_parse_response(http_res)
                except Exception as parse_exc_:
                    response_helpers.raise_parse_error(self.sdk_configuration.__dict__['_hooks'],
                        AfterParseErrorContext(_noresponse_hook_ctx),
                        http_res,
                        parse_exc_,
                    )
            _noresponse_response_cls = (
                response_helpers.StreamedAPIResponse
                if _noresponse_response_mode == "streaming"
                else response_helpers.APIResponse
            )
            return cast(Any, _noresponse_response_cls(
                raw=http_res,
                parser=_noresponse_parse_response,
                mode="buffered",
                client_ref=self,
                hook_ctx=AfterParseErrorContext(_noresponse_hook_ctx),
                hooks=self.sdk_configuration.__dict__.get("_hooks"),

            ))
        try:
            return _noresponse_parse_response(http_res)
        except Exception as parse_exc_:
            response_helpers.raise_parse_error(self.sdk_configuration.__dict__['_hooks'],
                AfterParseErrorContext(_noresponse_hook_ctx),
                http_res,
                parse_exc_,
            ) and whitespace are refused by the pattern, as is an exact-shape JWT; a hex digest such as a SHA-256 is allowed, because hashing an internal id is a common pseudonymous scheme. A value such as '07700900123' or 'jane.doe.gmail.com' cannot be told apart from an opaque id. It travels in bodies, and in a URL only as the path segment of GET /v1/accounts/{account_id}, its /assessments and its /linked_accounts. An assessment requested by a provider hook at pre_registration, which has no account yet, carries the server-issued account_id pre: followed by its assessment_id.
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

        request = models.operations.BindProvisionalAccountRequest(
            assessment_id=assessment_id,
            body=models.shared.AccountBindingRequest(
                account_id=account_id,
            ),
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request(
            method="POST",
            path="/v1/assessments/{assessment_id}/bind",
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
                request.body, False, False, "json", models.shared.AccountBindingRequest
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
            if utils.match_response(http_res, ["200", "201"], "application/json"):
                return models.operations.BindProvisionalAccountResponse(
                    result=unmarshal_json_response(
                        models.shared.AccountBinding, http_res
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
            operation_id="bindProvisionalAccount",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["assessments"],
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

    async def bind_account_async(
        self,
        assessment_id: str,
        *,
        account_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.operations.BindProvisionalAccountResponse:
        r"""Bind a provisional signup account

        One-time association to an opaque stable customer account. The assessment is its natural idempotency key. Repeating the same binding returns its first receipt; a conflicting target is refused. No arbitrary account merging.

        :param assessment_id: Path segment, matched case-sensitively. A value that does not match the assessment_id shape answers 404, not 400.
        :param account_id: Your own opaque identifier for the account being checked, scoped to your workspace. Use an id you mint, with no direct identifier (email, phone, name or national id) in it. '|' is accepted so an Auth0 user id such as 'auth0|64abc' passes unchanged; '@', '+', '
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.operations.BindProvisionalAccountRequest(
            assessment_id=assessment_id,
            body=models.shared.AccountBindingRequest(
                account_id=account_id,
            ),
        )

        _noresponse_response_mode, http_headers = response_helpers.consume_response_mode(http_headers)
        req = self._build_request_async(
            method="POST",
            path="/v1/assessments/{assessment_id}/bind",
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
            get_serialized_body=lambda: utils.serialize_request_body(request.body, False, False, "json", models.shared.AccountBindingRequest),
            allow_empty_value=None,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig("backoff", utils.BackoffStrategy(500, 8000, 2, 30000), True)

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "408",
                "429",
                "5XX"
            ])

        async def _noresponse_parse_response(http_res):


            response_data: Any = None
            if utils.match_response(http_res, ["200","201"], "application/json"):
                return models.operations.BindProvisionalAccountResponse(result=unmarshal_json_response(models.shared.AccountBinding, http_res )
                , headers=utils.get_response_headers(http_res.headers))
            if utils.match_response(http_res, "400", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.BadRequestErrorData, http_res)
                raise models.errors.BadRequestError(response_data, http_res)
            if utils.match_response(http_res, "401", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.AuthenticationErrorData, http_res)
                raise models.errors.AuthenticationError(response_data, http_res)
            if utils.match_response(http_res, "403", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.PermissionDeniedErrorData, http_res)
                raise models.errors.PermissionDeniedError(response_data, http_res)
            if utils.match_response(http_res, "404", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.NotFoundErrorData, http_res)
                raise models.errors.NotFoundError(response_data, http_res)
            if utils.match_response(http_res, "409", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.ConflictErrorData, http_res)
                raise models.errors.ConflictError(response_data, http_res)
            if utils.match_response(http_res, "429", "application/problem+json"):
                response_data = unmarshal_json_response(models.errors.RateLimitErrorData, http_res)
                raise models.errors.RateLimitError(response_data, http_res)
            if utils.match_response(http_res, "4XX", "*"):
                http_res_text = await utils.stream_to_text_async(http_res)
                raise models.errors.APIStatusError("API error occurred", http_res, http_res_text)
            if utils.match_response(http_res, "5XX", "*"):
                http_res_text = await utils.stream_to_text_async(http_res)
                raise models.errors.APIStatusError("API error occurred", http_res, http_res_text)

            raise models.errors.APIStatusError("Unexpected response received", http_res)
        _noresponse_hook_ctx = HookContext(config=self.sdk_configuration, base_url=base_url or "", operation_id="bindProvisionalAccount", oauth2_scopes=None, security_source=get_security_from_env(self.sdk_configuration.security, models.shared.Security), tags=["assessments"], extensions=None, response=ResponseContext(mode=_noresponse_response_mode, execution="async"))
        http_res = await self.do_request_async(
            hook_ctx=_noresponse_hook_ctx,
            request=req,
            is_error_status_code=lambda c: utils.match_status_codes(["4XX","5XX"], c),
            stream=_noresponse_response_mode == "streaming",
            retry_config=retry_config
        )
        if _noresponse_response_mode != "parsed":
            if utils.match_status_codes(["4XX","5XX"], http_res.status_code):
                await http_res.aread()
                try:
                    await _noresponse_parse_response(http_res)
                except Exception as parse_exc_:
                    await response_helpers.raise_parse_error_async(self.sdk_configuration.__dict__.get('_async_hooks'), self.sdk_configuration.__dict__.get('_hooks'),
                        AfterParseErrorContext(_noresponse_hook_ctx),
                        http_res,
                        parse_exc_,
                    )
            _noresponse_response_cls = (
                response_helpers.AsyncStreamedAPIResponse
                if _noresponse_response_mode == "streaming"
                else response_helpers.AsyncAPIResponse
            )
            return cast(Any, _noresponse_response_cls(
                raw=http_res,
                parser=_noresponse_parse_response,
                mode="buffered",
                client_ref=self,
                hook_ctx=AfterParseErrorContext(_noresponse_hook_ctx),
                hooks=self.sdk_configuration.__dict__.get("_hooks"),
                async_hooks=self.sdk_configuration.__dict__.get('_async_hooks'),
            ))
        try:
            return await _noresponse_parse_response(http_res)
        except Exception as parse_exc_:
            await response_helpers.raise_parse_error_async(self.sdk_configuration.__dict__.get('_async_hooks'), self.sdk_configuration.__dict__.get('_hooks'),
                AfterParseErrorContext(_noresponse_hook_ctx),
                http_res,
                parse_exc_,
            ) and whitespace are refused by the pattern, as is an exact-shape JWT; a hex digest such as a SHA-256 is allowed, because hashing an internal id is a common pseudonymous scheme. A value such as '07700900123' or 'jane.doe.gmail.com' cannot be told apart from an opaque id. It travels in bodies, and in a URL only as the path segment of GET /v1/accounts/{account_id}, its /assessments and its /linked_accounts. An assessment requested by a provider hook at pre_registration, which has no account yet, carries the server-issued account_id pre: followed by its assessment_id.
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

        request = models.operations.BindProvisionalAccountRequest(
            assessment_id=assessment_id,
            body=models.shared.AccountBindingRequest(
                account_id=account_id,
            ),
        )

        _noresponse_response_mode, http_headers = (
            response_helpers.consume_response_mode(http_headers)
        )
        req = self._build_request_async(
            method="POST",
            path="/v1/assessments/{assessment_id}/bind",
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
                request.body, False, False, "json", models.shared.AccountBindingRequest
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
            if utils.match_response(http_res, ["200", "201"], "application/json"):
                return models.operations.BindProvisionalAccountResponse(
                    result=unmarshal_json_response(
                        models.shared.AccountBinding, http_res
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
            operation_id="bindProvisionalAccount",
            oauth2_scopes=None,
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.shared.Security
            ),
            tags=["assessments"],
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


class AssessmentsWithRawResponse:
    def __init__(self, sdk: Assessments) -> None:
        self._sdk = sdk
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
        self.delete = response_helpers.to_raw_response_wrapper(
            sdk.delete, "http_headers"
        )
        self.delete_async = response_helpers.async_to_raw_response_wrapper(
            sdk.delete_async, "http_headers"
        )
        self.record_outcome = response_helpers.to_raw_response_wrapper(
            sdk.record_outcome, "http_headers"
        )
        self.record_outcome_async = response_helpers.async_to_raw_response_wrapper(
            sdk.record_outcome_async, "http_headers"
        )
        self.query = response_helpers.to_raw_response_wrapper(sdk.query, "http_headers")
        self.query_async = response_helpers.async_to_raw_response_wrapper(
            sdk.query_async, "http_headers"
        )
        self.aggregate = response_helpers.to_raw_response_wrapper(
            sdk.aggregate, "http_headers"
        )
        self.aggregate_async = response_helpers.async_to_raw_response_wrapper(
            sdk.aggregate_async, "http_headers"
        )
        self.search = response_helpers.to_raw_response_wrapper(
            sdk.search, "http_headers"
        )
        self.search_async = response_helpers.async_to_raw_response_wrapper(
            sdk.search_async, "http_headers"
        )
        self.retrieve_version = response_helpers.to_raw_response_wrapper(
            sdk.retrieve_version, "http_headers"
        )
        self.retrieve_version_async = response_helpers.async_to_raw_response_wrapper(
            sdk.retrieve_version_async, "http_headers"
        )
        self.bind_account = response_helpers.to_raw_response_wrapper(
            sdk.bind_account, "http_headers"
        )
        self.bind_account_async = response_helpers.async_to_raw_response_wrapper(
            sdk.bind_account_async, "http_headers"
        )


class AssessmentsWithStreamingResponse:
    def __init__(self, sdk: Assessments) -> None:
        self._sdk = sdk
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
        self.delete = response_helpers.to_streamed_response_wrapper(
            sdk.delete, "http_headers"
        )
        self.delete_async = response_helpers.async_to_streamed_response_wrapper(
            sdk.delete_async, "http_headers"
        )
        self.record_outcome = response_helpers.to_streamed_response_wrapper(
            sdk.record_outcome, "http_headers"
        )
        self.record_outcome_async = response_helpers.async_to_streamed_response_wrapper(
            sdk.record_outcome_async, "http_headers"
        )
        self.query = response_helpers.to_streamed_response_wrapper(
            sdk.query, "http_headers"
        )
        self.query_async = response_helpers.async_to_streamed_response_wrapper(
            sdk.query_async, "http_headers"
        )
        self.aggregate = response_helpers.to_streamed_response_wrapper(
            sdk.aggregate, "http_headers"
        )
        self.aggregate_async = response_helpers.async_to_streamed_response_wrapper(
            sdk.aggregate_async, "http_headers"
        )
        self.search = response_helpers.to_streamed_response_wrapper(
            sdk.search, "http_headers"
        )
        self.search_async = response_helpers.async_to_streamed_response_wrapper(
            sdk.search_async, "http_headers"
        )
        self.retrieve_version = response_helpers.to_streamed_response_wrapper(
            sdk.retrieve_version, "http_headers"
        )
        self.retrieve_version_async = (
            response_helpers.async_to_streamed_response_wrapper(
                sdk.retrieve_version_async, "http_headers"
            )
        )
        self.bind_account = response_helpers.to_streamed_response_wrapper(
            sdk.bind_account, "http_headers"
        )
        self.bind_account_async = response_helpers.async_to_streamed_response_wrapper(
            sdk.bind_account_async, "http_headers"
        )
