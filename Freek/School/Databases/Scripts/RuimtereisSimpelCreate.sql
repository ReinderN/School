/* Create-script voor RuimtereisSimpel
   Firebird 3, RelSQL4-versie 20-feb-2017
*/

create domain Reisnr     as integer;
create domain Objectnaam as varchar(10);
create domain Geldbedrag as numeric(5,2);
create domain Volgnr     as integer;

create table Reis
(nr                Reisnr        not null,
 vertrekdatum      date          not null,
 prijs             Geldbedrag,
 constraint pk_reis primary key (nr)
);

create table Hemelobject
(naam              Objectnaam    not null,
 moederobject      Objectnaam,
 constraint pk_hemelobject primary key (naam)
);

alter table Hemelobject
add constraint fk_satelliet_van_hemelobject
       foreign key (moederobject) references Hemelobject (naam)
       on delete cascade on update cascade;

create table Bezoek
(reis              Reisnr        not null,
 volgnr            Volgnr        not null,
 hemelobject       Objectnaam    not null,
 constraint pk_bezoek primary key (reis, volgnr),
 constraint fk_bezoek_tijdens_reis foreign key (reis)
    references Reis (nr)
    on delete cascade on update cascade,
 constraint fk_bezoek_aan_hemelobject
    foreign key (hemelobject) references Hemelobject (naam)
    on update cascade
);
