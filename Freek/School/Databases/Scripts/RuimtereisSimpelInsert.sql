/* Insert-script voor RuimtereisSimpel
   Firebird 3, RelSQL4-versie 18-feb-2020
*/

delete from Bezoek;
update Hemelobject set moederobject = null;
delete from Hemelobject;
delete from Reis;

insert into Reis values (31, '12-jan-2032',  2.50);
insert into Reis values (32, '03-jun-2032', 17.50);
insert into Reis values (33, '12-oct-2032',  2.65);
insert into Reis values (34, '10-jan-2033', 75.00);
insert into Reis values (35, '12-mar-2033', 16.50);
insert into Reis values (36, '27-jun-2033',  null);
insert into Reis values (37, '17-jul-2033', 60.00);

insert into Hemelobject values ('Zon',     null     );
insert into Hemelobject values ('Venus',   'Zon'    );
insert into Hemelobject values ('Aarde',   'Zon'    );
insert into Hemelobject values ('Maan',    'Aarde'  );
insert into Hemelobject values ('Mars',    'Zon'    );
insert into Hemelobject values ('Phobos',  'Mars'   );
insert into Hemelobject values ('Deimos',  'Mars'   );
insert into Hemelobject values ('Jupiter', 'Zon'    );
insert into Hemelobject values ('Io',      'Jupiter');

insert into Bezoek values (31, 1, 'Maan'   );
insert into Bezoek values (32, 1, 'Maan'   );
insert into Bezoek values (32, 2, 'Phobos' );
insert into Bezoek values (32, 3, 'Deimos' );
insert into Bezoek values (32, 4, 'Mars'   );
insert into Bezoek values (32, 5, 'Maan'   );
insert into Bezoek values (33, 1, 'Maan'   );
insert into Bezoek values (34, 1, 'Mars'   );
insert into Bezoek values (34, 2, 'Jupiter');
insert into Bezoek values (34, 3, 'Io'     );
insert into Bezoek values (35, 1, 'Maan'   );
insert into Bezoek values (35, 2, 'Mars'   );
insert into Bezoek values (35, 3, 'Maan'   );
insert into Bezoek values (36, 1, 'Mars'   );
insert into Bezoek values (36, 2, 'Jupiter');
insert into Bezoek values (36, 3, 'Io'     );
insert into Bezoek values (37, 1, 'Mars'   );

commit;
