/*
Enter your query here.
*/
SELECT CONCAT(Name,'(',LEFT(Occupation,1),')') FROM OCCUPATIONS ORDER BY Name ASC;
SELECT 'There are a total of', COUNT(Occupation), LOWER(CONCAT(Occupation,'s.')) FROM OCCUPATIONS GROUP BY Occupation ORDER BY COUNT(Occupation), Occupation ASC;
