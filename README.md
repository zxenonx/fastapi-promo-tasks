# fastapi-promo-tasks
KODECAMP 4.0 PROMOTIONAL TASK (Stage 1)

## Getting Started

To get started with the repository, follow these steps:

1. Clone the repository: 
```bash
git clone https://github.com/zxenonx/fastapi-promo-tasks.git`
```

2. Change into the project directory: 
```bash
cd fastapi-app
```

3. Create and activate a virtual environment: 
```bash
python -m venv venv source venv/bin/activate
```

4. Install the required dependencies: 
```bash
pip install -r requirements.txt
```

5. Start the FastAPI server: 
```bash
fastapi dev main.py
```

## Endpoints

## 1. `/items/` - Basic Query Parameters
This endpoint accepts multiple query parameters (name, category, price) and returns them in a structured format as a JSON response.

- URL: http://127.0.0.1:8000/items/?name=pomegranate&category=fruit&price=300   
- Method: GET
- Parameters:
  - name (string): The name of the item.
  - category (string): The category of the item.
  - price (float): The price of the item.
- Response:
```json
    {
        "name": "<name>",
        "category": "<category>",
        "price": <price>
    }
```

## 2. `/search/` - Query Parameters with Default Values and Optional Fields
This endpoint accepts query parameters (query, page, size) and returns search results and pagination info as a JSON response.

- URL: http://127.0.0.1:8000/search/?query=apple&page=1&size=5
- Method: GET
- Parameters:
  - query (string, optional): The search query.
  - page (integer, default=1): The page number.
  - size (integer, default=5): The number of items per page.
- Response:
```json
    {
        "items": [
            // Array of search results
        ],
        "total_fruits": <total_fruits>,
        "page": <page>,
        "size": <size>
    }
```

## 3. `/users/` - Request Body with Nested Pydantic Models
This endpoint accepts a complex JSON request body with nested Pydantic models (User) and returns the received data as JSON.

- URL: http://127.0.0.1:8000/users/
- Method: POST
- Request Body:
```json
    {
        "name": "<name>",
        "email": "<email>",
        "address": {
            "street": "<street>",
            "city": "<city>",
            "zip": "<zip>"
        }
    }
```
- Response:
```json
    {
        "name": "<name>",
        "email": "<email>",
        "address": {
            "street": "<street>",
            "city": "<city>",
            "zip": "<zip>"
        }
    }
```

## 4. `/validate/` - Query Parameters with String Validations
This endpoint accepts a query parameter (username) and validates it using string validations that includes length and regex. It returns a JSON response confirming the validation.

- URL: http://127.0.0.1:8000/validate/?username=mykie
- Method: GET
- Parameters:
  - username (string): The username.
- Response:
    ```json
    {
        "message": "Username is valid"
    }    
    ```

## 5. /reports/{report_id} - Combined Parameters and Validations
This endpoint accepts path parameters (report_id), query parameters (start_date, end_date), and a request body (Report) with validations. It returns a JSON response summarizing all the received data.

- URL: http://127.0.0.1:8000/reports/1
- Method: POST
- Parameters:
    - report_id (int, Path parameter): The report id.
    - start_date (datetime.date, optional): The start date.
    - end_date (datetime.date, optional): The end date.
- Request Body:   
    ```json
    {
        "title": "<title>",
        "content": "<content>"
    }
    ```
- Response:
    ```json
    {
        "report_id": <report_id>,
        "start_date": "<start_date>",
        "end_date": "<end_date>",
        "report": {
            "title": "<title>",
            "content": "<content>"
        }
    }
    ```
