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


class StockFinal(BaseModel):
    COAL: int
    IRON: int
    ALUMINIUM: int
    GOLD: int
    TIMBER: int


class ResumenInventario(BaseModel):
    stock_final: StockFinal
    producto_mas_rentable: Literal["COAL", "IRON", "ALUMINIUM", "GOLD", "TIMBER"] | None
