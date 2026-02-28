/* Write your PL/SQL query statement below */


select a.name employee from employee a, employee b
where b.id=a.managerid
and a.salary>b.salary;