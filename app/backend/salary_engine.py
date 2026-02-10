# backend/salary_engine.py

BASE_SALARY = {
    "frontend developer": 60000,
    "backend developer": 65000,
    "full stack developer": 70000,
    "data analyst": 55000,
    "data scientist": 90000,
    "machine learning engineer": 110000,
    "project manager": 80000,
    "ui designer": 55000,
    "digital marketing specialist": 45000,
}

SKILL_BONUS = {
    "react": 5000,
    "node": 5000,
    "sql": 3000,
    "python": 4000,
    "aws": 7000,
    "docker": 4000,
    "kubernetes": 8000,
    "power bi": 3000,
    "tableau": 3000,
    "ml": 10000,
    "deep learning": 12000,
}

def estimate_salary(role: str, skills: list[str]) -> dict:
    role = role.lower()
    base = BASE_SALARY.get(role, 50000)

    bonus = sum(SKILL_BONUS.get(s, 0) for s in skills)

    estimated = base + bonus

    return {
        "base_salary": base,
        "skill_bonus": bonus,
        "estimated_salary": estimated,
    }
