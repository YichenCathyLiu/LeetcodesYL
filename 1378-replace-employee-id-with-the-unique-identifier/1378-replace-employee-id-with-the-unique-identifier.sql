# Write your MySQL query statement below
select Employees.name, EmployeeUNI.unique_id
from Employees left join EmployeeUNI # use left join here: let EmployeeUNI join Employees from left!!!
on Employees.id = EmployeeUNI.id