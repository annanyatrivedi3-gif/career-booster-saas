# skill_gap.py

def analyze_skill_gaps(user_skills, role_required):
    """
    Compare user skills with required role skills
    Returns structured skill gap data
    """

    user_skills = [s.lower() for s in user_skills]
    role_required = [s.lower() for s in role_required]

    missing = [s for s in role_required if s not in user_skills]

    weak = []
    emerging = []

    # Example logic — we can expand this!
    for skill in user_skills:
        if skill in role_required:
            continue
        elif skill not in role_required:
            emerging.append(skill)

    return {
        "missing": missing,
        "weak": weak,
        "emerging": emerging,
        "total_required": len(role_required),
        "total_missing": len(missing),
    }
