from typing import List

from app.schemas.setProgressions import SetProgressionsResponseSchema
from app.db.client import get_supabase_client


def get_set_progressions_list() -> List[SetProgressionsResponseSchema]:
    """
    Retrieve list of all set progressions (challenges and assists) from the database.
    Returns:
        List of SetProgressionsResponseSchema objects
    """
    supabase = get_supabase_client()
    try:
        response = (
            supabase.table("set_progressions")
            .select("*")
            .order("display_order")
            .execute()
        )
        return [SetProgressionsResponseSchema(**item) for item in response.data]
    except Exception as e:
        print(f"Error fetching challenges and assists: {e}")
        raise
