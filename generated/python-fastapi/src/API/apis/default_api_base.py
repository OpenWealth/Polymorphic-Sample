# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from API.models.financial_instrument import FinancialInstrument


class BaseDefaultApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDefaultApi.subclasses = BaseDefaultApi.subclasses + (cls,)
    async def get_instrument_by_id(
        self,
        instrumentId: str,
    ) -> FinancialInstrument:
        """This is a description."""
        ...
