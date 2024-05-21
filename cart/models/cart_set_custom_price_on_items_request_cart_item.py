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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from cart.models.cart_money import CartMoney
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CartSetCustomPriceOnItemsRequestCartItem(BaseModel):
    """
    CartSetCustomPriceOnItemsRequestCartItem
    """ # noqa: E501
    id: Optional[StrictStr] = None
    free_of_charge: Optional[StrictBool] = Field(default=None, alias="freeOfCharge")
    unset: Optional[StrictBool] = None
    custom_price_row: Optional[CartMoney] = Field(default=None, alias="customPriceRow")
    custom_price_unit: Optional[CartMoney] = Field(default=None, alias="customPriceUnit")
    discount_percentage: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="discountPercentage")
    __properties: ClassVar[List[str]] = ["id", "freeOfCharge", "unset", "customPriceRow", "customPriceUnit", "discountPercentage"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CartSetCustomPriceOnItemsRequestCartItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of custom_price_row
        if self.custom_price_row:
            _dict['customPriceRow'] = self.custom_price_row.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_price_unit
        if self.custom_price_unit:
            _dict['customPriceUnit'] = self.custom_price_unit.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CartSetCustomPriceOnItemsRequestCartItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "freeOfCharge": obj.get("freeOfCharge"),
            "unset": obj.get("unset"),
            "customPriceRow": CartMoney.from_dict(obj.get("customPriceRow")) if obj.get("customPriceRow") is not None else None,
            "customPriceUnit": CartMoney.from_dict(obj.get("customPriceUnit")) if obj.get("customPriceUnit") is not None else None,
            "discountPercentage": obj.get("discountPercentage")
        })
        return _obj


