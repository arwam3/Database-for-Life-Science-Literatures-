USE LifeScienceDB;

## View: Authors interested in Immunology
CREATE VIEW View_Authors_Immunology AS
SELECT DISTINCT a.AuthorID, a.Name, a.Email, a.Affiliation
FROM Author a
JOIN AuthorField af ON a.AuthorID = af.AuthorID
JOIN BiomedicalField bf ON af.FieldID = bf.FieldID
WHERE bf.FieldName = 'Immunology';

## View: Open Access Journals published by Springer
CREATE VIEW View_OpenAccess_Journals_Springer AS
SELECT j.ISSN, j.Name AS JournalName, p.Name AS PublisherName, j.ImpactFactor, j.Country
FROM Journal j
JOIN Publisher p ON j.PublisherID = p.PublisherID
WHERE j.OpenAccess = 1 AND p.Name = 'Springer';

## View: Author citation counts (total citations received)
CREATE VIEW View_Author_Citation_Counts AS
SELECT a.AuthorID, a.Name, COUNT(*) AS TotalCitations
FROM Author a
JOIN Research_Authors ra ON a.AuthorID = ra.AuthorID
JOIN Citation c ON ra.ResearchID = c.CitedResearchID
GROUP BY a.AuthorID, a.Name
ORDER BY TotalCitations DESC;

## View: Research and their Authors (for easy lookup)
CREATE VIEW View_Research_Authors AS
SELECT r.ResearchID, r.Title, a.AuthorID, a.Name AS AuthorName
FROM Research r
JOIN Research_Authors ra ON r.ResearchID = ra.ResearchID
JOIN Author a ON ra.AuthorID = a.AuthorID;

## View: List all journals with their biomedical fields
CREATE VIEW View_Journal_BiomedicalFields AS
SELECT j.ISSN, j.Name AS JournalName, bf.FieldName
FROM Journal j
JOIN JournalField jf ON j.ISSN = jf.ISSN
JOIN BiomedicalField bf ON jf.FieldID = bf.FieldID;
