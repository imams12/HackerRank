/*
Enter your query here.
*/
SELECT DISTINCT a.x,a.y
FROM Functions a, Functions b
WHERE a.y = b.x AND a.x = b.y AND a.x <= a.y 
GROUP BY a.x,a.y
HAVING COUNT(*) > 1 OR ( a.x <> a.y )
ORDER BY a.x
