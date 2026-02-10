import { auth } from "@clerk/nextjs/server";
import Link from "next/link";

export default async function Dashboard() {
  const { userId } = await auth();

  return (
    <div className="p-10">
      <h1 className="text-3xl font-bold mb-4">Welcome to Career Booster</h1>
      <p className="text-gray-600 mb-6">
        Upload your resume and get AI-powered skill analysis.
      </p>

      <Link
        href="/resume/upload"
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
      >
        Upload Resume →
      </Link>
    </div>
  );
}
