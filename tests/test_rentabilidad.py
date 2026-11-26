from datetime import date
from decimal import Decimal

from app.rentabilidad import calcular_producto_mas_rentable
from app.schemas import Transaccion


def _transaccion(tipo, producto, cantidad, valor_unitario):
    return Transaccion(
        tipo=tipo,
        fecha=date(2026, 11, 26),
        producto=producto,
        cantidad=cantidad,
        valor_unitario=Decimal(valor_unitario),
    )


def test_acumula_importes_de_ventas_y_excluye_compras():
    transacciones = [
        _transaccion("SELL", "GOLD", 2, "10"),
        _transaccion("BUY", "IRON", 1000, "1000"),
        _transaccion("SELL", "IRON", 1, "30"),
        _transaccion("SELL", "GOLD", 3, "5"),
    ]

    assert calcular_producto_mas_rentable(transacciones) == "GOLD"


def test_lista_vacia_devuelve_none():
    assert calcular_producto_mas_rentable([]) is None


def test_solo_compras_devuelve_none():
    transacciones = [
        _transaccion("BUY", "IRON", 1000, "1000"),
        _transaccion("BUY", "GOLD", 3, "10"),
    ]

    assert calcular_producto_mas_rentable(transacciones) is None


def test_empate_se_resuelve_por_primera_venta_no_por_primera_compra():
    transacciones = [
        _transaccion("BUY", "COAL", 1, "100"),
        _transaccion("SELL", "GOLD", 1, "20"),
        _transaccion("SELL", "COAL", 1, "20"),
    ]

    assert calcular_producto_mas_rentable(transacciones) == "GOLD"


def test_venta_de_importe_cero_es_candidata():
    transacciones = [_transaccion("SELL", "TIMBER", 1, "0")]

    assert calcular_producto_mas_rentable(transacciones) == "TIMBER"


def test_importes_decimales_conservan_el_empate_exacto():
    transacciones = [
        _transaccion("SELL", "GOLD", 1, "0.30"),
        _transaccion("SELL", "COAL", 3, "0.10"),
    ]

    assert calcular_producto_mas_rentable(transacciones) == "GOLD"
