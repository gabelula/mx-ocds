## LICITACIONES PUBLICAS O INVITACIONES RESTRINGIDAS

# LICITACIONES (CDMX)
  It will need information published in the pdf in the links.

    # Ejercicio
    # Trimestre que se reporta
    # Tipo de Procedimiento
    # Categoria (Obra Pública, arrendamiento, adquisición de bienes y prestación de servicios)
    # Numero de expediente
    # Hipervínculo a la Convocatoria o invitación
    # Fecha de la Convocatoria o Invitación
    # Descripcion de las obras públicas, los bienes o servicios contratados
    # Participantes (nombre, apellido paterno, apellido materno)
    # Fecha de la Junta Publicada
    # Relacion con los nombres completos tanto de los participantes o invitados como de los servidores publicos (Nombre, apellido paterno, apellido materno)
    # Cargo del servidor publico
    # Hipervinculo al documento del Dictamen y/o Fallo
    # Nombre ( o razón social) del ganador o adjudicado
    # Razones que Justifiquen su elección
    # Unidad Administrativa Solicitante
    # Unidad Administrativa Resposable de la ejecucion
    # Numero del Contrato (Hipervínculo al documento del contrato)
    # Fecha del Contrato
    # Monto del Contrato con impuestos incluídos
    # Objeto del Contrato
    # Plazo de Entrega o Ejecucion de los Servicios Contratados u obra pública a realizar (Fecha de Inicio, FEcha de Termino)
    # Número del Convenio Modificatorio (Hipervínculo al convenio modificatorio)
    # Objeto del Convenio Modificatorio
    # Fecha de Firma del Convenio Modificatorio
    # Mecanismos de Vigilancia y Supervisión de la ejecución de cada uno de los contratos y/o convenios
    # Hipervínculo a los informes de avance de los servicios contratados

# INVITACIONES RESTRINGIDAS (CDMX)


# Tenders (OCDS)

    # Id
    # Title
    # Description
    # Status (planned, active, cancelled, unsuccesful or complete)
    # Items
    # minValue
    # value
    # procurementMethod
    # procurementMethodRationale
    # awardCriteria
    # awardCriteriaDetails
    # submissionMethod
    # submissionMethodDetails
    # tenderPeriod (startDate, endDate)
    # enquiryPeriod (startDate, endDate)
    # hasEnquiries
    # eligibilityCriteria
    # awardPeriod (startDate, endDate)
    # numberOfTenderers
    # tenderers
    # procuringEntity
    # documents
    # milestones
    # amendment

[Reference]: http://ocds.open-contracting.org/standard/r/1__0__RC/en/schema/reference/#tender


# Process #

1.  Remove unused rows and columns for CDMX's CSV (manually)
.
.
.
4. Map it

* Id            --> Número de expediente
* Title         --> Descripcion de las obras públicas, los bienes o servicios contratados
* Description   --> Descripcion de las obras públicas, los bienes o servicios contratados
* Status (planned, active, cancelled, unsuccesful or complete) -->  Calculate based on date...
* Items         --> (info from 'Hipervinculo a la Convocatoria o Invitacion')
* minValue      --> (info from 'Hipervinculo a la Convocatoria o Invitacion')
* value         --> (info from 'Hipervinculo a la Convocatoria o Invitacion')
* procurementMethod -> Tipo de Procedimiento
* procurementMethodRationale -> Razones que Justifiquen su elección
* awardCriteria        -> Hipervinculo al documento del Dictamen y/o Fallo
* awardCriteriaDetails -> Hipervinculo al documento del Dictamen y/o Fallo
* submissionMethod
* submissionMethodDetails
* tenderPeriod (startDate, endDate)
                        -> (Fecha de la Convocatoria o Invitacion)
* enquiryPeriod (startDate, endDate)
                        ->
* hasEnquiries
* eligibilityCriteria
* awardPeriod (startDate, endDate)
                        -> Fecha de la Junta Publica
* numberOfTenderers
* tenderers             -> Relacion con los nombres completos de los participantes o invitados (Organization template)
* procuringEntity
                        -> Relacion con los nombres completos tanto de los participantes o invitados como de los servidores publicos OR CEJUR (organization)
* documents (id, documentType, title, description, url, datePublished, dateModified, format, language)
                        -> Hipervínculo a la Convocatoria o invitación
                        -> Hipervinculo al documento del Dictamen y/o Fallo
* milestones
* amendment
