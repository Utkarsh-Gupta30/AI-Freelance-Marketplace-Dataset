-- USERS
CREATE TABLE users_json (
    record_id SERIAL PRIMARY KEY,
    data JSONB NOT NULL
);

-- CLIENTS
CREATE TABLE clients_json (
    record_id SERIAL PRIMARY KEY,
    data JSONB NOT NULL
);

-- FREELANCERS
CREATE TABLE freelancers_json (
    record_id SERIAL PRIMARY KEY,
    data JSONB NOT NULL
);

-- SKILLS
CREATE TABLE skills_json (
    record_id SERIAL PRIMARY KEY,
    data JSONB NOT NULL
);

-- FREELANCER SKILLS
CREATE TABLE freelancer_skills_json (
    record_id SERIAL PRIMARY KEY,
    data JSONB NOT NULL
);

-- CATEGORIES
CREATE TABLE categories_json (
    record_id SERIAL PRIMARY KEY,
    data JSONB NOT NULL
);

-- PROJECTS
CREATE TABLE projects_json (
    record_id SERIAL PRIMARY KEY,
    data JSONB NOT NULL
);

-- PROJECT SKILLS
CREATE TABLE project_skills_json (
    record_id SERIAL PRIMARY KEY,
    data JSONB NOT NULL
);

-- PROPOSALS
CREATE TABLE proposals_json (
    record_id SERIAL PRIMARY KEY,
    data JSONB NOT NULL
);

-- CONTRACTS
CREATE TABLE contracts_json (
    record_id SERIAL PRIMARY KEY,
    data JSONB NOT NULL
);

-- PAYMENTS
CREATE TABLE payments_json (
    record_id SERIAL PRIMARY KEY,
    data JSONB NOT NULL
);

-- REVIEWS
CREATE TABLE reviews_json (
    record_id SERIAL PRIMARY KEY,
    data JSONB NOT NULL
);

-- PORTFOLIO
CREATE TABLE portfolio_json (
    record_id SERIAL PRIMARY KEY,
    data JSONB NOT NULL
);

-- NOTIFICATIONS
CREATE TABLE notifications_json (
    record_id SERIAL PRIMARY KEY,
    data JSONB NOT NULL
);

-- AI RECOMMENDATIONS
CREATE TABLE ai_recommendations_json (
    record_id SERIAL PRIMARY KEY,
    data JSONB NOT NULL
);