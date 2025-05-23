## Create the database
CREATE DATABASE IF NOT EXISTS LifeScienceDB ;
## Use the database
USE LifeScienceDB;

## Publisher Table
CREATE TABLE `Publisher` (
    `PublisherID` INT PRIMARY KEY AUTO_INCREMENT,
    `Name` VARCHAR(255) NOT NULL
);

## Publication Type
CREATE TABLE `PublicationType` (
    `TypeID` INT PRIMARY KEY AUTO_INCREMENT,
    `TypeName` VARCHAR(50) UNIQUE NOT NULL ## e.g., Journal, Book, Ebook
);

## PublisherPublicationType
CREATE TABLE `PublisherPublicationType` (
    `PublisherID` INT,
    `TypeID` INT,
    PRIMARY KEY (`PublisherID`, `TypeID`),
    FOREIGN KEY (`PublisherID`) REFERENCES `Publisher`(`PublisherID`),
    FOREIGN KEY (`TypeID`) REFERENCES `PublicationType`(`TypeID`)
);

## Payment Methods
CREATE TABLE `PaymentMethod` (
    `MethodID` INT PRIMARY KEY AUTO_INCREMENT,
    `MethodName` VARCHAR(50) UNIQUE NOT NULL ## e.g., Cash, Bank Transfer
);

## PublisherPaymentMethod
CREATE TABLE `PublisherPaymentMethod` (
    `PublisherID` INT,
    `MethodID` INT,
    PRIMARY KEY (`PublisherID`, `MethodID`),
    FOREIGN KEY (`PublisherID`) REFERENCES `Publisher`(`PublisherID`),
    FOREIGN KEY (`MethodID`) REFERENCES `PaymentMethod`(`MethodID`)
);

## Biomedical Field
CREATE TABLE `BiomedicalField` (
    `FieldID` INT PRIMARY KEY AUTO_INCREMENT,
    `FieldName` VARCHAR(100) NOT NULL,
    `Description` TEXT
);

## Journal Table
CREATE TABLE `Journal` (
    `ISSN` VARCHAR(20) PRIMARY KEY,
    `Name` VARCHAR(255) NOT NULL,
    `ImpactFactor` DECIMAL(5,3),
    `Quarter` VARCHAR(10), ## Q1, Q2, Q3, Q4
    `PublisherID` INT,
    `Country` VARCHAR(100),
    `StartDate` DATE,
    `VolumePublicationRate` VARCHAR(20),
    `OpenAccess` TINYINT(1),
    FOREIGN KEY (`PublisherID`) REFERENCES `Publisher`(`PublisherID`)
);

## JournalField (Many-to-Many)
CREATE TABLE `JournalField` (
    `ISSN` VARCHAR(20),
    `FieldID` INT,
    PRIMARY KEY (`ISSN`, `FieldID`),
    FOREIGN KEY (`ISSN`) REFERENCES `Journal`(`ISSN`),
    FOREIGN KEY (`FieldID`) REFERENCES `BiomedicalField`(`FieldID`)
);

## Author Table
CREATE TABLE `Author` (
    `AuthorID` INT PRIMARY KEY AUTO_INCREMENT,
    `Name` VARCHAR(100) NOT NULL,
    `Qualification` VARCHAR(100),
    `Affiliation` VARCHAR(255),
    `JobTitle` VARCHAR(100),
    `Email` VARCHAR(100),
    `HIndex` INT
);

## AuthorField (Many-to-Many)
CREATE TABLE `AuthorField` (
    `AuthorID` INT,
    `FieldID` INT,
    PRIMARY KEY (`AuthorID`, `FieldID`),
    FOREIGN KEY (`AuthorID`) REFERENCES `Author`(`AuthorID`),
    FOREIGN KEY (`FieldID`) REFERENCES `BiomedicalField`(`FieldID`)
);

## Research Table
CREATE TABLE `Research` (
    `ResearchID` INT PRIMARY KEY AUTO_INCREMENT,
    `Title` VARCHAR(255) NOT NULL,
    `Abstract` TEXT,
    `PublicationDate` DATE,
    `FieldID` INT,
    `JournalISSN` VARCHAR(20),
    FOREIGN KEY (`FieldID`) REFERENCES `BiomedicalField`(`FieldID`),
    FOREIGN KEY (`JournalISSN`) REFERENCES `Journal`(`ISSN`)
);

## Research_Authors (Many-to-Many)
CREATE TABLE `Research_Authors` (
    `ResearchID` INT,
    `AuthorID` INT,
    PRIMARY KEY (`ResearchID`, `AuthorID`),
    FOREIGN KEY (`ResearchID`) REFERENCES `Research`(`ResearchID`) ON DELETE CASCADE,
    FOREIGN KEY (`AuthorID`) REFERENCES `Author`(`AuthorID`) ON DELETE CASCADE
);

## Citation Table (Self-referencing Many-to-Many)
CREATE TABLE `Citation` (
    `CitingResearchID` INT,
    `CitedResearchID` INT,
    PRIMARY KEY (`CitingResearchID`, `CitedResearchID`),
    FOREIGN KEY (`CitingResearchID`) REFERENCES `Research`(`ResearchID`) ON DELETE CASCADE,
    FOREIGN KEY (`CitedResearchID`) REFERENCES `Research`(`ResearchID`) ON DELETE CASCADE
);


