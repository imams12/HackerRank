/*
Enter your query here.
*/
SELECT DISTINCT CITY FROM STATION WHERE SUBSTRING(CITY,1,1) IN ('A','I','U','E','O') AND RIGHT(CITY,1) IN ('a','i','u','e','o')
