# backend/skills/extractor.py

import re
from typing import List
from .skill_list import TECH_SKILLS, NON_TECH_SKILLS
from .aliases import SKILL_ALIASES

ALL_SKILLS = TECH_SKILLS + NON_TECH_SKILLS

def normalize_skill(s: str) -> str:
    s = s.lower().strip()
    return SKILL_ALIASES.get(s, s)

def extract_skills(text: str) -> List[str]:
    """
    Keyword-based extraction over a large skill dictionary.
    All matching is case-insensitive and alias-normalized.
    """
    text = text.lower()
    found = set()

    for skill in ALL_SKILLS:
        normalized = normalize_skill(skill)
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"
        if re.search(pattern, text):
            found.add(normalized)

    return sorted(found)
