/* Insert-script voor Toetjesboek
   Firebird 3, RelSQL4-versie 20-feb-2017
*/

delete from Ingredient;
delete from Product;
delete from Gerecht;
delete from Eenheid;

insert into Gerecht values ('Coupe Kiwano', null, 20,
   'Schil de kiwano, snijd hem in stukjes, voeg de tequila toe en laat dit ' ||
   'mengsel 15 minuten staan. Neem per persoon 3 bolletjes ijs en voeg hier '||
   'de kiwano met tequila aan toe. Serveer met gezoete, stijfgeslagen '||
   'slagroom.');
insert into Gerecht values ('Glace Terrace', null, 5,
   'Neem drie bolletjes ijs, voeg hieraan de gesneden aardbeien toe, '||
   'besprenkel dit rijkelijk met pernod en maak dit bijzondere gerecht af '||
   'met versgemalen peper.');
insert into Gerecht values ('Mango Plus Plus', null, 8,
   'Snijd de - geschilde - mango in stukjes, meng deze met de gehalveerde '||
   'aardbeien, en serveer dit met de zure room.');

insert into Eenheid values ('liter');
insert into Eenheid values ('deciliter');
insert into Eenheid values ('stuks');
insert into Eenheid values ('gram');
insert into Eenheid values ('kilogram');
insert into Eenheid values ('eetlepel');
insert into Eenheid values ('theelepel');

insert into Product values ('ijs',       'liter',    1600);
insert into Product values ('kiwano',    'stuks',      40);
insert into Product values ('slagroom',  'deciliter', 336);
insert into Product values ('suiker',    'gram',        4);
insert into Product values ('tequila',   'eetlepel',   30);
insert into Product values ('aardbeien', 'gram',     0.25);
insert into Product values ('pernod',    'eetlepel',   35);
insert into Product values ('peper',     null,       null);
insert into Product values ('mango',     'stuks',      80);
insert into Product values ('zure room', 'deciliter', 195);
insert into Product values ('banaan',    'stuks',      40);

/* Opmerking: de (verplichte) volgnr-kolom wordt automatisch gevuld via een trigger.
   Omdat de values-lijst nu niet alle kolommen omvat, is opname van een kolommenlijst
   na de tabelnaam verplicht.
*/
insert into Ingredient (gerecht, product, hoeveelheidPP) values ('Coupe Kiwano',    'ijs',       0.15);
insert into Ingredient (gerecht, product, hoeveelheidPP) values ('Coupe Kiwano',    'kiwano',     0.5);
insert into Ingredient (gerecht, product, hoeveelheidPP) values ('Coupe Kiwano',    'slagroom',   0.3);
insert into Ingredient (gerecht, product, hoeveelheidPP) values ('Coupe Kiwano',    'suiker',      10);
insert into Ingredient (gerecht, product, hoeveelheidPP) values ('Coupe Kiwano',    'tequila',      1);
insert into Ingredient (gerecht, product, hoeveelheidPP) values ('Glace Terrace',   'ijs',        0.2);
insert into Ingredient (gerecht, product, hoeveelheidPP) values ('Glace Terrace',   'aardbeien',   50);
insert into Ingredient (gerecht, product, hoeveelheidPP) values ('Glace Terrace',   'pernod',       2);
insert into Ingredient (gerecht, product, hoeveelheidPP) values ('Glace Terrace',   'peper',     null);
insert into Ingredient (gerecht, product, hoeveelheidPP) values ('Mango Plus Plus', 'mango',      0.5);
insert into Ingredient (gerecht, product, hoeveelheidPP) values ('Mango Plus Plus', 'aardbeien',   50);
insert into Ingredient (gerecht, product, hoeveelheidPP) values ('Mango Plus Plus', 'zure room',  0.4);

commit;
