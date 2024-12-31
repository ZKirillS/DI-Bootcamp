SELECT 
	company_city,
    COUNT(DISTINCT employee_id) AS employee_per_city
    ROUND((COUNT(DISTINCT employee_id) * 100.0)/ SUM(COUNT(DISTINCT employee_id)) OVER(), 2)
FROM df_employee
GROUP BY company_city
ORDER BY employee_per_city DESC

SELECT 
    strftime('%Y-%m', date) AS month, 
    COUNT(DISTINCT employee_id) AS total_employees
FROM 
    df_employee2
GROUP BY 
    strftime('%Y-%m', date)
ORDER BY 
    month

SELECT 
    ROUND(AVG(total_employees), 2) AS average_employees
FROM (
    SELECT 
        strftime('%Y-%m', date) AS month, 
        COUNT(DISTINCT employee_id) AS total_employees
    FROM 
        df_employee2
    GROUP BY 
        strftime('%Y-%m', date)
) monthly_totals
