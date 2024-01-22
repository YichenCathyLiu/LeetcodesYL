# Write your MySQL query statement below
delete p2 from Person p1, Person p2
where p1.Email = p2.Email and p2.id > p1.id; # 这是删除的条件。它指定了当两个记录的 Email 相同时，并且第二个记录（p2）的 id 大于第一个记录（p1）的 id 时，删除这些记录。这样做的目的是保留 id 较小的记录，而删除 id 较大且具有相同 Email 的记录，从而保留唯一的 Email 记录。