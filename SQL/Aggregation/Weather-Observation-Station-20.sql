/*
Enter your query here.
*/
SELECT FLOOR(COUNT(ID)/2+0.5) INTO @F FROM STATION; 
SELECT CEILING(COUNT(ID)/2+0.5) INTO @C FROM STATION;
SELECT ROUND(AVG(LAT_N), 4) FROM (SELECT ROW_NUMBER() OVER () AS r, LAT_N FROM STATION ORDER BY LAT_N) temp WHERE r in (@F, @C);
