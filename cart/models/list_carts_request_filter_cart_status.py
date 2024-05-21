# coding: utf-8

"""
    Cart Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ListCartsRequestFilterCartStatus(str, Enum):
    """
    ListCartsRequestFilterCartStatus
    """

    """
    allowed enum values
    """
    UNKNOWN = 'UNKNOWN'
    ENABLED = 'ENABLED'
    DISABLED = 'DISABLED'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ListCartsRequestFilterCartStatus from a JSON string"""
        return cls(json.loads(json_str))


