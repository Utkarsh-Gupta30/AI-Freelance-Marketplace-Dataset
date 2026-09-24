-- Find projects within a given budget
CREATE OR REPLACE PROCEDURE find_projects_by_budget(
    IN max_budget NUMERIC
)
LANGUAGE plpgsql
AS $$
DECLARE
    project_rec RECORD;
BEGIN
    RAISE NOTICE 'Projects with budget <= %', max_budget;
    -- Assign the query results row-by-row into 'project_rec'
    FOR project_rec IN 
        SELECT 
            data->>'project_id' AS p_id, 
            data->>'title' AS p_title, 
            (data->>'budget')::NUMERIC AS p_budget
        FROM projects_json
        WHERE (data->>'budget')::NUMERIC <= max_budget
        ORDER BY (data->>'budget')::NUMERIC
    LOOP
        -- Print each record found
        RAISE NOTICE 'ID: %, Title: %, Budget: %', 
            project_rec.p_id, 
            project_rec.p_title, 
            project_rec.p_budget;
    END LOOP;
END;
$$;

CALL find_projects_by_budget(50000);


-- Inserts a notification
CREATE OR REPLACE PROCEDURE add_notification(
    IN p_user_id TEXT,
    IN p_title TEXT,
    IN p_message TEXT
)
LANGUAGE plpgsql
AS $$
DECLARE
    new_id INTEGER;
BEGIN

    SELECT COALESCE(MAX(record_id), 0) + 1
    INTO new_id
    FROM notifications_json;

    INSERT INTO notifications_json (data)
    VALUES (
        jsonb_build_object(
            'notification_id', new_id,
            'user_id', p_user_id,
            'title', p_title,
            'message', p_message,
            'notification_type', 'System',
            'is_read', false,
            'created_at', CURRENT_TIMESTAMP
        )
    );

    RAISE NOTICE 'Notification added successfully';

END;
$$;

CALL add_notification(
    '1',
    'Project Update',
    'Your project status has been updated.'
);

-- Checking
SELECT *
FROM notifications_json
ORDER BY record_id DESC
LIMIT 1;