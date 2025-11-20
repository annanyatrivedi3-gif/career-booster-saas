'use client';

import { useState, ChangeEvent, useMemo } from 'react';

interface ParsedData {
  skills?: string[];
  projects?: string[];
}

interface Course {
  skill: string;
  title: string;
  platform: string;
  link: string;
}

// LIVE BACKEND URL
const API = "https://career-booster-backend-otft.onrender.com";

const ROLE_SKILL_MAP: Record<string, string[]> = {
  'Frontend Developer': [
    'html', 'css', 'javascript', 'react', 'typescript', 'next.js', 'tailwind', 'responsive design', 'accessibility'
  ],
  'Backend Developer': [
    'node.js', 'express', 'python', 'flask', 'django', 'sql', 'postgresql', 'mongodb', 'rest api', 'docker'
  ],
  'Full Stack Developer': [
    'html', 'css', 'javascript', 'react', 'node.js', 'express', 'sql', 'docker', 'next.js', 'typescript'
  ],
  'Data Scientist': [
    'python', 'pandas', 'numpy', 'scikit-learn', 'machine learning', 'statistics', 'data visualization', 'nlp'
  ],
  'ML Engineer': [
    'python', 'tensorflow', 'pytorch', 'machine learning', 'deep learning', 'mlops', 'docker', 'model deployment'
  ],
  'DevOps Engineer': [
    'linux', 'docker', 'kubernetes', 'ci/cd', 'terraform', 'aws', 'monitoring', 'observability'
  ],
  'BI Analyst': [
    'excel', 'power bi', 'tableau', 'sql', 'data visualization', 'dax', 'power query'
  ],
  'Embedded Engineer': [
    'embedded c', 'arduino', 'raspberry pi', 'microcontroller', 'electronics', 'pcb design', 'iot'
  ],
  'Product Manager': [
    'product management', 'agile', 'scrum', 'stakeholder management', 'roadmapping', 'communication'
  ],
  'Security Engineer': [
    'cybersecurity', 'networking', 'penetration testing', 'linux', 'ethical hacking', 'security fundamentals'
  ]
};

const GENERAL_VALUE_SKILLS = [
  'git', 'github', 'communication', 'leadership', 'problem solving', 'project management',
  'sql', 'docker', 'testing', 'unit testing', 'ci/cd', 'aws', 'azure', 'power bi', 'tableau',
  'data visualization', 'regex', 'linux', 'typescript', 'api design'
];

