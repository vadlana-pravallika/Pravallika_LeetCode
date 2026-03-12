/* Write your PL/SQL query statement below */
select a.id, case
                when p_id is null then 'Root'
                when p_id is not null and a.id in (select b.p_id from tree b) then 'Inner'
                else
                   'Leaf' 
                end as type 
    from tree a;