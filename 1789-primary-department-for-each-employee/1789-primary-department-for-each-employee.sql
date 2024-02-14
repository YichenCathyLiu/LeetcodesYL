SELECT t1.employee_id, t1.department_id
FROM Employee t1
RIGHT JOIN Employee t2 ON t1.employee_id = t2.employee_id
GROUP BY t1.employee_id, t1.department_id
HAVING COUNT(t1.employee_id) = 1 OR MAX(t1.primary_flag) = 'Y';