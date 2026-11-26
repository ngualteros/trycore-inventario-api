# Trycore Inventario API

API de inventario con FastAPI. Su único endpoint de negocio,
`POST /inventario/resumen`, devuelve el stock final por producto y el producto con
mayor importe acumulado de ventas. El procesamiento es en memoria: cada petición
se calcula de forma independiente, sin persistencia.

## Ejecución local en Windows con PowerShell

Requisito: Python 3.12 (versión utilizada para la comprobación local).
Ejecuta los siguientes comandos desde la raíz del repositorio.

1. Crea el entorno virtual:

   ```powershell
   python -m venv .venv
   ```

2. Instala las dependencias:

   ```powershell
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

3. Inicia el servidor:

   ```powershell
   .\.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000
   ```

Los comandos usan directamente el intérprete del entorno virtual. No es necesario
activar `Activate.ps1` ni cambiar la política de ejecución de PowerShell.

Abre Swagger UI en <http://127.0.0.1:8000/api-docs>. El esquema OpenAPI está
disponible en <http://127.0.0.1:8000/openapi.json> y publica
`POST /inventario/resumen` con sus modelos de entrada y respuesta.

Para comprobar las respuestas desde otra terminal de PowerShell:

```powershell
(Invoke-WebRequest -Uri 'http://127.0.0.1:8000/api-docs' -UseBasicParsing).StatusCode
(Invoke-WebRequest -Uri 'http://127.0.0.1:8000/openapi.json' -UseBasicParsing).StatusCode
```

Ambos comandos deben mostrar `200`. Detén el servidor con `Ctrl+C` en la terminal
donde lo iniciaste.

## Contrato de POST /inventario/resumen

El cuerpo es una lista JSON de transacciones, sin un objeto contenedor. Cada
transacción exige `tipo` (BUY o SELL), `fecha` (YYYY-MM-DD), `producto` (COAL, IRON,
ALUMINIUM, GOLD o TIMBER), `cantidad` (entero mayor o igual a cero) y
`valor_unitario` (mayor o igual a cero, convertido a Decimal por el modelo).

En `/api-docs`, abre **POST /inventario/resumen**, pulsa **Try it out**, pega este
cuerpo y pulsa **Execute**:

```json
[
  {
    "tipo": "BUY",
    "fecha": "2026-11-26",
    "producto": "IRON",
    "cantidad": 10,
    "valor_unitario": 2
  },
  {
    "tipo": "SELL",
    "fecha": "2026-11-26",
    "producto": "IRON",
    "cantidad": 14,
    "valor_unitario": 2
  },
  {
    "tipo": "SELL",
    "fecha": "2026-11-26",
    "producto": "GOLD",
    "cantidad": 2,
    "valor_unitario": 20
  }
]
```

Respuesta esperada, HTTP 200:

```json
{
  "stock_final": {
    "COAL": 0,
    "IRON": -4,
    "ALUMINIUM": 0,
    "GOLD": -2,
    "TIMBER": 0
  },
  "producto_mas_rentable": "GOLD"
}
```

`stock_final` siempre incluye los cinco productos y conserva los saldos negativos.
`producto_mas_rentable` compara los importes de ventas (cantidad × valor unitario),
sin incluir compras: GOLD acumula 40 e IRON 28 en el ejemplo. En caso de empate
gana el producto cuya primera venta aparece antes en la lista, sin ordenar por
fecha. Una venta de importe cero también cuenta como candidata.

Una lista vacía (`[]`) devuelve todos los stocks en cero y
`producto_mas_rentable: null`. Si solo hay compras, se calcula el stock y el ganador
también es `null`. Las entradas inválidas, como una cantidad negativa, devuelven
HTTP 422 con los detalles de validación.

## Cálculos y pruebas

`app.stock.calcular_stock` recibe una lista de objetos `Transaccion` y devuelve el
stock entero de COAL, IRON, ALUMINIUM, GOLD y TIMBER. Cada producto empieza en cero:
BUY suma la cantidad y SELL la resta. Se conservan los saldos negativos y el valor
unitario no interviene en el cálculo.

`app.rentabilidad.calcular_producto_mas_rentable` utiliza Decimal para acumular los
importes de ventas. El endpoint reutiliza ambas funciones y el modelo `Transaccion`.

Con el entorno virtual creado, instala las dependencias de desarrollo (incluyen
las de la aplicación, pytest y httpx2 para TestClient) y ejecuta toda la suite desde
la raíz:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m pytest -q
```

La suite incluye las pruebas unitarias de stock y rentabilidad, y las de
integración HTTP con TestClient: resumen de compras y ventas, lista vacía, solo
compras, cantidad negativa (422), independencia entre peticiones y publicación del
contrato en OpenAPI. También comprueba que `/api-docs` sigue disponible. No requiere
iniciar Uvicorn.

## Cobertura de la lógica de negocio

Instala las dependencias de desarrollo, que incluyen pytest-cov, y ejecuta desde
la raíz del repositorio:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m pytest -q --cov=app.stock --cov=app.rentabilidad --cov-report=term-missing --cov-fail-under=80
```

El comando ejecuta toda la suite, incluidas las pruebas de integración, y mide
únicamente la cobertura de líneas de `app/stock.py` y `app/rentabilidad.py`.
El informe muestra la cobertura por módulo, el total y las líneas sin ejecutar.
La ejecución falla si hay pruebas fallidas o si la cobertura total de esos dos
módulos es inferior al 80 %. Los archivos de datos `.coverage` y `.coverage.*`
quedan excluidos de Git.
