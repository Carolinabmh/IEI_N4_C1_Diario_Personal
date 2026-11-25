# Diario Personal

Proyecto desarrollado para las Evaluaciones 1, 2 y 3 de Programación Backend de Ingeniería en Informática, INACAP, utilizando Python, Django y Django REST Framework.

## Descripción

Diario Personal es una aplicación web desarrollada en Django que tiene como propósito digitalizar y centralizar la gestión de entradas personales.

En la primera etapa se implementó la estructura inicial del proyecto, una página de bienvenida, rutas propias de la aplicación y una página de error 404 personalizada.

En la segunda etapa se incorporó una base de datos MySQL y se desarrolló una API REST utilizando Django REST Framework.

En la tercera etapa se implementaron operaciones CRUD mediante vistas basadas en clases (CBV), formularios personalizados, plantillas HTML y un menú de navegación que permite gestionar las entidades directamente desde la aplicación web.

## Tecnologías utilizadas

- Python
- Django
- Django REST Framework
- MySQL
- phpMyAdmin
- python-decouple
- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Git y GitHub

Las dependencias del proyecto se encuentran registradas en `requirements.txt`.

## Estructura del proyecto

El proyecto contiene las siguientes aplicaciones:

- **core:** configuración principal de Django.
- **entradas:** gestión de categorías, estados, entradas del diario e historial de cambios de estado.
- **usuarios:** gestión del modelo personalizado de usuarios, registro e inicio de sesión.
- **biblio_app:** aplicación de ejemplo incluida en el proyecto original del docente.

Los archivos principales utilizados son:

- `models.py`: definición de los modelos.
- `views.py`: vistas de la aplicación y ViewSets.
- `forms.py`: formularios personalizados.
- `serializer.py`: serialización de los modelos.
- `urls.py`: configuración de rutas.
- `templates/`: plantillas HTML.
- `static/`: archivos CSS, JavaScript e imágenes.
- `database.sql`: creación de la base de datos, usuario y permisos.
- `requirements.txt`: dependencias del proyecto.
- `.env`: variables de entorno para la configuración local.

## Modelo de datos

La aplicación utiliza los siguientes modelos:

- **Categoria:** clasifica las entradas del diario.
- **Estado:** identifica el estado de una entrada.
- **Entrada:** almacena el título, contenido y demás información de cada registro personal.
- **HistorialEstado:** permite registrar y consultar los cambios de estado de las entradas.
- **MiUsuario:** modelo personalizado basado en `AbstractUser`, con campos adicionales como teléfono, fecha de nacimiento y biografía.

Las relaciones entre los modelos se gestionan mediante el ORM de Django.

## Instalación y configuración

### 1. Clonar el repositorio

