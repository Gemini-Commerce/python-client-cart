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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CartCustomerData(BaseModel):
    """
    CartCustomerData
    """ # noqa: E501
    customer_grn: Optional[StrictStr] = Field(default=None, alias="customerGrn")
    firstname: Optional[StrictStr] = None
    lastname: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    phone_number: Optional[StrictStr] = Field(default=None, alias="phoneNumber")
    groups: Optional[List[StrictStr]] = None
    tax_code: Optional[StrictStr] = Field(default=None, alias="taxCode")
    certified_email: Optional[StrictStr] = Field(default=None, alias="certifiedEmail")
    sdi_code: Optional[StrictStr] = Field(default=None, alias="sdiCode")
    fiscal_code: Optional[StrictStr] = Field(default=None, alias="fiscalCode")
    company_name: Optional[StrictStr] = Field(default=None, alias="companyName")
    agent_grn: Optional[StrictStr] = Field(default=None, alias="agentGrn")
    __properties: ClassVar[List[str]] = ["customerGrn", "firstname", "lastname", "email", "phoneNumber", "groups", "taxCode", "certifiedEmail", "sdiCode", "fiscalCode", "companyName", "agentGrn"]

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
        """Create an instance of CartCustomerData from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CartCustomerData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "customerGrn": obj.get("customerGrn"),
            "firstname": obj.get("firstname"),
            "lastname": obj.get("lastname"),
            "email": obj.get("email"),
            "phoneNumber": obj.get("phoneNumber"),
            "groups": obj.get("groups"),
            "taxCode": obj.get("taxCode"),
            "certifiedEmail": obj.get("certifiedEmail"),
            "sdiCode": obj.get("sdiCode"),
            "fiscalCode": obj.get("fiscalCode"),
            "companyName": obj.get("companyName"),
            "agentGrn": obj.get("agentGrn")
        })
        return _obj


