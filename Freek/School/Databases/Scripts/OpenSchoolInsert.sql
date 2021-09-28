/* Insert-script voor OpenSchool
   Firebird 3, RelSQL4-versie 20-feb-2017
*/

delete from Tentamen;
delete from Inschrijving;
delete from Begeleider;
delete from Voorkenniseis;
delete from Student;
delete from Student1;
delete from Cursus;
update Docent
set    vervanger = null;
delete from Docent;
delete from Vakgroep;

insert into Vakgroep values ('IS', 'Informatiesystemen');
insert into Vakgroep values ('ST', 'Softwaretechnologie');

insert into Docent values ('DAT', 'C.Date',    null, 'IS');
insert into Docent values ('COD', 'E.Codd',    null, 'IS');
insert into Docent values ('BAC', 'C.Bachman', null, 'ST');
update Docent
set    vervanger = 'COD'
where  acr = 'DAT';
update Docent
set    vervanger = 'DAT'
where  acr = 'BAC';

insert into Cursus values ('II', 'Inleiding informatica',  80, 3, 'BAC');
insert into Cursus values ('DW', 'Discrete wiskunde',     120, 4, 'DAT');
insert into Cursus values ('DB', 'Databases',             120, 4, 'COD');
insert into Cursus values ('IM', 'Informatiemodelleren',  150, 5, 'DAT');
insert into Cursus values ('SW', 'Semantic web',          120, 4, null );

insert into Student values (1, 'Berk', 'DAT');
insert into Student values (2, 'Tack', 'DAT');
insert into Student values (3, 'Bos',  'COD');
insert into Student values (4, 'Eik',  null );

insert into Begeleider values ('DAT', 'DB');
insert into Begeleider values ('DAT', 'DW');
insert into Begeleider values ('DAT', 'IM');
insert into Begeleider values ('BAC', 'II');
insert into Begeleider values ('BAC', 'DB');

insert into Voorkenniseis values ('DB', 'II');
insert into Voorkenniseis values ('DB', 'DW');
insert into Voorkenniseis values ('IM', 'DB');
insert into Voorkenniseis values ('SW', 'DB');

insert into Inschrijving values (1, 'II', '12-jan-2021', 7,    false );
insert into Inschrijving values (1, 'DW', '19-jan-2021', 5,    false );
insert into Inschrijving values (1, 'DB', '18-mar-2021', 8,    false );
insert into Inschrijving values (1, 'IM', '20-jun-2021', null, false );
insert into Inschrijving values (2, 'II', '12-jan-2021', null, true );
insert into Inschrijving values (2, 'DW', '12-jan-2021', null, true );
insert into Inschrijving values (2, 'IM', '26-jan-2021', 5,    false );
insert into Inschrijving values (3, 'II', '16-jan-2021', null, null);
insert into Inschrijving values (4, 'II', '20-jan-2021', null, true );
insert into Inschrijving values (4, 'DB', '28-feb-2021', null, false );

insert into Tentamen values (1, 'II', 1, '17-apr-2021', 7   );
insert into Tentamen values (1, 'DW', 1, '17-apr-2021', 5   );
insert into Tentamen values (1, 'DB', 1, '19-apr-2021', 5   );
insert into Tentamen values (1, 'DB', 2, '26-jun-2021', 8   );
insert into Tentamen values (2, 'IM', 1, '06-apr-2021', 4   );
insert into Tentamen values (2, 'IM', 2, '11-jun-2021', 5   );
insert into Tentamen values (4, 'DB', 1, '26-jun-2021', null);

-- zie leereenheid 5, paragraaf 1.5
insert into Student1 values (1, 'Inge', null,  'Berk', 'DAT');
insert into Student1 values (2, 'Max',  null,  'Tack', 'DAT');
insert into Student1 values (3, 'Max',  null,  'Bos',  'COD');
insert into Student1 values (4, 'Iris', 'van', 'Eik',  null );

commit;
