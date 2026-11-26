# AI PROCESS

## 1. Introducción
Este documento registra el uso de herramientas de Inteligencia Artificial durante el análisis, diseño, implementación, pruebas y validación de la aplicación Trycore inventario.

## 2. Herramientas y metodología
### 2.1 Herramientas utilizadas
Las herramientas principales que se utilizaron para desarrollar el proyecto fueron:

- *ChatGPT:* Análisis funcional, evaluación de decisiones técnicas, planificación y revisión del desarrollo, construcción de prompts para Codex.
- *Codex en Visual Studio Code:* Inspección del repositorio, generación y modificación de código, ejecución de pruebas y validación de componentes.
- *Visual Studio Code:* Edición, inspección de archivos y ejecución de comandos.
- *Git y GitHub:* Control de versiones, seguimiento de funcionalidades y Pull Requests mediante Gitflow.
- *Swagger UI:* Validación manual de endpoints REST.

## 3. Historial cronológico

### Interacción 001
Fecha: 2026-11-25
Herramienta: ChatGPT

Trabaja en el repositorio abierto en VS Code. Esta tarea corresponde a la rama
feature/estructura-api del ejercicio de inventario de Trycore.

Objetivo de esta tarea: crear la base mínima de una aplicación FastAPI y
comprobar que se puede iniciar localmente en Windows con PowerShell.

1. Antes de editar, comprueba la rama activa, el estado de Git y la versión
   de Python disponible. Si la rama activa no es feature/estructura-api,
   detente e indícame cuál está activa.
2. Crea una aplicación mínima en app/main.py, con una instancia de FastAPI
   llamada app, un título descriptivo y Swagger UI configurado en /api-docs.
3. Declara las dependencias necesarias para ejecutar la aplicación. Añade
   al .gitignore el entorno virtual .venv y los archivos generados por Python.
4. Documenta en el README los comandos de PowerShell para crear el entorno
   virtual, instalar dependencias e iniciar el servidor. Usa el intérprete
   del entorno virtual de forma explícita para que la ejecución también
   funcione si PowerShell restringe la activación de scripts.
5. Si el entorno lo permite, inicia el servidor y verifica que GET /api-docs
   y GET /openapi.json responden HTTP 200. Detén el servidor de prueba al
   terminar. Si alguna comprobación falla, informa el error exacto.

Alcance: deja la aplicación sin endpoints de negocio en esta primera tarea.
El contrato JSON, los cálculos, las pruebas de negocio y la persistencia están
fuera de este cambio. No hagas commits, push ni abras Pull Requests.

Al terminar, enumera los archivos modificados, explica para qué sirve cada
uno y distingue las comprobaciones ejecutadas de las pendientes.


### Interacción 002
Fecha: 2026-11-25
Herramienta: ChatGPT

Prompt:

Trabaja en el repositorio abierto trycore-inventario-api. Quiero cerrar la primera fase, que consiste en la estructura mínima de FastAPI. Ya comprobé manualmente que /api-docs abre en el navegador.

1. Revisa git status, la rama actual, las ramas disponibles y el remoto origin. Comprueba que los cambios de esta fase están en feature/estructura-api y que la rama parte de develop. Si la situación es distinta, explícame qué encontraste antes de mover cambios o publicar.
2. Revisa .gitignore, requirements.txt, app/main.py y README.md. Confirma que .venv y __pycache__ quedan fuera del commit. Muéstrame un resumen breve de los cambios.
3. Si todo corresponde a esta fase, agrega únicamente los archivos de la estructura inicial, revisa el diff preparado y crea el commit “Configura la estructura inicial de la API de inventario”. Si ya existe ese commit, reutilízalo.
4. Sube la rama feature/estructura-api a origin. Crea o localiza el Pull Request con base develop y origen feature/estructura-api. Título: “Configura la estructura inicial de la API de inventario”. Incluye en la descripción qué se implementó y cómo se verificó. Deja el PR abierto para mi revisión.
5. Devuélveme el hash corto del commit, el enlace del PR y el estado final de Git. Si no puedes crear el PR desde este entorno, indícame cómo abrirlo en GitHub con las ramas correctas.

Limita esta tarea a Git y a la revisión de lo que ya existe.


### Interacción 003 
Fecha: 2026-11-26
Herramienta: ChatGPT

Prompt:

Implementa únicamente el modelo de entrada de una transacción de inventario con Pydantic en el proyecto FastAPI existente.

Git:
- Comprueba que el árbol de trabajo esté limpio. Actualiza develop desde origin con fast-forward y confirma que incluye el cambio de la estructura inicial.
- Crea desde develop la rama feature/modelo-transaccion.

