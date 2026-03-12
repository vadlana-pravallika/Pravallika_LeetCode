/* Write your PL/SQL query statement below */
select distinct a.employee_id , case 
        when (select count(*) from employee c where  c.employee_id = a.employee_id ) >1 then 
        (select b. department_id from employee b where b.primary_flag ='Y' and b.employee_id = a.employee_id) 
        else 
          a.department_id
          end as department_id
from employee a;