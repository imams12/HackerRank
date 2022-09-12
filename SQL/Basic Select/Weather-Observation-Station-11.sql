/*
Enter your query here.
*/
SELECT DISTINCT CITY FROM STATION WHERE SUBSTRING(CITY,1,1) NOT IN ('A','I','U','E','O') OR RIGHT(CITY,1) NOT IN ('a','i','u','e','o')
