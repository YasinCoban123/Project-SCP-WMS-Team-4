from fastapi import APIRouter, HTTPException
from schemas import Product
from database import products_collection

router = APIRouter()

products: list[Product] = []

# @router.post("/products", status_code=201)
# def create_product(product: Product):
#     products.append(product)
#     return product

@router.post("/products", status_code=201)
def create_product(product: Product):
    # Convert the Product object into a Python dictionary.
    product_data = product.model_dump()
    # Save the product in the MongoDB products collection.
    products_collection.insert_one(product_data)
    return product

# @router.get("/products")
# def get_products():
#     return products

@router.get("/products")
def get_products():
    # Read all products without MongoDB's internal _id field.
    products = list(products_collection.find({}, {"_id": 0}))

    # Return the products to the client.
    return products

# @router.put("/products/{product_id}")
# def update_product(product_id: int, updated_product: Product):
#     if updated_product.id != product_id:
#         raise HTTPException(status_code=400, detail="Product ID must match the ID in the URL") 
  
#     for index, product in enumerate(products): # enumerate gives an object with its index 
#         if product.id == product_id:
#             products[index] = updated_product
#             return updated_product
#     raise HTTPException(status_code=404, detail="Product not found")



@router.put("/products/{product_id}")
def update_product(product_id: int, updated_product: Product):
    # Check that the body ID matches the URL ID.
    if updated_product.id != product_id:
        raise HTTPException(
            status_code=400,
            detail="Product ID must match the ID in the URL"
        )

    # Find the product by its ID and update its fields.
    result = products_collection.update_one(
        {"id": product_id},
        {"$set": updated_product.model_dump()}
    )

    # Return 404 if no product matched the ID.
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")

    return updated_product

@router.delete("/products/{product_id}")
def delete_product(product_id: int):
    # Delete one product with the matching ID.
    result = products_collection.delete_one({"id": product_id})

    # Return 404 if no product was deleted.
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")

    return {"message": "Product deleted"}