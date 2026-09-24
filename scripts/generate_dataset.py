# Import Libraries
import json
import random
import os
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker("en_IN")
random.seed(42)
Faker.seed(42)

# Record Counts
USERS = 80
CLIENTS = 30
FREELANCERS = 50
SKILLS = 30
CATEGORIES = 10
PROJECTS = 60
PROJECT_SKILLS = 150
FREELANCER_SKILLS = 170
PROPOSALS = 240
CONTRACTS = 45
PAYMENTS = 80
REVIEWS = 90
PORTFOLIO = 100
NOTIFICATIONS = 250
AI_RECOMMENDATIONS = 180

# Create Output Folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FOLDER = os.path.join(BASE_DIR, "data")

# Helper Function
def save_json(filename, data):

    if os.path.isabs(filename):
        filepath = filename
    else:
        filepath = os.path.join(DATA_FOLDER, filename)

    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"✔ Saved {filepath}")

def load_json(filename):
    filepath = os.path.join(DATA_FOLDER, filename)

    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def random_datetime(start_days_ago=365):
    start = datetime.now() - timedelta(days=start_days_ago)
    end = datetime.now()

    return fake.date_time_between(
        start_date=start,
        end_date=end
    ).strftime("%Y-%m-%d %H:%M:%S")

# Master Lists
# 1. Skills
SKILL_LIST = [
    ("HTML", "Web Development"),
    ("CSS", "Web Development"),
    ("JavaScript", "Web Development"),
    ("React", "Web Development"),
    ("Angular", "Web Development"),
    ("Vue.js", "Web Development"),
    ("Node.js", "Backend"),
    ("Python", "Programming"),
    ("Java", "Programming"),
    ("C++", "Programming"),
    ("C#", "Programming"),
    ("PHP", "Programming"),
    ("Flutter", "Mobile Development"),
    ("React Native", "Mobile Development"),
    ("Kotlin", "Mobile Development"),
    ("Swift", "Mobile Development"),
    ("MySQL", "Database"),
    ("PostgreSQL", "Database"),
    ("MongoDB", "Database"),
    ("Machine Learning", "AI & ML"),
    ("Deep Learning", "AI & ML"),
    ("NLP", "AI & ML"),
    ("Computer Vision", "AI & ML"),
    ("TensorFlow", "AI & ML"),
    ("PyTorch", "AI & ML"),
    ("Docker", "DevOps"),
    ("Kubernetes", "DevOps"),
    ("AWS", "Cloud Computing"),
    ("Figma", "UI/UX"),
    ("Adobe Photoshop", "Graphic Design")
]

# 2. Categories
CATEGORY_LIST = [
    "Web Development",
    "Mobile Development",
    "AI & Machine Learning",
    "Data Science",
    "UI/UX Design",
    "Graphic Design",
    "Cloud Computing",
    "Cyber Security",
    "Blockchain",
    "DevOps"
]

CITIES = [
    "Pune",
    "Mumbai",
    "Delhi",
    "Bengaluru",
    "Hyderabad",
    "Chennai",
    "Kolkata",
    "Ahmedabad",
    "Jaipur",
    "Nagpur"
]

STATES = [
    "Maharashtra",
    "Delhi",
    "Karnataka",
    "Telangana",
    "Tamil Nadu",
    "West Bengal",
    "Gujarat",
    "Rajasthan"
]

PROFILE_IMAGES = [
    "profile1.jpg",
    "profile2.jpg",
    "profile3.jpg",
    "profile4.jpg",
    "profile5.jpg"
]

ACCOUNT_STATUS = [
    "Active",
    "Inactive",
    "Suspended"
]

COMPANIES = [
    "TechNova Solutions",
    "ByteCraft Technologies",
    "CodeFusion Pvt Ltd",
    "NextGen Systems",
    "CloudSphere",
    "InnovateX",
    "Digital Horizon",
    "VisionSoft",
    "FutureWorks",
    "DataBridge"
]

INDUSTRIES = [
    "Information Technology",
    "Healthcare",
    "Education",
    "Finance",
    "E-Commerce",
    "Manufacturing",
    "Retail",
    "Marketing",
    "Logistics",
    "Real Estate"
]

COMPANY_SIZES = [
    "Startup",
    "Small",
    "Medium",
    "Enterprise"
]

HEADLINES = [

    "Full Stack Developer",

    "Python Developer",

    "Machine Learning Engineer",

    "Flutter Developer",

    "UI/UX Designer",

    "Cloud Engineer",

    "Data Scientist",

    "React Developer",

    "Backend Developer",

    "DevOps Engineer"
]

