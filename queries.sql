USE LifeScienceDB;

## List the name of authors whose research of interest is Immunology
SELECT DISTINCT a.Name
FROM Author a
JOIN AuthorField af ON a.AuthorID = af.AuthorID
JOIN BiomedicalField bf ON af.FieldID = bf.FieldID
WHERE bf.FieldName = 'Immunology';

## Who is the author with the most citations in 2023
-- NOTE: This requires CitationDate in Citation table; adjust if not present
SELECT a.Name, COUNT(*) AS CitationCount
FROM Citation c
JOIN Research cited ON c.CitedResearchID = cited.ResearchID
JOIN Research_Authors ra ON cited.ResearchID = ra.ResearchID
JOIN Author a ON ra.AuthorID = a.AuthorID
WHERE YEAR(c.CitationDate) = 2023
GROUP BY a.AuthorID
ORDER BY CitationCount DESC
LIMIT 1;

## List open access journals published by Springer
SELECT j.Name
FROM Journal j
JOIN Publisher p ON j.PublisherID = p.PublisherID
WHERE j.OpenAccess = 1
  AND p.Name = 'Springer';

## List all publications (research titles) by author 'Dr. Alice Smith'
SELECT r.Title, r.PublicationDate
FROM Research r
JOIN Research_Authors ra ON r.ResearchID = ra.ResearchID
JOIN Author a ON ra.AuthorID = a.AuthorID
WHERE a.Name = 'Dr. Alice Smith';

## List journals and their impact factors that publish research in 'Genetics and Genomics'
SELECT DISTINCT j.Name, j.ImpactFactor
FROM Journal j
JOIN JournalField jf ON j.ISSN = jf.ISSN
JOIN BiomedicalField bf ON jf.FieldID = bf.FieldID
WHERE bf.FieldName = 'Genetics and Genomics';

## Count how many research papers each author has published
SELECT a.Name, COUNT(ra.ResearchID) AS NumberOfPapers
FROM Author a
LEFT JOIN Research_Authors ra ON a.AuthorID = ra.AuthorID
GROUP BY a.AuthorID, a.Name
ORDER BY NumberOfPapers DESC;

## List publishers who accept 'Ebook' publication type
SELECT DISTINCT p.Name
FROM Publisher p
JOIN PublisherPublicationType ppt ON p.PublisherID = ppt.PublisherID
JOIN PublicationType pt ON ppt.TypeID = pt.TypeID
WHERE pt.TypeName = 'Ebook';

## List payment methods accepted by 'Nature Publishing Group'
SELECT pm.MethodName
FROM Publisher p
JOIN PublisherPaymentMethod ppm ON p.PublisherID = ppm.PublisherID
JOIN PaymentMethod pm ON ppm.MethodID = pm.MethodID
WHERE p.Name = 'Nature Publishing Group';
