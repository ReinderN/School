/* Create-script voor OrderdatabaseC (versie met constraintnamen)
   Firebird 3, RelSQL4-versie 20-feb-2017
*/

create table Klant
(nr             integer      not null,
 naam           varchar(30)  not null,
 aanbrenger	integer,
 constraint pk_klant primary key (nr)
);

alter table Klant
add constraint fk_klant_aangebracht_door
    foreign key (aanbrenger) references Klant(nr)
    on update cascade;

create table Order_
(nr             integer      not null,
 klant          integer      not null,
 datum          date         default current_date  not null,
 totaalbedrag   numeric(7,2),
 constraint pk_order primary key (nr),
 constraint fk_order_van_klant
    foreign key (klant) references Klant(nr)
    on update cascade
);

create table Artikelgroep
(code           varchar(5)   not null,
 omschrijving   varchar(20)  not null,
 constraint pk_artikelgroep primary key (code),
 constraint un_artikelgroep unique (omschrijving)
);

create table Artikel
(nr               integer      not null,
 omschrijving     varchar(20)  not null,
 artikelgroep     varchar(5),
 verkoopprijs     numeric(7,2) not null,
 inkoopprijs      numeric(7,2) not null,
 voorraad         integer      default 0 not null,
 constraint pk_artikel primary key (nr),
 constraint un_artikel unique (omschrijving),
 constraint fk_artikel_bij_artikelgroep
    foreign key (artikelgroep) references Artikelgroep(code)
    on update cascade
);

create table Orderregel
(order_           integer      not null,
 volgnr           integer      not null,
 artikel          integer      not null,
 aantal           integer      not null,
 bedrag           numeric(7,2),
 constraint pk_orderregel primary key (order_, volgnr),
 constraint un_orderregel unique (order_, artikel),
 constraint fk_orderregel_van_order 
    foreign key (order_) references Order_(nr)
    on delete cascade on update cascade,
 constraint fk_orderregel_bij_artikel
    foreign key (artikel) references Artikel(nr)
    on update cascade
);

create table Kortingsinterval
(beginaantal      integer      not null,
 eindaantal       integer,
 korting          numeric(2,1) not null
);

create table Klacht
(nr               integer      not null,
 order_           integer      not null,
 volgnr           integer      not null,
 behandeld        boolean   default false not null,
 constraint pk_klacht primary key (nr),
 constraint fk_klacht_bij_orderregel 
    foreign key (order_, volgnr) references Orderregel(order_, volgnr)
    on delete cascade on update cascade
);
