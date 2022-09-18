/*
Enter your query here.
*/
SELECT MAX(salary * months), COUNT(salary * months) FROM Employee GROUP BY salary * months ORDER BY salary * months DESC limit 1