PROJECT_TITLES = [

    "AI Chatbot Development",
    "E-Commerce Website",
    "Restaurant Management System",
    "Hospital Management System",
    "Portfolio Website",
    "Weather Forecast App",
    "Stock Price Prediction",
    "Attendance Management System",
    "Expense Tracker",
    "Face Recognition System",
    "Online Learning Platform",
    "Hotel Booking Website",
    "Food Delivery Application",
    "CRM Dashboard",
    "Banking Management System",
    "AI Resume Analyzer",
    "Invoice Management System",
    "Travel Booking Portal",
    "Fitness Tracking App",
    "Movie Recommendation System"

]

PROJECT_STATUS = [
    "Draft",
    "Open",
    "In Progress",
    "Completed",
    "Cancelled",
    "Closed"
]

DIFFICULTY = [
    "Beginner",
    "Intermediate",
    "Advanced",
    "Expert"
]

PROPOSAL_STATUS = [
    "Submitted",
    "Shortlisted",
    "Accepted",
    "Rejected",
    "Withdrawn"
]

CONTRACT_STATUS = [
    "Active",
    "Completed",
    "Cancelled",
    "Expired"
]

PAYMENT_METHODS = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Wallet"
]

PAYMENT_STATUS = [
    "Pending",
    "Processing",
    "Paid",
    "Failed",
    "Refunded"
]

NOTIFICATION_TYPES = [
    "System",
    "Payment",
    "Proposal",
    "Project",
    "Review"
]

# Generate Skills
def generate_skills():

    skills = []

    for i, (name, category) in enumerate(SKILL_LIST, start=1):

        skills.append({
            "skill_id": i,
            "skill_name": name,
            "skill_category": category,
            "description": f"{name} related skill."
        })

    save_json("skills.json", skills)

    return skills

# Generate Categories
def generate_categories():

    categories = []

    for i, category in enumerate(CATEGORY_LIST, start=1):

        categories.append({
            "category_id": i,
            "category_name": category,
            "description": f"Projects related to {category}."
        })

    save_json("categories.json", categories)

    return categories

# Functions
def generate_users():

    users = []

    roles = (
        ["Client"] * CLIENTS +
        ["Freelancer"] * FREELANCERS
    )

    random.shuffle(roles)

    for i in range(1, USERS + 1):

        registration_date = fake.date_between(
            start_date="-2y",
            end_date="today"
        )

        created_dt = fake.date_time_between(start_date="-2y", end_date="now")
        updated_dt = fake.date_time_between(start_date=created_dt, end_date="now")

        created_at = created_dt.strftime("%Y-%m-%d %H:%M:%S")
        updated_at = updated_dt.strftime("%Y-%m-%d %H:%M:%S")

        user = {

            "user_id": i,

            "full_name": fake.name(),

            "email": fake.unique.email(),

            "phone": fake.unique.msisdn()[:10],

            "password_hash": fake.sha256(),

            "role": roles[i-1],

            "city": random.choice(CITIES),

            "state": random.choice(STATES),

            "country": "India",

            "profile_image": random.choice(PROFILE_IMAGES),

            "registration_date": str(registration_date),

            "account_status": random.choice(ACCOUNT_STATUS),

            "created_at": created_at,

            "updated_at": updated_at

        }

        users.append(user)

    save_json("users.json", users)

    return users

def generate_clients():

    users = load_json("users.json")

    clients = []

    client_users = [u for u in users if u["role"] == "Client"]

    for index, user in enumerate(client_users, start=1):

        clients.append({

            "client_id": index,

            "user_id": user["user_id"],

            "company_name": COMPANIES[(index - 1) % len(COMPANIES)],

            "industry": random.choice(INDUSTRIES),

            "company_size": random.choice(COMPANY_SIZES),

            "gst_number": fake.unique.bothify(text="27ABCDE####F1Z#"),

            "company_website": fake.url()

        })

    save_json("clients.json", clients)

    return clients

