# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from API.apis.default_api_base import BaseDefaultApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from API.models.extra_models import TokenModel  # noqa: F401
from API.models.financial_instrument import FinancialInstrument


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/financial-instruments/{instrumentId}",
    responses={
        200: {"model": FinancialInstrument, "description": "get instrument by id."},
        400: {"model": str, "description": "Unexpected error"},
    },
    tags=["default"],
    summary="This is a summary",
    response_model_by_alias=True,
)
async def get_instrument_by_id(
    instrumentId: str = Path(..., description="Instrument ID Parameter."),
) -> FinancialInstrument:
    """This is a description."""
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().get_instrument_by_id(instrumentId)
