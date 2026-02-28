/* Write your PL/SQL query statement below */

select b.name department,a.name Employee, a.salary from employee a,department b
where a.departmentid=b.id
and a.salary = (select max(salary) from employee c where c.departmentid=a.departmentid)
order by a.name;
