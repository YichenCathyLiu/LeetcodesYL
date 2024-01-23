# Write your MySQL query statement below
select sell_date, count(DISTINCT product) as num_sold,
Group_concat(Distinct product order by product) as products # group_concat
from Activities
group by sell_date;