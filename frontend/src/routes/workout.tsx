import { createFileRoute } from '@tanstack/react-router';

export const Route = createFileRoute('/workout')({
  component: Workout,
});

function Workout() {
  return (
    <div className="max-w-4xl">
      <h1 className="text-3xl font-bold mb-4">Workout Generator</h1>
      <p className="text-gray-600 mb-6">
        Create your personalized calisthenics workout routine.
      </p>

      <div className="space-y-6">
        <div className="p-6 border rounded-lg">
          <h2 className="text-xl font-semibold mb-4">Workout Configuration</h2>
          <form className="space-y-4">
            <div>
              <label className="block text-sm font-medium mb-2">
                Fitness Level
              </label>
              <select className="w-full px-3 py-2 border rounded-lg">
                <option>Beginner</option>
                <option>Intermediate</option>
                <option>Advanced</option>
              </select>
            </div>

            <div>
              <label className="block text-sm font-medium mb-2">
                Duration (minutes)
              </label>
              <input
                type="number"
                min="15"
                max="120"
                defaultValue="30"
                className="w-full px-3 py-2 border rounded-lg"
              />
            </div>

            <div>
              <label className="block text-sm font-medium mb-2">
                Focus Area
              </label>
              <select className="w-full px-3 py-2 border rounded-lg">
                <option>Full Body</option>
                <option>Upper Body</option>
                <option>Lower Body</option>
                <option>Core</option>
              </select>
            </div>

            <button
              type="submit"
              className="w-full px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
            >
              Generate Workout
            </button>
          </form>
        </div>

        <div className="p-6 border rounded-lg bg-gray-50">
          <p className="text-gray-600">
            Your generated workout will appear here after you submit the form.
          </p>
        </div>
      </div>
    </div>
  );
}
