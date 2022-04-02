DROP DATABASE IF EXISTS Pasteleria;
CREATE DATABASE pasteleria;
USE pasteleria;

CREATE TABLE Proveedor(
id_proveedor INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(100),
calle VARCHAR(100),
numero INT,
cp INT,
colonia VARCHAR(100),
estatus INT DEFAULT 1
);

CREATE TABLE Ingrediente(
id_ingrediente INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(100),
cantidad DOUBLE,
unidad VARCHAR(100),
estatus INT DEFAULT 1,
proveedor INT NOT NULL,
CONSTRAINT proveedor_ingredienteFK FOREIGN KEY (proveedor) REFERENCES Proveedor (id_proveedor)
);

CREATE TABLE Receta(
id_receta INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(100),
cantidad DOUBLE,
estatus INT DEFAULT 1,
ingrediente INT NOT NULL,
CONSTRAINT ingrediente_recetaFK FOREIGN KEY (ingrediente) REFERENCES Ingrediente (id_ingrediente)
);

CREATE TABLE Producto(
id_producto INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(100),
cantidad INT,
descripccion VARCHAR(100),
precio DOUBLE,
imagen LONGTEXT,
estatus INT DEFAULT 1,
receta INT NOT NULL,
CONSTRAINT producto_recetaFK FOREIGN KEY (receta) REFERENCES Receta (id_receta)
);

CREATE TABLE Persona(
id_persona INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(100),
a_paterno VARCHAR(100),
a_materno VARCHAR(100),
telefono VARCHAR(100),
correo VARCHAR(100),
calle VARCHAR(100),
numero INT,
cp INT,
colonia VARCHAR(100)
);

CREATE TABLE Rol(
id_rol INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(100)
);

CREATE TABLE Usuario(
id_usuario INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
usuario VARCHAR(100),
contrasena VARCHAR(250),
persona INT NOT NULL,
estatus INT DEFAULT 1,
ACTIVE TINYINT(1) DEFAULT NULL,
rol INT NOT NULL,
CONSTRAINT usuario_personaFK FOREIGN KEY (persona) REFERENCES Persona (id_persona),
CONSTRAINT usuario_rolFK FOREIGN KEY (rol) REFERENCES Rol (id_rol)
);

CREATE TABLE Ventas(
id_compra INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
fecha_compra DATE,
Total DOUBLE,
cantidad INT,
estatus INT DEFAULT 1,
usuario INT NOT NULL,
producto INT NOT NULL,
CONSTRAINT compra_usuarioFK FOREIGN KEY (usuario) REFERENCES Usuario (id_usuario),
CONSTRAINT compra_productoFK FOREIGN KEY (producto) REFERENCES Producto (id_producto)
);

CREATE TABLE Proveedor_Ingrediente(
id_pedido INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
fecha_ingreso DATE,
costo DOUBLE,
total DOUBLE,
cantidad DOUBLE,
estatus INT DEFAULT 1,
proveedor INT NOT NULL,
ingrediente INT NOT NULL,
CONSTRAINT proveedor_ingredenteiFK FOREIGN KEY (proveedor) REFERENCES Proveedor (id_proveedor),
CONSTRAINT provedor_ingrdienteinFK FOREIGN KEY (ingrediente) REFERENCES Ingrediente (id_ingrediente)
);

drop trigger if exists cancelar_tb_proveedor_ingrediente;
delimiter $$
create trigger cancelar_tb_pedido
before update on proveedor_ingrediente
for each row
begin
	update ingrediente i set i.cantidad = i.cantidad - new.cantidad where i.id_ingrediente = new.ingrediente;
end $$
Delimiter;

#Trigger para actualizar el costo total
drop trigger if exists actualizar_tb_proveedor_ingrediente;
delimiter $$
create trigger actualizar_tb_proveedor_ingrediente
before insert on proveedor_ingrediente
for each row
begin
	set new.total=(new.costo*new.cantidad);
    set new.fecha_ingreso = CURDATE();
    update ingrediente i set i.cantidad = i.cantidad + new.cantidad where i.id_ingrediente = new.ingrediente;
end $$
Delimiter;

Delimiter $$
drop trigger if exists hornear_tb_producto;
create trigger hornear_tb_producto
before update on producto
for each row
begin
	Declare CantidadProducida double;
    declare idAux int;
    select (new.cantidad-old.cantidad) into CantidadProducida;
    if CantidadProducida=6 then
		select 1 into cantidadProducida;
    else
		select 2 into cantidadProducida;
    end if;    
	#Bajar el stock de huevo 62.5 gr = huevo. 1 huevo por media docena
	update ingrediente set cantidad = cantidad-(1*CantidadProducida) where nombre = 'Huevo' and estatus<>0;
    #Bajar el stock de la azucar 70gr de azucar por media docena
    update ingrediente set cantidad = cantidad-(0.070*CantidadProducida) where nombre = 'Azucar' and estatus<>0;
    #Bajar stock de sal 1.4gr por media docena
    update ingrediente set cantidad = cantidad-(0.0014*CantidadProducida) where nombre = 'Sal' and estatus<>0;
    #bajar stock de harina 60gr de harina por media docena
    update ingrediente set cantidad = cantidad-(0.060*CantidadProducida) where nombre = 'Harina' and estatus<>0;
    #bajar stock de Mantequilla 60gr de mantequilla por media docena
    update ingrediente set cantidad = cantidad-(0.060*CantidadProducida) where nombre = 'Mantequilla' and estatus<>0;
    #bajar stock de polvo 4gr de polvo para hornear por media docena
    update ingrediente set cantidad = cantidad-(0.004*CantidadProducida) where nombre = 'Polvo para hornear' and estatus<>0;
    #bajar stock de harina 8.5gr de vainilla por media docena
    update ingrediente set cantidad = cantidad-(0.0085*CantidadProducida) where nombre = 'Vainilla' and estatus<>0;
    #bajar stock de harina 40gr de leche por media docena
    update ingrediente set cantidad = cantidad-(0.040*CantidadProducida) where nombre = 'Harina' and estatus<>0;
    
    #Ingrediente que cambia
    select id_ingrediente from ingrediente inner join receta on
    receta.ingrediente = ingrediente.id_ingrediente inner join producto on
    producto.receta = receta.id_receta where producto.id_producto = old.id_producto into idAux ;
    
    #Bajar stock del ingrediente que cambia 10gr
    update ingrediente set cantidad = cantidad-(0.010*CantidadProducida) where id_ingrediente = idAux and estatus<>0;
end $$