Implementación:
- Crea app/schemas.py con un modelo Transaccion compatible con la versión de Pydantic instalada.
- Define estos campos obligatorios: tipo (BUY o SELL), fecha (una fecha como 2026-11-26), producto (COAL, IRON, ALUMINIUM, GOLD o TIMBER), cantidad (entero mayor o igual a cero) y valor_unitario (número mayor o igual a cero).
- Conserva la precisión decimal del valor unitario.
- Limita el cambio al modelo de una transacción. La lista de transacciones, los cálculos de stock y rentabilidad, y la ruta HTTP se implementarán en fases posteriores.

Verificación:
- Usa el intérprete de .venv para comprobar una venta válida con valor decimal y casos inválidos de cantidad negativa, valor unitario negativo, producto desconocido y fecha inválida.
- Indica qué resultado obtuviste en cada caso. La validación debe funcionar directamente con el modelo, sin arrancar el servidor.
- Revisa el diff y, si las comprobaciones pasan, crea el commit “Define el modelo de entrada de las transacciones”, sube la rama y abre un PR hacia develop para revisión. Devuélveme el enlace y el estado final de Git.Implementa únicamente el modelo de entrada de una transacción de inventario con Pydantic en el proyecto FastAPI existente.

Git:
- Comprueba que el árbol de trabajo esté limpio. Actualiza develop desde origin con fast-forward y confirma que incluye el cambio de la estructura inicial.
- Crea desde develop la rama feature/modelo-transaccion.

Implementación:
- Crea app/schemas.py con un modelo Transaccion compatible con la versión de Pydantic instalada.
- Define estos campos obligatorios: tipo (BUY o SELL), fecha (una fecha como 2026-11-26), producto (COAL, IRON, ALUMINIUM, GOLD o TIMBER), cantidad (entero mayor o igual a cero) y valor_unitario (número mayor o igual a cero).
- Conserva la precisión decimal del valor unitario.
- Limita el cambio al modelo de una transacción. La lista de transacciones, los cálculos de stock y rentabilidad, y la ruta HTTP se implementarán en fases posteriores.

Verificación:
- Usa el intérprete de .venv para comprobar una venta válida con valor decimal y casos inválidos de cantidad negativa, valor unitario negativo, producto desconocido y fecha inválida.
- Indica qué resultado obtuviste en cada caso. La validación debe funcionar directamente con el modelo, sin arrancar el servidor.
- Revisa el diff y, si las comprobaciones pasan, crea el commit “Define el modelo de entrada de las transacciones”, sube la rama y abre un PR hacia develop para revisión. Devuélveme el enlace y el estado final de Git.


### Interacción 004
Fecha: 2026-11-26
Herramienta: ChatGPT

En el repositorio trycore-inventario-api, implementa el cálculo del stock final por producto y sus pruebas unitarias.

1. Comprueba el estado de Git. Con el árbol limpio, actualiza develop desde origin mediante fast-forward y verifica que ya contiene app/schemas.py del PR #2. Crea desde ahí la rama feature/calculo-stock.

2. Implementa una función de negocio llamada calcular_stock que reciba una lista de objetos Transaccion y devuelva un diccionario con el stock entero de COAL, IRON, ALUMINIUM, GOLD y TIMBER. Ubícala en un módulo separado de main.py y de los esquemas. Reutiliza el modelo existente.

3. Aplica estas reglas: cada producto empieza en cero, BUY suma la cantidad y SELL la resta. Conserva los saldos negativos. Incluye siempre los cinco productos en el resultado. El valor unitario no interviene en el stock.

4. Añade pruebas con pytest y compara resultados concretos:
   - Lista vacía: los cinco productos quedan en cero.
   - BUY de 10 IRON y SELL de 14 IRON: IRON queda en -4 y los demás en cero.
   - Dos compras de GOLD de 3 y 5 unidades, y una venta de 2 TIMBER: GOLD queda en 8, TIMBER en -2 y los demás en cero.
   Ejecuta las pruebas con el intérprete de .venv e informa el comando y el resultado real. Si agregas pytest como dependencia de desarrollo, sigue la convención del repositorio y documenta cómo instalarla.

5. Limita este cambio al cálculo de stock y sus pruebas. El producto más rentable y el endpoint HTTP tendrán sus propias fases.

6. Si las pruebas pasan, revisa el diff, crea el commit “Calcula el stock final por producto”, sube la rama y abre un PR desde feature/calculo-stock hacia develop. Deja el PR abierto para mi revisión. Devuélveme el enlace, el hash del commit y el resultado de las pruebas.