def generate_freelancers():

    users = load_json("users.json")

    freelancers = []

    freelancer_users = [

        u for u in users

        if u["role"] == "Freelancer"

    ]

    for index, user in enumerate(

        freelancer_users,

        start=1

    ):

        freelancers.append({

            "freelancer_id": index,

            "user_id": user["user_id"],

            "headline": random.choice(HEADLINES),

            "bio": fake.paragraph(nb_sentences=3),

            "experience_years": random.randint(1, 10),

            "hourly_rate": round(random.uniform(10, 100), 2),

            "education": random.choice([

                "B.Tech",

                "M.Tech",

                "BCA",

                "MCA",

                "B.Sc Computer Science"

            ]),

            "availability": random.choice([

                "Available",

                "Busy",

                "On Leave"

            ]),

            "average_rating": round(

                random.uniform(3.5, 5.0),

                1

            ),

            "completed_projects": random.randint(0, 100)

        })

    save_json(

        "freelancers.json",

        freelancers

    )

    return freelancers

def generate_freelancer_skills():

    freelancers = load_json("freelancers.json")
    skills = load_json("skills.json")

    freelancer_skills = []
    record_id = 1

    proficiency_levels = [
        "Beginner",
        "Intermediate",
        "Advanced",
        "Expert"
    ]

    used_pairs = set()

    while len(freelancer_skills) < FREELANCER_SKILLS:

        freelancer = random.choice(freelancers)
        skill = random.choice(skills)

        pair = (
            freelancer["freelancer_id"],
            skill["skill_id"]
        )

        if pair in used_pairs:
            continue

        used_pairs.add(pair)

        freelancer_skills.append({

            "freelancer_skill_id": record_id,

            "freelancer_id": freelancer["freelancer_id"],

            "skill_id": skill["skill_id"],

            "proficiency_level": random.choice(proficiency_levels),

            "experience_years": random.randint(1,10)

        })

        record_id += 1

    save_json(
        "freelancer_skills.json",
        freelancer_skills
    )

    return freelancer_skills

def generate_projects():

    clients = load_json("clients.json")
    categories = load_json("categories.json")

    projects = []

    for i in range(1, PROJECTS + 1):

        created_dt = fake.date_time_between(
            start_date="-2y",
            end_date="now"
        )

        updated_dt = fake.date_time_between(
            start_date=created_dt,
            end_date="now"
        )

        deadline = fake.date_between(
            start_date="today",
            end_date="+180d"
        )

        project = {

            "project_id": i,

            "client_id": random.choice(clients)["client_id"],

            "category_id": random.choice(categories)["category_id"],

            "title": random.choice(PROJECT_TITLES),

            "description": fake.paragraph(nb_sentences=5),

            "budget": random.randint(10000, 300000),

            "currency": "INR",

            "difficulty": random.choice(DIFFICULTY),

            "deadline": str(deadline),

            "project_status": random.choice(PROJECT_STATUS),

            "created_at": created_dt.strftime("%Y-%m-%d %H:%M:%S"),

            "updated_at": updated_dt.strftime("%Y-%m-%d %H:%M:%S")

        }

        projects.append(project)

    save_json("projects.json", projects)

    return projects

def generate_project_skills():

    projects = load_json("projects.json")
    skills = load_json("skills.json")

    project_skills = []

    used_pairs = set()

    record_id = 1

    while len(project_skills) < PROJECT_SKILLS:

        project = random.choice(projects)
        skill = random.choice(skills)

        pair = (
            project["project_id"],
            skill["skill_id"]
        )

        if pair in used_pairs:
            continue

        used_pairs.add(pair)

        project_skills.append({

            "project_skill_id": record_id,

            "project_id": project["project_id"],

            "skill_id": skill["skill_id"],

            "is_required": random.choice([True, False])

        })

        record_id += 1

    save_json(
        "project_skills.json",
        project_skills
    )

    return project_skills

def generate_proposals():

    projects = load_json("projects.json")
    freelancers = load_json("freelancers.json")

    proposals = []

    used_pairs = set()

    for proposal_id in range(1, PROPOSALS + 1):

        while True:

            project = random.choice(projects)
            freelancer = random.choice(freelancers)

            pair = (
                project["project_id"],
                freelancer["freelancer_id"]
            )

            if pair not in used_pairs:
                used_pairs.add(pair)
                break

        created_dt = fake.date_time_between(
            start_date="-1y",
            end_date="now"
        )

        updated_dt = fake.date_time_between(
            start_date=created_dt,
            end_date="now"
        )

        proposals.append({

            "proposal_id": proposal_id,

            "project_id": project["project_id"],

            "freelancer_id": freelancer["freelancer_id"],

            "bid_amount": random.randint(5000, 300000),

            "estimated_days": random.randint(3, 90),

            "cover_letter": fake.paragraph(nb_sentences=4),

            "proposal_status": random.choice(PROPOSAL_STATUS),

            "created_at": created_dt.strftime("%Y-%m-%d %H:%M:%S"),

            "updated_at": updated_dt.strftime("%Y-%m-%d %H:%M:%S")

        })

    save_json("proposals.json", proposals)

    return proposals

