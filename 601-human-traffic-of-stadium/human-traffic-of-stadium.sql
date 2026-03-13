/* Write your PL/SQL query statement below */
select 
    id, 
    to_char(visit_date, 'yyyy-mm-dd') visit_date, 
    people
from (
    select
        id, 
        visit_date, 
        people,
        count(*) over(partition by id_group) rowcnt
    from (
        select 
            s.*,
            id - rank() over(order by id) id_group
        from stadium s 
        where people >= 100
    )
)
where rowcnt >= 3
order by 2