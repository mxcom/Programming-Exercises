create table User (
    UserID int NOT NULL AUTO_INCREMENT,
    Sex VARCHAR(255)
    LastName varchar(255) NOT NULL,
    FirstName varchar(255) NOT NULL,
    mail
    passwdhash varchar(255) NOT NULL
    passwdsalt varchar(255) NOT NULL
    PRIMARY KEY(UserID)

)

create table Steps (
    UserID int
    Steps int
    Measuretime DATETIME
    FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
    PRIMARY KEY (PersonID,Measuretime)

)

create table Bloodpressure (
    UserID int
    Systolic int
    Diastolic int
    Measuretime DATETIME
    PRIMARY KEY (UserID,Measuretime)
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
)


create table Weight   (
    UserID int
    Grams int
    Measuretime DATETIME
    PRIMARY KEY (UserID,Measuretime)
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
)


create table Height   (
    UserID int
    dm int
    Measuretime DATETIME
    PRIMARY KEY (UserID,Measuretime)
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
)


create table Sleep   (
    UserID int
    Quality int
    Measuretime DATETIME
    PRIMARY KEY (UserID,Measuretime)
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
)


create table Water   (
    UserID int
    Mililitres int
    Measuretime DATETIME
    PRIMARY KEY (UserID,Measuretime)
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
)


create table Calories   (
    UserID int
    Grams int
    Measuretime DATETIME
    PRIMARY KEY (UserID,Measuretime)
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
)