```powershell
git clone -b dev-diario https://github.com/Carolinabmh/IEI_N4_C1_Diario_Personal.git
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

Iniciar el servicio MySQL mediante WampServer y acceder a phpMyAdmin.

El archivo `database.sql`, ubicado en la raíz del proyecto, contiene las instrucciones necesarias para:

- Crear la base de datos `diario_personal_v2`.
- Crear el usuario `diario_app`.
- Otorgar permisos sobre la base de datos.

Antes de ejecutar el script, reemplazar la contraseña de ejemplo por una contraseña propia.

### 5. Configurar las variables de entorno

Crear un archivo `.env` en la raíz del proyecto con las siguientes variables:

```dotenv
SECRET_KEY=CLAVE_SECRETA_LOCAL
NAME=diario_personal_v2
HOST=localhost
PORT=3306
USER=diario_app
PASSWORD=CONTRASENA_MYSQL
```

Los valores deben reemplazarse por los correspondientes al entorno local.

Durante el desarrollo se utilizó el usuario root de MySQL. Para una nueva instalación se puede utilizar el usuario diario_app definido en el script SQL.

El archivo `.env` contiene información sensible y no debe publicarse con credenciales reales.

### 6. Aplicar las migraciones

```powershell
python manage.py migrate
```

### 7. Crear un superusuario

```powershell
python manage.py createsuperuser
```

### 8. Verificar la configuración

```powershell
python manage.py check
```

### 9. Iniciar el servidor

```powershell
python manage.py runserver
```

La aplicación estará disponible en:

http://127.0.0.1:8000/

El panel de administración de Django estará disponible en:

http://127.0.0.1:8000/admin/

## API REST

La API REST fue implementada mediante serializers, ViewSets y DefaultRouter de Django REST Framework.

Los endpoints principales de entradas son:

- `GET /api/entradas/`
- `GET /api/entradas/{id}/`
- `POST /api/entradas/`
- `PUT /api/entradas/{id}/`
- `PATCH /api/entradas/{id}/`
- `DELETE /api/entradas/{id}/`

También se encuentran disponibles las siguientes rutas:

- `/api/categorias/`
- `/api/estados/`
- `/api/historial-estados/`
- `/api/usuarios/`

Las rutas permiten gestionar los recursos mediante los métodos HTTP habilitados en sus respectivos ViewSets.

La API de usuarios permite la consulta de información por parte del administrador.

La raíz de la API se encuentra en:

http://127.0.0.1:8000/api/

## CRUD mediante vistas basadas en clases (CBV)

En la Evaluación 3 se implementaron las operaciones de creación, consulta, actualización y eliminación de registros mediante las vistas genéricas de Django.

Las vistas utilizadas son:

- **ListView:** muestra el listado de registros.
- **DetailView:** muestra la información detallada de un registro.
- **CreateView:** permite crear nuevos registros.
- **UpdateView:** permite modificar registros existentes.
- **DeleteView:** permite eliminar registros mediante una confirmación previa.

Estas vistas fueron implementadas para las cinco entidades principales del proyecto.

### Entradas

| Operación | Ruta |
|---|---|
| Listar | `/entradas/` |
| Crear | `/entradas/crear/` |
| Detalle | `/entradas/{id}/` |
| Editar | `/entradas/{id}/editar/` |
| Eliminar | `/entradas/{id}/eliminar/` |

### Categorías

| Operación | Ruta |
|---|---|
| Listar | `/categorias/` |
| Crear | `/categorias/crear/` |
| Detalle | `/categorias/{id}/` |
| Editar | `/categorias/{id}/editar/` |
| Eliminar | `/categorias/{id}/eliminar/` |

### Estados

| Operación | Ruta |
|---|---|
| Listar | `/estados/` |
| Crear | `/estados/crear/` |
| Detalle | `/estados/{id}/` |
| Editar | `/estados/{id}/editar/` |
| Eliminar | `/estados/{id}/eliminar/` |

### Historial de estados

| Operación | Ruta |
|---|---|
| Listar | `/historial/` |
| Crear | `/historial/crear/` |
| Detalle | `/historial/{id}/` |
| Editar | `/historial/{id}/editar/` |
| Eliminar | `/historial/{id}/eliminar/` |

### Usuarios

| Operación | Ruta |
|---|---|
| Listar | `/usuarios/` |
| Crear | `/usuarios/crear/` |
| Detalle | `/usuarios/{id}/` |
| Editar | `/usuarios/{id}/editar/` |
| Eliminar | `/usuarios/{id}/eliminar/` |

## Formularios personalizados

Los formularios se encuentran definidos en los archivos `forms.py` de las aplicaciones correspondientes.

Se utilizaron formularios de Django basados en los modelos, definiendo los campos que se presentan al usuario.

También se incorporaron widgets personalizados y atributos HTML como:

- Clases de Bootstrap.
- Placeholder.
- Campos de texto.
- Áreas de texto.
- Listas desplegables.
- Casillas de verificación.
- Campos de fecha.
- Campos de contraseña.

Los formularios se mantienen separados de las vistas para facilitar la organización y el mantenimiento del código.

## Interfaz y navegación

La interfaz web fue desarrollada utilizando plantillas HTML, Bootstrap y una hoja de estilos CSS personalizada.

Se implementó una plantilla base denominada `base.html`, que permite reutilizar el menú de navegación y los estilos en las diferentes páginas de la aplicación.

La aplicación cuenta con:

- Página de bienvenida pública.
- Menú de navegación adaptable.
- Listados de registros.
- Vistas de detalle.
- Formularios de creación y edición.
- Confirmaciones de eliminación.
- Botones para navegar entre las diferentes vistas.
- Página de error 404 personalizada.

## Gestión de usuarios

Como funcionalidad complementaria se incorporaron las siguientes opciones:

- Registro de usuarios.
- Inicio de sesión.
- Cierre de sesión.
- Diferenciación entre usuarios normales y administradores.

Cada usuario normal puede consultar y gestionar sus propias entradas personales.

El administrador puede acceder a la gestión general de usuarios, categorías, estados y entradas.

Las funcionalidades de autenticación y seguridad serán ampliadas en la siguiente etapa del proyecto.

## Persistencia de datos

La información se almacena en MySQL mediante el ORM de Django.

Las tablas y registros pueden consultarse desde phpMyAdmin.

La estructura de la base de datos se administra mediante las migraciones de Django.

## Pruebas realizadas

Durante el desarrollo se realizaron pruebas de:

- Creación de registros.
- Listado y consulta de registros.
- Actualización de registros.
- Eliminación de registros.
- Navegación entre las páginas.
- Visualización de la página de bienvenida.
- Registro e inicio de sesión de usuarios.
- Cierre de sesión.
- Visualización de entradas según el usuario autenticado.
- Consulta de los endpoints de la API REST.
- Persistencia de información en MySQL.

Las pruebas se realizaron mediante el navegador web, la interfaz de Django REST Framework y la revisión de las solicitudes HTTP en la terminal del servidor.

## Control de versiones

El código fuente se encuentra alojado en GitHub:

https://github.com/Carolinabmh/IEI_N4_C1_Diario_Personal

La rama de desarrollo utilizada es `dev-diario`.

## Estado del proyecto

### Evaluación 1

- Estructura inicial del proyecto.
- Página de bienvenida.
- Configuración de rutas.
- Página de error 404 personalizada.

### Evaluación 2

- Modelos y relaciones.
- Migraciones.
- Conexión con MySQL.
- Serializers y ViewSets.
- API REST.
- Variables de entorno.
- Script SQL.

### Evaluación 3

- CRUD de las cinco entidades principales.
- Implementación de 25 vistas basadas en clases.
- Formularios personalizados.
- Widgets y atributos HTML.
- Plantillas HTML.
- Bootstrap y CSS personalizado.
- Menú de navegación.
- Gestión de usuarios.
- Pruebas de funcionamiento.

El proyecto continúa en desarrollo como parte de las evaluaciones de Programación Backend.

## Información académica

- **Institución:** INACAP.
- **Carrera:** Ingeniería en Informática.
- **Asignatura:** Programación Backend.
- **Proyecto:** Diario Personal.
- **Evaluación:** Evaluación N°3.
