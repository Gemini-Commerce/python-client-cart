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
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from cart.models.cart_localized_text import CartLocalizedText
from cart.models.cart_money import CartMoney
from typing import Optional, Set
from typing_extensions import Self

class CartPaymentData(BaseModel):
    """
    CartPaymentData
    """ # noqa: E501
    code: Optional[StrictStr] = None
    title: Optional[CartLocalizedText] = None
    payload: Optional[StrictStr] = None
    fee: Optional[CartMoney] = None
    amount: Optional[CartMoney] = None
    label: Optional[CartLocalizedText] = None
    description: Optional[CartLocalizedText] = None
    vat_amount: Optional[CartMoney] = Field(default=None, alias="vatAmount")
    vat_percentage: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="vatPercentage")
    vat_inaccurate: Optional[StrictBool] = Field(default=None, alias="vatInaccurate")
    vat_calculated: Optional[StrictBool] = Field(default=None, alias="vatCalculated")
    is_upfront: Optional[StrictBool] = Field(default=None, alias="isUpfront")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["code", "title", "payload", "fee", "amount", "label", "description", "vatAmount", "vatPercentage", "vatInaccurate", "vatCalculated", "isUpfront"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CartPaymentData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of title
        if self.title:
            _dict['title'] = self.title.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fee
        if self.fee:
            _dict['fee'] = self.fee.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amount
        if self.amount:
            _dict['amount'] = self.amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of label
        if self.label:
            _dict['label'] = self.label.to_dict()
        # override the default output from pydantic by calling `to_dict()` of description
        if self.description:
            _dict['description'] = self.description.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vat_amount
        if self.vat_amount:
            _dict['vatAmount'] = self.vat_amount.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CartPaymentData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "code": obj.get("code"),
            "title": CartLocalizedText.from_dict(obj["title"]) if obj.get("title") is not None else None,
            "payload": obj.get("payload"),
            "fee": CartMoney.from_dict(obj["fee"]) if obj.get("fee") is not None else None,
            "amount": CartMoney.from_dict(obj["amount"]) if obj.get("amount") is not None else None,
            "label": CartLocalizedText.from_dict(obj["label"]) if obj.get("label") is not None else None,
            "description": CartLocalizedText.from_dict(obj["description"]) if obj.get("description") is not None else None,
            "vatAmount": CartMoney.from_dict(obj["vatAmount"]) if obj.get("vatAmount") is not None else None,
            "vatPercentage": obj.get("vatPercentage"),
            "vatInaccurate": obj.get("vatInaccurate"),
            "vatCalculated": obj.get("vatCalculated"),
            "isUpfront": obj.get("isUpfront")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


