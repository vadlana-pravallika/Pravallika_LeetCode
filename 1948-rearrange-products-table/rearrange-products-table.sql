/* Write your PL/SQL query statement below */
select product_id , store, price from(
select product_id, 'store1' store, store1 price from products
union
select product_id, 'store2' store, store2 price from products
union
select product_id, 'store3' store, store3 price from products
)
where price is not null