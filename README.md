# QA Automation Suite — demoqa.com

Suite de pruebas automatizadas end-to-end sobre [demoqa.com](https://demoqa.com/), desarrollada como solución a la prueba técnica de QA.

> Esta solución se encuentra en la rama `cesar` de este repositorio, sin alterar `main`.

## Stack tecnológico

- **Python** + **pytest** como framework de testing
- **Playwright** como herramienta de automatización de navegador

### Sobre el cambio de Selenium/Docker a Playwright

El repositorio original está configurado para ejecutarse con **Selenium** dentro de un contenedor **Docker** (`docker compose exec app python3 -m pytest ...`).

Las instrucciones de la evaluación permiten explícitamente el uso de cualquier framework de automatización:

> "candidates are free to use any automation testing tool or framework they are more familiar with, as long as the proposed solution allows the assigned test cases to be executed and properly validated."

Con base en eso, esta rama implementa la solución con **Playwright + pytest**, ejecutado directamente en un entorno virtual de Python (sin Docker), por ser la herramienta con la que se tiene mayor familiaridad. Las instrucciones de instalación y ejecución más abajo reemplazan al comando de Docker del `README` original para efectos de esta rama.

## Estructura del proyecto

```
├── pages/                  # Page Objects (patrón POM)
│   ├── base_page.py        # Clase base: navegación con reintento, remove_ads(), etc.
│   ├── practice_form_page.py
│   ├── select_menu_page.py
│   ├── web_tables_page.py
│   ├── user_validation.py  # Modal de registro/validación de Web Tables
│   └── register_page.py
├── tests/                  # Casos de prueba, un archivo por feature
│   ├── test_practice_form.py
│   ├── test_select_menu.py
│   ├── test_web_tables_crud.py
│   ├── test_validation.py
│   └── test_register_user.py
├── utils/
│   └── data_generator.py   # Generación de datos de prueba aleatorios (Faker)
├── requirements.txt
└── pytest.ini
```

## Instalación

> Requiere Python 3.10+ instalado.

```bash
# 1. Cambiarse a la rama de la solución
git checkout cesar

# 2. Crear y activar un entorno virtual
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Instalar los navegadores que usa Playwright
playwright install
```

## Cómo correr los tests

Correr toda la suite:

```bash
pytest
```

Correr un archivo específico:

```bash
pytest tests/test_select_menu.py
```

Correr en un navegador específico (por defecto Playwright usa Chromium; el proyecto se validó también en Firefox):

```bash
pytest --browser firefox
```

Correr en modo visual (ver el navegador mientras ejecuta):

```bash
pytest --headed
```

## Mapeo de casos de prueba asignados

| Caso asignado | Archivo de test |
|---|---|
| Case 1: Llenar el Practice Form con valores random | `tests/test_practice_form.py` |
| Case 2: Crear un nuevo usuario con valores random | `tests/test_register_user.py` |
| Case 3: Widgets / Select Menu (valores específicos) | `tests/test_select_menu.py` |
| Case 4: Web Tables — agregar, editar, eliminar | `tests/test_web_tables_crud.py` |
| Case 5: Web Tables — formato incorrecto y campos vacíos | `tests/test_validation.py` |

## Notas de diseño

- **Page Object Model**: cada pantalla tiene su propia clase en `pages/`, heredando de `BasePage` (navegación común y limpieza de anuncios). Los tests en `tests/` no contienen selectores CSS ni lógica de bajo nivel de Playwright — solo orquestan llamadas a métodos de las Page Objects y hacen las aserciones.
- **Manejo de anuncios**: `demoqa.com` muestra banners publicitarios que pueden interferir con clics; `BasePage.remove_ads()` los elimina del DOM tras cada navegación.
- **Robustez ante inestabilidad del sitio**: `BasePage.navigate_to()` incluye reintento automático ante timeouts de red, dado que `demoqa.com` es un sitio de práctica público que ocasionalmente responde lento.
- **Selectores estables sobre componentes dinámicos (React)**: para verificar selecciones en componentes tipo `react-select` (Select Menu) y celdas de tabla (Web Tables), se priorizó el uso de roles de accesibilidad (`get_by_role`) y filtrado por texto (`filter(has_text=...)`) por encima de clases CSS generadas dinámicamente, que resultaron inconsistentes entre navegadores (Chromium/Firefox) en pruebas iniciales.
- **Sobre la validación de "wrong login"**: los puntos de evaluación mencionan "wrong Login" como ejemplo ilustrativo de validación de errores, pero ninguno de los 5 casos asignados incluye un flujo de login. El requisito de validar errores de formato/campos vacíos se cubre en el Case 5 (`test_validation.py`), sobre el formulario de Web Tables.

## Bonus: pruebas de performance (ReqRes API)

Se implementó el bonus de performance testing usando **Locust**, por ser una herramienta basada en Python, consistente con el resto del stack del proyecto.

### Estructura

```
performance/
└── locustfile.py   # Define un usuario simulado que ejercita los 5 endpoints de ReqRes
```

### Instalación

```bash
pip install locust   # ya incluido en requirements.txt
```

### Configuración de la API key

La API key de ReqRes se lee desde una variable de entorno (nunca hardcodeada en el código):

```powershell
# PowerShell (Windows)
$env:REQRES_API_KEY="tu_api_key_aqui"
```
```bash
# macOS / Linux
export REQRES_API_KEY="tu_api_key_aqui"
```

### Ejecución

Con interfaz web (`http://localhost:8089`):

```bash
locust -f performance/locustfile.py
```

En modo headless, generando un reporte CSV:

```bash
locust -f performance/locustfile.py --headless -u 20 -r 2 --run-time 1m --csv=performance/report
```

### Endpoints cubiertos

| Endpoint | Peso relativo |
|---|---|
| `GET /api/users?page=2` | 3 |
| `GET /api/users/2` | 3 |
| `POST /api/users` | 1 |
| `PUT /api/users/2` | 1 |
| `DELETE /api/users/2` | 1 |

Las lecturas (`GET`) tienen mayor peso que las escrituras, simulando un patrón de uso más cercano a un flujo real (se lee con más frecuencia de la que se crea/edita/elimina).

### Resultado de las pruebas

Se ejecutaron tres corridas independientes contra los 5 endpoints de ReqRes:

**Corridas 1 y 2** — 5 usuarios concurrentes, spawn rate 1, ~1 minuto:

| Endpoint | Corrida 1 (fails/requests) | Corrida 2 (fails/requests) |
|---|---|---|
| GET /api/users?page=2 | 0/78 (0%) | 0/60 (0%) |
| GET /api/users/2 | 0/63 (0%) | 0/58 (0%) |
| PUT /api/users/2 | 0/20 (0%) | 0/15 (0%) |
| POST /api/users | 5/26 (~19%) | 6/14 (~43%) |
| DELETE /api/users/2 | 7/26 (~27%) | 4/19 (~21%) |

**Corrida 3** — modo headless, 20 usuarios concurrentes, spawn rate 2, 1 minuto (`locust -f performance/locustfile.py --headless -u 20 -r 2 --run-time 1m --csv=performance/report`):

| Endpoint | Fails/Requests | Tasa de error |
|---|---|---|
| GET /api/users?page=2 | 0/173 | 0% |
| GET /api/users/2 | 0/181 | 0% |
| PUT /api/users/2 | 33/55 | 60% |
| POST /api/users | 45/69 | ~65% |
| DELETE /api/users/2 | 45/61 | ~74% |

**Hallazgo**: en las tres corridas, los endpoints de lectura (`GET`) no presentaron
ningún fallo, incluso al cuadruplicar la concurrencia (5 → 20 usuarios). Los endpoints
de escritura (`POST`, `PUT`, `DELETE`) sí muestran errores `429 Too Many Requests`, y su
tasa de error **escala con la carga**: con 5 usuarios concurrentes, `PUT` se mantuvo sin
fallos, pero al subir a 20 usuarios alcanzó ~60% de error. Esto confirma que ReqRes
aplica un límite de tasa (*rate limiting*) específico para operaciones de escritura, cuyo
umbral se supera más rápido a medida que aumenta la concurrencia — comportamiento
esperable en una API pública de uso gratuito.