"use client";

import { useState } from "react";
import { ROLES } from "@/data/roles"; // <-- CORRECT import path

// ----------------------
// TYPE DEFINITIONS
// ----------------------

type ParsedResume = {
  parsed: {
    text: string;
    skills: string[];
  };
};

type AnalysisResponse = {
  role: string;
  skills: string[];
  required: string[];
  missing: string[];
  match_score: number;
  salary_range: { min: string; max: string };
  career_paths: string[];
  job_description: string;
  courses: Course[];
};

type Course = {
  skill: string;
  title: string;
  platform: string;
  url: string;
};

// ----------------------
// MAIN COMPONENT
// ----------------------

export default function UploadResume() {
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);

  const [parsed, setParsed] = useState<ParsedResume | null>(null);
  const [selectedRole, setSelectedRole] = useState("");
  const [analysis, setAnalysis] = useState<AnalysisResponse | null>(null);

  // ----------------------
  // UPLOAD + PARSE RESUME
  // ----------------------
  const handleUpload = async () => {
    if (!file) {
      alert("Please select a file first");
      return;
    }

    setLoading(true);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await fetch("http://localhost:5000/upload-resume", {
        method: "POST",
        body: formData,
      });

      const data = (await res.json()) as ParsedResume;
      setParsed(data);
      setAnalysis(null);
    } catch (err) {
      console.error(err);
      alert("Error uploading resume");
    } finally {
      setLoading(false);
    }
  };

  // ----------------------
  // ANALYZE RESUME
  // ----------------------
  const handleAnalyze = async () => {
    if (!parsed) {
      alert("Upload resume first");
      return;
    }

    if (!selectedRole) {
      alert("Select a role first");
      return;
    }

    setLoading(true);

    try {
      const res = await fetch("http://localhost:5000/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          skills: parsed.parsed.skills,
          role: selectedRole,
        }),
      });

      const data = (await res.json()) as AnalysisResponse;
      setAnalysis(data);
    } catch (err) {
      console.error(err);
      alert("Error analyzing resume");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-10 text-white">
      <h1 className="text-3xl font-bold mb-6">Upload Your Resume</h1>

      {/* FILE UPLOAD */}
      <div className="mb-4">
        <input
          type="file"
          accept=".pdf,.doc,.docx"
          onChange={(e) => setFile(e.target.files?.[0] || null)}
          className="text-black"
        />
      </div>

      <button
        onClick={handleUpload}
        className="bg-green-600 px-4 py-2 rounded hover:bg-green-700"
      >
        {loading ? "Processing..." : "Upload"}
      </button>

      {/* EXTRACTED SKILLS */}
      {parsed && (
        <div className="mt-8 bg-gray-900 p-4 rounded">
          <h2 className="text-xl font-bold mb-3">Extracted Skills</h2>
          <div className="flex flex-wrap gap-2">
            {parsed.parsed.skills.map((skill) => (
              <span
                key={skill}
                className="bg-blue-600 px-3 py-1 rounded text-sm"
              >
                {skill}
              </span>
            ))}
          </div>
        </div>
      )}

      {/* ROLE SELECTOR */}
      {parsed && (
        <div className="mt-6">
          <label className="text-lg block mb-2">Select Your Target Role:</label>

          <select
            className="text-black p-2 rounded w-64"
            value={selectedRole}
            onChange={(e) => setSelectedRole(e.target.value)}
          >
            <option value="">Choose...</option>
            {ROLES.map((role: string) => (
              <option key={role} value={role}>
                {role}
              </option>
            ))}
          </select>

          <button
            onClick={handleAnalyze}
            className="bg-purple-600 text-white px-4 py-2 ml-4 rounded hover:bg-purple-700"
          >
            Analyze Resume
          </button>
        </div>
      )}

      {/* ANALYSIS RESULTS */}
      {analysis && (
        <div className="mt-10 bg-gray-900 p-6 rounded">
          <h2 className="text-2xl font-bold mb-4">Analysis Results</h2>

          <p className="text-lg mb-2">
            <strong>Match Score:</strong>{" "}
            <span className="text-green-400">{analysis.match_score}%</span>
          </p>

          <p className="text-lg mb-2">
            <strong>Salary Estimate:</strong>{" "}
            {analysis.salary_range.min} – {analysis.salary_range.max}
          </p>

          <h3 className="font-bold mt-4">Missing Core Skills:</h3>

          {analysis.missing?.length === 0 ? (
            <p className="text-green-300 mt-2">No core skills missing. Great!</p>
          ) : (
            <ul className="list-disc ml-6 mt-2">
              {analysis.missing.map((s) => (
                <li key={s}>{s}</li>
              ))}
            </ul>
          )}

          <h3 className="font-bold mt-5">Recommended Career Paths:</h3>
          <ul className="list-disc ml-6 mt-2">
            {analysis.career_paths.map((p) => (
              <li key={p}>{p}</li>
            ))}
          </ul>

          <h3 className="font-bold mt-5">AI-Generated Job Description:</h3>
          <p className="mt-2 text-gray-300">{analysis.job_description}</p>
        </div>
      )}

      {/* COURSE RECOMMENDATIONS */}
      {analysis?.courses && analysis.courses.length > 0 && (
        <div className="mt-10">
          <h2 className="text-2xl font-bold mb-4">Recommended Courses</h2>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {analysis.courses.map((c) => (
              <div key={c.url} className="bg-gray-900 p-5 rounded shadow-lg">
                <h3 className="text-lg font-bold mb-2">{c.title}</h3>
                <p className="text-sm text-gray-300 mb-1">
                  Skill: <strong>{c.skill}</strong>
                </p>
                <p className="text-sm text-gray-400 mb-4">
                  Platform: {c.platform}
                </p>

                <a
                  href={c.url}
                  target="_blank"
                  rel="noreferrer"
                  className="bg-blue-600 px-3 py-2 rounded text-white hover:bg-blue-700 inline-block"
                >
                  View Course →
                </a>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
