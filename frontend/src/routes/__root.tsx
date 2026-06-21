import { Link, Outlet, createRootRoute } from '@tanstack/react-router';
import { TanStackRouterDevtools } from '@tanstack/react-router-devtools';
import { Box, Container, Group, NavLink, Stack, Text } from '@mantine/core';

export const Route = createRootRoute({
  component: RootComponent,
  notFoundComponent: () => {
    return (
      <Container size="lg" py="xl">
        <Stack gap="md">
          <Text size="lg" fw={600}>
            This page does not exist
          </Text>
          <Link to="/" className="mantine-UnstyledButton-root">
            <Text c="blue" td="underline">
              Start Over
            </Text>
          </Link>
        </Stack>
      </Container>
    );
  },
});

function RootComponent() {
  return (
    <>
      <Box height={60} px="md" py="xs" withBorder>
        <Group justify="flex-start" gap="lg" h="100%">
          <NavLink
            component={Link}
            to="/"
            label="Home"
            activeProps={{
              fw: 700,
              c: 'blue',
            }}
            activeOptions={{ exact: true }}
          />
          <NavLink
            component={Link}
            to="/workout"
            label="Workout"
            activeProps={{
              fw: 700,
              c: 'blue',
            }}
          />
        </Group>
      </Box>

      <main>
        <Container size="lg" py="lg">
          <Outlet />
        </Container>
      </main>

      <TanStackRouterDevtools position="bottom-right" initialIsOpen={false} />
    </>
  );
}
