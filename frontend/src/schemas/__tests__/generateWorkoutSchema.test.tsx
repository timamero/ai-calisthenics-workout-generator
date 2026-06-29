import { describe, it, expect } from 'vitest';
import {
  GenerateWorkoutFormSchema,
  GenerateWorkoutResponseSchema,
} from '../generateWorkoutSchema';
import { mockGenerateWorkoutResponse } from '../../tests/mocks';

describe('GenerateWorkoutFormSchema', () => {
  it('accepts valid form data', () => {
    const validInput = {
      equipment: ['pull-up-bar', 'rings'],
      fitness_level: 'intermediate',
      target_muscles: ['back', 'core'],
      duration_minutes: 30,
      additional_notes: 'Avoid overhead pressing, shoulder issue',
    };

    const result = GenerateWorkoutFormSchema.safeParse(validInput);
    expect(result.success).toBe(true);
  });

  it('rejects an invalid fitness level', () => {
    const invalidInput = {
      equipment: ['pull-up-bar'],
      fitness_level: 'expert', // not in the allowed enum
      target_muscles: ['back'],
      duration_minutes: 30,
    };

    const result = GenerateWorkoutFormSchema.safeParse(invalidInput);
    expect(result.success).toBe(false);
  });

  it('rejects a negative duration', () => {
    const invalidInput = {
      equipment: [],
      fitnessLevel: 'beginner',
      target_muscles: ['legs'],
      duration_minutes: -5,
    };

    const result = GenerateWorkoutFormSchema.safeParse(invalidInput);
    expect(result.success).toBe(false);
  });

  it('allows additional_notes to be omitted', () => {
    const validInput = {
      equipment: ['pull up bar'],
      fitness_level: 'beginner',
      target_muscles: ['legs'],
      duration_minutes: 20,
    };

    const result = GenerateWorkoutFormSchema.safeParse(validInput);
    expect(result.success).toBe(true);
  });
});

describe('GenerateWorkoutResponseSchema', () => {
  it('accepts valid response dataa', () => {
    const validInput = mockGenerateWorkoutResponse;

    const result = GenerateWorkoutResponseSchema.safeParse(validInput);

    expect(result.success).toBe(true);
  });

  it('rejects an invalid workout_data value', () => {
    const invalidInput = {
      ...mockGenerateWorkoutResponse,
      workout: {
        ...mockGenerateWorkoutResponse.workout,
        workout_data: {
          data: [
            ...mockGenerateWorkoutResponse.workout.workout_data.data,
            {
              id: '00000000-0000-0000-0000-000000000000',
              sets: [
                {
                  id: '00000000-0000-0000-0000-000000000000',
                  fields: {
                    reps: '0', // invalid value
                    rest: 'string',
                    time: 'string',
                    setProgressions: [
                      {
                        id: '00000000-0000-0000-0000-000000000000',
                        value: 0,
                        set_progression_id: 0,
                      },
                    ],
                  },
                  completed: true,
                  completed_at: 'string',
                },
              ],
              type: 'exercise',
              order: 0,
              tracked: ['string'],
              exercise_id: 0,
            },
          ],
        },
      },
    };

    const result = GenerateWorkoutResponseSchema.safeParse(invalidInput);
    expect(result.success).toBe(false);
  });

  it('rejects missing workout', () => {
    const validInput = mockGenerateWorkoutResponse;

    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    const { workout, ...invalidInput } = validInput;

    const result = GenerateWorkoutResponseSchema.safeParse(invalidInput);
    expect(result.success).toBe(false);
  });

  it('rejects missing workout.workout_data.data', () => {
    const invalidInput = {
      ...mockGenerateWorkoutResponse,
      workout: {
        ...mockGenerateWorkoutResponse.workout,
        workout_data: {},
      },
    };

    const result = GenerateWorkoutResponseSchema.safeParse(invalidInput);
    expect(result.success).toBe(false);
  });

  it('rejects invalid workout name', () => {
    const invalidInput = {
      ...mockGenerateWorkoutResponse,
      workout: {
        ...mockGenerateWorkoutResponse.workout,
        name: 1234,
      },
    };

    const result = GenerateWorkoutResponseSchema.safeParse(invalidInput);
    expect(result.success).toBe(false);
  });

  it('rejects invalid remaining_generations', () => {
    const invalidInput = {
      ...mockGenerateWorkoutResponse,
      remaining_generations: 1.4,
    };

    const result = GenerateWorkoutResponseSchema.safeParse(invalidInput);
    expect(result.success).toBe(false);
  });

  it('rejects an invalid fitness level', () => {
    const invalidInput = {
      ...mockGenerateWorkoutResponse,
      workout: {
        ...mockGenerateWorkoutResponse.workout,
        fitness_level: 'expert', // not in the allowed enum
      },
    };

    const result = GenerateWorkoutResponseSchema.safeParse(invalidInput);
    expect(result.success).toBe(false);
  });

  it('rejects a negative duration', () => {
    const invalidInput = {
      ...mockGenerateWorkoutResponse,
      workout: {
        ...mockGenerateWorkoutResponse.workout,
        duration_minutes: -5,
      },
    };

    const result = GenerateWorkoutResponseSchema.safeParse(invalidInput);
    expect(result.success).toBe(false);
  });

  it('allows additional_notes to be omitted', () => {
    const validInput = {
      ...mockGenerateWorkoutResponse,
      workout: {
        name: 'Generated workout name',
        equipment: ['pull up bar'],
        fitness_level: 'beginner',
        target_muscles: ['legs'],
        duration_minutes: 20,
        workout_data: { ...mockGenerateWorkoutResponse.workout.workout_data },
        notes: 'AI notes',
      },
    };

    const result = GenerateWorkoutResponseSchema.safeParse(validInput);

    expect(result.success).toBe(true);
  });

  it('allows notes to be omitted', () => {
    const validInput = {
      ...mockGenerateWorkoutResponse,
      workout: {
        name: 'Generated workout name',
        equipment: ['pull up bar'],
        fitness_level: 'beginner',
        target_muscles: ['legs'],
        duration_minutes: 20,
        workout_data: { ...mockGenerateWorkoutResponse.workout.workout_data },
        additional_notes: 'User notes',
      },
    };

    const result = GenerateWorkoutResponseSchema.safeParse(validInput);

    expect(result.success).toBe(true);
  });
});
