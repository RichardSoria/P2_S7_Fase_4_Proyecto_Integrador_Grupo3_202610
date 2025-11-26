# Sistema de Gestión Parroquial de Catequesis


## 📝 Descripción del Proyecto

Este sistema implementa una **Interfaz Web** desarrollada con **Django**
para gestionar los registros del sistema parroquial de catequesis.
Permite una interacción **directa, segura y eficiente** con una base de
datos **SQL Server** existente (Legacy), sin modificar su estructura
original.

La aplicación utiliza el **panel administrativo de Django** como
interfaz principal, proporcionando un **CRUD completo** para la entidad
`Catequizado`, con validaciones robustas integradas en el modelo.

------------------------------------------------------------------------

## ✨ Características Principales

-   **CRUD Completo:** Crear, leer, actualizar y eliminar registros de
    catequizados en SQL Server.\
-   **Validación de Integridad:** Validadores como `RegexValidator` y
    `MinValueValidator` garantizan consistencia en campos críticos
    (cédula, nombres, etc.).\
-   **Conexión Segura a SQL Server:** Configuración desacoplada mediante
    archivo externo `db_config.json`.\
-   **Mapeo Legacy:** ORM configurado por ingeniería inversa para
    adaptarse al esquema `[Proceso]`.\
-   **Admin Personalizado:** Filtros, búsquedas avanzadas y organización
    con `fieldsets`.

------------------------------------------------------------------------

## 🛠️ Tecnologías Utilizadas

-   **Lenguaje:** Python 3.x\
-   **Framework Web:** Django\
-   **Base de Datos:** Microsoft SQL Server\
-   **Conector:** `mssql-django`\
-   **Driver:** ODBC Driver 17 for SQL Server

------------------------------------------------------------------------

## 🚀 Instalación y Configuración

### 1. Instalación de Dependencias
**`pip install django mssql-django`**

------------------------------------------------------------------------

### 2. Creación del Proyecto Django
**`django-admin startproject proyecto
cd proyecto`**

------------------------------------------------------------------------

### 3. Creación de la Aplicación (Módulo)
**`python manage.py startapp app`**

------------------------------------------------------------------------

### 4. Configuración de la base de datos (Seguridad)

Cree un archivo en la raíz del proyecto llamado:\
**`db_config.json`**

Contenido ejemplo:

``` json
{
    "ENGINE": "mssql",
    "NAME": "NOMBRE_DE_SU_BD",
    "USER": "USUARIO_SQL",
    "PASSWORD": "SU_CONTRASEÑA",
    "HOST": "NOMBRE_SERVIDOR\SQLEXPRESS",
    "DRIVER": "ODBC Driver 17 for SQL Server"
}
```

💡 **Importante:** Agregar `db_config.json` al `.gitignore`.

------------------------------------------------------------------------

### 5. Inicialización del proyecto

``` bash
# Migración del sistema de autenticación de Django
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Generar modelo desde la BD Legacy
python manage.py inspectdb Catequizado | Out-File -Encoding utf8 app/models.py
```

------------------------------------------------------------------------

### 6. Ejecutar el servidor

``` bash
python manage.py runserver
```

Acceso al admin:\
http://127.0.0.1:8000/admin

------------------------------------------------------------------------

## 📚 Evidencia del Proyecto

**Video demostrativo:**\
https://youtu.be/km6OqQKJH2M

------------------------------------------------------------------------
