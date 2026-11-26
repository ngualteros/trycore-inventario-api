from app.schemas import Transaccion


def calcular_stock(transacciones: list[Transaccion]) -> dict[str, int]:
    """Calcula las existencias de cada producto, incluidos saldos negativos."""
    stock = {"COAL": 0, "IRON": 0, "ALUMINIUM": 0, "GOLD": 0, "TIMBER": 0}

    for transaccion in transacciones:
        if transaccion.tipo == "BUY":
            stock[transaccion.producto] += transaccion.cantidad
        else:
            stock[transaccion.producto] -= transaccion.cantidad

    return stock
