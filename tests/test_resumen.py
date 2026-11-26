import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def transacciones():
    return [
        {
            "tipo": "BUY",
            "fecha": "2026-11-26",
            "producto": "IRON",
            "cantidad": 10,
            "valor_unitario": 2,
        },
        {
            "tipo": "SELL",
            "fecha": "2026-11-26",
            "producto": "IRON",
            "cantidad": 14,
            "valor_unitario": 2,
        },
        {
            "tipo": "SELL",
            "fecha": "2026-11-26",
            "producto": "GOLD",
            "cantidad": 2,
            "valor_unitario": 20,
        },
    ]


def test_resumen_con_compras_y_ventas(client, transacciones):
    response = client.post("/inventario/resumen", json=transacciones)

    assert response.status_code == 200
    assert response.json() == {
        "stock_final": {"COAL": 0, "IRON": -4, "ALUMINIUM": 0, "GOLD": -2, "TIMBER": 0},
        "producto_mas_rentable": "GOLD",
    }


def test_resumen_vacio(client):
    response = client.post("/inventario/resumen", json=[])

    assert response.status_code == 200
    assert response.json() == {
        "stock_final": {"COAL": 0, "IRON": 0, "ALUMINIUM": 0, "GOLD": 0, "TIMBER": 0},
        "producto_mas_rentable": None,
    }


def test_resumen_con_solo_compras(client):
    response = client.post(
        "/inventario/resumen",
        json=[
            {
                "tipo": "BUY",
                "fecha": "2026-11-26",
                "producto": "TIMBER",
                "cantidad": 3,
                "valor_unitario": 5,
            }
        ],
    )

    assert response.status_code == 200
    assert response.json() == {
        "stock_final": {"COAL": 0, "IRON": 0, "ALUMINIUM": 0, "GOLD": 0, "TIMBER": 3},
        "producto_mas_rentable": None,
    }


def test_cantidad_negativa_devuelve_422(client, transacciones):
    transacciones[0]["cantidad"] = -1
    response = client.post("/inventario/resumen", json=transacciones)

    assert response.status_code == 422
    assert any(
        error["loc"] == ["body", 0, "cantidad"]
        and error["type"] == "greater_than_equal"
        for error in response.json()["detail"]
    )


def test_peticiones_no_comparten_estado(client, transacciones):
    primera = client.post("/inventario/resumen", json=transacciones)
    vacia = client.post("/inventario/resumen", json=[])
    repetida = client.post("/inventario/resumen", json=transacciones)

    assert primera.status_code == vacia.status_code == repetida.status_code == 200
    assert vacia.json() == {
        "stock_final": {"COAL": 0, "IRON": 0, "ALUMINIUM": 0, "GOLD": 0, "TIMBER": 0},
        "producto_mas_rentable": None,
    }
    assert repetida.json() == primera.json()


def test_openapi_publica_el_contrato_y_swagger_sigue_disponible(client):
    response = client.get("/openapi.json")

    assert response.status_code == 200
    schema = response.json()
    assert set(schema["paths"]) == {"/inventario/resumen"}
    operation = schema["paths"]["/inventario/resumen"]["post"]
    entrada = operation["requestBody"]["content"]["application/json"]["schema"]
    assert entrada["type"] == "array"
    assert entrada["items"]["$ref"] == "#/components/schemas/Transaccion"
    salida = operation["responses"]["200"]["content"]["application/json"]["schema"]
    assert salida["$ref"] == "#/components/schemas/ResumenInventario"
    modelos = schema["components"]["schemas"]
    resumen = modelos["ResumenInventario"]
    assert set(resumen["required"]) == {"stock_final", "producto_mas_rentable"}
    assert resumen["properties"]["stock_final"]["$ref"] == "#/components/schemas/StockFinal"
    ganador = resumen["properties"]["producto_mas_rentable"]["anyOf"]
    assert {"type": "null"} in ganador
    stock = modelos["StockFinal"]
    productos = {"COAL", "IRON", "ALUMINIUM", "GOLD", "TIMBER"}
    assert set(stock["properties"]) == set(stock["required"]) == productos
    assert all(campo["type"] == "integer" for campo in stock["properties"].values())
    docs = client.get("/api-docs")
    assert docs.status_code == 200
    assert "SwaggerUIBundle" in docs.text
