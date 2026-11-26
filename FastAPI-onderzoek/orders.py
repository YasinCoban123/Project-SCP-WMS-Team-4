from fastapi import APIRouter

router = APIRouter()


@router.get("/orders")
def get_orders():
    return [{"id": 10, "reference": "ORDER-10"}]