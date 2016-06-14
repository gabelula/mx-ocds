## Validation

Data pass validation succesful.

## Basic level completed.

### Recommendations

* procurement details missing. I still did not see the glossary.
* amount of items not matching between stages

OCDS-87SD3T-AD-SF-DRM-066-2015  ITEMS IN Tender:  2  Awards:  2  Contract:  1
OCDS-87SD3T-SEFIN-AD-SF-DRM-002-2015  ITEMS IN Tender:  5  Awards:  5  Contract:  1
OCDS-87SD3T-SEFIN-DRM-A-014-2015  ITEMS IN Tender:  3  Awards:  3  Contract:  1
OCDS-87SD3T-SEFIN-DRM-A-015-2015  ITEMS IN Tender:  3  Awards:  3  Contract:  1
OCDS-87SD3T-SEFIN-DRM-AD-003-2016-2  ITEMS IN Tender:  5  Awards:  5  Contract:  1
OCDS-87SD3T-SEFIN-DRM-AD-003-2016  ITEMS IN Tender:  2  Awards:  2  Contract:  1
OCDS-87SD3T-SEFIN-DRM-AD-006-2016-2  ITEMS IN Tender:  2  Awards:  2  Contract:  1
OCDS-87SD3T-SEFIN-DRM-AD-009-2016  ITEMS IN Tender:  2  Awards:  2  Contract:  1
OCDS-87SD3T-SEFIN-DRM-AD-073-2016  ITEMS IN Tender:  2  Awards:  2  Contract:  1
OCDS-87SD3T-SEFIN-DRM-AD-074-2016  ITEMS IN Tender:  2  Awards:  2  Contract:  1
OCDS-87SD3T-SEFIN-DRM-AD-CC-002-2016  ITEMS IN Tender:  4  Awards:  4  Contract:  1
OCDS-87SD3T-SEFIN-DRM-AD-CC-003-2016  ITEMS IN Tender:  2  Awards:  2  Contract:  1
OCDS-87SD3T-SEFIN-DRM-AD-CC-008-2015  ITEMS IN Tender:  3  Awards:  3  Contract:  1
OCDS-87SD3T-SEFIN-DRM-AD-CC-009-2015  ITEMS IN Tender:  7  Awards:  7  Contract:  1
OCDS-87SD3T-SEFIN-DRM-LPN-007-2015  ITEMS IN Tender:  3  Awards:  3  Contract:  1

* Correct the supplier details or publish empty fields instead of the placeholders. DONE
* Ensure all contracts have a status. DONE
* Ensure all documents have a document type. NOT DONE

## Intermediate level not completed

### Fixes Required or Recommended to reach Intermediate Level

  * 8 contracts have "releases.tender.eligibilityCriteria":"" . NEW ISSUE

## Validation & Implementation Issues to be addressed before launch:

* Check that pre-go live releases pass validation. Pay special attention to all URIs and URLs, especially Buyer and Supplier ContactPoint URIs. DONE

* Ensure that the API is publicly available with clear documentation on how to use it. Minor. NOT DONE
* Confirm and document the publication pattern i.e. there will only be a single release produced for each contracting process (ocid).Minor. NOT DONE
* Verify the publication pattern holds for the URIs generated for each release.Minor. NOT DONE
