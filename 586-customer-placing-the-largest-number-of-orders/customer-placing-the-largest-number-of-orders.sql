/* Write your PL/SQL query statement below  

select customer_number,  row_number() over (order by count(*) desc) r from orders group by  customer_number  */
select customer_number from(
select  rownum sl,customer_number from (
select customer_number,count(customer_number) cnt from orders
group by customer_number
order by cnt desc))
where sl=1; 





