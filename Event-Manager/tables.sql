CREATE TABLE Event
(
    Event_id INT PRIMARY KEY NOT NULL,
    Name VARCHAR(100),
    Location TEXT(500),
    Date DATE,
    Start_time TIME,
    End_time TIME,
    Event_type TEXT(500),
    Profits_expected BIGINT,
    Profits_gained BIGINT
);
CREATE TABLE City_details
(
    City VARCHAR(100) PRIMARY KEY,
    Zip_Code INT ,
    State VARCHAR(100)
);
CREATE TABLE Time
(
    Event_id INT ,
    Duration FLOAT,
    PRIMARY KEY (`Event_id`),
    FOREIGN KEY (`Event_id`) REFERENCES `EVENT` (`Event_id`) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE Employee
(
    Employee_id INT PRIMARY KEY NOT NULL,
    Name VARCHAR(100),
    Building_Name VARCHAR(100),
    Street VARCHAR(100) ,
    City VARCHAR(100),
    Contact_Number VARCHAR(15),
    Email_id VARCHAR(50),
    Work_Role VARCHAR(100),
    FOREIGN KEY (`City`) REFERENCES `City_details` (`City`) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Hourly_Employee
(
    Employee_id INT NOT NULL,
    Pay_scale INT,
    PRIMARY KEY (`Employee_id`),
    FOREIGN KEY (`Employee_id`) REFERENCES `EMPLOYEE` (`Employee_id`) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE Salaried_Employee
(
    Employee_id INT NOT NULL,
    Salary INT,
    PRIMARY KEY (`Employee_id`),
    FOREIGN KEY (`Employee_id`) REFERENCES `EMPLOYEE` (`Employee_id`) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE Employee_Events
(
    Event_id INT NOT NULL,
    Employee_id INT  NOT NULL,
    PRIMARY KEY (`Event_id`,`Employee_id`),
    FOREIGN KEY (`Employee_id`) REFERENCES `EMPLOYEE` (`Employee_id`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (`Event_id`) REFERENCES `EVENT` (`Event_id`) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE Spectators
(
    Name VARCHAR(100),
    Ticket_Number INT,
    Contact_Number VARCHAR(15),
    Event_id INT,
    PRIMARY KEY (`Event_id`,`Ticket_Number`),
    FOREIGN KEY (`Event_id`) REFERENCES `EVENT` (`Event_id`) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE Admin
(
    Name VARCHAR(100),
    Contact_Number VARCHAR(15) PRIMARY KEY NOT NULL,
    Building_Name VARCHAR(100),
    Street VARCHAR(100),
    City VARCHAR(100),
    Date_of_Birth DATE,
    Email_Id VARCHAR(50),
    Event_id INT,
    Salary INT,
    Number_Of_Employees_working_under INT,
    FOREIGN KEY (`Event_id`) REFERENCES `EVENT` (`Event_id`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (`City`) REFERENCES `City_details` (`City`) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE Admin_age
(
    Contact_Number VARCHAR(15) PRIMARY KEY NOT NULL,
    Age INT,
    FOREIGN KEY (`Contact_Number`) REFERENCES `Admin` (`Contact_Number`) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE Equipments
(
    Equipment_id INT PRIMARY KEY NOT NULL,
    Name VARCHAR(100),
    Availability BOOLEAN,
    Quantity INT,
    Cost INT
);
CREATE TABLE Equipments_events
(
    Equipment_id INT ,
    Event_id INT ,
    FOREIGN KEY (`Equipment_id`) REFERENCES `Equipments` (`Equipment_id`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (`Event_id`) REFERENCES `EVENT` (`Event_id`) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE Equip_Role
(
    Equipment_id INT PRIMARY KEY NOT NULL,
    Role TEXT(1000),
    FOREIGN KEY (`Equipment_id`) REFERENCES `Equipments` (`Equipment_id`) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Relates
(
    Event_id INT ,
    Performer_id INT ,
    Name_of_Performance VARCHAR(100) ,
    Equipment_id INT ,
    Employee_id INT ,
    Owner_Name VARCHAR(100) ,
    Company_Name VARCHAR(100) ,
    PRIMARY KEY (`Event_id`,`Performer_id` , `Name_of_Performance`,`Employee_id`,`Owner_Name` , `Company_Name`),
    FOREIGN KEY (`Event_id`) REFERENCES `Event` (`Event_id`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (`Equipment_id`) REFERENCES `Equipments` (`Equipment_id`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (`Employee_id` ) REFERENCES `Employee` (`Employee_id`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (`Performer_id` ) REFERENCES `Performers` (`Performer_id`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (`Owner_Name` , `Company_Name`) REFERENCES `Partners` (`Owner_Name` , `Company_Name`) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE Partners
(
    Owner_Name VARCHAR(100) NOT NULL,
    Company_Name VARCHAR(100) NOT NULL,
    Building_Name VARCHAR(100),
    Street VARCHAR(100),
    City VARCHAR(100),
    PRIMARY KEY(`Owner_Name` , `Company_Name`),
    FOREIGN KEY (`City`) REFERENCES `City_details` (`City`) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE Partner_payment
(
    Event_id INT NOT NULL,
    Owner_Name VARCHAR(100) NOT NULL,
    Company_Name VARCHAR(100) NOT NULL,
    Payment_details INT,
    PRIMARY KEY (`Event_id`,`Owner_Name`,`Company_Name`),
    FOREIGN KEY (`Event_id`) REFERENCES `EVENT` (`Event_id`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (`Owner_Name`,`Company_Name`) REFERENCES `Partners` (`Owner_Name`,`Company_Name`) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE Role
(
    Event_id INT NOT NULL,
    Owner_Name VARCHAR(100) NOT NULL,
    Company_Name VARCHAR(100) NOT NULL,
    Partner_role VARCHAR(100),
    PRIMARY KEY (`Event_id`,`Owner_Name`,`Company_Name`),
    FOREIGN KEY (`Event_id`) REFERENCES `EVENT` (`Event_id`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (`Owner_Name`,`Company_Name`) REFERENCES `Partners` (`Owner_Name`,`Company_Name`) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE Performers
(
    Name VARCHAR(100),
    Contact_Number VARCHAR(15),
    Building_Name VARCHAR(100),
    Street VARCHAR(100),
    City VARCHAR(100),
    Date_of_Birth DATE,
    Performer_id INT PRIMARY KEY NOT NULL,
    FOREIGN KEY (`City`) REFERENCES `City_details` (`City`) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE Performer_events
(
    Performer_id INT  NOT NULL,
    Event_id INT  NOT NULL,
    PRIMARY KEY(`Performer_id`,`Event_id`),
    FOREIGN KEY (`Performer_id`) REFERENCES `Performers` (`Performer_id`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (`Event_id`) REFERENCES `EVENT` (`Event_id`) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE Performance
(
    Performer_id INT ,
    Name_of_Performance VARCHAR(100),
    Number_of_Performers INT,
    Payment_amount INT,
    Equipment_id INT,
    PRIMARY KEY (`Performer_id`,`Name_of_Performance`),
    FOREIGN KEY (`Performer_id`) REFERENCES `Performers` (`Performer_id`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (`Equipment_id`) REFERENCES `Equipments` (`Equipment_id`) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE Performer_age
(
    Age INT,
    Performer_id INT PRIMARY KEY NOT NULL,
    FOREIGN KEY (`Performer_id`) REFERENCES `Performers` (`Performer_id`) ON DELETE CASCADE ON UPDATE CASCADE
);
