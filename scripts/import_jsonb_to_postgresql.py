import json
import os
import sys
import psycopg2
from psycopg2.extras import Json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

FILES = {
    "users_json": "users.json",
    "clients_json": "clients.json",
    "freelancers_json": "freelancers.json",
    "skills_json": "skills.json",
    "freelancer_skills_json": "freelancer_skills.json",
    "categories_json": "categories.json",
    "projects_json": "projects.json",
    "project_skills_json": "project_skills.json",
    "proposals_json": "proposals.json",
    "contracts_json": "contracts.json",
    "payments_json": "payments.json",
    "reviews_json": "reviews.json",
    "portfolio_json": "portfolio.json",
    "notifications_json": "notifications.json",
    "ai_recommendations_json": "ai_recommendations.json",
}


def load_json(filename):
    with open(os.path.join(DATA_DIR, filename), "r", encoding="utf-8") as f:
        return json.load(f)


def main():

    conn = psycopg2.connect(
        host=os.getenv("PGHOST", "localhost"),
        port=os.getenv("PGPORT", "5433"),
        dbname=os.getenv("PGDATABASE", "freelance_marketplace"),
        user=os.getenv("PGUSER", "postgres"),
        password=os.getenv("PGPASSWORD", "Kali@321"),
    )

    try:
        cur = conn.cursor()

        # Clear existing JSONB data
        for table in FILES:
            cur.execute(f"TRUNCATE TABLE {table} RESTART IDENTITY;")

        total = 0

        for table, filename in FILES.items():

            records = load_json(filename)

            for record in records:
                cur.execute(
                    f"""
                    INSERT INTO {table} (data)
                    VALUES (%s)
                    """,
                    (Json(record),)
                )

            print(f"{filename}: {len(records)} records")
            total += len(records)

        conn.commit()

        print("\n--------------------------------")
        print("JSONB IMPORT COMPLETED")
        print(f"Total records imported: {total}")
        print("--------------------------------")

    except Exception as e:
        conn.rollback()
        print("Import failed:", e)
        sys.exit(1)

    finally:
        conn.close()


if __name__ == "__main__":
    main()