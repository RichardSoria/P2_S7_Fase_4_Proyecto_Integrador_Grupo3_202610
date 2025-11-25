from django.contrib import admin
from .models import Catequizado

"""
Configuración del Panel Administrativo para el modelo Catequizado.
Permite gestionar la visualización, búsqueda y filtrado de los estudiantes
directamente desde la interfaz de Django.
"""

@admin.register(Catequizado)
class CatequizadoAdmin(admin.ModelAdmin):
    # --- Visualización en la Lista Principal ---
    # Define qué columnas se muestran en la tabla de registros.
    # Se han seleccionado los datos más relevantes para una vista rápida.
    list_display = (
        "idcatequizado",
        "nombres",
        "apellidos",
        "cedulaidentidad",
        "nombrerepresentante",
        "telefonorepresentante",
    )

    # --- Configuración de Búsqueda ---
    # Permite buscar por ID, nombres, apellidos o cédula.
    # Django genera automáticamente consultas SQL con LIKE.
    search_fields = ("idcatequizado", "nombres", "apellidos", "cedulaidentidad")

    # --- Filtros Laterales ---
    # Agrega una barra lateral para filtrar rápidamente los datos.
    # Útil para encontrar estudiantes parroquia de origen.
    list_filter = (
        "parroquiabautismo",
    )

    # --- Ordenamiento ---
    # Ordena la lista por ID descendente (los registros más nuevos primero).
    ordering = ("-idcatequizado",)

    # --- Paginación ---
    # Limita el número de registros por página para no saturar la vista.
    list_per_page = 20

    # --- Organización del Formulario de Edición (Fieldsets) ---
    # Divide el formulario en secciones lógicas para mejorar la experiencia de usuario (UX).
    fieldsets = (
        (
            "Identificación del Sistema",
            {"fields": ("idcatequizado", "idparroquiapertenece")},
        ),
        (
            "Información Personal",
            {
                "fields": (
                    "nombres",
                    "apellidos",
                    "cedulaidentidad",
                    "fechanacimiento",
                    "direcciondomicilio",
                ),
                "classes": ("wide",),  # Ocupa todo el ancho disponible
            },
        ),
        (
            "Información del Representante",
            {
                "fields": (
                    "nombrerepresentante",
                    "telefonorepresentante",
                    "emailrepresentante",
                ),
                "description": "Datos de contacto del padre, madre o tutor legal.",
            },
        ),
        (
            "Datos Sacramentales",
            {
                "fields": ("fechabautismo", "parroquiabautismo"),
                "classes": (
                    "collapse",
                ),  # Permite ocultar/colapsar esta sección si no se usa mucho
            },
        ),
    )