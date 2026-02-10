from typing import List, Dict
from recommendations import recommend_courses
import statistics

# ----------------------------------------------
# ROLE → REQUIRED SKILLS
# ----------------------------------------------

ROLE_SKILLS: Dict[str, List[str]] = {
    "Frontend Developer": ["html", "css", "javascript", "react", "nextjs", "git"],
    "Backend Developer": ["node", "express", "mongodb", "sql", "rest api"],
    "Full Stack Developer": ["html", "css", "javascript", "react", "node", "express", "sql"],
    "Software Engineer": ["python", "java", "git", "linux"],
    "Machine Learning Engineer": ["python", "machine learning", "pandas", "numpy", "tensorflow"],
    "Data Analyst": ["python", "excel", "power bi", "sql"],
    "Data Scientist": ["python", "machine learning", "pandas", "statistics"],
    "DevOps Engineer": ["linux", "docker", "kubernetes", "aws", "jenkins"],
    "Cloud Engineer": ["aws", "azure", "gcp", "ec2", "s3"],
    "Product Manager": ["agile", "ui/ux", "communication", "jira"],
    "Business Analyst": ["excel", "sql", "process mapping"],
    "UI/UX Designer": ["figma", "ui/ux", "design thinking"],
    "Cybersecurity Analyst": ["network security", "penetration testing", "linux"],
}

# ----------------------------------------------
# SALARY ESTIMATOR
# ----------------------------------------------

BASE_SALARIES = {
    "Frontend Developer": (4, 12),
    "Backend Developer": (5, 16),
    "Full Stack Developer": (6, 20),
    "Software Engineer": (6, 18),
    "Machine Learning Engineer": (8, 25),
    "Data Scientist": (8, 22),
    "Data Analyst": (4, 10),
    "DevOps Engineer": (8, 22),
    "Cloud Engineer": (8, 24),
    "Product Manager": (10, 30),
    "UI/UX Designer": (5, 14),
    "Cybersecurity Analyst": (6, 18),
}

# ----------------------------------------------
# CALCULATE MATCH SCORE
# ----------------------------------------------

def calculate_match(user_skills: List[str], req: List[str]) -> int:
    if not req:
        return 0
    matched = len([s for s in req if s in user_skills])
    return int((matched / len(req)) * 100)


# ----------------------------------------------
# MAIN ANALYSIS FUNCTION
# ----------------------------------------------

def analyze_skills(skills: List[str], role: str, user_id=None) -> Dict:
    skills = [s.lower().strip() for s in skills]

    required = ROLE_SKILLS.get(role, [])
    missing = [s for s in required if s not in skills]
    score = calculate_match(skills, required)

    salary = estimate_salary(role, skills)
    career_paths = recommend_career_paths(skills)
    description = generate_job_description(role, skills)
    courses = recommend_courses(missing)

    return {
        "role": role,
        "skills": skills,
        "required": required,
        "missing": missing,
        "match_score": score,
        "salary_range": salary,
        "career_paths": career_paths,
        "job_description": description,
        "courses": courses,
    }


# ----------------------------------------------
# CAREER PATH RECOMMENDATION
# ----------------------------------------------

def recommend_career_paths(skills: List[str]) -> List[str]:
    best_roles = []

    for role, req in ROLE_SKILLS.items():
        match = calculate_match(skills, req)
        if match >= 40:
            best_roles.append((role, match))

    best_roles.sort(key=lambda x: x[1], reverse=True)
    return [r[0] for r in best_roles[:5]]


# ----------------------------------------------
# JOB DESCRIPTION GENERATOR
# ----------------------------------------------

def generate_job_description(role: str, skills: List[str]) -> str:
    skills_list = ", ".join(skills[:10])
    return (
        f"We are seeking a skilled {role} with experience in {skills_list}. "
        f"The ideal candidate can work collaboratively, deliver high-quality output, "
        f"and continuously learn new technologies."
    )


# ----------------------------------------------
# SALARY ESTIMATION
# ----------------------------------------------

def estimate_salary(role: str, skills: List[str]) -> Dict[str, str]:
    if role not in BASE_SALARIES:
        return {"min": "N/A", "max": "N/A"}

    base_min, base_max = BASE_SALARIES[role]
    boost = min(len(skills) // 5, 5)

    return {
        "min": f"{base_min + boost} LPA",
        "max": f"{base_max + 2 * boost} LPA",
    }


# ----------------------------------------------
# USER HISTORY STORAGE (IN-MEMORY)
# ----------------------------------------------

USER_HISTORY = {}

def get_user_history(user_id):
    return USER_HISTORY.get(user_id, [])
