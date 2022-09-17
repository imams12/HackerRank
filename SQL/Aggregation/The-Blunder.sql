/*
Enter your query here.
*/
SELECT CEIL(AVG(Salary) - AVG(CONVERT(REPLACE(CAST(Salary as char),'0',''),UNSIGNED))) FROM EMPLOYEES
