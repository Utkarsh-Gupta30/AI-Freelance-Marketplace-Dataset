-- Display users
SELECT
    data->>'user_id' AS user_id,
    data->>'full_name' AS full_name,
    data->>'email' AS email,
    data->>'role' AS role
FROM users_json;


-- Find freelancers
SELECT
    data->>'user_id' AS user_id,
    data->>'full_name' AS name,
    data->>'city' AS city
FROM users_json
WHERE data->>'role' = 'Freelancer';


-- Projects above a budget
SELECT
    data->>'project_id' AS project_id,
    data->>'title' AS project_title,
    (data->>'budget')::NUMERIC AS budget
FROM projects_json
WHERE (data->>'budget')::NUMERIC > 50000;


-- High-rated freelancers
SELECT
    data->>'freelancer_id' AS freelancer_id,
    data->>'headline' AS headline,
    (data->>'average_rating')::NUMERIC AS rating
FROM freelancers_json
WHERE (data->>'average_rating')::NUMERIC >= 4.5;


-- Multi-table JOIN

-- Projects with client company
SELECT
    p.data->>'project_id' AS project_id,
    p.data->>'title' AS project_title,
    c.data->>'company_name' AS company_name
FROM projects_json p
JOIN clients_json c
    ON p.data->>'client_id' = c.data->>'client_id';


-- Bigger JOIN

-- Projects + categories + clients
SELECT
    p.data->>'project_id' AS project_id,
    p.data->>'title' AS project_title,
    c.data->>'company_name' AS company_name,
    cat.data->>'category_name' AS category
FROM projects_json p
JOIN clients_json c
    ON p.data->>'client_id' = c.data->>'client_id'
JOIN categories_json cat
    ON p.data->>'category_id' = cat.data->>'category_id';


-- Freelancer + skills
SELECT
    f.data->>'freelancer_id' AS freelancer_id,
    u.data->>'full_name' AS freelancer_name,
    s.data->>'skill_name' AS skill
FROM freelancers_json f
JOIN users_json u
    ON f.data->>'user_id' = u.data->>'user_id'
JOIN freelancer_skills_json fs
    ON f.data->>'freelancer_id' = fs.data->>'freelancer_id'
JOIN skills_json s
    ON fs.data->>'skill_id' = s.data->>'skill_id';


-- GROUP BY / HAVING

-- Count proposals for every project
SELECT
    p.data->>'project_id' AS project_id,
    p.data->>'title' AS project_title,
    COUNT(pr.record_id) AS proposal_count
FROM projects_json p
JOIN proposals_json pr
    ON p.data->>'project_id' = pr.data->>'project_id'
GROUP BY
    p.data->>'project_id',
    p.data->>'title'
HAVING COUNT(pr.record_id) >= 5
ORDER BY proposal_count DESC;


-- Aggregate query

-- Average freelancer rating
SELECT
    ROUND(AVG((data->>'average_rating')::NUMERIC), 2)
        AS average_freelancer_rating
FROM freelancers_json;

-- Maximum hourly rate
SELECT
    MAX((data->>'hourly_rate')::NUMERIC) AS maximum_hourly_rate
FROM freelancers_json;


-- Correlated subquery

-- Find freelancers whose hourly rate is higher than the average hourly rate
SELECT
    f.data->>'freelancer_id' AS freelancer_id,
    f.data->>'headline' AS headline,
    (f.data->>'hourly_rate')::NUMERIC AS hourly_rate
FROM freelancers_json f
WHERE (f.data->>'hourly_rate')::NUMERIC >
(
    SELECT AVG((f2.data->>'hourly_rate')::NUMERIC)
    FROM freelancers_json f2
);

-- Find projects whose budget is greater than the average project budget
SELECT
    data->>'project_id' AS project_id,
    data->>'title' AS project_title,
    (data->>'budget')::NUMERIC AS budget
FROM projects_json
WHERE (data->>'budget')::NUMERIC >
(
    SELECT AVG((data->>'budget')::NUMERIC)
    FROM projects_json
);


-- AI recommendation
SELECT
    data->>'recommendation_id' AS recommendation_id,
    data->>'project_id' AS project_id,
    data->>'freelancer_id' AS freelancer_id,
    (data->>'recommendation_score')::NUMERIC AS score,
    data->>'reason' AS reason
FROM ai_recommendations_json
WHERE (data->>'recommendation_score')::NUMERIC >= 0.80
ORDER BY score DESC;
