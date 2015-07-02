"tender": {
    "id": "Numero de Expediente",
    "title": ,
    "description": "Descripcion de las obras públicas, los bienes o servicios contratados",
    "status": "tender.status",
    "items": [
        {
            "id": "constant:1",
            "description": "title",
            "classification": {
                "scheme": "constant:GSIN",
                "description": "gsin"
            }
        }
    ],
   "minValue",
   "value",
   "procurementMethod": "Tipo de Procedimiento",
   "procurementMethodRationale",
   "awardCriteria",
   "awardCriteriaDetails": "competitive_procurement_strategy",
   "submissionMethod",
   "submissionMethodDetails",
   "tenderPeriod": {
     "startDate": "Fecha de la Convocatoria o Invitacion",
     "endDate": "Fecha de la Convocatoria o Invitacion"
   },
   "enquiryPeriod",
   "hasEnquiries",
   "eligibilityCriteria",
   "awardPeriod": "Ejecucion de los Servicios Contratados u obra publica a realizar – Fecha de Inicio to Ejecucion de los Servicios Contratados u obra publica a realizar – Fecha de Término",
   "numberOfTenderers": "Calculated field based on tenderers",
   "tenderers" : ["Relacion con los nombres completos de los participantes o invitados"],
   "procuringEntity": {
       "name": "Unidad Administrativa Resposable de la ejecucion"
   },
  "documents": [
        {
            "id": "1",
            "url": "Hipervínculo a la Convocatoria o invitación"
        },
        {
            "id": "2",
            "url": "Hipervínculo a los informes de avance de los servicios contratados "
        },
        {
          "id": "3",
          "url": "Numero del Contrato"
        },
        {
          "id": "4",
          "url": "Número del Convenio Modificatorio "
        }
    ],
   "milestones",
   "amendment"
}

# TENDERS (LICITACIONES)

## Ejercicio (not neded)

  The year that the tender starts at.

## Trimestre que se reporta (not needed)

  Months that the tender happens.

## Tipo de Procedimiento (procurementMethod):

  At OCDS we have the options [Open, Selective, Limited]
  At CDMX's data the options are [LICITACIÓN PÚBLICA NACIONAL, INVITACION RESTRINGIDA INTERNACIONAL A CUANDO MENOS TRES PROVEEDORES]

## Categoria (not needed)

  The options are Obra Pública, arrendamiento, adquisición de bienes y prestación de servicios.

## Numero de expediente (Id)

## Hipervínculo a la Convocatoria o invitación (Document)

## Fecha de la Convocatoria o Invitación (tenderPeriod)

  This field has all the dates that the tender is for submissions.

## Descripcion de las obras públicas, los bienes o servicios contratados (Description)

## Relacion con los nombres completos de los participantes o invitados (tenderers)

  This are organizations. We only have their unique name here.

## Fecha de la Junta Publicada (not sure where)

## Relacion con los nombres completos tanto de los participantes o invitados como de los servidores publicos (Not needed)

  These are the public officers

## Cargo del servidor publico (Not Needed)

## Hipervinculo al documento del Dictamen y/o Fallo (Documents)

## Nombre ( o razón social) del ganador o adjudicado <--- THIS GOES INTO THE RELEASE/AWARD
## Razones que Justifiquen su elección <--- THIS GOES INTO THE RELEASE/AWARD

## Unidad Administrativa Solicitante <--- THIS GOES INTO THE RELEASE AS BUYER

## Unidad Administrativa Responsable de la ejecucion (procuringEntity)

  This is an organization by the name 'Unidad Administrativa Responsable de la ejecucion'

## Numero del Contrato (Documents)

## Fecha del Contrato <--- THIS GOES INTO THE RELASE / AWARD / DATE

## Monto del Contrato con impuestos incluídos <--- THIS GOES INTO THE RELASE / AWARD / VALUE

## Objeto del Contrato <--- THIS GOES INTO THE RELASE / AWARD / TITLE

## Plazo de Entrega o Ejecucion de los Servicios Contratados u obra pública a realizar (awardPeriod)

## Número del Convenio Modificatorio (Documents)

## Objeto del Convenio Modificatorio (NotSureYet)
## Fecha de Firma del Convenio Modificatorio (NotSureYet)
## Mecanismos de Vigilancia y Supervisión de la ejecución de cada uno de los contratos y/o convenios

## Hipervínculo a los informes de avance de los servicios contratados (Document)





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