def generate_contracts():

    proposals = load_json("proposals.json")

    accepted = [
        p for p in proposals
        if p["proposal_status"] == "Accepted"
    ]

    random.shuffle(accepted)

    contracts = []

    contract_id = 1

    for proposal in accepted[:CONTRACTS]:

        start_date = fake.date_between(
            start_date="-180d",
            end_date="today"
        )

        end_date = start_date + timedelta(
            days=random.randint(15,120)
        )

        contracts.append({

            "contract_id": contract_id,

            "proposal_id": proposal["proposal_id"],

            "start_date": str(start_date),

            "end_date": str(end_date),

            "contract_amount": proposal["bid_amount"],

            "proposal_status": random.choices(PROPOSAL_STATUS,weights=[40, 20, 20, 15, 5],k=1)[0],

            "created_at": fake.date_time_between(
                start_date="-180d",
                end_date="now"
            ).strftime("%Y-%m-%d %H:%M:%S"),

            "updated_at": fake.date_time_between(
                start_date="-30d",
                end_date="now"
            ).strftime("%Y-%m-%d %H:%M:%S")

        })

        contract_id += 1

    save_json("contracts.json", contracts)

    return contracts

def generate_payments():

    contracts = load_json("contracts.json")

    payments = []

    payment_id = 1

    while len(payments) < PAYMENTS:

        contract = random.choice(contracts)

        created_dt = fake.date_time_between(
            start_date="-180d",
            end_date="now"
        )

        updated_dt = fake.date_time_between(
            start_date=created_dt,
            end_date="now"
        )

        payments.append({

            "payment_id": payment_id,

            "contract_id": contract["contract_id"],

            "amount": round(
                contract["contract_amount"] /
                random.randint(1,3),
                2
            ),

            "payment_method": random.choice(PAYMENT_METHODS),

            "transaction_id": fake.unique.uuid4(),

            "payment_status": random.choice(PAYMENT_STATUS),

            "payment_date": str(
                fake.date_between(
                    start_date="-180d",
                    end_date="today"
                )
            ),

            "created_at": created_dt.strftime("%Y-%m-%d %H:%M:%S"),

            "updated_at": updated_dt.strftime("%Y-%m-%d %H:%M:%S")

        })

        payment_id += 1

    save_json("payments.json", payments)

    return payments

def generate_reviews():

    contracts = load_json("contracts.json")
    proposals = load_json("proposals.json")

    reviews = []

    review_id = 1

    for _ in range(REVIEWS):

        contract = random.choice(contracts)

        proposal = next(
            p for p in proposals
            if p["proposal_id"] == contract["proposal_id"]
        )

        reviews.append({

            "review_id": review_id,

            "contract_id": contract["contract_id"],

            "reviewer_user_id": random.randint(1, USERS),

            "reviewed_user_id": random.randint(1, USERS),

            "rating": round(
                random.uniform(3.0,5.0),
                1
            ),

            "review": fake.sentence(nb_words=15),

            "review_date": str(
                fake.date_between(
                    start_date="-180d",
                    end_date="today"
                )
            ),

            "created_at": fake.date_time_between(
                start_date="-180d",
                end_date="now"
            ).strftime("%Y-%m-%d %H:%M:%S"),

            "updated_at": fake.date_time_between(
                start_date="-30d",
                end_date="now"
            ).strftime("%Y-%m-%d %H:%M:%S")

        })

        review_id += 1

    save_json("reviews.json", reviews)

    return reviews

def generate_portfolio():

    freelancers = load_json("freelancers.json")

    portfolio = []

    for i in range(1, PORTFOLIO + 1):

        freelancer = random.choice(freelancers)

        portfolio.append({

            "portfolio_id": i,

            "freelancer_id": freelancer["freelancer_id"],

            "project_title": random.choice(PROJECT_TITLES),

            "project_description": fake.paragraph(),

            "project_link": fake.url(),

            "technologies_used": ", ".join(
                random.sample(
                    [s[0] for s in SKILL_LIST],
                    random.randint(2,5)
                )
            ),

            "completion_year": random.randint(
                2020,
                2026
            )

        })

    save_json("portfolio.json", portfolio)

    return portfolio

