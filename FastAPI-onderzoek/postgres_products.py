from fastapi import APIRouter, HTTPException
from psycopg.errors import UniqueViolation

from schemas import Product
from postgres_database import get_connection

router = APIRouter(prefix="/postgres", tags=["PostgreSQL"])


@router.post("/products", status_code=201)
def create_product(product: Product):
    try:
        with get_connection() as connection:
            # Insert the product into PostgreSQL.
            connection.execute(
                """
                INSERT INTO products (id, name, quantity)
                VALUES (%s, %s, %s)
                """,
                (product.id, product.name, product.quantity),
            )

    except UniqueViolation:
        raise HTTPException(
            status_code=409,
            detail="A product with this ID already exists",
        )

    return product


@router.get("/products")
def get_products():
    with get_connection() as connection:
        rows = connection.execute(
            "SELECT id, name, quantity FROM products ORDER BY id;"
        ).fetchall()

    products = []
    for row in rows:
        products.append({
            "id": row[0],
            "name": row[1],
            "quantity": row[2],
        })

    return products
