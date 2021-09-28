/* Insert-script voor BoekenClub
   Firebird 3, RelSQL-versie 29-maa-2021
*/
insert into Genre values (1, 'Astrologie');
insert into Genre values (2, 'Thriller');
insert into Genre values (3, 'Kinderboek');
insert into Genre values (4, 'Humor');

insert into Auteur values (1, 'Mellie Uyldert', 'V');
insert into Auteur values (5, 'Nicci French', 'V');
insert into Auteur values (7, 'Roald Dahl', 'M');
insert into Auteur values (10, 'John Grisham', 'M');

insert into Boek values(1, 1, 'Astrologie I', 39.95, 4.40, 1);
insert into Boek values(2, 1, 'Astrologie II', 39.95, 0, 1);
insert into Boek values(10, 5, 'Het veilige huis', 19.95, 3.60, 2);
insert into Boek values(11, 7, 'Matilda', 25.75, 5.00, 3);
insert into Boek values(15, 7, 'De GVR', 25.75, 5.00, 3);
insert into Boek values(23, 10, 'De Rainmaker', 49.95, 4.40, 2);

insert into Lid values (13, null, 'Rozen',   '01-jan-2020', '26-jun-2020', 'M', '19-feb-1986');
insert into Lid values (22, 13,   'Schoen',  '23-jan-2020', null,          'M', '12-mar-1996');
insert into Lid values (23, null, 'Janssen', '16-mar-2020', null,          'V', '25-aug-1980');
insert into Lid values (41, 22,   'Koning',  '27-jun-2020', '08-aug-2020', 'V', '23-may-1995');
insert into Lid values (45, 23,   'Tromp',   '12-aug-2020', null,          'M', '05-jan-1999');
insert into Lid values (56, 22,   'Peterse', '24-apr-2020', '14-oct-2020', 'V', '10-may-1993');
insert into Lid values (77, 56,   'Jansen',  '12-dec-2020', null,          'M', '13-oct-1977');

insert into Bestelling values (1, 22, '27-apr-2020');
insert into Bestelling values (2, 41, '13-jul-2020');
insert into Bestelling values (3, 56, '24-oct-2020');
insert into Bestelling values (4, 77, '11-nov-2020');
insert into Bestelling values (5, 56, '03-dec-2020');

insert into Bestelregel values (1, 1, 1, 1);
insert into Bestelregel values (1, 2, 23, 1);
insert into Bestelregel values (2, 1, 2, 1);
insert into Bestelregel values (2, 2, 15, 3);
insert into Bestelregel values (2, 3, 10, 1);
insert into Bestelregel values (3, 1, 23, 1);
insert into Bestelregel values (4, 1, 2, 2);
insert into Bestelregel values (5, 1, 10, 1);
insert into Bestelregel values (5, 2, 11, 1);
