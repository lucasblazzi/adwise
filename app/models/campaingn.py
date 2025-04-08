from typing import List, TypedDict, Dict


class Address(TypedDict):
    street: str
    city: str
    state: str
    number: int


class Company(TypedDict):
    name: str
    description: str
    website: str
    products: List[str]
    address: Address
    differentiation: List[str]
    values: List[str]


class Product(TypedDict):
    name: str
    description: List[str]
    price: float
    currency: str
    link: str

    
class Campaingn(TypedDict):
    objective: str
    product: Product
    client: Dict
    company: Company
    language: str
