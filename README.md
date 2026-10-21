# Diario Personal

Proyecto desarrollado para las Evaluaciones 1 y 2 de Backend con Python, Django y Django REST Framework.

## Descripción

Diario Personal es una aplicación desarrollada en Django que tiene como propósito digitalizar y centralizar la gestión de entradas personales.

En la primera etapa se implementó la estructura inicial del proyecto, una página de bienvenida, rutas propias de la aplicación y una página de error 404 personalizada.

En la segunda etapa se incorporó una base de datos MySQL y se desarrolló una API REST utilizando Django REST Framework, que permite gestionar la información del diario mediante operaciones CRUD.

## Tecnologías utilizadas

- Python
- Django
- Django REST Framework
- MySQL
- phpMyAdmin
- python-decouple
- Git y GitHub

Las dependencias del proyecto se encuentran registradas en `requirements.txt`.

## Estructura del proyecto

El proyecto contiene las siguientes aplicaciones:

- **core:** configuración principal de Django.
- **entradas:** gestión de categorías, estados, entradas del diario e historial de cambios de estado.
- **usuarios:** gestión del modelo personalizado de usuarios.
- **biblio_app:** aplicación de ejemplo incluida en el proyecto original del docente.

## Modelo de datos

La aplicación utiliza los siguientes modelos:

- **Categoria:** clasifica las entradas del diario.
- **Estado:** identifica el estado de una entrada.
- **Entrada:** almacena el título, contenido y demás información de cada registro personal.
- **HistorialEstado:** registra los cambios de estado de las entradas.
- **MiUsuario:** modelo personalizado basado en `AbstractUser`, con campos adicionales como teléfono, fecha de nacimiento y biografía.

Las relaciones entre los modelos se gestionan mediante el ORM de Django.

## Instalación y configuración

### 1. Clonar el repositorio

```powershell
git clone https://github.com/Carolinabmh/IEI_N4_C1_Diario_Personal.git
cd IEI_N4_C1_Diario_Personal
```

### 2. Crear y activar el entorno virtual

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Instalar las dependencias

```powershell
pip install -r requirements.txt
```

### 4. Configurar la base de datos

Crear una base de datos MySQL denominada `diario_personal_v2`.

La conexión se configura mediante variables de entorno almacenadas localmente en un archivo `.env`, ubicado en la raíz del proyecto.

Las variables utilizadas son:

```dotenv
SECRET_KEY=CLAVE_SECRETA_LOCAL
NAME=diario_personal_v2
HOST=localhost
PORT=3306
USER=USUARIO_MYSQL
PASSWORD=CONTRASENA_MYSQL
```

Los valores de ejemplo deben reemplazarse por los correspondientes al entorno local.

El archivo `.env` contiene información sensible y no debe publicarse con credenciales reales.

### 5. Aplicar las migraciones

```powershell
python manage.py migrate
```

### 6. Crear un superusuario

```powershell
python manage.py createsuperuser
```

### 7. Iniciar el servidor

```powershell
python manage.py runserver
```

La aplicación estará disponible en:

http://127.0.0.1:8000/

El panel de administración de Django estará disponible en:

http://127.0.0.1:8000/admin/

## API REST

La API REST fue implementada mediante serializers, ModelViewSets y DefaultRouter de Django REST Framework.

Los endpoints principales son:

- `GET /api/entradas/`
- `GET /api/entradas/{id}/`
- `POST /api/entradas/`
- `PUT /api/entradas/{id}/`
- `PATCH /api/entradas/{id}/`
- `DELETE /api/entradas/{id}/`

También se encuentran disponibles las rutas:

- `/api/categorias/`
- `/api/estados/`
- `/api/historial-estados/`
- `/api/usuarios/`

Estas rutas permiten gestionar los recursos correspondientes mediante los métodos HTTP habilitados en sus ViewSets.

La raíz de la API se encuentra en:

http://127.0.0.1:8000/api/

## Persistencia de datos

La información se almacena en MySQL mediante el ORM de Django.

Las tablas y registros pueden consultarse desde phpMyAdmin. La estructura de la base de datos se administra mediante las migraciones de Django.

## Control de versiones

El código fuente se encuentra alojado en GitHub:

https://github.com/Carolinabmh/IEI_N4_C1_Diario_Personal

La rama de desarrollo utilizada es `dev-diario`.

## Estado del proyecto

Se implementaron los modelos de datos, las migraciones, los serializers, los ViewSets, las rutas REST y la conexión con MySQL.

Se realizaron pruebas de creación, consulta, actualización y eliminación de registros mediante la interfaz de Django REST Framework, verificando también su persistencia en phpMyAdmin.

El proyecto continúa en desarrollo como parte de las evaluaciones de Backend.