CREATE TABLE Kategorie(
    Nr_kategorii    SERIAL PRIMARY KEY,
    Nazwa           VARCHAR(25) NOT NULL UNIQUE
);

CREATE TABLE Kraje(
    Kod_kraju   VARCHAR(2) NOT NULL PRIMARY KEY,
    Nazwa       VARCHAR(40) NOT NULL UNIQUE,
    Waluta      VARCHAR(10)
);

CREATE TABLE Podroze(
    Nr_podrozy              SERIAL PRIMARY KEY,
    Nazwa                   VARCHAR(40) NOT NULL UNIQUE,
    Data_rozpoczecia        DATE UNIQUE,
    Data_zakonczenia        DATE UNIQUE,
    Opis                    TEXT
);

CREATE TABLE Miejsca(
    Nr_miejsca              SERIAL PRIMARY KEY,
    Kod_kraju               VARCHAR(2) REFERENCES  Kraje,
    Nazwa                   VARCHAR(40) NOT NULL UNIQUE,
    Szerokosc_geograficzna  VARCHAR(13),
    Dlugosc_geograficzna    VARCHAR(14),
    Opis                    TEXT
);

CREATE TABLE Kategorie_miejsc(
    Nr_miejsca      INTEGER REFERENCES Miejsca,
    Nr_kategorii    INTEGER REFERENCES Kategorie,
    PRIMARY KEY (Nr_miejsca, Nr_kategorii)
);

CREATE TABLE Miejsca_podrozy(
    Nr_podrozy  INTEGER REFERENCES Podroze,
    Nr_miejsca  INTEGER REFERENCES Miejsca,
    Pozycja     INTEGER,
    PRIMARY KEY (Nr_podrozy, Nr_miejsca, Pozycja)
);

ALTER TABLE miejsca
    ADD CONSTRAINT miejsca_ck_dlug_geog CHECK ( REGEXP_LIKE ( dlugosc_geograficzna,
                                                              '([01][0-9][0-9]�[0-5][0-9]''[0-5][0-9]''''[EW])' ) );

ALTER TABLE miejsca
    ADD CONSTRAINT miejsca_ck_szer_geog CHECK ( REGEXP_LIKE ( szerokosc_geograficzna,
                                                              '([0-9][0-9]�[0-5][0-9]''[0-5][0-9]''''[NS])' ) );