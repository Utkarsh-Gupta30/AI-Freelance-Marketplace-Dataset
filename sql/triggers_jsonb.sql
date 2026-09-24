-- Automatically creates a notification whenever a new proposal is inserted
CREATE OR REPLACE FUNCTION notify_new_proposal()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
DECLARE
    project_client TEXT;
    new_notification_id INTEGER;
BEGIN

    SELECT data->>'client_id'
    INTO project_client
    FROM projects_json
    WHERE data->>'project_id' = NEW.data->>'project_id'
    LIMIT 1;

    SELECT COALESCE(MAX(record_id), 0) + 1
    INTO new_notification_id
    FROM notifications_json;

    INSERT INTO notifications_json (data)
    VALUES (
        jsonb_build_object(
            'notification_id', new_notification_id,
            'user_id', project_client,
            'title', 'New Proposal',
            'message',
            'A new proposal has been submitted for your project.',
            'notification_type', 'Proposal',
            'is_read', false,
            'created_at', CURRENT_TIMESTAMP
        )
    );

    RETURN NEW;
END;
$$;

-- Create trigger
CREATE TRIGGER trg_new_proposal_notification
AFTER INSERT ON proposals_json
FOR EACH ROW
EXECUTE FUNCTION notify_new_proposal();

-- Insert
INSERT INTO proposals_json (data)
VALUES (
    jsonb_build_object(
        'proposal_id', 9999,
        'project_id', 1,
        'freelancer_id', 1,
        'bid_amount', 25000,
        'estimated_days', 15,
        'cover_letter', 'Interested in this project.',
        'proposal_status', 'Pending',
        'created_at', CURRENT_TIMESTAMP
    )
);

-- Checking
SELECT *
FROM notifications_json
ORDER BY record_id DESC
LIMIT 1;