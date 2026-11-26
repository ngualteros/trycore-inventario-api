# Trycore Inventario API

Base mínima de una API de inventario con FastAPI. Esta etapa no incluye endpoints
de negocio, contratos JSON de inventario, cálculos ni persistencia.

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
