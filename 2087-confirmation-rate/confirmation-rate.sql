/* Write your PL/SQL query statement below */
SELECT a.user_id,
       nvl(round((SELECT COUNT(*)
          FROM confirmations b
         WHERE a.user_id = b.user_id
           AND b.action = 'confirmed')
       /
       nullif(
           (SELECT COUNT(*)
              FROM confirmations b
             WHERE a.user_id = b.user_id),0
           
       ),2) ,0) AS confirmation_rate
FROM signups a;