/* Create-script voor ToetjesboekKS
   (met kunstmatige sleutels, zonder triggers)
   Firebird 3, RelSQL4-versie 20-feb-2017
*/

create table Gerecht
(id              integer        not null,
 naam            varchar(25)    not null,
 energiePP       numeric(7,2),
 bereidingstijd  integer        not null,
 bereidingswijze varchar(250)   not null,
 primary key (id),
 unique (naam)
);

create table Eenheid
(naam            varchar(12)    not null,
 primary key (naam)
);

create table Product
(id              integer        not null,
 naam            varchar(20)    not null,
 eenheid         varchar(12),
 energiePE       numeric(7,2),
 primary key (id),
 foreign key (eenheid) references Eenheid (naam)
    on update cascade,
 unique (naam)
);

create table     Ingredient
(gerecht         integer        not null,
 product         integer        not null,
 hoeveelheidPP   numeric(5,2),
 volgnr          integer,
 primary key (gerecht, product),
 foreign key (gerecht) references Gerecht (id)
    on delete cascade on update cascade,
 foreign key (product) references Product (id)
    on update cascade
);

commit;

