# backend/skills/role_map.py

from __future__ import annotations
from typing import Dict, List, TypedDict

class RoleDefinition(TypedDict, total=False):
    required: List[str]
    optional: List[str]
    category: str

ROLE_MAP: Dict[str, RoleDefinition] = {
    # -------- ENGINEERING / TECH --------
    "frontend developer": {
        "category": "engineering",
        "required": ["javascript", "react", "html", "css"],
        "optional": ["typescript", "nextjs", "tailwind", "jest"],
    },
    "backend developer": {
        "category": "engineering",
        "required": ["node", "express", "sql"],
        "optional": ["python", "mongodb", "aws", "docker"],
    },
    "full stack developer": {
        "category": "engineering",
        "required": ["javascript", "react", "node", "express", "sql"],
        "optional": ["typescript", "nextjs", "docker", "aws"],
    },
    "react developer": {
        "category": "engineering",
        "required": ["javascript", "react", "html", "css"],
        "optional": ["typescript", "redux", "nextjs"],
    },
    "nextjs developer": {
        "category": "engineering",
        "required": ["javascript", "react", "nextjs"],
        "optional": ["typescript", "tailwind", "node"],
    },
    "node developer": {
        "category": "engineering",
        "required": ["javascript", "node", "express"],
        "optional": ["mongodb", "postgresql", "docker"],
    },
    "python developer": {
        "category": "engineering",
        "required": ["python", "git"],
        "optional": ["django", "flask", "fastapi", "sql"],
    },
    "django developer": {
        "category": "engineering",
        "required": ["python", "django", "postgresql"],
        "optional": ["rest api", "docker", "celery"],
    },
    "flask developer": {
        "category": "engineering",
        "required": ["python", "flask", "rest api"],
        "optional": ["docker", "aws", "postgresql"],
    },
    "java developer": {
        "category": "engineering",
        "required": ["java", "spring boot"],
        "optional": ["microservices", "docker", "kubernetes"],
    },
    "golang developer": {
        "category": "engineering",
        "required": ["go", "rest api"],
        "optional": ["grpc", "kubernetes", "docker"],
    },
    "android developer": {
        "category": "engineering",
        "required": ["kotlin", "android"],
        "optional": ["firebase", "rest api"],
    },
    "ios developer": {
        "category": "engineering",
        "required": ["swift", "ios"],
        "optional": ["swiftui", "core data"],
    },
    "flutter developer": {
        "category": "engineering",
        "required": ["dart", "flutter"],
        "optional": ["firebase", "rest api"],
    },
    "react native developer": {
        "category": "engineering",
        "required": ["javascript", "react native"],
        "optional": ["typescript", "redux"],
    },
    "embedded engineer": {
        "category": "engineering",
        "required": ["embedded systems", "c", "c++"],
        "optional": ["rtos", "arduino"],
    },
    "devops engineer": {
        "category": "devops",
        "required": ["linux", "docker", "kubernetes", "ci/cd"],
        "optional": ["aws", "terraform", "ansible"],
    },
    "cloud engineer": {
        "category": "devops",
        "required": ["aws", "linux", "network security"],
        "optional": ["terraform", "kubernetes"],
    },
    "site reliability engineer": {
        "category": "devops",
        "required": ["linux", "monitoring", "incident management"],
        "optional": ["prometheus", "grafana", "kubernetes"],
    },

    # -------- DATA / ANALYTICS --------
    "data analyst": {
        "category": "data",
        "required": ["sql", "excel", "tableau"],
        "optional": ["power bi", "python", "statistics"],
    },
    "business analyst": {
        "category": "data",
        "required": ["business analysis", "sql", "requirements gathering"],
        "optional": ["tableau", "power bi"],
    },
    "bi analyst": {
        "category": "data",
        "required": ["sql", "power bi", "excel"],
        "optional": ["tableau", "python"],
    },
    "data scientist": {
        "category": "data",
        "required": ["python", "pandas", "numpy", "ml"],
        "optional": ["tensorflow", "pytorch", "sql"],
    },
    "machine learning engineer": {
        "category": "data",
        "required": ["python", "ml", "deep learning"],
        "optional": ["pytorch", "tensorflow", "mlflow"],
    },
    "ml ops engineer": {
        "category": "data",
        "required": ["python", "ml", "docker", "kubernetes"],
        "optional": ["mlflow", "airflow", "aws"],
    },
    "analytics engineer": {
        "category": "data",
        "required": ["sql", "dbt", "data modeling"],
        "optional": ["python", "airflow"],
    },

    # -------- SECURITY --------
    "security engineer": {
        "category": "security",
        "required": ["network security", "linux", "owasp"],
        "optional": ["penetration testing", "kali linux"],
    },
    "penetration tester": {
        "category": "security",
        "required": ["penetration testing", "kali linux"],
        "optional": ["burp suite", "network security"],
    },

    # -------- PRODUCT / PROJECT --------
    "product manager": {
        "category": "product",
        "required": ["product management", "roadmapping", "stakeholder management"],
        "optional": ["data analysis", "ux research"],
    },
    "associate product manager": {
        "category": "product",
        "required": ["product management", "communication"],
        "optional": ["sql", "analytics"],
    },
    "technical product manager": {
        "category": "product",
        "required": ["product management", "api", "system design"],
        "optional": ["sql", "cloud"],
    },
    "project manager": {
        "category": "management",
        "required": ["project management", "agile", "stakeholder management"],
        "optional": ["jira", "risk management"],
    },
    "scrum master": {
        "category": "management",
        "required": ["scrum", "agile", "facilitation"],
        "optional": ["jira", "kanban"],
    },

    # -------- DESIGN / CREATIVE --------
    "ui designer": {
        "category": "design",
        "required": ["ui design", "figma"],
        "optional": ["design systems", "prototyping"],
    },
    "ux designer": {
        "category": "design",
        "required": ["ux design", "ux research"],
        "optional": ["figma", "prototyping"],
    },
    "product designer": {
        "category": "design",
        "required": ["ui design", "ux design", "figma"],
        "optional": ["prototyping", "interaction design"],
    },
    "graphic designer": {
        "category": "design",
        "required": ["graphic design"],
        "optional": ["illustration", "branding"],
    },
    "motion designer": {
        "category": "design",
        "required": ["motion graphics", "video editing"],
        "optional": ["after effects", "premiere pro"],
    },

    # -------- MARKETING / GROWTH --------
    "digital marketing specialist": {
        "category": "marketing",
        "required": ["digital marketing", "seo", "sem"],
        "optional": ["google analytics", "google ads", "facebook ads"],
    },
    "performance marketer": {
        "category": "marketing",
        "required": ["performance marketing", "google ads", "facebook ads"],
        "optional": ["analytics", "landing page optimization"],
    },
    "content marketer": {
        "category": "marketing",
        "required": ["content marketing", "content writing"],
        "optional": ["seo", "email marketing"],
    },
    "seo specialist": {
        "category": "marketing",
        "required": ["seo", "keyword research"],
        "optional": ["technical seo", "content writing"],
    },
    "social media manager": {
        "category": "marketing",
        "required": ["social media marketing", "content planning"],
        "optional": ["graphic design", "copywriting"],
    },

    # -------- SALES / CUSTOMER --------
    "sales development representative": {
        "category": "sales",
        "required": ["b2b sales", "lead generation", "crm"],
        "optional": ["cold calling", "email outreach"],
    },
    "account executive": {
        "category": "sales",
        "required": ["b2b sales", "negotiation", "crm"],
        "optional": ["presentation skills", "pipeline management"],
    },
    "customer success manager": {
        "category": "customer",
        "required": ["customer success", "communication", "account management"],
        "optional": ["product knowledge", "data analysis"],
    },
    "customer support specialist": {
        "category": "customer",
        "required": ["customer support", "communication"],
        "optional": ["ticketing tools", "knowledge base management"],
    },

    # -------- HR / PEOPLE --------
    "hr generalist": {
        "category": "hr",
        "required": ["recruitment", "employee engagement"],
        "optional": ["payroll", "performance management"],
    },
    "talent acquisition specialist": {
        "category": "hr",
        "required": ["recruitment", "talent acquisition"],
        "optional": ["employer branding", "interviewing"],
    },
    "learning and development specialist": {
        "category": "hr",
        "required": ["training and development", "presentation skills"],
        "optional": ["instructional design"],
    },

    # -------- FINANCE / OPS --------
    "financial analyst": {
        "category": "finance",
        "required": ["financial analysis", "excel", "financial modeling"],
        "optional": ["power bi", "sql"],
    },
    "accountant": {
        "category": "finance",
        "required": ["bookkeeping", "accounts payable", "accounts receivable"],
        "optional": ["taxation", "excel"],
    },
    "operations manager": {
        "category": "operations",
        "required": ["operations management", "process improvement"],
        "optional": ["supply chain", "logistics"],
    },
    "supply chain analyst": {
        "category": "operations",
        "required": ["supply chain", "excel"],
        "optional": ["sql", "inventory management"],
    },

    # -------- EDUCATION / HEALTHCARE --------
    "teacher": {
        "category": "education",
        "required": ["classroom management", "communication"],
        "optional": ["curriculum design", "assessment"],
    },
    "training instructor": {
        "category": "education",
        "required": ["training and development", "presentation skills"],
        "optional": ["instructional design"],
    },
    "nurse": {
        "category": "healthcare",
        "required": ["healthcare operations", "patient care"],
        "optional": ["electronic medical records"],
    },
    "hospital administrator": {
        "category": "healthcare",
        "required": ["healthcare operations", "people management"],
        "optional": ["budgeting", "process improvement"],
    },

    # -------- GENERIC NON-TECH ROLES --------
    "store manager": {
        "category": "retail",
        "required": ["store management", "customer support", "inventory management"],
        "optional": ["sales", "people management"],
    },
    "front office executive": {
        "category": "hospitality",
        "required": ["hospitality", "customer support"],
        "optional": ["front office", "communication"],
    },
}
