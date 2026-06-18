import { Link, Outlet, createRootRoute } from "@tanstack/react-router";
import { TanStackRouterDevtools } from "@tanstack/react-router-devtools";

export const Route = createRootRoute({
  component: RootComponent,
  notFoundComponent: () => {
    return (
      <div className="p-4">
        <p className="text-lg font-semibold">This page does not exist</p>
        <Link to="/" className="text-blue-600 hover:underline">
          Start Over
        </Link>
      </div>
    );
  },
});

function RootComponent() {
  return (
    <>
      <div className="p-4 border-b">
        <nav className="flex gap-4 text-lg">
          <Link
            to="/"
            activeProps={{
              className: "font-bold text-blue-600",
            }}
            activeOptions={{ exact: true }}
            className="hover:text-blue-600 transition-colors"
          >
            Home
          </Link>
          <Link
            to="/workout"
            activeProps={{
              className: "font-bold text-blue-600",
            }}
            className="hover:text-blue-600 transition-colors"
          >
            Workout
          </Link>
        </nav>
      </div>

      <main className="p-4">
        <Outlet />
      </main>

      <TanStackRouterDevtools position="bottom-right" initialIsOpen={false} />
    </>
  );
}
