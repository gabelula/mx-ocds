# REVIEWS

# Validation

Using http://standard.open-contracting.org/validator/
Schema: http://standard.open-contracting.org/schema/1__0__0/release-package-schema.json
Version: 1.0.1


## URI not well formed. URI should be a String or not be presented if NULL.

For example, for OCID 'OCDS-87SD3T-SEFIN-AD-SF-DRM-002-2015':

WWW.MAKSEGURIDAD.COM' is not a 'uri' 	 	
    releases/0/tender/tenderers/1/contactPoint/url

'No Capturado' is not a 'uri' 	
    releases/0/awards/0/suppliers/0/contactPoint/url
    releases/0/tender/tenderers/0/contactPoint/url
    releases/0/tender/tenderers/2/contactPoint/url

'WWW.FINANZAS.DF.GOB.MX' is not a 'uri' 	
    releases/0/buyer/contactPoint/url


## Items with an empty array

* in awards: OCDS-87SD3T-SEFIN-AD-SF-DRM-005-2015
* in awards: OCDS-87SD3T-SEFIN-DRM-AD-012-2015
* in awards: OCDS-87SD3T-SEFIN-DRM-A-014-2015
* in contracts: OCDS-87SD3T-SEFIN-DRM-LPN-016-2015

## Validations http://standard.open-contracting.org/validator/data/842a65a3-bd41-4962-a2df-de989a445757

# Notes

- Extension on multi-year
- Each time they publish data they are publishing only one release
However, there is a potential issue with the release.id, which appears to always be '1'. It would be useful to prefix the full OCID onto this, so that if someone did want to bundle together multiple releases in future, they would not need to change the release IDs in order to make sure all release IDs in the package are unique (see http://standard.open-contracting.org/latest/en/schema/identifiers/#local-identifiers)

- Tag on releases
  - 73% contract
  - 20% award
  - 7% tender

- Exchange Rate: CDMX need it in award, contract and implementation phases. https://github.com/open-contracting/standard/issues/277

# Phases

## Planning

None of the releases are only planning's ones.

### budget
  Only fields filled are project (description) and amount (in MX).

### rationale
  None of the planning phases have a 'rationale' field.
### documents
  From 15 releases, only 4 have a document each. All of the documents are 'Autorización Presupuestal'. For example: http://www.innovacion.finanzas.df.gob.mx/ocpsefin/interfase2/grp/ocds/archivos/autorizacion_405_20160505_135705.pdf

## Buyer
  It is always "Secretaria de Finanzas"

## Tender

AwardCriteria:

- 93% bestValueToGovernment
- 7% bestProposal

EligibilityCriteria:

- 67% "Servicio, Condiciones, Precio, Otro & Anexo Tecnico"
- 22% "Servicio, Condiciones, Precio"
- 11% "Servicio, Precio"

Has Enquiries?

- 80% yes
- 20% no

Enquiry period

- 80% of the releases do not have startDate and endDate

Number of tenderers

- 33% - 1
- 27% - 2
- 33% - 3

Are they only adding the tenderers that are already in their system (that have won an award before).

procurement method

- 73% limited
- 20% selective
- 7% open

status
- 93% complete
- 7% active

For the active one, check if they added a contract phase or not.

submission method is always 'written'

documents
  - 38% "Estudio de Precio de Mercado"
  - 62% "Requisición"

items units
  - 58% SER
  - 42% PZA

procuring entity
  it is always 'secretaria de finanzas'

tenderers
  identifier.URI is not going to a list of providers
  publish the list of providers or remove identifier?

## Awards
## Contracts
