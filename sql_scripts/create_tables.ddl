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
    Data_rozpoczecia        DATE NOT NULL UNIQUE,
    Data_zakonczenia        DATE NOT NULL UNIQUE,
    Opis                    TEXT
);

CREATE TABLE Miejsca(
    Nr_miejsca              SERIAL PRIMARY KEY,
    Kod_kraju               VARCHAR(2) REFERENCES  Kraje,
    Nazwa                   VARCHAR(40) NOT NULL UNIQUE,
    Szerokosc_geograficzna  VARCHAR(12),
    Dlugosc_geograficzna    VARCHAR(13),
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