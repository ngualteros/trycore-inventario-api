from datetime import date
from decimal import Decimal

from app.schemas import Transaccion
from app.stock import calcular_stock


def test_lista_vacia_devuelve_cero_para_todos_los_productos():
    assert calcular_stock([]) == {
        "COAL": 0,
        "IRON": 0,
        "ALUMINIUM": 0,
        "GOLD": 0,
        "TIMBER": 0,
    }


def test_ventas_superiores_a_compras_conservan_stock_negativo():
    transacciones = [
        Transaccion(
            tipo="BUY",
            fecha=date(2026, 11, 26),
            producto="IRON",
            cantidad=10,
            valor_unitario=Decimal("12.50"),
        ),
        Transaccion(
            tipo="SELL",
            fecha=date(2026, 11, 26),
            producto="IRON",
            cantidad=14,
            valor_unitario=Decimal("20.75"),
        ),
    ]

    assert calcular_stock(transacciones) == {
        "COAL": 0,
        "IRON": -4,
        "ALUMINIUM": 0,
        "GOLD": 0,
        "TIMBER": 0,
    }


def test_acumula_compras_y_separa_el_stock_por_producto():
    transacciones = [
        Transaccion(
            tipo="BUY",
            fecha=date(2026, 11, 26),
            producto="GOLD",
            cantidad=3,
            valor_unitario=Decimal("100.25"),
        ),
        Transaccion(
            tipo="BUY",
            fecha=date(2026, 11, 26),
            producto="GOLD",
            cantidad=5,
            valor_unitario=Decimal("0"),
        ),
        Transaccion(
            tipo="SELL",
            fecha=date(2026, 11, 26),
            producto="TIMBER",
            cantidad=2,
            valor_unitario=Decimal("7.90"),
        ),
    ]

    assert calcular_stock(transacciones) == {
        "COAL": 0,
        "IRON": 0,
        "ALUMINIUM": 0,
        "GOLD": 8,
        "TIMBER": -2,
    }
