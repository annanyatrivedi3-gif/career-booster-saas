# backend/job_description.py

def generate_job_description(role: str, skills: list[str]) -> str:
    """
    Generates a clean job description tailored to the user's extracted skills.
    """
    skills_formatted = ", ".join(skills[:10])

    jd = f"""
Role: {role.title()}

Overview:
You will be responsible for leveraging your skills in {skills_formatted} to deliver
high-quality work within a collaborative environment.

Responsibilities:
- Apply core skills ({skills_formatted}) in daily workflow.
- Communicate effectively with cross-functional teams.
- Contribute to technical design, implementation, and optimization.
- Continuously improve product quality and performance.

Preferred:
- Passion for continuous learning.
- Ability to work independently and in teams.
- Familiarity with modern project management tools.

This job description is auto-generated based on your real skills.
"""
    return jd.strip()
