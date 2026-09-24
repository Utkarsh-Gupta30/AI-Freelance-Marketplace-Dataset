-- Creating view for summary table 
CREATE OR REPLACE VIEW project_summary_json AS
SELECT
    p.data->>'project_id' AS project_id,
    p.data->>'title' AS project_title,
    c.data->>'company_name' AS client_company,
    cat.data->>'category_name' AS category,
    (p.data->>'budget')::NUMERIC AS budget,
    p.data->>'project_status' AS project_status
FROM projects_json p
LEFT JOIN clients_json c
    ON p.data->>'client_id' = c.data->>'client_id'
LEFT JOIN categories_json cat
    ON p.data->>'category_id' = cat.data->>'category_id';

-- Testing view table
SELECT * FROM project_summary_json;


-- Freelancer Performance
CREATE OR REPLACE VIEW freelancer_performance_json AS
SELECT
    f.data->>'freelancer_id' AS freelancer_id,
    u.data->>'full_name' AS freelancer_name,
    (f.data->>'average_rating')::NUMERIC AS average_rating,
    (f.data->>'completed_projects')::INTEGER AS completed_projects,
    (f.data->>'hourly_rate')::NUMERIC AS hourly_rate
FROM freelancers_json f
JOIN users_json u
    ON f.data->>'user_id' = u.data->>'user_id';

-- Testing freelancer performance table
SELECT *
FROM freelancer_performance_json
ORDER BY average_rating DESC;