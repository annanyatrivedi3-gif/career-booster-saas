# backend/career_paths.py

from skills.role_map import ROLE_MAP

def recommend_career_paths(skills: list[str]) -> list[str]:
    """
    Suggests alternative career paths based on skill overlap with other roles.
    """

    matches = []

    for role, data in ROLE_MAP.items():
        required = data.get("required", [])
        score = len([s for s in required if s in skills])

        if score >= 2:  # MIN OVERLAP
            matches.append((role, score))

    # Sort by highest match
    matches.sort(key=lambda x: x[1], reverse=True)

    # Return top 5 alternative roles
    return [m[0] for m in matches[:5]]
