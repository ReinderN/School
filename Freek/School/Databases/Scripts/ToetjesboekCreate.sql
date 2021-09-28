/* Create-script voor Toetjesboek
   (met stored procedure en triggers voor automatische berekening van energiePP)
   Firebird 3, RelSQL4-versie 20-feb-2017
*/

------------------------ Tabellen -------------------------

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
    on delete cascade on update cascade,
 foreign key (product) references Product (naam)
    on update cascade
);

commit;
 
--------------- Stored procedure en triggers --------------------

set term ^;
--
-- stored procedure en vijf triggers voor automatische berekening
-- en invulling van Gerecht.energiePP
--
create procedure pGerecht_update_energiePP(gerechtnaam varchar(25))
as begin
   update Gerecht
   set    energiePP = (select sum(P.energiePE * I.hoeveelheidPP)
                       from   Ingredient I
                              join Product P on I.product = P.naam
                       where  I.gerecht = :gerechtnaam)
   where  naam = :gerechtnaam;
   end^

create trigger tIngredient_ai
for Ingredient after insert
as begin
   execute procedure pGerecht_update_energiePP(new.gerecht);
   end^

create trigger tIngredient_ad
for Ingredient after delete
as begin
   execute procedure pGerecht_update_energiePP(old.gerecht);
   end^

create trigger tIngredient_au
for Ingredient after update
as begin
   if (old.hoeveelheidPP <> new.hoeveelheidPP)
      then execute procedure pGerecht_update_energiePP(new.gerecht);
   end^

create trigger tProduct_au
for Product after update
as declare variable gerechtnaam varchar(25);
   begin
   if (old.energiePE <> new.energiePE)
      then for select gerecht
               from   Ingredient
               where  product = new.naam
               into   :gerechtnaam
           do execute procedure pGerecht_update_energiePP(:gerechtnaam);
   end^

create trigger tGerecht_au
for Gerecht after update
as begin
   if (old.energiePP <> new.energiePP)
      then execute procedure pGerecht_update_energiePP(old.naam);
   end^

--
-- trigger voor automatische berekening en invulling van een nieuw Ingredient.volgnr
--
create trigger tIngredient_bi
for Ingredient before insert
as begin
   select max(volgnr) + 1
   from   Ingredient
   where  gerecht = new.gerecht
   into   new.volgnr;

   if (new.volgnr is null)
      then new.volgnr = 1;
   end^

--
-- trigger voor cascading delete van verwijzing van Ingredient naar Gerecht
--
create trigger tGerecht_bd_cascadingDelete
for Gerecht before delete as
   begin
   delete 
   from  Ingredient
   where gerecht = old.naam;
   end^

set term ;^

commit;
