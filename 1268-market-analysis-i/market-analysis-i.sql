select user_id as buyer_id, to_char(trunc(join_date), 'yyyy-mm-dd') as join_date, 
case when orders_in_2019 is null then 0 
else orders_in_2019 end as orders_in_2019 from users u 
left join 
(select buyer_id, count(*) orders_in_2019 from orders 
where order_date between '2019-01-01' and '2019-12-31' group by buyer_id) tbl 
on u.user_id = tbl.buyer_id
order by buyer_id