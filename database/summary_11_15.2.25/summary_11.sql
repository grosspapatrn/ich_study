# Вывести список сервисных классов со средней стоимостью билета в каждом классе.

select service_class , avg(price) over(partition by service_class) as avg_price
from tickets;

select service_class , avg(price) as avg_price
from tickets
group by service_class;


# Вывести список сервисных классов со средней ценой в каждом классе
# и ранком каждого класса в зависимости от средней цены в сервисном классе.

# USE airport;
SELECT service_class, ROUND(AVG(price),2) AS avg_price, DENSE_RANK() OVER(ORDER BY AVG(price) DESC) as class_rank
FROM tickets GROUP BY service_class;

select service_class , avg(price) as avg_price, RANK() OVER(ORDER BY avg(price) DESC)
from tickets
group by service_class;


use airport;

select service_class, avg(price) avg_price from tickets group by service_class;

# Вывести количество билетов для каждой поездки.

select trip_id, count(id) counted from tickets group by trip_id order by counted desc;


# Вывести топ 2 поездок (trips) по их средней стоимости билетов.

select trip_id, avg(price) from tickets group by trip_id;


select air.model_name, round(avg(tick.price), 2) avg_air_amount, row_number() over (order by avg(tick.price) desc) amount_rank
from airliners air left join trips tr on tr.airliner_id = air.id join tickets tick on tick.trip_id = tr.id group by air.model_name;


# Разбить все страны на 3 группы по средней продолжительности жизни,
# при этом указать количество городов в каждой стране, где это возможно.

use hr;

select first_name, last_name, salary from employees
where salary between 10000 and 20000;

