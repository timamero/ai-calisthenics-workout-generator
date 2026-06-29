import { z } from 'zod';

export const WorkoutBase = z.object({
  equipment: z.array(z.string()),
  fitness_level: z.union([
    z.literal('beginner'),
    z.literal('intermediate'),
    z.literal('advanced'),
  ]),
  target_muscles: z.array(z.string()),
  duration_minutes: z.number().int(),
  additional_notes: z.string().nullish(),
});

const SetProgressionSchema = z.object({
  id: z.string(),
  set_progression_id: z.number(),
  value: z.union([z.number(), z.string(), z.null()]),
});

const SetFieldsSchema = z.object({
  reps: z.nullable(z.number()),
  time: z.nullable(z.string()), // ISO 8601 duration
  rest: z.nullable(z.string()), // ISO 8601 duration
  setProgressions: z.nullable(z.array(SetProgressionSchema)),
});

const SetSchema = z.object({
  id: z.string(),
  fields: SetFieldsSchema,
  completed: z.boolean(),
  completed_at: z.nullable(z.string()), // ISO 8601 datetime
});

const ExerciseSchema = z.object({
  id: z.string(),
  exercise_id: z.number(),
  order: z.number(),
  type: z.literal('exercise'),
  tracked: z.array(z.string()),
  sets: z.array(SetSchema),
});

const SupersetSchema = z.object({
  id: z.string(),
  order: z.number(),
  type: z.literal('superset'),
  exercises: z.array(ExerciseSchema),
});

const SectionSchema = z.object({
  id: z.string(),
  name: z.nullable(z.string()),
  order: z.number(),
  type: z.literal('section'),
  items: z.array(z.union([ExerciseSchema, SupersetSchema])),
});

export const WorkoutDataSchema = z.object({
  data: z.array(z.union([ExerciseSchema, SectionSchema, SupersetSchema])),
});

export const GenerateWorkoutRequestSchema = WorkoutBase.extend({
  equipment: z.array(z.string()).min(1),
  target_muscles: z.array(z.string()).min(1),
  duration_minutes: z.number().int().min(1),
});

export const DetailedWorkout = WorkoutBase.extend({
  name: z.string(),
  workout_data: WorkoutDataSchema,
});

export const GenerateWorkoutResponseSchema = z.object({
  workout: DetailedWorkout,
  remaining_generations: z.number().int(),
});
