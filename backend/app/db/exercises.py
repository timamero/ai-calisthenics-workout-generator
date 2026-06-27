from app.db.client import get_supabase_client
from app.schemas.exercise import ExerciseFilterParams


def get_exercises(filter_query: ExerciseFilterParams):
    supabase = get_supabase_client()

    muscles = filter_query.muscles
    equipments = filter_query.equipments
    difficulty = filter_query.difficulty
    emphasis = filter_query.emphasis
    q = filter_query.q

    try:
        query = supabase.table("exercises").select("*")

        conditions = ""

        if muscles:
            muscle_conditions = ",".join(
                [f'target_muscles.cs.{{"{m}"}}' for m in muscles]
            )
            conditions = conditions + muscle_conditions

        if equipments:
            equipment_conditions = ",".join(
                [f'required_equipment.cs.{{"{e}"}}' for e in equipments]
            )
            conditions = conditions + "," + equipment_conditions

        if conditions:
            query = query.or_(conditions)

        if difficulty:
            query.eq("difficulty", difficulty)

        if emphasis:
            query.eq("emphasis", emphasis)

        if q:
            query.ilike("name", f"%{q}%")

        response = query.execute()
        return response.data
    except Exception as e:
        print(f"Error fetching exercises: {e}")
