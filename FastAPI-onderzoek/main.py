from fastapi import FastAPI, HTTPException
from schemas import Product
import products
import orders 
import postgres_products
from postgres_database import get_connection

app = FastAPI()

app.include_router(products.router)
app.include_router(orders.router)
app.include_router(postgres_products.router)

@app.get("/")
def say_hello():
    return {"message": "Hello Basel"}





@app.get("/postgres/test")
def test_postgres_connection():
    with get_connection() as connection:
        result = connection.execute(
            "SELECT current_database();"
        ).fetchone()

        if result is None:
            raise HTTPException(
                status_code=500,
                detail="The query returned no result",
            )

        return {
            "message": "Connected to PostgreSQL",
            "database": result[0],
        }