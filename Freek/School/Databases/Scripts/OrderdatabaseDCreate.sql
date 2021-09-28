/* Create-script voor OrderdatabaseD (versie met domeinen)
   Firebird 3, RelSQL4-versie 20-feb-2017
*/

create domain Klantnr                   as integer;
create domain Klantnaam                 as varchar(30);
create domain Ordernr                   as integer;
create domain Volgnr                    as integer;
create domain Geldbedrag                as numeric(7,2);
create domain Artikelnr                 as integer;
create domain Artikelomschrijving       as varchar(20);
create domain Artikelgroepomschrijving  as varchar(20);
create domain Artikelgroepcode          as varchar(5);
create domain Aantal                    as integer;
create domain Klachtnr                  as integer;
create domain Percentage                as numeric(2,1);
create domain Datum                     as date;

create table Klant
(nr             Klantnr      not null,
 naam           Klantnaam    not null,
 aanbrenger     Klantnr,
 constraint pk_klant primary key (nr)
);

alter table Klant
add constraint fk_klant_aangebracht_door 
    foreign key (aanbrenger) references Klant(nr)
    on update cascade;

create table Order_
(nr               Ordernr      not null,
 klant            Klantnr      not null,
 datum            Datum        default current_date  not null,
 totaalbedrag     Geldbedrag,
 constraint pk_order primary key (nr),
 constraint fk_order_van_klant
    foreign key (klant) references Klant(nr)
    on update cascade
);

create table Artikelgroep
(code             Artikelgroepcode          not null,
 omschrijving     Artikelgroepomschrijving  not null,
 constraint pk_artikelgroep primary key (code),
 constraint un_artikelgroep unique (omschrijving)
);

create table Artikel
(nr               Artikelnr           not null,
 omschrijving     Artikelomschrijving not null,
 artikelgroep     Artikelgroepcode,
 verkoopprijs     Geldbedrag          not null,
 inkoopprijs      Geldbedrag          not null,
 voorraad         Aantal              default 0 not null,
 constraint pk_artikel primary key (nr),
 constraint un_artikel unique (omschrijving),
 constraint fk_artikel_bij_artikelgroep
    foreign key (artikelgroep) references Artikelgroep(code)
    on update cascade
);

create table Orderregel
(order_           Ordernr    not null,
 volgnr           Volgnr     not null,
 artikel          Artikelnr  not null,
 aantal           Aantal     not null,
 bedrag           Geldbedrag,
 constraint pk_orderregel primary key (order_, volgnr),
 constraint un_orderregel unique (order_, artikel),
 constraint fk_orderregel_van_order_ 
    foreign key (order_) references Order_(nr)
    on delete cascade on update cascade,
 constraint fk_orderregel_bij_artikel
    foreign key (artikel) references Artikel(nr)
    on update cascade
);

create table Kortingsinterval
(beginaantal      Aantal      not null,
 eindaantal       Aantal      not null,
 korting          Percentage  not null
);
/* Aanvullende regel: beginaantal <= eindaantal en intervallen
   aaneensluitend vanaf 0 (implementeren via triggers).
   Daarom geen primaire sleutel.
*/

create table Klacht
(nr              Klachtnr     not null,
 order_          Ordernr      not null,
 volgnr          Volgnr       not null,
 behandeld       boolean      default false not null,
 constraint pk_klacht primary key (nr),
 constraint fk_klacht_bij_order_regel 
    foreign key (order_, volgnr) references Orderregel(order_, volgnr)
    on delete cascade on update cascade
);
