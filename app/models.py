from django.db import models
from django.core.validators import RegexValidator

"""
Modelo que representa la tabla Proceso.Catequizado en la base de datos SQL Server.
Actúa como la fuente única de verdad para la validación y estructura de datos.
"""


class Catequizado(models.Model):
    # --- Identificadores ---
    idcatequizado = models.PositiveIntegerField(
        db_column="idCatequizado", primary_key=True, verbose_name="ID"
    )

    # Se utiliza PositiveIntegerField para evitar IDs negativos por error
    idparroquiapertenece = models.PositiveIntegerField(
        db_column="idParroquiaPertenece", verbose_name="ID Parroquia de Origen"
    )

    # --- Datos Personales con Validaciones ---
    nombres = models.CharField(
        max_length=255,
        db_collation="Modern_Spanish_CI_AS",
        verbose_name="Nombres",
        validators=[
            # Validador para permitir solo letras (incluyendo tildes/ñ) y espacios.
            # Evita el ingreso de números o símbolos en el nombre.
            RegexValidator(
                regex=r"^[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s]+$",
                message="Los nombres solo pueden contener letras y espacios.",
            )
        ],
    )

    apellidos = models.CharField(
        max_length=255,
        db_collation="Modern_Spanish_CI_AS",
        verbose_name="Apellidos",
        validators=[
            RegexValidator(
                regex=r"^[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s]+$",
                message="Los apellidos solo pueden contener letras y espacios.",
            )
        ],
    )

    cedulaidentidad = models.CharField(
        db_column="cedulaIdentidad",
        max_length=10,
        db_collation="Modern_Spanish_CI_AS",
        verbose_name="Cédula de Identidad",
        validators=[
            # Validación estricta: Exactamente 10 dígitos numéricos.
            # ^ inicio, \d dígitos, {10} cantidad exacta, $ fin.
            RegexValidator(
                regex=r"^\d{10}$",
                message="La cédula debe tener exactamente 10 números (sin letras ni guiones).",
            )
        ],
    )

    fechanacimiento = models.DateField(
        db_column="fechaNacimiento", verbose_name="Fecha de Nacimiento"
    )

    direcciondomicilio = models.CharField(
        db_column="direccionDomicilio",
        max_length=255,
        db_collation="Modern_Spanish_CI_AS",
        verbose_name="Dirección del Domicilio",  # Corregido error ortográfico
        validators=[
            # Permite letras, números y caracteres básicos de puntuación (,.-) para direcciones.
            RegexValidator(
                regex=r"^[A-Za-z0-9ÁÉÍÓÚáéíóúÑñÜü\s,.-]+$",
                message="La dirección contiene caracteres no permitidos.",
            )
        ],
    )

    # --- Datos del Representante ---
    nombrerepresentante = models.CharField(
        db_column="nombreRepresentante",
        max_length=255,
        db_collation="Modern_Spanish_CI_AS",
        verbose_name="Nombre del Representante",
        validators=[
            RegexValidator(
                regex=r"^[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s]+$",
                message="El nombre del representante solo puede contener letras y espacios.",
            )
        ],
    )

    telefonorepresentante = models.CharField(
        db_column="telefonoRepresentante",
        max_length=255,
        db_collation="Modern_Spanish_CI_AS",
        verbose_name="Teléfono del Representante",
        validators=[
            RegexValidator(
                regex=r"^\d{10}$",  # Mismo formato estándar de 10 dígitos
                message="El teléfono debe tener exactamente 10 números (sin letras ni guiones).",
            )
        ],
    )

    emailrepresentante = models.CharField(
        db_column="emailRepresentante",
        max_length=255,
        db_collation="Modern_Spanish_CI_AS",
        verbose_name="Email del Representante",
        validators=[
            # Validación simple de formato de correo electrónico
            RegexValidator(
                regex=r"^[\w\.-]+@[\w\.-]+\.\w{2,4}$",
                message="Ingrese un correo electrónico válido.",
            )
        ],
    )

    # --- Datos Sacramentales ---
    fechabautismo = models.DateField(
        db_column="fechaBautismo", verbose_name="Fecha de Bautismo"
    )

    parroquiabautismo = models.CharField(
        db_column="parroquiaBautismo",
        max_length=255,
        db_collation="Modern_Spanish_CI_AS",
        verbose_name="Parroquia de Bautismo",
        validators=[
            RegexValidator(
                regex=r"^[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s]+$",
                message="La parroquia de bautismo solo puede contener letras y espacios.",
            )
        ],
    )

    # Configuración de metadatos para conectar con SQL Server existente
    class Meta:
        # managed = False indica a Django que NO intente crear/modificar la tabla,
        # ya que es una base de datos legacy (existente).
        managed = False
        db_table = "[Proceso].[Catequizado]"  # Apunta al esquema específico
        verbose_name = "Catequizado"
        verbose_name_plural = "Catequizados"

    # Representación en cadena para mostrar nombres reales en el Admin en lugar de "Object(1)"
    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
