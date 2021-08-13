CREATE VIEW ventas
AS SELECT com.name as nombre, cha.amount as cantidad, cha.created_at as fecha
FROM companies as com
INNER JOIN charges as cha ON com.id=cha.company_id
ORDER BY com.name;

CREATE VIEW ventas_diarias
AS SELECT nombre, SUM(cantidad), fecha FROM ventas
GROUP BY (fecha, nombre)
ORDER BY fecha;