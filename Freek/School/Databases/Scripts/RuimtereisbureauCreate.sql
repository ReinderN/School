/* Create-script voor Ruimtereisbureau (versie zonder domeinen)
   Firebird 3, RelSQL4-versie 20-feb-2017
*/

create table Transport
(code              varchar(2)     not null,
 omschrijving      varchar(12)    not null,
 constraint pk_transport primary key (code),
 constraint un_transportomschrijving unique (omschrijving)
);

create table Reis
(nr                integer        not null,
 vertrekdatum      date           not null,
 transport         varchar(2)     not null,
 duur              integer,
 prijs             numeric(5,2),
 constraint pk_reis primary key (nr),
 constraint fk_reis_met_transport
    foreign key (transport) references Transport(code)
    on update cascade,
 constraint ch_reisnr check (nr between 1 and 2000),
 constraint ch_reisduur check (not(prijs is not null and duur is null))
);

create table Hemelobject
(naam              varchar(10)    not null,
 moederobject      varchar(10),
 afstand           numeric(10,3),
 diameter          integer,
 constraint pk_hemelobject primary key (naam),
 constraint ch_afstand check (afstand > 0),
 constraint ch_diameter check (diameter > 0),
 constraint ch_nietSatellietVanZichzelf
    check (moederobject != naam)
);

alter table Hemelobject
add constraint fk_satelliet_van_hemelobject
       foreign key (moederobject) references Hemelobject(naam)
       on delete cascade on update cascade;

create table Bezoek
(reis              integer         not null,
 volgnr            integer         not null,
 hemelobject       varchar(10)     not null,
 verblijfsduur     integer         not null,
 constraint pk_bezoek primary key (reis, volgnr),
 constraint fk_bezoek_tijdens_reis
    foreign key (reis) references Reis(nr)
    on delete cascade on update cascade,
 constraint fk_bezoek_aan_hemelobject
    foreign key (hemelobject) references Hemelobject(naam)
    on update cascade,
 constraint ch_volgnr check (volgnr > 0)
);

create table Klant
(nr                integer       not null,
 naam              varchar(10)   not null,
 geboortedatum     date          not null,
 constraint pk_klant primary key (nr),
 constraint un_klantnaam unique (naam),
 constraint ch_klantnr check (nr > 0)
);

create table Deelname
(reis              integer       not null,
 klant             integer       not null,
 constraint pk_deelname primary key (reis, klant),
 constraint fk_deelname_aan_reis
    foreign key (reis) references Reis(nr)
    on update cascade,
 constraint fk_deelname_door_klant
    foreign key (klant) references Klant(nr)
    on update cascade
);
