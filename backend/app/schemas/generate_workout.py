from typing import List, Optional, Literal
from uuid import UUID

from pydantic import BaseModel, Field


class WorkoutBase(BaseModel):
    equipment: list[str]
    fitness_level: Literal["beginner", "intermediate", "advanced"]
    target_muscles: list[str]
    duration_minutes: int
    additional_notes: str | None = None


class GenerateWorkoutRequestSchema(WorkoutBase):
    equipment: list[str] = Field(min_length=1)
    target_muscles: list[str] = Field(min_length=1)
    duration_minutes: int = Field(ge=1)


class SetProgressionSchema(BaseModel):
    id: UUID
    set_progression_id: int
    value: Optional[int | str] = None


class SetFieldsSchema(BaseModel):
    reps: Optional[int] = None
    time: Optional[str] = None  # ISO 8601 duration string
    rest: Optional[str] = None  # ISO 8601 duration string
    setProgressions: Optional[List[SetProgressionSchema]]


class SetSchema(BaseModel):
    id: UUID
    completed: bool
    completed_at: Optional[str] = None  # ISO 8601 timestamp or null
    fields: SetFieldsSchema


class WorkoutExerciseSchema(BaseModel):
    id: UUID
    exercise_id: int
    tracked: List[str]
    order: int
    type: Literal["exercise"] = "exercise"
    sets: List[SetSchema]


class SupersetSchema(BaseModel):
    id: UUID
    order: int
    type: Literal["superset"] = "superset"
    exercises: List[WorkoutExerciseSchema]


class SectionSchema(BaseModel):
    id: UUID
    name: Optional[str]
    order: int
    type: Literal["section"] = "section"
    items: List[WorkoutExerciseSchema | SupersetSchema]


class WorkoutDataSchema(BaseModel):
    data: List[WorkoutExerciseSchema | SectionSchema | SupersetSchema]


class DetailedWorkout(WorkoutBase):
    name: str
    workout_data: WorkoutDataSchema


class GenerateWorkoutResponseSchema(BaseModel):
    workout: DetailedWorkout
    remaining_generations: int
