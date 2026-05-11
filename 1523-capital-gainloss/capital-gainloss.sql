/* Write your PL/SQL query statement below */
select stock_name, sum(sell) - sum(buy)  as capital_gain_loss from
(
select stock_name,sum(Price) as sell  , null as buy
from stocks
where operation='Sell'
group by stock_name
union
select stock_name,null as sell  , sum(Price) as buy
from stocks
where operation='Buy'
group by stock_name)
group by stock_name