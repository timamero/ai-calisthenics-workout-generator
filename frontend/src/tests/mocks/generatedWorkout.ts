export const mockGenerateWorkoutResponse = {
  workout: {
    name: 'Generated workout name',
    equipment: ['pull-up-bar', 'rings'],
    fitness_level: 'intermediate',
    target_muscles: ['back', 'core'],
    duration_minutes: 30,
    additional_notes: 'Avoid overhead pressing, shoulder issue',
    notes: 'AI notes',
    workout_data: {
      data: [
        {
          id: '00000000-0000-0000-0000-000000000000',
          sets: [
            {
              id: '00000000-0000-0000-0000-000000000000',
              fields: {
                reps: 0,
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
        {
          id: '00000000-0000-0000-0000-000000000000',
          name: 'string',
          type: 'section',
          items: [
            {
              id: '00000000-0000-0000-0000-000000000000',
              sets: [
                {
                  id: '00000000-0000-0000-0000-000000000000',
                  fields: {
                    reps: 0,
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
            {
              id: '00000000-0000-0000-0000-000000000000',
              type: 'superset',
              order: 0,
              exercises: [
                {
                  id: '00000000-0000-0000-0000-000000000000',
                  sets: [
                    {
                      id: '00000000-0000-0000-0000-000000000000',
                      fields: {
                        reps: 0,
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
          ],
          order: 0,
        },
        {
          id: '00000000-0000-0000-0000-000000000000',
          type: 'superset',
          order: 0,
          exercises: [
            {
              id: '00000000-0000-0000-0000-000000000000',
              sets: [
                {
                  id: '00000000-0000-0000-0000-000000000000',
                  fields: {
                    reps: 0,
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
      ],
    },
  },
  remaining_generations: 20,
};
