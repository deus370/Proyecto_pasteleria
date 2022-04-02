/* Registros Proveedores*/
INSERT INTO Proveedor(nombre, calle, cp, colonia) VALUES ("San Juan", "Km. 2 Carretera", 47093, "San Juan de los Lagos");
INSERT INTO Proveedor(nombre, calle, numero, cp, colonia) VALUES ("DICSA", "Calle 8",  117, 94500, "Córdoba");
INSERT INTO Proveedor(nombre, calle, numero, cp, colonia) VALUES ("La Fina", "Av. Insurgentes Sur",  116, 03100, "Del Valle");
INSERT INTO Proveedor(nombre, calle, numero, cp, colonia) VALUES ("Fábrica de Harinas Elizondo", "Ferrocarril de Cuernavaca ",  887, 11500, "Irrigación");
INSERT INTO Proveedor(nombre, calle, numero, cp, colonia) VALUES ("CALLE GOLFO DE MEXICO", "CALLE GOLFO DE MEXICO",  604, 66477, "San Nicolas de los Garza");
INSERT INTO Proveedor(nombre, calle, numero, cp, colonia) VALUES ("MEXICANA SA DE CV", "San martin",  116, 37400, "Satelite");

/* Resgistros Ingredientes*/
INSERT INTO Ingrediente(nombre, cantidad, unidad, estatus, proveedor) VALUES ("Huevo", 50, "pz", 1);
INSERT INTO Ingrediente(nombre, cantidad, unidad, estatus, proveedor) VALUES ("Azucar", 50, "gr", 2);
INSERT INTO Ingrediente(nombre, cantidad, unidad, estatus, proveedor) VALUES ("Sal", 50, "gr", 3);
INSERT INTO Ingrediente(nombre, cantidad, unidad, estatus, proveedor) VALUES ("Harina", 50, "gr", 4);
INSERT INTO Ingrediente(nombre, cantidad, unidad, estatus, proveedor) VALUES ("Mantequilla", 50, "gr", 5);
INSERT INTO Ingrediente(nombre, cantidad, unidad, estatus, proveedor) VALUES ("Polvo para Hornear", 50, "gr", 2);
INSERT INTO Ingrediente(nombre, cantidad, unidad, estatus, proveedor) VALUES ("Vainilla", 50, "gr", 6);
INSERT INTO Ingrediente(nombre, cantidad, unidad, estatus, proveedor) VALUES ("Leche", 50, "gr", 6);
INSERT INTO Ingrediente(nombre, cantidad, unidad, estatus, proveedor) VALUES ("Nuez", 50, "", 1);
INSERT INTO Ingrediente(nombre, cantidad, unidad, estatus, proveedor) VALUES ("Chocolate", 50, "", 1);
INSERT INTO Ingrediente(nombre, cantidad, unidad, estatus, proveedor) VALUES ("Fresa", 50, "", 2);

/* Recetas*/
 insert into Receta(nombre, cantidad, ingrediente) values ("panque fresa", 20, 9);



/* Producto*/


/* Persona*/
INSERT INTO Persona(nombre, a_paterno, a_materno, telefono, correo, calle, numero, cp, colonia) VALUES("Hector", "Ramirez", "Lopez", "4773549863", "hector@gmail.com", "San Martin", 116, 37408, "San martin");
INSERT INTO Persona(nombre, a_paterno, a_materno, telefono, correo, calle, numero, cp, colonia) VALUES("Alan", "Martinez", "Romero", "4776547690", "alan@gmail.com", "Jicama", 132, 367400, "Las Mandarinas");
INSERT INTO Persona(nombre, a_paterno, a_materno, telefono, correo, calle, numero, cp, colonia) VALUES("Jona", "Torres", "Piñon", "4771659279", "jona@gmail.com", "Blvdv. Aeropuerto", 243, 67800, "Blvd. Aeropuerto");


/* Rol*/
INSERT INTO Rol(nombre) VALUES ("admin");
INSERT INTO Rol(nombre) VALUES ("cliente");
INSERT INTO Rol(nombre) VALUES ("empleado");

/* Usuario*/
INSERT INTO Usuario(usuario, contrasena, persona, rol) VALUES("hector370", "12345", 1, 1);
INSERT INTO Usuario(usuario, contrasena, persona, rol) VALUES("alan270", "12345", 2, 2);
INSERT INTO Usuario(usuario, contrasena, persona, rol) VALUES("hachiko", "12345", 3, 3);