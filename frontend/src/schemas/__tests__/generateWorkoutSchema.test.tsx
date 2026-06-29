import { describe, it, expect } from 'vitest';
import { GenerateWorkoutFormSchema } from '../generateWorkoutSchema';

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
