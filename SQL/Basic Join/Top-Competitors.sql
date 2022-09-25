/*
Solution 1
*/
SELECT h.hacker_id, h.name FROM hackers h
JOIN Submissions s ON h.hacker_id = s.hacker_id
JOIN Challenges c ON s.challenge_id = c.challenge_id
JOIN Difficulty d ON c.difficulty_level = d.difficulty_level
WHERE s.score = d.score
GROUP BY h.hacker_id, h.name
HAVING COUNT(h.hacker_id) > 1
ORDER BY COUNT(h.hacker_id) DESC, h.hacker_id;


/*
Solution 2
*/
SELECT h.hacker_id, h.name FROM Submissions s, Difficulty d, Challenges c, Hackers h  
WHERE s.hacker_id = h.hacker_id AND s.challenge_id = c.challenge_id AND d.difficulty_level = c.difficulty_level AND s.score = d.score
GROUP BY h.hacker_id, h.name
HAVING COUNT(s.challenge_id) > 1
ORDER BY COUNT(s.challenge_id) DESC, h.hacker_id;
