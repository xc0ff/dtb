"""TODO: docstring"""

from types import SimpleNamespace

import hashlib

import requests

from .utils import constants


QUERY_STRING = """
query ViewDropCampaigns {
    currentUser {
        dropCampaigns {
            id
            endAt
            game {
                displayName
            }
        }
    }
}
"""


class Overseer:
    """TODO: docstring"""

    _QUERIES = SimpleNamespace(
        ViewDropCampaigns=SimpleNamespace(
            operation="ViewDropCampaigns",
            hash=""
        ),
        ViewCampaignDetails=SimpleNamespace(
            operation="ViewCampaignDetails",
            hash=""
        ),
    )

    def __init__(self):
        self._client_id = constants.CLIENT_ID
        self._auth_token = constants.AUTH_TOKEN

    def _make_authorized_request(self, operation: str, query_hash: str, variables: dict=None):
        headers = {
            "Content-Type": "text/plain;charset=UTF-8",
            # "Client-ID": CLIENT_ID
            "Authorization": f"OAuth {self._auth_token}",
        }

        data = {
            "operationName": operation,
            "variables": variables,
            "extensions": {
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": query_hash,
                }
            },
        }

        r = requests.post(constants.GQL_API_URL, timeout=30, headers=headers, json=data)
        print(r.text)

    def get_drop_campaigns(self) -> list:
        """TODO: docstring"""
        
        hash_object = hashlib.sha256(QUERY_STRING.encode("utf-8"))
        query_hash = hash_object.hexdigest()

        self._make_authorized_request(
            self._QUERIES.ViewDropCampaigns.operation, query_hash
        )

        return []

    def get_campaign_details(self, id: int) -> list:
        """TODO: docstring"""

        # self._make_authorized_request(
        #   operation=self._QERIES.ViewCampaignDetails.operation,
        #   query_hash=self._QUERIES.ViewCampaignDetails.hash,
        #   variables={
        #       "id": id
        #   })

        return []
