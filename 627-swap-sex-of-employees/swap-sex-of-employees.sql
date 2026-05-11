/* Write your PL/SQL query statement below */
UPDATE  salary set sex = case 
                         when sex='m' then 'f'
                         when sex='f' then 'm'
                         end;