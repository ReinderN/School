/* Create-script voor ToetjesboekZT (versie zonder triggers)
   Firebird 3, RelSQL4-versie 20-feb-2017
*/

create table Gerecht
(naam            varchar(25)    not null,
 energiePP       numeric(7,2),
 bereidingstijd  integer        not null,
 bereidingswijze varchar(250)   not null,
 primary key (naam)
);

create table Eenheid
(naam            varchar(12)    not null,
 primary key (naam)
);

create table Product
(naam            varchar(20)    not null,
 eenheid         varchar(12),
 energiePE       numeric(7,2),
 primary key (naam),
 foreign key (eenheid) references Eenheid (naam)
    on update cascade
);

create table Ingredient
(gerecht         varchar(25)    not null,
 product         varchar(20)    not null,
 hoeveelheidPP   numeric(5,2),
 volgnr          integer        not null,
 primary key (gerecht, product),
 foreign key (gerecht) references Gerecht (naam)
    on update cascade,
 foreign key (product) references Product (naam)
    on update cascade
);

commit;
