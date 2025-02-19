use hr;

SELECT employee_id, first_name, last_name, salary,department_id,
sum(salary) OVER (PARTITION BY department_id ORDER BY employee_id) AS relative_cumulative, -- относительная кумулятивная для департамента
sum(salary) OVER (PARTITION BY department_id) AS cumulative, -- кумулятивная для департамента
sum(salary) OVER (), -- общая для всей таблицы, но на каждой отдельной строке
sum(salary) OVER (PARTITION BY department_id ORDER BY employee_id) / sum(salary) OVER (PARTITION BY department_id) * 100 AS '%_of_total',
salary / sum(salary) OVER (PARTITION BY department_id) * 100 AS '%_of_total_individual' FROM employees;


-- Изменить предыдущий запрос таким образом, чтобы для каждого типа самолетов (model_name)
-- выводилось количество самолетов этого типа.

use airport;
select model_name, count(id) over(partition by model_name)
from airliners;

-- Вывести все уникальные значения моделей, их количество в таблице,  а так же общее число самолетов.

use airport;
select model_name, count(id), sum(count(id)) over()
from airliners
group by model_name;

SELECT *
FROM tickets;

SELECT client_id, cli.name, COUNT(tic.id) OVER(PARTITION BY client_id) AS summary
FROM tickets AS tic
LEFT JOIN clients AS cli ON tic.client_id = cli.id
ORDER BY summary DESC;