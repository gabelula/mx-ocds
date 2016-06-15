## Validation

Data pass validation succesful.

## Validation & Implementation Issues to be addressed before launch:

* Check that pre-go live releases pass validation. Pay special attention to all URIs and URLs, especially Buyer and Supplier ContactPoint URIs. DONE

* Ensure that the API is publicly available with clear documentation on how to use it. Minor. NOT DONE
* Confirm and document the publication pattern i.e. there will only be a single release produced for each contracting process (ocid).Minor. NOT DONE
* Verify the publication pattern holds for the URIs generated for each release.Minor. NOT DONE

## Basic level completed.

### Recommendations

* procurement details missing. I still did not see the glossary.
* amount of items DO match between stages. DONE
* Correct the supplier details or publish empty fields instead of the placeholders. DONE
* Ensure all contracts have a status. DONE
* Ensure all documents have a document type. NOT DONE

## Intermediate level not completed

### Fixes Required or Recommended to reach Intermediate Level

#### buyer & supplier blocks
  * 8 contracts have "releases.tender.eligibilityCriteria":"" . NEW ISSUE
  * Provide buyer and supplier scheme. NOT DONE
  * Ensure all buyers have a name and a legal name. DONE
  * Ensure all suppliers have a name and a legal name. (37% of the analized releases do not have supplier's name) NOT DONE
  * Ensure all contracts have a rationale

#### planning
  * Ensure all contracts have a rationale.Required Minor. NOT DONE
  * Ensure all contracts have a budget description.Required Minor. NOT DONE.
  * Provide a budget id where available.Recommended Minor. NOT DONE
  * Provide a budget source where available. Recommended Moderate. NOT DONE
  * Provide a budget URI where available. Recommended Moderate. NOT DONE

#### tender block

  * Ensure all contracts have a minimum value, this includes the amount and currency. Required Minor. NOT DONE
  * Source and update the enquiry periods, this includes the start and end dates Required Moderate. NOT DONE. <--- THEY ARE ALL DIRECT AWARDS
  * Provide classification for tender items Required Moderate. NOT DONE.
  * Decide on an Item Classification Scheme - internal or external from the codelist. NOT DONE
  * Provide Award Criteria Details where available Recommended Moderate
  * Provide Submission Method Details where available Recommended Moderate. NOT DONE.
  * Provide the Classification URI if available Recommended Moderate. NOT DONE.
  * Provider Tenderer’s scheme where available Recommended Moderate. NOT DONE.
  * Provide a legal name for tenderers where available Recommended Minor. DONE

#### award block:
  * Provide the Award Items Classification URI if available Recommended Moderate. NOT DONE

#### contract block:
  * Provide classification for contract items Required Moderate NOT DONE
  * Decide on an Item Classification Scheme - internal or external from the codelist NOT DONE

#### documents

  * missing documents as CDMX is still working on them. TO DO

#### implementation

  * also missing documents  

## Advance level

I'm looking at what we have from advance level

### Tender
  * Items's unit (name)
    * missing value
  * Tenderers's identifier (id, uri, name)
    * missing scheme
  * Missing milestones

### Award
  * Item's unit (name)
    * missing value

### Contract
  * Item's unit (name)
    * missing value
  * Implementation!!! We have transactions!
    * missing status
