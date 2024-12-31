SELECT 
    MIN(total_employees) AS min_employees, 
    MAX(total_employees) AS max_employees,
    (SELECT strftime('%Y-%m', date) 
     FROM df_employee2 
     GROUP BY strftime('%Y-%m', date)
     HAVING COUNT(DISTINCT employee_id) = MIN(total_employees)
    ) AS min_month,
    (SELECT strftime('%Y-%m', date) 
     FROM df_employee2 
     GROUP BY strftime('%Y-%m', date)
     HAVING COUNT(DISTINCT employee_id) = MAX(total_employees)
    ) AS max_month
FROM (
    SELECT 
        strftime('%Y-%m', date) AS month, 
        COUNT(DISTINCT employee_id) AS total_employees
    FROM 
        df_employee2
    GROUP BY 
        strftime('%Y-%m', date)
) monthly_totals




SELECT 
    strftime('%Y-%m', date) AS month, 
    function_group, 
    COUNT(DISTINCT employee_id) AS total_employees,
    AVG(COUNT(DISTINCT employee_id)) OVER(PARTITION BY function_group, strftime('%Y-%m', date)) AS average_employees
FROM 
    df_employee2
GROUP BY 
    strftime('%Y-%m', date), function_group
ORDER BY 
    month, function_group;



SELECT 
    ROUND(AVG(salary), 2) AS annual_average_salary
FROM 
    df_employee2