### Interacción 005
Fecha: 2026-11-26
Herramienta: ChatGPT

Prompt:

En el repositorio trycore-inventario-api, implementa la función de negocio que identifica el producto más rentable según las reglas del ejercicio.

1. Revisa el estado de Git. Actualiza develop desde origin con fast-forward, comprueba que ya contiene app/stock.py del PR #3 y crea desde ahí la rama feature/producto-mas-rentable.

2. Reutiliza el modelo Transaccion. Implementa una función que reciba las transacciones en su orden original y devuelva el nombre del producto con mayor importe acumulado de ventas. Para cada SELL, suma cantidad × valor_unitario al total de ese producto. Utiliza Decimal para los importes.

3. Considera candidatos únicamente a los productos con al menos una venta. Si la lista está vacía o solo contiene compras, devuelve None, que en la futura respuesta JSON será null. Si dos productos empatan en el total, gana aquel cuya primera venta aparezca antes en la lista.

4. Añade pruebas unitarias con pytest para estos casos:
   - Ventas acumuladas: GOLD vende 2 × 10 y luego 3 × 5; IRON vende 1 × 30. Gana GOLD con 35. Incluye una compra de IRON de importe alto para comprobar que las compras se excluyen.
   - Lista vacía y lista con solo compras: ambas devuelven None.
   - Empate: primero aparece una compra de COAL, luego una venta de GOLD por 20 y después una venta de COAL por 20. Gana GOLD porque realizó la primera venta.
   - Una única venta de TIMBER con importe cero: gana TIMBER porque sí hubo una venta.

5. Ejecuta toda la suite de pytest con el intérprete de .venv, incluidas las pruebas de stock. Mantén esta fase limitada a la función de negocio y sus pruebas. El endpoint se implementará en el siguiente paso.

6. Si las pruebas pasan, revisa el diff, crea el commit “Calcula el producto más rentable por ventas”, sube la rama y abre un PR hacia develop. Déjalo abierto para mi revisión e informa el enlace, el hash del commit y el resultado real de pytest.

### Interacción 006
Fecha: 2026-11-26
Herramienta: ChatGPT

Prompt:

En trycore-inventario-api, implementa el único endpoint de negocio: POST /inventario/resumen. Su responsabilidad es recibir las transacciones, llamar a las funciones de negocio existentes y devolver el resumen.

1. Comprueba que el árbol de trabajo esté limpio. Actualiza develop desde origin mediante fast-forward y verifica que contiene calcular_stock y calcular_producto_mas_rentable. Crea desde ahí feature/endpoint-resumen.

2. Revisa si el enunciado disponible o el repositorio ya fija un ejemplo exacto del JSON de entrada y salida. Respeta ese contrato. Si no hay un formato previo, usa una lista JSON de objetos Transaccion como cuerpo de entrada y un objeto de respuesta con los campos stock_final y producto_mas_rentable. Documenta el formato utilizado con un ejemplo que se pueda copiar en Swagger.

3. Reutiliza el modelo Transaccion y las dos funciones existentes. Declara el modelo de respuesta para que Swagger muestre los cinco productos y que el ganador puede ser null. Conserva la documentación en /api-docs. El procesamiento es en memoria y cada petición se calcula de forma independiente.

4. Añade pruebas de integración que envíen peticiones HTTP a la aplicación FastAPI con TestClient. Comprueba el código de estado y el contenido de la respuesta:
   - Compra de 10 IRON a 2, venta de 14 IRON a 2 y venta de 2 GOLD a 20: HTTP 200, stock IRON = -4, GOLD = -2, los otros tres productos en cero y ganador GOLD (40 frente a 28).
   - Lista vacía: HTTP 200, los cinco stocks en cero y ganador null.
   - Solo una compra de 3 TIMBER: HTTP 200, TIMBER = 3, los otros cuatro stocks en cero y ganador null.
   - Transacción con cantidad -1: HTTP 422.

5. Actualiza el apartado del README que aún dice que no existen endpoints. Ejecuta toda la suite con el intérprete de .venv y comprueba en /openapi.json que POST /inventario/resumen está publicado.

6. Si las verificaciones pasan, revisa el diff, crea el commit “Expone el resumen de inventario mediante FastAPI”, sube la rama y abre un PR hacia develop. Déjalo abierto para revisión. Devuélveme el enlace, el hash, el resultado real de pytest y el JSON exacto que puedo pegar en Swagger para reproducir el primer caso.

