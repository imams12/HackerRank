/*
Solution 1
*/
SELECT IF(GRADE >= 8, NAME, 'NULL'), GRADE, MARKS FROM STUDENTS, GRADES WHERE MARKS BETWEEN MIN_MARK AND MAX_MARK ORDER BY GRADE DESC, NAME, MARKS;

/*
Solution 2
*/
SELECT
    CASE
        WHEN Grades.Grade < 8 THEN 'NULL'
        ELSE Students.Name
        END,
    Grades.Grade,
    Students.Marks    
FROM Students
LEFT JOIN Grades ON Students.Marks BETWEEN Grades.Min_Mark AND Grades.Max_Mark
ORDER BY Grades.Grade DESC, Students.Name
;
