# Extensions

Extensions are not an official part of the standard, and will only be considered to become so as part of the upgrade process to 1.1, which will take place over Q2/Q3 this year.

### Process for developing official extensions of OCDS is to

  - Post, or add to, an issue in the [issue tracker](https://github.com/open-contracting/standard/issues) describing the extension required
  - Engage in the discussion there on a proposed extension - and share examples of data using a proposed extension

## Multi-year Contract

[Issue #293](https://github.com/open-contracting/standard/issues/293)

  - Propose extension
  - Sample of data
  - Justification
  - Create the [JSON Schema Patch and Readme file](http://standard.open-contracting.org/latest/en/extensions/developing/) required


##### Problem to resolve

Some contracts that are multi-year. The same contract is used for different years (with a maximum of 4 years). We know if the contract is multi-year in the budget part.
We need to model:
  - is the contract multi-year
  - how many years is the contract for
  - how much budget per year is saved for the contract
  - what is the maximum value of the contract for all the years
  - there is no new contract every year

##### Propose Extension

- Contract.period should have startDate and endDate for the whole period
- An optional "multiYear":true field could be added to the period block (see below).
- Contract.value : a field to show what is the max value for all the years
- "If there is then a desire to show the break-down of amounts for each year, I would suggest considering whether this could be done with line-items. E.g., having a line-item for 2015, one for 2016 and so-on, each with the specific values for that year."


###### Planning

```
"planning": {
                "budget": {
                    "multiYear": true
                    "amount": {
                        "amount": 7054250.52,
                        "currency": "MXN"
                    },
                    "amountYear": {
                      "amount": 1000,
                      "currency": "MXN"
                    }
                    "project": "AUTORIZACION PRESUPUESTAL SPP/471/2015"
                }
            }
```

- multiyear flag : we need a way to know if this is a multi-year budget
- amount is for the total (as in the OCDS)
- we do not add period because it is going to be in the contract.period
- amount per year for each year : estimated budget for each year (it depends a lot on the dollar/mxn rate)

###### Contract

```
       "contracts": [
                {
                    "id": "1",
                    "awardID": "1",
                    "title": "CS-MA-009/2015",
                    "description": "SOLUCIÓN DE AUTENTICACIÓN BIOMÉTRICA POR VOZ",
                    "status": "active",
                    "multiYear": true
                    "period": {
                        "startDate": "2015-11-27T00:00:00-06:00",  
                        "endDate": "2019-12-31T00:00:00-06:00"
                    },
                    "value": {
                         "amount": 1209300.00,  //  total value for the contract for all the years
                         "currency": "USD"
                    },
                    "valueYear": {
                        "amount": 403100.03,  // this is only for 2015
                        "currency": "USD"
                    },   
                    "items": [
                        {
                            "id": "1",
                            "description": "SOLUCION AUTENTIC BIOMETRICA X VOZ 2015",
                            "quantity": 347500,
                            "unit": {
                                "name": "SER"
                            }
                        }
                    ],
                    "dateSigned": "2015-11-27T00:00:00-06:00",
                    "documents": []
                }
       ]
```

- multiyear : this is a multi-year contract
- period : period startDate and endDate for the whole time of the contract
- valueYear : value per year spend on this contract

##### Sample of data


##### Justification

## Compare Federal vs CDMX
