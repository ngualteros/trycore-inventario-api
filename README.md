# Trycore Inventario API

API de inventario con FastAPI, modelo de transacción y cálculo del stock final por
producto. Esta etapa no incluye endpoints de negocio, cálculo de rentabilidad ni
persistencia.

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
disponible en <http://127.0.0.1:8000/openapi.json>. Al no haber endpoints de negocio,
el campo `paths` del esquema estará vacío.

Para comprobar las respuestas desde otra terminal de PowerShell:

```powershell
(Invoke-WebRequest -Uri 'http://127.0.0.1:8000/api-docs' -UseBasicParsing).StatusCode
(Invoke-WebRequest -Uri 'http://127.0.0.1:8000/openapi.json' -UseBasicParsing).StatusCode
```

Ambos comandos deben mostrar `200`. Detén el servidor con `Ctrl+C` en la terminal
donde lo iniciaste.

## Cálculo de stock y pruebas unitarias

`app.stock.calcular_stock` recibe una lista de objetos `Transaccion` y devuelve el
stock entero de COAL, IRON, ALUMINIUM, GOLD y TIMBER. Cada producto empieza en cero:
BUY suma la cantidad y SELL la resta. Se conservan los saldos negativos y el valor
unitario no interviene en el cálculo.

Con el entorno virtual creado, instala las dependencias de desarrollo (incluyen
las dependencias de la aplicación) y ejecuta las pruebas desde la raíz:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m pytest -q
```

Las pruebas comparan los cinco productos en cada resultado: lista vacía con todos
en cero; compra de 10 IRON y venta de 14 IRON con saldo -4; y compras de 3 y 5 GOLD
con venta de 2 TIMBER, que dejan GOLD en 8 y TIMBER en -2. Se ejecutan directamente
sobre la función, sin iniciar el servidor.
