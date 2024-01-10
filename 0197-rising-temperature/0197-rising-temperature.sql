# Write your MySQL query statement below
select w2.id
from Weather w1
join Weather w2 # supportive form
ON DATEDIFF (w1.recordDate ,w2.recordDate) = -1
and w1.temperature < w2.temperature