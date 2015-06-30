
## PROVEEDORES


# Proveedores (CDMX)
 	  # Ejercicio
    # Nombre de la persona física/ Razón social X (Nombre(s)	Apellido paterno	Apellido materno)
    # Giro (principales tres actividades)
    # Nombre del representante de la empresa (Nombre(s)	Apellido paterno	Apellido materno)
    # Domicilio fiscal (Calle	Número exterior	Número interior	Colonia	Delegación	Código postal)
    # Dirección electrónica de la página web
    # Teléfono oficial
    # Correo electrónico

# Organization (OCDS)
    # Identifier (scheme, id, legalName, url)
    # AdditionalIdentifier
    # Name
    # Address (streetAddress, locality, region, postalCode, countryName)
    # ContactPoint (name, email, telephone, faxNumber, url)

# Process #

 1. Remove unused rows and columns for CDMX's CSV (manually)
 2. Merge all the files from different years
    csvstack FilesToStack > proveedores.csv
 3. Replace 'X' for blank cells
 4. Merge
		 - Nombre de la persona fisica/Razon Social = Nombre + Apellido paterno + Apellido materno (=SI(ESBLANCO(E50);D50;CONCATENAR(D50;" ";E50;" ";F50)))
     - Direccion = Calle 'no.' Numero exterior ',' Numero interior
     - Nombre del representante = Nombre + Apellido paterno + Apellido materno ()
    CHECK CSVKIT
 5. Apply formats
			* phone
			* email
 6. Mapp it
		* Identifier (scheme, id, legalName, url) -> Nombre de la persona fisica
    * AdditionalIdentifier
    * Name                                    ->  Nombre de la persona física
    * Address (streetAddress, locality, region, postalCode, countryName)
    *       . streetAddress -> Direccion (Calle 'no.' Numero exterior ',' Numero interior)
    *       . locality      -> Colonia
    *       . region        -> Delegación
    *       . postalCode    -> Código postal
    *       . countryName   -> Mexico
    * ContactPoint (name, email, telephone, faxNumber, url)
    *       . name          -> Nombre del Representante (Nombre + Apellido paterno + Apellido materno)
    *       . email         -> Correo electrónico
    *       . telephone     -> Teléfono oficial
    *       . faxNumber
    *       . url           -> Dirección electrónica de la página web
 7. Clean duplicates by Name
    * When different addresses, keep the one from the last year
    * Remove Ejecucion
