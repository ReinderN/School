/* Insert-script voor HetCommentaar
   Firebird 3, RelSQL4-versie 20-feb-2017
*/

delete from Bijdragerelatie;
delete from Reactie;
delete from Bijdrage;
delete from Commentator;
delete from Bijdragesoort;
delete from Contributie;
update Lid
set hoofdlid = null;
delete from Lid;
delete from Lidsoort;

insert into Lidsoort values ('R', 'regulier',  60);
insert into Lidsoort values ('G', 'gezinslid', 30);
insert into Lidsoort values ('S', 'sponsor', 1000);

insert into Lid values (120, 'van Es', 'R', null, 'a.vanes@abc.nl',  'a@#1wxz!q',  '1357AC', '10');
insert into Lid values (121, 'Lieve',  'G', 120,  'j.lieve@wxs.nl',  'Hhg!23wzk9', '1357AC', '10');
insert into Lid values (122, 'Mattic', 'R', null, 'info@mattic.com', '5%&dDW34',   '9753ZW',' 9A');
insert into Lid values (130, 'Kooy',   'S', null, 'kooy@sweb.eu',    '10pK&1$vQ',  '5786GJ', '130');

insert into Contributie values (120, 2021,   60);
insert into Contributie values (121, 2021,   30);
insert into Contributie values (122, 2021, 1500);
insert into Contributie values (130, 2021,   75);
insert into Contributie values (120, 2022,   80);
insert into Contributie values (121, 2022,   30);
insert into Contributie values (122, 2022, 2000);

insert into Bijdragesoort values ('Ar', 'Artikel');
insert into Bijdragesoort values ('Co', 'Column');
insert into Bijdragesoort values ('Au', 'Audiobrief');
insert into Bijdragesoort values ('Fi', 'Film');

insert into Commentator values (1, 'Winter');
insert into Commentator values (2, 'Veldman');
insert into Commentator values (3, 'Wierda');
insert into Commentator values (4, 'Knoop');
insert into Commentator values (5, 'Boer');

insert into Bijdrage values (1200, 'Het nieuwe narcisme',                'Ar', 3, '2021-10-15');
insert into Bijdrage values (1650, 'Bitcoins: hoe werkt het?',           'Ar', 5, '2021-12-12');
insert into Bijdrage values (1903, 'Het nieuwe papier',                  'Ar', 1, '2022-01-09');
insert into Bijdrage values (1923, 'Het nieuwe papier',                  'Au', 1, '2022-01-10');
insert into Bijdrage values (2201, 'De overname van de publieke ruimte', 'Fi', 2, '2022-02-22');
insert into Bijdrage values (2560, 'Van ruilhandel tot bitcoin',         'Ar', 5, '2022-02-22');

insert into Reactie values (120, 1200, '2021-10-15', 'Toen ik ...' );
insert into Reactie values (130, 1200, '2021-10-15', 'Wat een ...' );
insert into Reactie values (120, 1200, '2021-10-16', 'Eigenlijk ...' );
insert into Reactie values (122, 2201, '2022-02-22', 'Natuurlijk ...' );
insert into Reactie values (122, 2560, '2022-02-22', 'Soms ...' );
insert into Reactie values (130, 2201, '2022-02-23', 'Wat me ...' );

insert into Bijdragerelatie values (1903, 1923);
insert into Bijdragerelatie values (1923, 1903);
insert into Bijdragerelatie values (2201, 1200);
insert into Bijdragerelatie values (2201, 1903);
insert into Bijdragerelatie values (2560, 1650);

commit;