### Interacción 007
Fecha: 2026-11-17 
Herramienta: Codex

Prompt:

 En trycore-inventario-api, verifica y deja reproducible la cobertura de la lógica de negocio. El objetivo es alcanzar al menos el 80 % de cobertura de líneas sobre app/stock.py y app/rentabilidad.py.

1. Comprueba el estado de Git, actualiza develop desde origin mediante fast-forward y verifica que contiene POST /inventario/resumen. Crea desde develop la rama feature/cobertura-negocio.

2. Revisa las dependencias de desarrollo. Reutiliza la herramienta de cobertura existente o, si hace falta, añade pytest-cov a requirements-dev.txt siguiendo la convención del repositorio.

3. Ejecuta toda la suite con el intérprete de .venv. Limita la medición a los dos módulos que contienen las reglas de negocio y configura el umbral del 80 %. Usa este comando desde la raíz del repositorio:

.\.venv\Scripts\python.exe -m pytest -q --cov=app.stock --cov=app.rentabilidad --cov-report=term-missing --cov-fail-under=80

4. Si el resultado está por debajo del 80 %, identifica qué comportamiento quedó sin probar y añade pruebas unitarias con entradas y resultados esperados concretos. Si ya se cumple el umbral, conserva las pruebas existentes.

5. Documenta en el README el comando para reproducir la medición. Comprueba que los archivos generados por la herramienta, como .coverage, queden fuera del commit.

6. Revisa el diff, crea un commit en imperativo, sube la rama y abre un PR hacia develop. Déjalo abierto para mi revisión. Devuélveme el enlace, el hash del commit, el número de pruebas aprobadas y la tabla real de cobertura por módulo y total.

## 8. Limitaciones conocidas y Reflexión

Durante el desarrollo identifiqué algunas limitaciones y posibles mejoras que considero importantes para una evolución futura de la aplicación.

**8.1. Ejecución local**

La aplicación fue desarrollada y validada en un entorno local utilizando Python, FastAPI y Swagger.

No implementé una infraestructura de despliegue en la nube, ya que el objetivo principal era entregar una solución funcional y verificable dentro del alcance del desafío.

Para utilizarla en producción sería necesario definir una estrategia de despliegue, configuración de entornos y administración de infraestructura.

**8.2. Seguridad y autenticación**

La API no incluye mecanismos de autenticación ni gestión de roles y permisos.

Esta funcionalidad no fue incorporada porque no formaba parte del alcance establecido para el desafío. Sin embargo, sería necesaria antes de exponer los servicios a usuarios externos en un entorno productivo.

**8.3. Persistencia de la información**

La aplicación procesa las transacciones de compra y venta recibidas mediante una solicitud a la API, generando los resultados correspondientes sin necesidad de almacenar permanentemente la información.

En una evolución futura, se podría incorporar una base de datos que permita mantener un historial de transacciones, consultar movimientos anteriores y realizar un seguimiento del inventario a lo largo del tiempo.

### Reflexión final

El desarrollo de este desafío fue una oportunidad para aplicar y fortalecer mis conocimientos en ingeniería de software, programación, automatización y desarrollo de APIs REST.

Uno de los principales retos fue interpretar correctamente los requisitos del negocio y traducirlos en una solución capaz de procesar transacciones de compra y venta, calcular el stock final por producto e identificar el producto con mayor importe acumulado de ventas. Para ello, analicé las reglas de negocio, los posibles escenarios de ejecución y las validaciones necesarias para garantizar la consistencia de los resultados.

Durante el proyecto utilicé ChatGPT para analizar requisitos, evaluar alternativas y tomar decisiones técnicas, mientras que Codex me apoyó en la implementación, revisión del código y ejecución de pruebas automatizadas.

Considero que uno de los aprendizajes más importantes fue la necesidad de mantener un criterio propio frente a las recomendaciones de IA, evaluando aspectos como la complejidad arquitectónica, la separación de responsabilidades, la legibilidad del código y la mantenibilidad de la solución.

También reforcé mis conocimientos en Python, FastAPI, APIs REST, validación de datos, testing y Gitflow, especialmente durante la implementación de la lógica de negocio, la integración de ramas mediante Pull Requests y las validaciones funcionales realizadas manualmente a través de Swagger.

Mi principal conclusión es que la Inteligencia Artificial puede acelerar significativamente el desarrollo de software, pero no reemplaza el análisis, el criterio técnico ni la validación humana. El verdadero valor está en saber utilizarla como herramienta de apoyo para construir soluciones funcionales, comprender las decisiones tomadas y garantizar la calidad de los resultados.