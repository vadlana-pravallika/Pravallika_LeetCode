/* Write your PL/SQL query statement below */
select category,accounts_count from (
select 'Low Salary' category, (select count(*) from accounts where income<20000) as accounts_count from dual
union
select 'Average Salary' category, (select count(*) from accounts where income between 20000 and 50000) as accounts_count from dual
union
select 'High Salary' category, (select count(*) from accounts where income>50000) as accounts_count from dual)
order by accounts_count