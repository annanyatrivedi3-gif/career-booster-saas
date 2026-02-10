"use client";

import { useState } from "react";
import { Upload, FileText, Search, Loader2, CheckCircle } from "lucide-react";
import { ROLES } from "@/data/roles";

type ParsedResume = {
  parsed: {
    text: string;
    skills: string[];
  };
};

type Course = {
  skill: string;
  title: string;
  platform: string;
  url: string;
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

export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [parsed, setParsed] = useState<ParsedResume | null>(null);
  const [selectedRole, setSelectedRole] = useState("");
  const [analysis, setAnalysis] = useState<AnalysisResponse | null>(null);
  const [loading, setLoading] = useState(false);

  // -------------------------------
  // Upload Resume
  // -------------------------------
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

      const json = (await res.json()) as ParsedResume;
      setParsed(json);
      setAnalysis(null);
    } catch {
      alert("Upload failed!");
    }

    setLoading(false);
  };

  // -------------------------------
  // Analyze Resume
  // -------------------------------
  const handleAnalyze = async () => {
    if (!parsed) {
      alert("Upload resume first");
      return;
    }

    if (!selectedRole) {
      alert("Select a target role");
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

      const json = (await res.json()) as AnalysisResponse;
      setAnalysis(json);
    } catch {
      alert("Analysis failed!");
    }

    setLoading(false);
  };

  return (
    <div className="min-h-screen p-10 bg-gradient-to-br from-[#0A0A0F] via-[#141421] to-black text-white">
      <div className="max-w-4xl mx-auto space-y-10">

        <h1 className="text-5xl font-extrabold text-center tracking-tight bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">
          AI Resume Analyzer
        </h1>

        {/* UPLOAD BOX */}
        <div className="bg-white/5 border border-white/10 p-8 rounded-2xl backdrop-blur-xl shadow-xl space-y-4">
          <h2 className="text-xl font-semibold flex items-center gap-2">
            <Upload className="text-blue-400" />
            Upload Your Resume
          </h2>

          <label className="block p-6 border border-white/10 bg-white/5 rounded-xl cursor-pointer hover:bg-white/10 transition">
            <div className="flex flex-col items-center">
              <FileText className="w-10 h-10 text-gray-300 mb-2" />
              <span className="text-gray-300 text-center">
                {file ? file.name : "Click to select your resume (.pdf or .docx)"}
              </span>
            </div>

            <input
              type="file"
              accept=".pdf,.doc,.docx"
              className="hidden"
              onChange={(event) =>
                setFile(event.target.files ? event.target.files[0] : null)
              }
            />
          </label>

          <button
            onClick={handleUpload}
            disabled={loading}
            className="w-full bg-gradient-to-r from-blue-600 to-indigo-600 hover:opacity-90 py-3 rounded-xl text-lg font-semibold flex justify-center items-center gap-2 disabled:opacity-50"
          >
            {loading ? <Loader2 className="animate-spin" /> : <Upload />}
            {loading ? "Processing..." : "Upload & Extract"}
          </button>
        </div>

        {/* SKILLS DISPLAY */}
        {parsed && (
          <div className="bg-white/5 border border-white/10 p-8 rounded-2xl backdrop-blur-xl shadow-xl">
            <h2 className="text-2xl font-bold mb-4">Extracted Skills</h2>
            <div className="flex flex-wrap gap-2">
              {parsed.parsed.skills.map((skill) => (
                <span
                  key={skill}
                  className="px-3 py-1 rounded-lg bg-blue-500/20 text-blue-300 border border-blue-500/30 text-sm"
                >
                  {skill}
                </span>
              ))}
            </div>
          </div>
        )}

        {/* ROLE SELECT */}
        {parsed && (
          <div className="bg-white/5 border border-white/10 p-8 rounded-2xl backdrop-blur-xl shadow-xl space-y-4">
            <h2 className="text-xl font-bold flex items-center gap-2">
              <Search className="text-purple-400" />
              Select Target Role
            </h2>

            <select
              value={selectedRole}
              onChange={(e) => setSelectedRole(e.target.value)}
              className="w-full p-3 rounded-xl bg-black/30 border border-white/10 text-white"
            >
              <option value="">Choose a role…</option>
              {ROLES.map((role) => (
                <option key={role} value={role}>
                  {role}
                </option>
              ))}
            </select>

            <button
              onClick={handleAnalyze}
              disabled={loading}
              className="w-full bg-gradient-to-r from-purple-600 to-pink-600 hover:opacity-90 py-3 rounded-xl text-lg font-semibold flex justify-center items-center gap-2 disabled:opacity-50"
            >
              {loading ? <Loader2 className="animate-spin" /> : <Search />}
              {loading ? "Analyzing..." : "Analyze Resume"}
            </button>
          </div>
        )}

        {/* ANALYSIS RESULTS */}
        {analysis && (
          <div className="bg-white/5 border border-white/10 p-8 rounded-2xl backdrop-blur-xl shadow-xl space-y-6">
            <h2 className="text-2xl font-bold flex items-center gap-2">
              <CheckCircle className="text-green-400" />
              Analysis Results
            </h2>

            <p className="text-lg">
              <strong>Match Score:</strong>{" "}
              <span className="text-green-300">{analysis.match_score}%</span>
            </p>

            <p className="text-lg">
              <strong>Estimated Salary:</strong>{" "}
              {analysis.salary_range.min} - {analysis.salary_range.max}
            </p>

            <h3 className="text-xl font-semibold mt-6">Missing Skills</h3>
            <ul className="list-disc ml-6 text-red-300">
              {analysis.missing.map((skill) => (
                <li key={skill}>{skill}</li>
              ))}
            </ul>

            <h3 className="text-xl font-semibold mt-6">Career Paths</h3>
            <ul className="list-disc ml-6 text-blue-300">
              {analysis.career_paths.map((path) => (
                <li key={path}>{path}</li>
              ))}
            </ul>

            <h3 className="text-xl font-semibold mt-6">AI-Generated Job Description</h3>
            <p className="text-gray-300">{analysis.job_description}</p>
          </div>
        )}

        {/* COURSES */}
        {analysis?.courses && analysis.courses.length > 0 && (
          <div className="bg-white/5 border border-white/10 p-8 rounded-2xl backdrop-blur-xl shadow-xl space-y-4">
            <h2 className="text-2xl font-bold">Recommended Courses</h2>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {analysis.courses.map((course) => (
                <div
                  key={course.url}
                  className="bg-black/30 border border-white/10 rounded-xl p-5 hover:border-blue-500 transition"
                >
                  <h3 className="font-semibold text-lg">{course.title}</h3>
                  <p className="text-sm text-gray-300 mt-1">
                    Skill: <strong>{course.skill}</strong>
                  </p>
                  <p className="text-sm text-gray-400">Platform: {course.platform}</p>

                  <a
                    href={course.url}
                    target="_blank"
                    className="mt-3 inline-block bg-blue-600 hover:bg-blue-700 px-3 py-2 rounded-lg text-white text-sm"
                  >
                    View Course →
                  </a>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
