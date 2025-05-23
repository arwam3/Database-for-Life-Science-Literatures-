USE LifeScienceDB;

## BiomedicalField (at least 10)
INSERT INTO BiomedicalField (FieldName, Description) VALUES
('Genetics and Genomics', 'Study of genes and their functions.'),
('Immunology', 'Study of the immune system.'),
('Cell and Developmental Biology', 'Study of cell structure and function.'),
('Neuroscience', 'Study of the nervous system.'),
('Biochemistry', 'Study of chemical processes in living organisms.'),
('Pharmacology', 'Study of drug action.'),
('Microbiology', 'Study of microorganisms.'),
('Molecular Biology', 'Study of biology at molecular level.'),
('Pathology', 'Study of disease causes and effects.'),
('Physiology', 'Study of body functions.');

## Publisher (10 rows)
INSERT INTO Publisher (Name) VALUES
('Nature Publishing Group'),
('Elsevier'),
('Springer'),
('Wiley-Blackwell'),
('Taylor & Francis'),
('Oxford University Press'),
('Cambridge University Press'),
('American Chemical Society'),
('IEEE'),
('PLOS');

## PublicationType (3 rows)
INSERT INTO PublicationType (TypeName) VALUES
('Journal'),
('Book'),
('Ebook');

## PublisherPublicationType (link publishers and types, at least 10 rows)
INSERT INTO PublisherPublicationType (PublisherID, TypeID) VALUES
(1, 1),
(1, 3),
(2, 1),
(2, 2),
(3, 1),
(4, 1),
(5, 2),
(6, 1),
(7, 3),
(8, 1);

## PaymentMethod (at least 5)
INSERT INTO PaymentMethod (MethodName) VALUES
('Cash'),
('Bank Transfer'),
('Online Payment'),
('Credit Card'),
('Cheque');

## PublisherPaymentMethod (link publishers and payment methods, at least 10)
INSERT INTO PublisherPaymentMethod (PublisherID, MethodID) VALUES
(1, 1),
(1, 3),
(2, 2),
(2, 4),
(3, 3),
(4, 1),
(4, 2),
(5, 4),
(6, 5),
(7, 3);

## Journal (at least 10 journals)
INSERT INTO Journal (ISSN, Name, ImpactFactor, Quarter, PublisherID, Country, StartDate, VolumePublicationRate, OpenAccess) VALUES
('JNL001', 'Genetics Today', 5.23, 'Q1', 1, 'USA', '2001-01-01', 'Monthly', 1),
('JNL002', 'ImmunoReview', 4.85, 'Q2', 2, 'UK', '1995-05-01', 'Quarterly', 1),
('JNL003', 'Cell Insights', 3.75, 'Q2', 3, 'Germany', '2010-03-15', 'Monthly', 0),
('JNL004', 'NeuroScience World', 4.10, 'Q1', 4, 'USA', '2005-06-01', 'Bi-monthly', 1),
('JNL005', 'BioChem Research', 3.50, 'Q3', 5, 'Canada', '2000-07-20', 'Quarterly', 0),
('JNL006', 'Pharma Today', 3.20, 'Q4', 6, 'USA', '2012-01-10', 'Monthly', 1),
('JNL007', 'Microbial Life', 2.85, 'Q3', 7, 'UK', '1998-09-05', 'Bi-monthly', 0),
('JNL008', 'Molecular Biology Journal', 4.95, 'Q1', 8, 'USA', '2003-11-11', 'Monthly', 1),
('JNL009', 'Pathology Reports', 3.60, 'Q4', 9, 'USA', '2007-02-14', 'Quarterly', 0),
('JNL010', 'Physiology Letters', 3.80, 'Q2', 10, 'Netherlands', '2015-05-21', 'Monthly', 1);

## JournalField (link journals to biomedical fields, at least 10)
INSERT INTO JournalField (ISSN, FieldID) VALUES
('JNL001', 1),
('JNL002', 2),
('JNL003', 3),
('JNL004', 4),
('JNL005', 5),
('JNL006', 6),
('JNL007', 7),
('JNL008', 8),
('JNL009', 9),
('JNL010', 10);

