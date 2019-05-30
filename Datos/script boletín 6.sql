create table depart(
dept_no integer,
dnombre varchar(20),
loc varchar(20),
primary key (dept_no)
);

insert into depart
values ('10','CONTABILIDAD','SEVILLA');
insert into depart
values ('20','INVESTIGACION','MADRID');
insert into depart
values ('30','VENTAS','BARCELONA');
insert into depart
values ('40','PRODUCCION','BILBAO');


create table emple(
emp_no integer,
apellidos varchar(20),
oficio varchar(20),
dir integer,
fecha_alt date,
salario integer,
comision integer,
dept_no integer,
primary key (emp_no),
foreign key (dept_no) references depart (dept_no)
);

insert into emple (emp_no, apellidos, oficio, dir, fecha_alt, salario, dept_no)
values ('7369','SANCHEZ','EMPLEADO','7902','17/12/1980','104000','20');
insert into emple
values ('7499','ARROYO','VENDEDOR','7698','20/02/1980','208000','39000','30');
insert into emple
values ('7521','SALA','VENDEDOR','7698','22/02/1981','162500','162500','30');
insert into emple (emp_no, apellidos, oficio, dir, fecha_alt, salario, dept_no)
values ('7566','JIMENEZ','DIRECTOR','7839','02/04/1981','386750','20');
insert into emple
values ('7654','MARTIN','VENDEDOR','7698','29/09/1981','162500','182000','30');
insert into emple(emp_no, apellidos, oficio, dir, fecha_alt, salario, dept_no)
values ('7698','NEGRO','DIRECTOR','7839','01/05/1981','370500','30');
insert into emple(emp_no, apellidos, oficio, dir, fecha_alt, salario, dept_no)
values ('7788','GIL','ANALISTA','7566','09/11/1981','390000','20');
insert into emple(emp_no, apellidos, oficio, fecha_alt, salario, dept_no)
values ('7839','REY','PRESIDENTE','17/11/1981','650000','10');
insert into emple
values ('7844','TOVAR','VENDEDOR','7698','08/09/1981','195000','0','30');
insert into emple(emp_no, apellidos, oficio, dir, fecha_alt, salario, dept_no)
values ('7876','ALONSO','EMPLEADO','7788','23/09/1981','143000','20');
insert into emple(emp_no, apellidos, oficio, dir, fecha_alt, salario, dept_no)
values ('7900','JIMENO','EMPLEADO','7698','03/12/1981','1235000','30');
insert into emple(emp_no, apellidos, oficio, dir, fecha_alt, salario, dept_no)
values ('7902','FERNANDEZ','ANALISTA','7566','03/12/1981','390000','20');
insert into emple(emp_no, apellidos, oficio, dir, fecha_alt, salario, dept_no)
values ('7934','MUÑOZ','EMPLEADO','7782','23/01/1982','169000','10');

