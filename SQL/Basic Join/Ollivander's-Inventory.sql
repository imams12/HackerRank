/*
Enter your query here.
*/
SELECT w.id, wp.age, w.coins_needed, w.power FROM Wands w 
JOIN Wands_Property wp ON w.code = wp.code
WHERE wp.is_evil = 0 AND w.coins_needed = (SELECT MIN(coins_needed) FROM Wands w1 JOIN wands_property wp1 ON w1.code = wp1.code WHERE w1.power = w.power AND wp1.age = wp.age)
ORDER BY w.power DESC, wp.age DESC;
