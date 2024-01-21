# Write your MySQL query statement below
select *
from Patients
where substring(conditions,1,5)='DIAB1' or locate(' DIAB1',conditions)!=0