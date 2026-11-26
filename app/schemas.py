from datetime import date
from decimal import Decimal
from typing import Literal

from pydantic import BaseModel, Field


class Transaccion(BaseModel):
    tipo: Literal["BUY", "SELL"]
    fecha: date
    producto: Literal["COAL", "IRON", "ALUMINIUM", "GOLD", "TIMBER"]
    cantidad: int = Field(ge=0)
    valor_unitario: Decimal = Field(ge=0)
