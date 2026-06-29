from typing import Literal

from pydantic import BaseModel, Field


class GenerateWorkoutRequestSchema(BaseModel):
    equipment: list[str] = Field(min_length=1)
    fitness_level: Literal["beginner", "intermediate", "advanced"]
    target_muscles: list[str] = Field(min_length=1)
    duration_minutes: int = Field(ge=1)
    additional_notes: str | None = None
