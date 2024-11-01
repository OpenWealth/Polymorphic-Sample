# coding: utf-8

"""
    Financial Instrument Sample Polymorph

    This is the description.

    The version of the OpenAPI document: 1.0.0
    Contact: openwealth@synpulse.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json




from pydantic import ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from API.models.financial_instrument import FinancialInstrument
from API.models.identification import Identification
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Option(FinancialInstrument):
    """
    Schema of a equity instrument.
    """ # noqa: E501
    type: StrictStr = Field(description="Type of the financial instrument.")
    name: Optional[StrictStr] = Field(default=None, description="Name of the financial instrument.")
    identification_list: Optional[List[Identification]] = Field(default=None, description="List of identification key value pairs.", alias="identificationList")
    underlying_instrument: Optional[FinancialInstrument] = Field(default=None, alias="underlyingInstrument")
    __properties: ClassVar[List[str]] = ["type", "name", "identificationList", "underlyingInstrument"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Cash', 'Bond', 'Equity', 'Option'):
            raise ValueError("must be one of enum values ('Cash', 'Bond', 'Equity', 'Option')")
        return value

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
        """Create an instance of Option from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in identification_list (list)
        _items = []
        if self.identification_list:
            for _item in self.identification_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict['identificationList'] = _items
        # override the default output from pydantic by calling `to_dict()` of underlying_instrument
        if self.underlying_instrument:
            _dict['underlyingInstrument'] = self.underlying_instrument.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Option from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "name": obj.get("name"),
            "identificationList": [Identification.from_dict(_item) for _item in obj.get("identificationList")] if obj.get("identificationList") is not None else None,
            "underlyingInstrument": FinancialInstrument.from_dict(obj.get("underlyingInstrument")) if obj.get("underlyingInstrument") is not None else None
        })
        return _obj


