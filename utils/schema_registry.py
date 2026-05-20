from models.user_model import User, UserResponse
from models.product_model import Product
from models.order_model import Order

SCHEMA_REGISTRY = {
    ("GET", "/users"): User,
    ("POST", "/users"): UserResponse,
    ("GET", "/products"): Product,
    ("GET", "/carts"): Order
}