def generate_notifications():

    notifications = []

    for i in range(1, NOTIFICATIONS + 1):

        notifications.append({

            "notification_id": i,

            "user_id": random.randint(1, USERS),

            "title": fake.sentence(nb_words=4),

            "message": fake.sentence(nb_words=10),

            "notification_type": random.choice(
                NOTIFICATION_TYPES
            ),

            "is_read": random.choice([True,False]),

            "created_at": fake.date_time_between(
                start_date="-365d",
                end_date="now"
            ).strftime("%Y-%m-%d %H:%M:%S")

        })

    save_json(
        "notifications.json",
        notifications
    )

    return notifications

def generate_ai_recommendations():

    projects = load_json("projects.json")
    freelancers = load_json("freelancers.json")

    recommendations = []

    for i in range(1, AI_RECOMMENDATIONS + 1):

        recommendations.append({

            "recommendation_id": i,

            "project_id": random.choice(
                projects
            )["project_id"],

            "freelancer_id": random.choice(
                freelancers
            )["freelancer_id"],

            "recommendation_score": round(
                random.uniform(0.50,1.00),
                2
            ),

            "reason": random.choice([

                "Skill Match",

                "High Rating",

                "Similar Project Experience",

                "Fast Delivery",

                "Budget Friendly"

            ]),

            "generated_at": fake.date_time_between(
                start_date="-180d",
                end_date="now"
            ).strftime("%Y-%m-%d %H:%M:%S")

        })

    save_json(
        "ai_recommendations.json",
        recommendations
    )

    return recommendations

def generate_raw_dataset():

    users = load_json("users.json")
    clients = load_json("clients.json")
    freelancers = load_json("freelancers.json")
    skills = load_json("skills.json")
    projects = load_json("projects.json")
    project_skills = load_json("project_skills.json")
    proposals = load_json("proposals.json")
    contracts = load_json("contracts.json")
    payments = load_json("payments.json")
    reviews = load_json("reviews.json")
    categories = load_json("categories.json")

    raw_data = []

    for proposal in proposals[:100]:

        project = next(
            p for p in projects
            if p["project_id"] == proposal["project_id"]
        )

        client = next(
            c for c in clients
            if c["client_id"] == project["client_id"]
        )

        client_user = next(
            u for u in users
            if u["user_id"] == client["user_id"]
        )

        freelancer = next(
            f for f in freelancers
            if f["freelancer_id"] == proposal["freelancer_id"]
        )

        freelancer_user = next(
            u for u in users
            if u["user_id"] == freelancer["user_id"]
        )

        category = next(
            c for c in categories
            if c["category_id"] == project["category_id"]
        )

        project_skill_names = []

        for ps in project_skills:

            if ps["project_id"] == project["project_id"]:

                skill = next(
                    s for s in skills
                    if s["skill_id"] == ps["skill_id"]
                )

                project_skill_names.append(skill["skill_name"])

        contract = next(
            (
                c for c in contracts
                if c["proposal_id"] == proposal["proposal_id"]
            ),
            None
        )

        payment = None

        if contract:

            payment = next(
                (
                    p for p in payments
                    if p["contract_id"] == contract["contract_id"]
                ),
                None
            )

        review = None

        if contract:

            review = next(
                (
                    r for r in reviews
                    if r["contract_id"] == contract["contract_id"]
                ),
                None
            )

        raw_data.append({

            "project_id": project["project_id"],

            "project_title": project["title"],

            "category": category["category_name"],

            "client_name": client_user["full_name"],

            "client_email": client_user["email"],

            "client_phone": client_user["phone"],

            "company_name": client["company_name"],

            "freelancer_name": freelancer_user["full_name"],

            "freelancer_email": freelancer_user["email"],

            "skills": ", ".join(project_skill_names),

            "budget": project["budget"],

            "proposal_amount": proposal["bid_amount"],

            "contract_amount":
            contract["contract_amount"]
            if contract else None,

            "payment_method":
            payment["payment_method"]
            if payment else None,

            "payment_status":
            payment["payment_status"]
            if payment else None,

            "rating":
            review["rating"]
            if review else None,

            "review":
            review["review"]
            if review else None

        })

    save_json(
        "../raw_dataset/raw_freelance_data.json",
        raw_data
    )

# Main Function
def main():

    generate_skills()
    generate_categories()
    generate_users()
    generate_clients()
    generate_freelancers()
    generate_freelancer_skills()
    generate_projects()
    generate_project_skills()
    generate_proposals()
    generate_contracts()
    generate_payments()
    generate_reviews()
    generate_portfolio()
    generate_notifications()
    generate_ai_recommendations()
    generate_raw_dataset()

if __name__ == "__main__":
    main()

