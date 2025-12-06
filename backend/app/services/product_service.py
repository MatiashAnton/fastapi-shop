from sqlalchemy.orm import Session
from typing import List
from backend.app.repositories.product_repository import ProductRepository
from backend.app.repositories.category_repository import CategoryRepository
from backend.app.schemas.product import ProductCreate, ProductResponse, ProductListResponse
from fastapi import HTTPException, status


class ProductService:
	def __init__(self, db: Session):
		self.repository = ProductRepository(db)
		self.category_repository = CategoryRepository(db)

	def get_all_products(self) -> ProductListResponse:
		products = self.repository.get_all_products()
		products_response = [ProductResponse.model_validate(product) for product in products]
		return ProductListResponse(products=products_response, total=len(products_response))

	def get_product_by_id(self, product_id: int) -> ProductResponse:
		product = self.repository.get_product_by_id(product_id)
		if not product:
			raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {product_id} not found")
		return ProductResponse.model_validate(product)
	
	def get_products_by_category(self, category_id: int) -> ProductListResponse:
		category = self.category_repository.get_category_by_id(category_id)
		if not category:
			raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category with id {category_id} not found")
		products = self.repository.get_by_category(category_id)
		products_response = [ProductResponse.model_validate(product) for product in products]
		return ProductListResponse(products=products_response, total=len(products_response))

	def create_product(self, product_data: ProductCreate) -> ProductResponse:
		category = self.category_repository.get_category_by_id(product_data.category_id)
		if not category:
			raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Category with id {product_data.category_id} does not exist")
		product = self.repository.create_product(product_data)
		return ProductResponse.model_validate(product)
	



