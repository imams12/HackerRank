/*
Enter your query here.
*/
SELECT h.hacker_id, h.name, COUNT(c.challenge_id) AS c_count FROM Hackers h
JOIN Challenges c ON h.hacker_id = c.hacker_id
GROUP BY h.hacker_id, h.name
HAVING c_count = ( SELECT MAX(temp1.cnt) FROM ( SELECT COUNT(hacker_id) AS cnt FROM Challenges GROUP BY hacker_id ORDER BY hacker_id ) AS temp1 )OR c_count IN ( SELECT temp2.cnt FROM ( SELECT COUNT(*) AS cnt FROM Challenges GROUP BY hacker_id ) AS temp2 GROUP BY temp2.cnt HAVING COUNT(temp2.cnt) = 1 )
ORDER BY c_count DESC, h.hacker_id;
