/* Create-script voor OpenSchool
   Firebird 3, RelSQL-versie 18-feb-2020
*/

create table Vakgroep
(code               char(2)       not null,
 naam               varchar(25)   not null,
 primary key (code)
);

create table Docent
(acr               char(3)      not null,
 naam              varchar(20)  not null,
 vervanger         char(3),
 vakgroep          char(2)      not null,
 primary key (acr),
 foreign key (vakgroep) references Vakgroep(code)
    on update cascade,
 unique(naam)
);

alter table Docent
add
foreign key (vervanger) references Docent(acr)
   on update cascade;

create table Student
(nr                integer      not null,
 naam              varchar(20)  not null,
 mentor            char(3),
 primary key (nr),
 foreign key (mentor) references Docent(acr)
    on update cascade
);

-- variant van Student t.b.v. hoofdstuk 4, paragraaf 4.1.5
create table Student1
(nr                integer      not null,
 voornaam          varchar(15)  not null,
 voorvoegsel       varchar(7),
 naam              varchar(20)  not null,
 mentor            char(3),
 primary key (nr),
 foreign key (mentor) references Docent(acr)
    on update cascade
);

create table Cursus
(code              varchar(4)    not null,
 naam              varchar(25)   not null,
 uren              integer       not null,
 credits           numeric(4,1)  not null,
 examinator        char(3),
 primary key (code),
 foreign key (examinator) references Docent(acr)
    on update cascade,
 unique (naam)
);

create table Begeleider
(docent            char(3)      not null,
 cursus            varchar(4)   not null,
 primary key (docent, cursus),
 foreign key (docent) references Docent(acr)
    on delete cascade on update cascade,
 foreign key (cursus) references Cursus(code)
    on update cascade
);

create table Voorkenniseis
(cursus            varchar(4)   not null,
 voorkennis        varchar(4)   not null,
 primary key (cursus, voorkennis),
 foreign key (cursus) references Cursus(code)
    on delete cascade on update cascade,
 foreign key (voorkennis) references Cursus(code)
    on update cascade
);

create table Inschrijving
(student           integer      not null,
 cursus            varchar(4)   not null,
 datum             date         default current_date   not null,
 cijfer            numeric(2),
 vrijstelling      boolean,
 primary key (student, cursus),
 foreign key (student) references Student(nr)
    on delete cascade on update cascade,
 foreign key (cursus) references Cursus(code)
    on update cascade
);

create table Tentamen
(student           numeric(4)   not null,
 cursus            varchar(4)   not null,
 volgnr            numeric(2)   not null,
 datum             date         not null,
 cijfer            numeric(2),
 primary key (student, cursus, volgnr),
 foreign key (student, cursus) references Inschrijving(student, cursus)
    on delete cascade on update cascade,
 unique (student, cursus, datum)
);

--
-- twee extra tabellen t.b.v. voorbeeld 11.13
--
create table DWCursus
(code              varchar(4)    not null,
 naam              varchar(25)   not null,
 begeleid          boolean       not null,
 primary key (code)
);

create table DWCursusresultaat
(cursuscode               varchar(4)    not null,
 cursusnaam               varchar(25)   not null,
 jaar                     integer       not null,
 maand                    integer       not null,
 aantal_inschrijvingen    integer,
 aantal_afgerond          integer,
 primary key (cursuscode, jaar, maand)
);
