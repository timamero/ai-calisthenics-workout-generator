import { createFileRoute } from '@tanstack/react-router';
import {
  Container,
  Title,
  Text,
  Stack,
  Paper,
  Select,
  NumberInput,
  Button,
} from '@mantine/core';
import { useState } from 'react';

export const Route = createFileRoute('/workout')({
  component: Workout,
});

function Workout() {
  const [fitnessLevel, setFitnessLevel] = useState<string | null>('Beginner');
  const [duration, setDuration] = useState<number | string>(30);
  const [focusArea, setFocusArea] = useState<string | null>('Full Body');

  return (
    <Container size="lg" py="xl">
      <Stack gap="xl">
        <Stack gap="sm">
          <Title order={1}>Workout Generator</Title>
          <Text c="dimmed" size="md">
            Create your personalized calisthenics workout routine.
          </Text>
        </Stack>

        <Paper p="lg" radius="md" withBorder>
          <Stack gap="md">
            <Title order={2} size="lg">
              Workout Configuration
            </Title>

            <form>
              <Stack gap="md">
                <Select
                  label="Fitness Level"
                  placeholder="Select fitness level"
                  value={fitnessLevel}
                  onChange={setFitnessLevel}
                  data={['Beginner', 'Intermediate', 'Advanced']}
                  searchable
                />

                <NumberInput
                  label="Duration (minutes)"
                  placeholder="Enter duration"
                  value={duration}
                  onChange={setDuration}
                  min={15}
                  max={120}
                />

                <Select
                  label="Focus Area"
                  placeholder="Select focus area"
                  value={focusArea}
                  onChange={setFocusArea}
                  data={['Full Body', 'Upper Body', 'Lower Body', 'Core']}
                  searchable
                />

                <Button type="submit" fullWidth size="md">
                  Generate Workout
                </Button>
              </Stack>
            </form>
          </Stack>
        </Paper>

        <Paper p="lg" radius="md" bg="gray.0" withBorder>
          <Text c="dimmed" ta="center">
            Your generated workout will appear here after you submit the form.
          </Text>
        </Paper>
      </Stack>
    </Container>
  );
}
