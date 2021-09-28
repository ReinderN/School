/* Create-script voor RuimtereisbureauD (versie met domeinen)
   Firebird 3, RelSQL4-versie 20-feb-2017
*/

create domain Transportcode         as varchar(2);
create domain Transportomschrijving as varchar(12);
create domain Reisnr                as integer        check (value > 0);
create domain Objectnaam            as varchar(10);
create domain Aantal                as integer        check (value >= 0);
create domain Geldbedrag            as numeric(5,2);
create domain Klantnr               as integer        check (value > 0);
create domain Afstand               as numeric(10,3)  check (value > 0);
create domain Diameter              as integer        check (value > 0);
create domain Volgnr                as integer        check (value > 0);
create domain Klantnaam             as varchar(10);
create domain Datum                 as date;

create table Transport
(code           Transportcode          not null,
 omschrijving   Transportomschrijving  not null,
 constraint pk_transport primary key (code),
 constraint un_transportomschrijving unique (omschrijving)
);

create table Reis
(nr             Reisnr         not null,
 vertrekdatum   Datum          not null,
 transport      Transportcode  not null,
 duur           Aantal,
 prijs          Geldbedrag,
 constraint pk_reis primary key (nr),
 constraint fk_reis_met_transport
    foreign key (transport) references Transport(code)
    on update cascade
);

create table Hemelobject
(naam           Objectnaam    not null,
 moederobject   Objectnaam,
 afstand        Afstand,
 diameter       Diameter,
 constraint pk_hemelobject primary key (naam)
);

alter table Hemelobject
add constraint fk_satelliet_van_hemelobject
       foreign key (moederobject) references Hemelobject(naam)
       on delete cascade on update cascade;

create table Bezoek
(reis           Reisnr        not null,
 volgnr         Volgnr        not null,
 hemelobject    Objectnaam    not null,
 verblijfsduur  Aantal        not null,
 constraint pk_bezoek primary key (reis, volgnr),
 constraint fk_bezoek_tijdens_reis
    foreign key (reis) references Reis(nr)
    on delete cascade on update cascade,
 constraint fk_bezoek_aan_hemelobject
    foreign key (hemelobject) references Hemelobject(naam)
    on update cascade
);

create table Klant
(nr             Klantnr       not null,
 naam           Klantnaam     not null,
 geboortedatum  Datum         not null,
 constraint pk_klant primary key (nr),
 constraint un_klantnaam unique (naam)
);

create table Deelname
(reis           Reisnr      not null,
 klant          Klantnr     not null,
 constraint pk_deelname primary key (reis, klant),
 constraint fk_deelname_aan_reis
    foreign key (reis) references Reis(nr)
    on update cascade,
 constraint fk_deelname_door_klant
    foreign key (klant) references Klant(nr)
    on update cascade
);

commit;