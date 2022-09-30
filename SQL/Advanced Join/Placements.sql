/*
Enter your query here.
*/
SELECT s.Name FROM Students s
JOIN Friends f ON s.ID = f.ID
JOIN Packages p ON p.ID = f.Friend_ID
WHERE p.Salary > (SELECT p2.Salary FROM Packages p2 WHERE p2.ID = s.ID)
ORDER BY p.Salary;