## Author (at least 10 authors)
INSERT INTO Author (Name, Qualification, Affiliation, JobTitle, Email, HIndex) VALUES
('Dr. Alice Smith', 'PhD in Genetics', 'Harvard University', 'Professor', 'alice.smith@harvard.edu', 45),
('Dr. Bob Johnson', 'MD', 'Stanford University', 'Researcher', 'bob.johnson@stanford.edu', 38),
('Dr. Clara Davis', 'PhD in Immunology', 'Oxford University', 'Lecturer', 'clara.davis@ox.ac.uk', 30),
('Dr. Daniel Lee', 'PhD', 'MIT', 'Scientist', 'daniel.lee@mit.edu', 50),
('Dr. Emma Wilson', 'PhD in Microbiology', 'UCLA', 'Assistant Professor', 'emma.wilson@ucla.edu', 28),
('Dr. Frank Harris', 'MD', 'Johns Hopkins', 'Senior Researcher', 'frank.harris@jh.edu', 40),
('Dr. Grace Kim', 'PhD in Neuroscience', 'Yale University', 'Lecturer', 'grace.kim@yale.edu', 35),
('Dr. Henry Clark', 'PhD', 'Cambridge University', 'Scientist', 'henry.clark@cam.ac.uk', 42),
('Dr. Isabella Moore', 'PhD in Biochemistry', 'UCSF', 'Professor', 'isabella.moore@ucsf.edu', 37),
('Dr. Jack Martinez', 'PhD', 'Imperial College', 'Research Fellow', 'jack.martinez@imperial.ac.uk', 29);

## AuthorField (link authors to biomedical fields, at least 10)
INSERT INTO AuthorField (AuthorID, FieldID) VALUES
(1, 1),
(2, 1),
(3, 2),
(4, 4),
(5, 7),
(6, 2),
(7, 4),
(8, 3),
(9, 5),
(10, 8);

## Research (at least 10 research papers)
INSERT INTO Research (Title, Abstract, PublicationDate, FieldID, JournalISSN) VALUES
('Gene Editing Techniques', 'A study on CRISPR-Cas9 and gene therapies.', '2023-01-15', 1, 'JNL001'),
('Immune System Disorders', 'Analysis of autoimmune diseases.', '2023-03-22', 2, 'JNL002'),
('Cell Growth and Differentiation', 'Insights into cell development.', '2022-12-10', 3, 'JNL003'),
('Neural Networks and Brain Functions', 'Understanding nervous system.', '2023-04-05', 4, 'JNL004'),
('Biochemical Pathways in Metabolism', 'Study of metabolic processes.', '2023-02-19', 5, 'JNL005'),
('New Drug Delivery Methods', 'Advances in pharmacology.', '2022-11-11', 6, 'JNL006'),
('Microbial Resistance Mechanisms', 'How microbes resist antibiotics.', '2023-01-28', 7, 'JNL007'),
('Molecular Biology of Cancer', 'Cancer on molecular level.', '2023-05-02', 8, 'JNL008'),
('Pathology of Infectious Diseases', 'Study of disease pathology.', '2022-10-15', 9, 'JNL009'),
('Physiology of Exercise', 'Impact of exercise on body.', '2023-03-29', 10, 'JNL010');

## Research_Authors (link research and authors, at least 10)
INSERT INTO Research_Authors (ResearchID, AuthorID) VALUES
(1, 1),
(1, 2),
(2, 3),
(2, 6),
(3, 8),
(4, 4),
(4, 7),
(5, 9),
(6, 6),
(7, 5),
(8, 10),
(9, 6),
(10, 7);

## Citation (at least 10 citations)
INSERT INTO Citation (CitingResearchID, CitedResearchID) VALUES
(2, 1),
(3, 1),
(4, 2),
(5, 3),
(6, 5),
(7, 6),
(8, 7),
(9, 8),
(10, 9),
(1, 10);
