/*
Enter your query here.
*/
SELECT t.id,
       t.name,
       sum(t.total)
FROM
(SELECT h.hacker_id AS id,
       h.name AS name,
       MAX(s.score) AS total
FROM Hackers h
JOIN Submissions s ON h.hacker_id = s.hacker_id
GROUP BY id, name, s.challenge_id) AS t
GROUP BY t.id, t.name
HAVING sum(t.total) > 0 
ORDER BY sum(t.total) DESC, t.id ASC;
