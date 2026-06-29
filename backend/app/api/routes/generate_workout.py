from fastapi import APIRouter

from ...schemas.generate_workout import GenerateWorkoutRequestSchema

router = APIRouter(prefix="/generate-workout")


@router.post(
    "/",
)
def generate_workout(request: GenerateWorkoutRequestSchema):
    """Generate a workout plan from validated user input."""
    return {
        "workout": {
            "name": "Stub calisthenics workout",
            "equipment": request.equipment,
            "fitness_level": request.fitness_level,
            "target_muscles": request.target_muscles,
            "duration_minutes": request.duration_minutes,
            "additional_notes": request.additional_notes,
            "exercises": [],
        },
        "remaining_generations": 20,
    }
