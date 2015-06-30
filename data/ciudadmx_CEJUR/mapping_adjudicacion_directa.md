## ADJUDICACION DIRECTA

# ADJUDICACIONES (CDMX)

    # Ejercicio
    #	Tipo de procedimiento
    # Categoría (Obra Pública, arrendamiento, adquisición de bienes y prestación de servicios)
    # Número de Expediente
    # Motivos y fundamentos legales aplicados
    # Descripción de los bienes o servicios contratados
    # Cotizaciones consideradas
      - Nombre de los proveedores
           - Nombre(s)	Apellido paterno	Apellido materno
      	   - Monto de las cotizaciones con impuestos incluidos
    # Nombre (o razón social) de la persona adjudicada
           - Nombre(s)	Apellido paterno	Apellido materno
    # Unidad administrativa solicitante
    # Unidad administrativa responsable de la ejecución
    # Número del contrato (hipervínculo al documento del contrato)
    # Fecha del contrato
    # Monto del contrato con impuestos incluidos
    # Objeto del contrato
    # Plazo de entrega o de ejecución de los servicios u obra contratados
           - Fecha de inicio
           - Fecha de término
    # Números de convenios modificatorios (Hipervínculo al documento del convenio modificatorio)
    # Objeto del convenio
    # Fecha de firma del convenio
    # Mecanismos de vigilancia y supervisión
    # Hipervínculo al documento de estudios de impacto urbano y ambiental
    # Hipervínculo a los informes de avance sobre las obras o servicios contratados
    # En obra pública por invitación restringida deberá publicar además:
    	      - Lugar de la obra pública
            - Estudios de impacto urbano y ambiental
            - Hipervínculo a los Informes de avance de las obras públicas


# Awards (OCDS)

    # Id
    # Title
    # Description
    # Status (pending, active, cancelled, unsuccesful)
    # date
    # value
    # suppliers
    # Items
    # documents
    # amendment

[Reference]: http://ocds.open-contracting.org/standard/r/1__0__RC/en/schema/reference/#tender


# Process #

1.  Remove unused rows and columns for CDMX's CSV (manually)
.
.
.
4. Map it
  # Id            --> Número de expediente
  # Title         --> Descripción de los bienes o servicios contratados
  # Description   --> Descripción de los bienes o servicios contratados
  # Status (pending, active, cancelled, unsuccesful)
  # Date          --> Fecha del contrato
  # Value (amount, currency)
                  --> Monto del contrato con impuestos incluidos
  # Suppliers (organization)
                  --> Nombre de los proveedores (link to proveedores's list)
  # Items
  # documents
                  --> Número del contrato (hipervínculo al documento del contrato)
  # amendment
