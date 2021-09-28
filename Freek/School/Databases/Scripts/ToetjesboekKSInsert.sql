/* Insert-script voor ToetjesboekKS
   (versie met kunstmatige sleutels, zonder triggers)
   Firebird 3, RelSQL4-versie 20-feb-2017
*/

delete from Ingredient;
delete from Gerecht;
delete from Product;
delete from Eenheid;

insert into Gerecht values (1, 'Coupe Kiwano', 431, 20,
   'Schil de kiwano, snijd hem in stukjes, voeg de tequila toe en laat dit ' ||
   'mengsel 15 minuten staan. Neem per persoon 3 bolletjes ijs en voeg hier '||
   'de kiwano met tequila aan toe. Serveer met gezoete, stijfgeslagen '||
   'slagroom.');
insert into Gerecht values (2, 'Glace Terrace', 403, 5,
   'Neem drie bolletjes ijs, voeg hieraan de gesneden aardbeien toe, '||
   'besprenkel dit rijkelijk met pernod en maak dit bijzondere gerecht af '||
   'met versgemalen peper.');
insert into Gerecht values (3, 'Mango Plus Plus', 131, 8,
   'Snijd de - geschilde - mango in stukjes, meng deze met de gehalveerde '||
   'aardbeien, en serveer dit met de zure room.');

insert into Eenheid values ('liter');
insert into Eenheid values ('deciliter');
insert into Eenheid values ('stuks');
insert into Eenheid values ('gram');
insert into Eenheid values ('kilogram');
insert into Eenheid values ('eetlepel');
insert into Eenheid values ('theelepel');
 
insert into Product values (1,  'ijs',       'liter',    1600);
insert into Product values (3,  'kiwano',    'stuks',      40);
insert into Product values (4,  'slagroom',  'deciliter', 336);
insert into Product values (5,  'suiker',    'gram',        4);
insert into Product values (6,  'tequila',   'eetlepel',   30);
insert into Product values (7,  'aardbeien', 'gram',     0.25);
insert into Product values (10, 'pernod',    'eetlepel',   35);
insert into Product values (12, 'peper',     null,       null);
insert into Product values (13, 'mango',     'stuks',      80);
insert into Product values (14, 'zure room', 'deciliter', 195);
insert into Product values (15, 'banaan',    'stuks',      40);

insert into Ingredient values (1, 1,  0.15, 1);
insert into Ingredient values (1, 3,   0.5, 2);
insert into Ingredient values (1, 4,   0.3, 3);
insert into Ingredient values (1, 5,    10, 4);
insert into Ingredient values (1, 6,     1, 5);
insert into Ingredient values (2, 1,   0.2, 1);
insert into Ingredient values (2, 7,    50, 2);
insert into Ingredient values (2, 10,    2, 3);
insert into Ingredient values (2, 12, null, 4);
insert into Ingredient values (3, 13,  0.5, 1);
insert into Ingredient values (3, 7,    50, 2);
insert into Ingredient values (3, 14,  0.4, 3);

commit;
