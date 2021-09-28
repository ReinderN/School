/* Create-script voor Orderdatabase
   Firebird 3, RelSQL4-versie 20-feb-2017
*/

create table Klant
(nr               integer      not null,
 naam             varchar(30)  not null,
 aanbrenger       integer,
 primary key (nr)
);

alter table Klant
add
foreign key (aanbrenger) references Klant(nr)
   on update cascade;

create table Order_
(nr               integer      not null,
 klant            integer      not null,
 datum            date         default  current_date   not null,
 totaalbedrag     numeric(7,2),
 primary key (nr),
 foreign key (klant) references Klant(nr)
    on update cascade
);

create table Artikelgroep
(code             varchar(5)   not null,
 omschrijving     varchar(20)  not null,
 primary key (code),
 unique (omschrijving)
);

create table Artikel
(nr               integer      not null,
 omschrijving     varchar(20)  not null,
 artikelgroep     varchar(5),
 verkoopprijs     numeric(7,2) not null,
 inkoopprijs      numeric(7,2) not null,
 voorraad         integer      default 0 not null,
 primary key (nr),
 unique (omschrijving),
 foreign key (artikelgroep) references Artikelgroep(code)
    on update cascade
);

create table Orderregel
(order_           integer      not null,
 volgnr           integer      not null,
 artikel          integer      not null,
 aantal           integer      not null,
 bedrag           numeric(7,2),
 primary key (order_, volgnr),
 unique (order_, artikel),
 foreign key (order_) references Order_(nr)
    on delete cascade on update cascade,
 foreign key (artikel) references Artikel(nr)
    on update cascade
);

create table Kortingsinterval
(beginaantal      integer      not null,
 eindaantal       integer,
 korting          numeric(2,1) not null
);
/* Er geldt nog de regel: beginaantal <= eindaantal en intervallen
   aaneensluitend vanaf 0 (implementeren via triggers).
   Hierom geen primaire sleutel.
*/

create table Klacht
(nr               integer      not null,
 order_           integer      not null,
 volgnr           integer      not null,
 behandeld        boolean   default false not null,
 primary key (nr),
 foreign key (order_, volgnr) references Orderregel(order_, volgnr)
    on update cascade
);

commit;