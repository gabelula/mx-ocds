# Portal

- REVIEW http://www14.df.gob.mx/virtual/contratosabiertos/cdmx3/public/home2


## API


http://www.contratosabiertos.cdmx.gob.mx/api deberia dar una documentación de la api

http://www.contratosabiertos.cdmx.gob.mx/OCDS-87SD3T-SEFIN-DRM-AD-CC-008-2015.json deberia devolver un JSON valido

### Todos

Trae todos un array con los contratos.
http://www.contratosabiertos.cdmx.gob.mx/api/contratos/todos

Formato de cada contrato:

{

    "id": "6",
    "ocdsid": "OCDS-87SD3T-SEFIN-DRM-AD-006-2015",
    "ejercicio": "2015",
    "cvedependencia": "901",
    "nomdependencia": "SECRETARÍA DE FINANZAS",
    "published_date": "2015-12-02",
    "uri": "http://www.contratosabiertos.cdmx.gob.mx/OCDS-87SD3T-SEFIN-DRM-AD-006-2015.json",
    "publisher_id": "1",
    "created_at": "2016-05-05 00:24:33",
    "updated_at": "2016-05-17 17:34:50"

},

- ocdsid deberia llamarse OCID
- que es publisher_id
- que es cvedependencia ?
