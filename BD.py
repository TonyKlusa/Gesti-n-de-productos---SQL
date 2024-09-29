'''

CREATE database Productos;
use Productos;

CREATE TABLE Productos(
codigo_producto char(8) primary key ,
producto varchar(25) not null,
precio decimal(10,2) not null,
cantidad_stock int not null,
marca char(25) not null
);

create table ProductosElectronicos(
codigo_producto char(8) primary key ,
modelo char(50),
foreign key (codigo_producto) references Productos (codigo_producto)
);

create table ProductosAlimenticios(
codigo_producto char(8) primary key ,
peso decimal(10,2),
foreign key (codigo_producto) references Productos (codigo_producto)
);

select * FROM PRODUCTOS
'''