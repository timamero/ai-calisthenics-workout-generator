import { createFileRoute } from '@tanstack/react-router';
import { Container, Title, Text, Stack, Paper } from '@mantine/core';

export const Route = createFileRoute('/')({
  component: Home,
});

export function Home() {
  return (
    <Container size="lg" py="xl">
      <Stack gap="xl">
        <Stack gap="sm">
          <Title order={1}>AI Calisthenics Workout Generator</Title>
          <Text c="dimmed" size="md">
            Create personalized calisthenics workout routines powered by AI.
          </Text>
        </Stack>

        <Stack gap="md">
          <Paper p="lg" radius="md" bg="blue.0" withBorder>
            <Stack gap="sm">
              <Title order={2} size="lg">
                Welcome!
              </Title>
              <Text c="dark">
                This application helps you generate custom calisthenics workouts
                tailored to your fitness level and goals.
              </Text>
            </Stack>
          </Paper>

          <Paper p="lg" radius="md" bg="green.0" withBorder>
            <Stack gap="sm">
              <Title order={2} size="lg">
                Get Started
              </Title>
              <Text c="dark">
                Head over to the <strong>Workout</strong> section to begin
                generating your personalized routine.
              </Text>
            </Stack>
          </Paper>
        </Stack>
      </Stack>
    </Container>
  );
}
