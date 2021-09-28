-- voorbeeld 12.9
-- RelSQL4-versie 20-feb-2017
connect 'Ruimtereisbureau.fdb' user 'Ruimtereisbureau' password 'pw';
grant select on Reis to Tom with grant option;
connect 'Ruimtereisbureau.fdb' user 'Tom' password 'pw';
grant select on Reis to Luc;
grant select on Reis to Sofie with grant option;
connect 'Ruimtereisbureau.fdb' user 'Sofie' password 'pw';
grant select on Reis to Jip, Lisa;

-- voorbeeld 12.10
connect 'Ruimtereisbureau.fdb' user 'Ruimtereisbureau' password 'pw';
grant update (prijs) on Reis to Luc, Sofie with grant option;
connect 'Ruimtereisbureau.fdb' user 'Luc' password 'pw';
grant update (prijs) on Reis to Sofie with grant option;
connect 'Ruimtereisbureau.fdb' user 'Sofie' password 'pw';
grant update (prijs) on Reis to Jip, Lisa;
