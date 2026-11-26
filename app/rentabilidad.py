from decimal import Decimal

from app.schemas import Transaccion


def calcular_producto_mas_rentable(transacciones: list[Transaccion]) -> str | None:
    """Devuelve el producto con más ventas acumuladas; desempata por primera venta."""
    ventas: dict[str, Decimal] = {}

    for transaccion in transacciones:
        if transaccion.tipo == "SELL":
            importe = transaccion.cantidad * transaccion.valor_unitario
            ventas[transaccion.producto] = (
                ventas.get(transaccion.producto, Decimal("0")) + importe
            )

    # El diccionario conserva el orden de primera venta; max elige el primer empate.
    return max(ventas, key=lambda producto: ventas[producto], default=None)
