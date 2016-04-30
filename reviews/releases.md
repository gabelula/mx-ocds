# Revision  JSON Abril, 29, 2016

## Validator

Link: http://standard.open-contracting.org/validator/


## Wrong Encoding

*Error message: 'utf-8' codec can't decode byte 0xd3 in position 894: invalid continuation byte*

For example in:

  - "locality": "M�XICO D. F.",
  - "name": "SECRETAR�A DE FINANZAS",

## URI

*'No Capturado' is not a 'uri'*

    - releases/0/tender/tenderers/0/contactPoint/url
    - releases/0/tender/tenderers/2/contactPoint/url
    - releases/0/awards/0/suppliers/0/contactPoint/url

*'WWW.FINANZAS.DF.GOB.MX' is not a 'uri'*

    - releases/0/tender/procuringEntity/contactPoint/url
    - releases/0/buyer/contactPoint/url

*'WWW.MAKSEGURIDAD.COM' is not a 'uri'*

    - releases/0/tender/tenderers/1/contactPoint/url
