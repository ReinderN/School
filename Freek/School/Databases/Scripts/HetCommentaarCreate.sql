/* Create-script voor HetCommentaar
   versie zonder constraintnamen en zonder domeinen
   Firebird 3, versie 18-feb-2020
*/

create table Lidsoort
(code               char(1)      not null,
 omschrijving       varchar(9)   not null,
 minimumcontributie numeric (7,2),
 primary key (code),
 unique (omschrijving)
);

create table Lid
(nr                integer       not null,
 naam              varchar(20)   not null,
 lidsoort          char(1)       not null,
 hoofdlid          integer,
 email             varchar(25)   not null,
 wacntwoord        varchar(30)   not null,
 postcode          varchar(6),
 huisnr            varchar(8),
 primary key (nr),
 unique(email),
 foreign key (lidsoort) references Lidsoort(code)
    on update cascade
);

alter table Lid
add
foreign key (hoofdlid) references Lid(nr)
   on update cascade;

create table Contributie
(lid               integer       not null,
 jaar              numeric(4)    not null,
 bedrag            numeric(7,2)  not null,
 primary key (lid, jaar),
 foreign key (lid) references Lid(nr)
    on update cascade
);

create table Commentator
(nr                 integer      not null,
 naam               varchar(25)  not null,
 primary key (nr),
 unique (naam)
);

create table Bijdragesoort
(code               char(2)      not null,
 naam               varchar(20)  not null,
 primary key (code),
 unique (naam)
);

create table Bijdrage
(nr              integer         not null,
 titel           varchar(50)     not null,
 soort           char(2)         not null,
 commentator     integer         not null,
 datum           date,
 primary key (nr),
 unique(titel, soort),
 foreign key (soort) references Bijdragesoort(code)
    on update cascade,
 foreign key (commentator) references Commentator(nr)
    on update cascade
);

create table Reactie
(lid            integer         not null,
 bijdrage       integer         not null,
 datum          date            not null,
 tekst          varchar(500)    not null,
 primary key (lid, bijdrage, datum),
 foreign key (lid) references Lid(nr)
    on update cascade,
 foreign key (bijdrage) references Bijdrage(nr)
    on delete cascade on update cascade
);

create table Bijdragerelatie
(bijdrage                 integer      not null,
 gerelateerde_bijdrage    integer      not null,
 primary key (bijdrage, gerelateerde_bijdrage),
 foreign key (bijdrage) references Bijdrage(nr)
    on delete cascade on update cascade,
 foreign key (gerelateerde_bijdrage) references Bijdrage(nr)
    on delete cascade on update cascade
);

commit;
