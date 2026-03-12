/* Write your PL/SQL query statement below */
select teacher_id,count(subject_id) cnt from(
select  distinct(subject_id) subject_id,teacher_id  from teacher)
group by teacher_id;