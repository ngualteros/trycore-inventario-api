from fastapi import FastAPI

from app.rentabilidad import calcular_producto_mas_rentable
from app.schemas import ResumenInventario, StockFinal, Transaccion
from app.stock import calcular_stock

app = FastAPI(
    title="Trycore - API de inventario",
    docs_url="/api-docs",
)


@app.post("/inventario/resumen", response_model=ResumenInventario)
def resumir_inventario(transacciones: list[Transaccion]) -> ResumenInventario:
    """Calcula el resumen de esta petición en memoria, sin guardar transacciones."""
    return ResumenInventario(
        stock_final=StockFinal(**calcular_stock(transacciones)),
        producto_mas_rentable=calcular_producto_mas_rentable(transacciones),
    )
