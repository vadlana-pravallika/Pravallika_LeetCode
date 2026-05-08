/* Write your PL/SQL query statement below */
select day AS Day,round(nvl(sum(cancel)/sum(cnt),0),2) AS "Cancellation Rate" from(
select request_at day, null cancel, count(*) cnt
from trips a
where client_id in (select users_id from users where banned ='No')
  and driver_id in (select users_id from users where banned ='No')
  and request_at between '2013-10-01' AND '2013-10-03'
group by request_at
union
select request_at day, count(*) cancel, null cnt
from trips a
where client_id in (select users_id from users where banned ='No')
  and driver_id in (select users_id from users where banned ='No')
  and status <> 'completed'
  and request_at between '2013-10-01' AND '2013-10-03'
group by request_at)
group by day
order by day;


