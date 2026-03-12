/* Write your PL/SQL query statement below */
select substr(transaction_date,1,11) transaction_date, sum(nvl(odd,0)) odd_sum,sum(nvl(even,0)) even_sum from (
select transaction_date, case when mod(amount,2)=1 then amount else null end as odd,  case when mod(amount,2)=0 then amount else null end as even from transactions)
group by transaction_date
order by 1;