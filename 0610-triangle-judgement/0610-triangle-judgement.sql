# Write your MySQL query statement below
# case 的用法：有点像if和switch
select x, y, z,
    case when abs(x-y) < z and z < x+y then 'Yes' # case when then else end
    else 'No' end triangle
from Triangle