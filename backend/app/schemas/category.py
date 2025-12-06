from pydantic import BaseModel, Field
from typing import Optional


class CategoryBase(BaseModel):
	name: str = Field(..., min_length=5, max_length=100, description="Category Name")
	slug: Optional[str] = Field(None, title="URL-friendly category name", max_length=255)


class CategoryCreate(CategoryBase):
	pass


class CategoryResponse(CategoryBase):
	id: int = Field(..., description="Unique category identifier")

	class Config:
		form_attributes = True