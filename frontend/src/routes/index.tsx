import { createFileRoute } from '@tanstack/react-router';

export const Route = createFileRoute('/')({
  component: Home,
});

function Home() {
  return (
    <div className="max-w-4xl">
      <h1 className="text-3xl font-bold mb-4">
        AI Calisthenics Workout Generator
      </h1>
      <p className="text-gray-600 mb-6">
        Create personalized calisthenics workout routines powered by AI.
      </p>
      <div className="space-y-4">
        <div className="p-4 bg-blue-50 rounded-lg">
          <h2 className="text-lg font-semibold mb-2">Welcome!</h2>
          <p className="text-gray-700">
            This application helps you generate custom calisthenics workouts
            tailored to your fitness level and goals.
          </p>
        </div>
        <div className="p-4 bg-green-50 rounded-lg">
          <h2 className="text-lg font-semibold mb-2">Get Started</h2>
          <p className="text-gray-700">
            Head over to the <strong>Workout</strong> section to begin
            generating your personalized routine.
          </p>
        </div>
      </div>
    </div>
  );
}
