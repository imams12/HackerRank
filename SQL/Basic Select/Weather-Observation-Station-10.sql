/*
Enter your query here.
*/
SELECT DISTINCT CITY FROM STATION WHERE RIGHT(CITY,1) NOT IN ('a','i','u','e','o')
