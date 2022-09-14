/*
Enter your query here.
*/
SELECT c.company_code, c.founder, COUNT(DISTINCT lm.lead_manager_code), COUNT(DISTINCT sm.senior_manager_code), COUNT(DISTINCT m.manager_code), COUNT(DISTINCT e.employee_code) FROM Company c, Lead_Manager lm, Senior_manager sm, Manager m, Employee e
WHERE c.company_code = lm.company_code AND lm.lead_manager_code = sm.lead_manager_code AND sm.senior_manager_code = m.senior_manager_code AND m.manager_code = e.manager_code GROUP BY c.company_code, c.founder
ORDER BY c.company_code;
