create table User (
    UserID INT NOT NULL AUTO_INCREMENT,
    Sex VARCHAR(255),
    LastName VARCHAR(255) NOT NULL,
    FirstName VARCHAR(255) NOT NULL,
    mail VARCHAR(255),
    passwdhashandsalt VARCHAR(255) NOT NULL,
    isadmin BOOLEAN,
    PRIMARY KEY(UserID)
);

create table Steps (
    UserID INT,
    Steps INT,
    Measuretime DATETIME,
    FOREIGN KEY (UserID) REFERENCES User(UserID),
    PRIMARY KEY (UserID,Measuretime)
);

create table Bloodpressure (
    UserID INT,
    Systolic INT,
    Diastolic INT,
    Measuretime DATETIME,
    PRIMARY KEY (UserID,Measuretime),
    FOREIGN KEY (UserID) REFERENCES User(UserID)
);

create table Weight   (
    UserID INT,
    Grams INT,
    Measuretime DATETIME,
    PRIMARY KEY (UserID,Measuretime),
    FOREIGN KEY (UserID) REFERENCES User(UserID)
);

create table Height   (
    UserID INT,
    cm INT,
    Measuretime DATETIME,
    PRIMARY KEY (UserID,Measuretime),
    FOREIGN KEY (UserID) REFERENCES User(UserID)
);

create table Sleep   (
    UserID INT,
    Quality INT,
    Measuretime DATETIME,
    PRIMARY KEY (UserID,Measuretime),
    FOREIGN KEY (UserID) REFERENCES User(UserID)
);

create table Water   (
    UserID INT,
    Mililitres INT,
    Measuretime DATETIME,
    PRIMARY KEY (UserID,Measuretime),
    FOREIGN KEY (UserID) REFERENCES User(UserID)
);

create table Calories   (
    UserID INT,
    Grams INT,
    Measuretime DATETIME,
    PRIMARY KEY (UserID,Measuretime),
    FOREIGN KEY (UserID) REFERENCES User(UserID)
);

COMMIT;