export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [parsedData, setParsedData] = useState<ParsedData | null>(null);
  const [manualSkills, setManualSkills] = useState('');
  const [missingSkills, setMissingSkills] = useState<string[]>([]);
  const [gapData, setGapData] = useState<Course[]>([]);
  const [selectedRole, setSelectedRole] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const normalize = (s: string) => s.trim().toLowerCase();

  const parsedSkillSet = useMemo(() => {
    const arr = parsedData?.skills ?? [];
    return new Set(arr.map(s => normalize(s)));
  }, [parsedData]);

  const detectBestRole = () => {
    if (!parsedData?.skills || parsedData.skills.length === 0) return '';
    let bestRole = '';
    let bestScore = -1;

    for (const role of Object.keys(ROLE_SKILL_MAP)) {
      const desired = ROLE_SKILL_MAP[role].map(normalize);
      const overlap = desired.filter(d => parsedSkillSet.has(d)).length;
      if (overlap > bestScore) {
        bestScore = overlap;
        bestRole = role;
      }
    }
    return bestRole;
  };

  const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
    setFile(e.target.files?.[0] ?? null);
  };

  const handleUpload = async () => {
    if (!file) {
      setError('Choose a resume file first (.pdf/.docx).');
      return;
    }

    setLoading(true);
    setError('');
    setParsedData(null);
    setGapData([]);
    setMissingSkills([]);

    const formData = new FormData();
    formData.append('resume', file);

    try {
      const res = await fetch(`${API}/upload`, {
        method: 'POST',
        body: formData
      });

      if (!res.ok) {
        setError(`Backend error: ${res.status}`);
        return;
      }

      const data = await res.json();
      if (!data.skills) data.skills = [];
      if (!data.projects) data.projects = [];
      setParsedData(data);

      if (!selectedRole) {
        const detected = detectBestRole();
        if (detected) setSelectedRole(detected);
      }
    } catch (err) {
      console.error(err);
      setError('Error connecting to backend.');
    } finally {
      setLoading(false);
    }
  };

  const addMissingSkills = () => {
    if (!parsedData) return;
    const newList = manualSkills.split(',')
      .map(s => s.trim())
      .filter(s => s.length > 0);

    if (newList.length === 0) return;

    const combined = Array.from(new Set([...(parsedData.skills || []), ...newList]));
    setParsedData({ ...parsedData, skills: combined });
    setManualSkills('');
  };

  const computeMissingForRole = (role: string) => {
    const desired = ROLE_SKILL_MAP[role]?.map(normalize) || [];
    const missing = desired.filter(d => !parsedSkillSet.has(d));

    const extras = GENERAL_VALUE_SKILLS
      .map(normalize)
      .filter(g => !parsedSkillSet.has(g) && !missing.includes(g))
      .slice(0, 3);

    const combined = [...missing, ...extras];

    return combined.map(s => s
      .split(' ')
      .map(w => w.charAt(0).toUpperCase() + w.slice(1))
      .join(' ')
    );
  };

  const analyzeSkillGap = async () => {
    if (!parsedData || !parsedData.skills || parsedData.skills.length === 0) {
      setError('Upload resume or add skills first.');
      return;
    }

    const role = selectedRole || detectBestRole();
    if (!role) {
      setError('Select a role or upload a resume with clear skills.');
      return;
    }

    setLoading(true);
    setError('');
    setGapData([]);
    setMissingSkills([]);

    const missing = computeMissingForRole(role);
    setMissingSkills(missing);

    try {
      const payloadSkills = missing.map(s => s.toLowerCase());

      const res = await fetch(`${API}/course-recommendations`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ missing_skills: payloadSkills })
      });

      if (!res.ok) {
        setError(`Backend error: ${res.status}`);
        return;
      }

      const data = await res.json();
      setGapData(data.courses || []);
    } catch (err) {
      console.error(err);
      setError('Error connecting to backend.');
    } finally {
      setLoading(false);
    }
  };

  const roleOptions = Object.keys(ROLE_SKILL_MAP);

  return (
    <main className="min-h-screen bg-neutral-900 text-slate-100 flex items-center justify-center p-6">
      <div className="w-full max-w-4xl">
        <header className="mb-6 text-center">
          <h1 className="text-4xl font-extrabold text-white">Career Booster</h1>
          <p className="mt-2 text-slate-300">
            Role-based skill gap analysis + course recommendations
          </p>
        </header>

        <section className="bg-neutral-850/60 border border-neutral-800 rounded-2xl shadow-2xl p-6">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

            {/* LEFT */}
            <div className="p-4 space-y-4">
              <label className="block text-sm font-medium text-slate-300">Upload Resume (PDF/DOCX)</label>
              <input
                type="file"
                accept=".pdf,.docx"
                onChange={handleFileChange}
                className="block w-full text-sm text-slate-200 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:bg-neutral-700 file:text-cyan-200"
              />

              <div>
                <label className="block text-sm font-medium text-slate-300">Select Role</label>
                <select
                  value={selectedRole}
                  onChange={(e) => setSelectedRole(e.target.value)}
                  className="mt-2 w-full bg-neutral-800 text-slate-100 px-3 py-2 rounded-md border border-neutral-700"
                >
                  <option value="">-- Auto Detect --</option>
                  {roleOptions.map(r => (
                    <option key={r} value={r}>{r}</option>
                  ))}
                </select>
              </div>

              <div className="flex gap-3">
                <button
                  onClick={handleUpload}
                  className="flex-1 bg-cyan-600 hover:bg-cyan-500 text-neutral-900 font-semibold py-2 rounded-md"
                >
                  Upload & Parse
                </button>

                <button
                  onClick={analyzeSkillGap}
                  className="flex-1 bg-indigo-700 hover:bg-indigo-600 text-white font-semibold py-2 rounded-md"
                >
                  Analyse Skill Gap
                </button>
              </div>

              <div className="text-sm text-slate-400">
                <p>
                  Status: {loading ? <span className="text-yellow-300">Processing...</span> : <span className="text-emerald-400">Idle</span>}
                </p>
                {error && <p className="text-red-400 mt-2">{error}</p>}
              </div>

              {/* Add Skills */}
              <div className="mt-4">
                <label className="block text-sm text-slate-300">Add Missing Skills (comma separated)</label>
                <input
                  value={manualSkills}
                  onChange={(e) => setManualSkills(e.target.value)}
                  placeholder="e.g. Power BI, Kubernetes"
                  className="mt-2 w-full px-3 py-2 rounded-md bg-neutral-800 text-slate-100 border border-neutral-700"
                />
                <div className="mt-2 flex gap-2">
                  <button onClick={addMissingSkills} className="bg-emerald-600 hover:bg-emerald-500 px-3 py-1 rounded-md text-neutral-900 font-medium">
                    Add
                  </button>
                  <button onClick={() => setManualSkills('')} className="bg-neutral-700 hover:bg-neutral-650 px-3 py-1 rounded-md text-slate-200">
                    Clear
                  </button>
                </div>
              </div>
            </div>

            {/* RIGHT */}
            <div className="p-4 bg-neutral-850 rounded-xl border border-neutral-800">
              <h3 className="text-lg font-semibold text-white mb-3">Parsed Resume</h3>

              {/* SKILLS */}
              <div className="mb-4">
                <div className="flex justify-between items-center mb-2">
                  <span className="text-sm text-slate-300">Skills</span>
                  <span className="text-xs text-slate-400">{parsedData?.skills?.length ?? 0}</span>
                </div>

                <div className="max-h-40 overflow-auto rounded">
                  <table className="w-full text-left">
                    <tbody>
                      {(parsedData?.skills?.length ?? 0) > 0 ? (
                        parsedData!.skills!.map((s, i) => (
                          <tr key={i} className="odd:bg-neutral-860 even:bg-neutral-855">
                            <td className="px-3 py-2 text-slate-100">{s}</td>
                          </tr>
                        ))
                      ) : (
                        <tr><td className="px-3 py-3 text-slate-400">No skills parsed.</td></tr>
                      )}
                    </tbody>
                  </table>
                </div>
              </div>

              {/* PROJECTS */}
              <div>
                <div className="flex justify-between items-center mb-2">
                  <span className="text-sm text-slate-300">Projects</span>
                  <span className="text-xs text-slate-400">{parsedData?.projects?.length ?? 0}</span>
                </div>

                <div className="max-h-40 overflow-auto rounded">
                  <table className="w-full text-left">
                    <tbody>
                      {(parsedData?.projects?.length ?? 0) > 0 ? (
                        parsedData!.projects!.map((p, i) => (
                          <tr key={i} className="odd:bg-neutral-860 even:bg-neutral-855">
                            <td className="px-3 py-2 text-slate-100">{p}</td>
                          </tr>
                        ))
                      ) : (
                        <tr><td className="px-3 py-3 text-slate-400">No projects found.</td></tr>
                      )}
                    </tbody>
                  </table>
                </div>
              </div>
            </div>

          </div>

          {/* Missing Skills */}
          {missingSkills.length > 0 && (
            <div className="mt-6 bg-neutral-850 border border-neutral-800 rounded-md p-4">
              <h3 className="text-md font-semibold text-cyan-300 mb-2">Recommended Skills</h3>
              <div className="grid grid-cols-2 md:grid-cols-4 gap-2">
                {missingSkills.map((ms, i) => (
                  <div key={i} className="px-3 py-2 rounded-md bg-neutral-800 border border-neutral-750 text-slate-100 text-sm">
                    {ms}
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Course Recommendations */}
          {gapData.length > 0 && (
            <div className="mt-6 bg-neutral-850 border border-neutral-800 rounded-md p-4">
              <h3 className="text-md font-semibold text-cyan-300 mb-3">Recommended Courses</h3>

              <div className="overflow-auto max-h-72">
                <table className="w-full text-left">
                  <thead>
                    <tr className="text-xs text-slate-400">
                      <th className="px-3 py-2">Skill</th>
                      <th className="px-3 py-2">Course</th>
                      <th className="px-3 py-2">Platform</th>
                      <th className="px-3 py-2">Link</th>
                    </tr>
                  </thead>
                  <tbody>
                    {gapData.map((c, i) => (
                      <tr key={i} className="odd:bg-neutral-860 even:bg-neutral-855">
                        <td className="px-3 py-2 text-slate-100">{c.skill}</td>
                        <td className="px-3 py-2 text-slate-100">{c.title}</td>
                        <td className="px-3 py-2 text-cyan-200">{c.platform}</td>
                        <td className="px-3 py-2">
                          <a href={c.link} target="_blank" className="text-indigo-300 underline">View</a>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          <div className="mt-4 text-xs text-slate-500">Tip: Auto-detect role works best with resumes containing technical skills.</div>
        </section>
      </div>
    </main>
  );
}
