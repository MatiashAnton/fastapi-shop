from pydantic import BaseModel, Field
from typing import Optional


class CartItemBase(BaseModel):
	product_id: int = Field(..., description="ID of the product to add to the cart")
	quantity: int = Field(..., gt=0, description="Quantity of the product to add")


class CartItemCreate(CartItemBase):
	pass


class CartItemUpdate(BaseModel):
	product_id: int = Field(..., description="ID of the product in the cart")
	quantity: int = Field(..., gt=0, description="Updated quantity of the product in the cart")


class CartItem(BaseModel):
	product_id: int
	name: str = Field(..., description="Name of the product")
	price: float = Field(..., description="Price of the product")
	quantity: int = Field(..., description="Quantity of the product in the cart")
	subtotal: float = Field(..., description="Subtotal price for this cart item")
	image_url: Optional[str] = Field(None, description="URL of the product image")


class CartResponse(BaseModel):
	items: list[CartItem] = Field(..., description="List of items in the cart")
	total_quantity: int = Field(..., description="Total quantity of items in the cart")
	total_price: float = Field(..., description="Total price of all items in the cart")