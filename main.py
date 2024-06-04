import datetime
from typing import Annotated, Any
from fastapi import FastAPI, Path, Query

from schemas import Report, User

app = FastAPI()

fruits = [
    {"name": "Star Apple", "category": "Fruit", "price": 0.5},
    {"name": "Apple", "category": "Fruit", "price": 0.9},
    {"name": "Banana", "category": "Fruit", "price": 0.3},
    {"name": "Strawberry", "category": "Fruit", "price": 0.7},
    {"name": "Orange", "category": "Fruit", "price": 0.6},
    {"name": "Grapes", "category": "Fruit", "price": 1.2},
]

@app.get("/")
def health_check():
    return {"status": "active"}

'''
Task 1: Basic Query Parameters
Description: Create an endpoint that accepts multiple query parameters and returns them in a structured format.

Details:

Endpoint: /items/
Query Parameters: name, category, price
Return a JSON response with the query parameters in a dictionary format.
'''
@app.get("/items/")  # http://127.0.0.1:8000/items/?name=pomegranate&category=fruit&price=300    
def read_items(name: str, category: str, price: float) -> dict[str, str | float]:
    """Creates an endpoint that accepts multiple query parameters and returns them in a structured format.

    Args:
        name (str): The name of the item.
        category (str): The category of the item.
        price (float): The price of the item.

    Returns:
        dict[str, str | float]: A dictionary with the query parameters.
    """
    return {"name": name, "category": category, "price": price}


'''
Task 2: Query Parameters with Default Values and Optional Fields
Description: Create an endpoint that uses query parameters with default values and optional fields.

Details:

Endpoint: /search/
Query Parameters: query, page, size
Return a JSON response with the search results and pagination info.
'''
@app.get("/search/")    # http://127.0.0.1:8000/search/?query=apple&page=1&size=5
def search_items(query: str | None = None, page: int = 1, size: int = 5) -> dict[str, Any]:
    """Creates an endpoint that uses query parameters with default values and optional fields.

    Args:
        query (str | None, optional): The search query. Defaults to None.
        page (int, optional): The page number. Defaults to 1.
        size (int, optional): The number of items per page. Defaults to 5.

    Returns:
        dict[str, Any]: A dictionary with the search results and pagination info.
    """
    start_index = (page - 1) * size
    end_index = start_index + size
    filtered_fruits = fruits
    if query:
        filtered_fruits = [fruit for fruit in filtered_fruits if query.lower() in fruit["name"].lower()]
    return {"items": filtered_fruits[start_index:end_index], "total_fruits": len(filtered_fruits), "page": page, "size": size}

'''
Task 3: Request Body with Nested Pydantic Models
Description: Create an endpoint that accepts a complex JSON request body with nested Pydantic models.

Details:

Endpoint: /users/
Request Body: Pydantic model with nested fields for address and profile
User: name, email, address: Address
Address: street, city, zip
Return the received data as JSON.
'''
@app.post("/users/")  # http://127.0.0.1:8000/users/
def create_user(user: User) -> User:
    """Creates an endpoint that accepts a complex JSON request body with nested Pydantic models.

    Args:
        user (User): Pydantic model with nested fields for address and profile.

    Returns:
        User: The received data as JSON.
    """
    return user

'''
Task 4: Query Parameters with String Validations
Description: Create an endpoint that validates query parameters using string validations that includes length and regex.

Details:

Endpoint: /validate/
Query Parameters: username
Return a JSON response confirming the validation.
'''
@app.get("/validate/")  # http://127.0.0.1:8000/validate/?username=mykie
def validate_username(username: Annotated[str, Query(min_length=3, max_length=20, regex="^[a-zA-Z][a-zA-Z0-9]+$")]) -> dict[str, Any]:
    """Creates an endpoint that validates query parameters using string validations that includes length and regex.

    Args:
        username (str): The username. Defaults to 3, max_length=20, regex="^[a-zA-Z][a-zA-Z0-9]+$")].

    Returns:
        dict[str, Any]: A JSON response confirming the validation.
    """
    return {"message": "Username is valid"}


'''
Task 5: Combined Parameters and Validations

Description: Create an endpoint that combines path parameters, query parameters, and request body with validations.

Details:

    Endpoint: /reports/{report_id}
    Path Parameter: report_id (must be positive)
    Query Parameters: start_date, end_date
    Request Body: Pydantic model with fields: title, content
    Return a JSON response summarizing all the received data.
'''
@app.post("/reports/{report_id}")  # http://127.0.0.1:8000/reports/1
def create_report(report_id: Annotated[int, Path(gt=0)], start_date: Annotated[datetime.date, Query(example="2024-01-01")], end_date: Annotated[datetime.date, Query(example="2024-12-31")], report: Report) -> dict[str, Any]:
    """Creates an endpoint that combines path parameters, query parameters, and request body with validations.

    Args:
        report (Report): Pydantic model with fields: title, content.
        report_id (int): The report id.
        start_date (datetime.date): The start date. Defaults to "2022-01-01".
        end_date (datetime.date): The end date. Defaults to "2022-12-31".

    Returns:
        dict[str, Any]: A JSON response summarizing all the received data.
    """
    return {"report_id": report_id, "start_date": start_date, "end_date": end_date, "report": report}