CREATE TEMP TABLE emp_dataset AS
SELECT 
    e.employee_id,
    e.employee_name,
    e.GEN,
    e.age,
    s.date,
    s.salary,
    f.function_group,
    c.company_name,
    c.company_city,
    c.company_state,
    c.company_type,
    c.const_site_category
FROM 
    salaries s
LEFT JOIN 
    employees e ON s.employee_id = e.employee_id
LEFT JOIN 
    functions f ON s.function_code = f.function_code
LEFT JOIN 
    companies c ON s.company_name = c.company_name
    
    
    
CREATE TABLE df_employee AS
SELECT 
    employee_id || '_' || CAST(date AS TEXT) AS id,
    DATE(date) AS month_year,
    employee_id,
    employee_name,
    GEN,
    age,
    salary,
    function_group,
    company_name,
    company_city,
    company_state,
    company_type,
    const_site_category
FROM 
    emp_dataset;