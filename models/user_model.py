from pydantic import BaseModel


class Geolocation(BaseModel):
    lat: str
    long: str


class Address(BaseModel):
    city: str
    street: str
    number: int
    zipcode: str
    geolocation: Geolocation


class Name(BaseModel):
    firstname: str
    lastname: str


class User(BaseModel):
    id: int
    email: str
    username: str
    password: str
    name: Name
    address: Address
    phone: str


class UserResponse(BaseModel):
    id: int
