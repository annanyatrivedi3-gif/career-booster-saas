from flask import Flask, request, jsonify
from flask_cors import CORS

from analyzer import (
    analyze_skills,
    recommend_career_paths,
    estimate_salary,
    generate_job_description,
    get_user_history,
)
from skill_gap import analyze_skill_gaps
from recommendations import recommend_courses
from resume_parser import parse_resume

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return {"status": "Backend running"}


@app.route("/upload-resume", methods=["POST"])
def upload_resume():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    parsed = parse_resume(file)

    return jsonify({"parsed": parsed}), 200


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json(force=True)
    skills = data.get("skills", [])
    role = data.get("role", "")
    user_id = data.get("user_id", None)

    result = analyze_skills(skills, role, user_id)
    return jsonify(result), 200


@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json(force=True)
    missing = data.get("missing", [])
    courses = recommend_courses(missing)
    return jsonify({"courses": courses}), 200


@app.route("/job-description", methods=["POST"])
def job_description():
    data = request.get_json()
    role = data.get("role", "")
    skills = data.get("skills", [])

    description = generate_job_description(role, skills)
    return jsonify({"description": description}), 200


@app.route("/career-paths", methods=["POST"])
def career_paths():
    data = request.get_json()
    skills = data.get("skills", [])

    paths = recommend_career_paths(skills)
    return jsonify({"paths": paths}), 200


@app.route("/salary", methods=["POST"])
def salary():
    data = request.get_json()
    role = data.get("role", "")
    skills = data.get("skills", [])

    return jsonify(estimate_salary(role, skills)), 200


@app.route("/skill-gaps", methods=["POST"])
def skill_gaps():
    data = request.get_json()

    user_skills = data.get("skills", [])
    role_required = data.get("required", [])

    gaps = analyze_skill_gaps(user_skills, role_required)

    return jsonify(gaps)



@app.route("/history", methods=["GET"])
def history():
    user_id = request.args.get("user_id")
    return jsonify(get_user_history(user_id)), 200


if __name__ == "__main__":
    app.run(port=5000, debug=True)
