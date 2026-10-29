from __future__ import annotations
from noresponse.models.shared import accountdirectorypage as shared_accountdirectorypage
from noresponse.types import BaseModel
from typing import Dict, List
from typing_extensions import TypedDict


class SearchAccountsResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_accountdirectorypage.AccountDirectoryPageTypedDict


class SearchAccountsResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_accountdirectorypage.AccountDirectoryPage
