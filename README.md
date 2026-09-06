# QA Automation Suite — demoqa.com

Suite de pruebas automatizadas end-to-end sobre [demoqa.com](https://demoqa.com/), desarrollada como solución a la prueba técnica de QA.

> Esta solución se encuentra en la rama `qa-automation-cesar-villacis` de este repositorio, sin alterar `main`.

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
git checkout qa-automation-cesar-villacis

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
python -m pytest tests
```

Correr un archivo específico:

```bash
pytest -m tests/test_select_menu.py
```

Correr en un navegador específico (por defecto Playwright usa Chromium; el proyecto se validó también en Firefox):

```bash
pytest -m --browser firefox
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

