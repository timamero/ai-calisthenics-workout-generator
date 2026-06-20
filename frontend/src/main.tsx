import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { RouterProvider, createRouter } from "@tanstack/react-router";
import "@mantine/core/styles.css";
import { MantineProvider } from "@mantine/core";

import "./styles/global.css";
import theme, { resolver } from "./theme";

import { routeTree } from "./routeTree.gen";

// Set up a Router instance
const router = createRouter({
  routeTree,
  defaultPreload: "intent",
  scrollRestoration: true,
});

// Register the router instance for type safety
declare module "@tanstack/react-router" {
  interface Register {
    router: typeof router;
  }
}

const rootElement = document.getElementById("root")!;

if (!rootElement.innerHTML) {
  const root = createRoot(rootElement);
  root.render(
    <StrictMode>
      <MantineProvider theme={theme} cssVariablesResolver={resolver}>
        <RouterProvider router={router} />
      </MantineProvider>
    </StrictMode>,
  );
}
