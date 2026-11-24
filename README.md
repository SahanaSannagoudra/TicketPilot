# TicketPilot – AI-Powered Support Ticket Assistant

TicketPilot is a Python-based AI support assistant that uses Google's Gemini API and function calling to retrieve customer order information.

Instead of directly searching for order details, Gemini understands the customer's request, decides when to call a Python function, and uses the returned information to generate a helpful response.

## Features

- AI-powered customer query understanding
- Gemini function calling
- Python-based order lookup
- Handles valid and invalid order IDs
- Generates natural-language responses
- Uses environment variables to protect API credentials

## Technologies Used

- Python
- Google Gemini API
- Google Gen AI SDK
- python-dotenv

## Project Structure

```text
TicketPilot/
│
├── backend/
│   ├── __init__.py
│   ├── main.py
│   └── tools.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## How It Works

1. The customer enters an order-related question.
2. Gemini understands the request.
3. Gemini requests the `lookup_order_status` function when needed.
4. Python executes the function and retrieves the order details.
5. The result is sent back to Gemini.
6. Gemini generates a customer-friendly response.

## Setup Instructions

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd TicketPilot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment (Windows PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure your API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Replace the placeholder with your own Gemini API key. Never publish your actual API key.

### 6. Run the project

```bash
python backend/main.py
```

## Sample Test Cases

| Order ID | Expected Result |
|---|---|
| ORD1001 | Shipped |
| ORD1002 | Processing |
| ORD1003 | Delivered |
| ORD9999 | Order not found |

## Learning Outcomes

Through this project, I learned:

- How to connect Python applications with an LLM API
- How function calling works
- How an LLM can request external tools
- How to execute tool calls in Python
- How to pass function results back to an LLM
- How to handle missing data and generate useful responses

## Future Improvements

- Add customer lookup functionality.
- Integrate a database for order management.
- Build a web-based customer support interface.
- Add support for more customer service queries.

---

**Project:** TicketPilot  
**Category:** Generative AI / LLM Function Calling  
**Status:** Initial implementation completed