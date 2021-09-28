/* Conversiescript OrderdatabaseCConversie.sql
   Firebird 3, RelSQL4-versie 20-feb-2017

   Dit script gaat ervan uit dat de gebruiker is ingelogd op OrderdatabaseC.fdb
   (versie met constraintnamen, gecreëerd met script OrderdatabaseCCreate.sql)
*/

--  1 Creëer Client, nog zonder de recursieve aanbrenger-verwijzing
create table Client
(nr             integer      not null,
 voorletters    varchar(8)   not null,
 voorvoegsel    varchar(8),
 achternaam     varchar(20)  not null,
 aanbrenger	integer,
 constraint pk_client primary key (nr)
);

-- 2 Kopieer de populatie van Klant naar Client
insert into Client (nr, voorletters, achternaam, aanbrenger)
   select nr, '', naam, aanbrenger
   from   Klant;

-- 3 Breng in Client de recursieve aanbrenger-verwijzing aan
alter table Client
add constraint fk_client_aangebracht_door
    foreign key (aanbrenger) references Client(nr)
    on update cascade;

-- 4 Maak nieuwe kolom Order_.client
alter table Order_
add client integer not null;

-- 5 Vul Order_.client vanuit Order_.klant en commit
update Order_
set    client = klant;
commit;

-- 6 Leg een verwijssleutel van Order_ naar Client
alter table Order_
add constraint fk_order_van_client
       foreign key (client) references Client(nr)
       on update cascade;

-- 7 Verwijder de oude verwijssleutel van Order_ naar Klant
reconnect;
alter table Order_
drop constraint fk_order_van_klant;

-- 8 Verwijder kolom Order_.klant
alter table Order_
drop klant;

-- 9 Verwijder de recursieve verwijzing van Klant en daarna Klant zelf
reconnect;
alter table Klant
drop constraint fk_aanbrenger_van_klant;
/* alternatief:
update Klant
set    aanbrenger = null
*/
drop table Klant;
