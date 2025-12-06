from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from .category import CategoryResponse


class ProductBase(BaseModel):
	name: str = Field(..., min_length=5, max_length=100, description="Product Name")
	description: Optional[str] = Field(None, max_length=500, description="Product Description")
	price: float = Field(..., gt=0, description="Product Price")
	category_id: int = Field(..., description="ID of the category this product belongs to")
	image_url: Optional[str] = Field(None, description="URL of the product image")


class ProductCreate(ProductBase):
	pass


class ProductResponse(BaseModel):
	id: int = Field(..., description="Unique product identifier")
	name: str
	description: Optional[str]
	price: float
	category_id: int
	image_url: Optional[str]
	created_at: datetime
	category: CategoryResponse = Field(..., description="Category details of the product")

	class Config:
		form_attributes = True


class ProductListResponse(BaseModel):
	products: list[ProductResponse] = Field(..., description="List of products")
	total: int = Field(..., description="Total number of products")

	class Config:
		form_attributes = True





