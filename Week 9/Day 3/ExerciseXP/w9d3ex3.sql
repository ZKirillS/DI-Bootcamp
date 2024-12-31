SELECT 
	company_name,
    COUNT(DISTINCT employee_id) AS employee_per_company
FROM df_employee
GROUP BY company_name
ORDER BY employee_per_company DESC



