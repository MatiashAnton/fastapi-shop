from sqlalchemy.orm import Session
from typing import List
from backend.app.repositories.category_repository import CategoryRepository
from backend.app.schemas.category import CategoryCreate, CategoryResponse
from fastapi import HTTPException, status


class CategoryService:
	def __init__(self, db: Session):
		self.db = db
		self.repository = CategoryRepository(db)

	def get_all_categories(self) -> List[CategoryResponse]:
		categories = self.repository.get_all_categories()
		return [CategoryResponse.model_validate(category) for category in categories]

	def get_category_by_id(self, category_id: int) -> CategoryResponse:
		category = self.repository.get_category_by_id(category_id)
		if not category:
			raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category with id {category_id} not found")
		return CategoryResponse.model_validate(category)
	
	def create_category(self, category_data: CategoryCreate) -> CategoryResponse:
		category = self.repository.create_category(category_data)
		return CategoryResponse.model_validate(category)



