
import os
import json
import traceback

from dotenv import load_dotenv
from google import genai

from tools import lookup_order_status


# ==========================================
# 1. LOAD API KEY AND CONNECT TO GEMINI
# ==========================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "Gemini API key not found. Check your root .env file."
    )

client = genai.Client(api_key=api_key)

MODEL = "gemini-3.5-flash-lite"


# ==========================================
# 2. DEFINE THE FUNCTION TOOL
# ==========================================

order_tool = {
    "type": "function",
    "name": "lookup_order_status",
    "description": (
        "Find the current status and delivery details "
        "of a customer order using its order ID."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "order_id": {
                "type": "string",
                "description": "The customer's order ID."
            }
        },
        "required": ["order_id"]
    }
}


# ==========================================
# 3. CUSTOMER QUESTION
# ==========================================

user_message = "Can you check the status of order ORD1001?"

print("\n===================================")
print("       TICKETPILOT STARTED")
print("===================================")

print("\nCustomer:", user_message)


# ==========================================
# 4. SEND REQUEST TO GEMINI
# ==========================================

try:

    print("\nSending request to Gemini...", flush=True)

    interaction = client.interactions.create(
    model=MODEL,
    input=(
        "You are TicketPilot, a helpful customer support assistant. "
        "When asked about an order, use the lookup_order_status "
        "function to retrieve the actual order details. "
        "Never invent order information."
        "\n\nCustomer question: " + user_message
    ),
    tools=[order_tool],
    timeout=120
)

    print("Gemini responded successfully!", flush=True)


    # ==========================================
    # 5. INSPECT GEMINI'S RESPONSE
    # ==========================================

    print("\n--- GEMINI RESPONSE ---")

    function_results = []

    for step in interaction.steps:

        if step.type == "function_call":

            print("\nGemini requested a function call!")

            print("Function name:", step.name)
            print("Arguments:", step.arguments)

            if step.name == "lookup_order_status":

                # Extract order ID
                order_id = step.arguments.get("order_id", "")

                # Execute our Python function
                result = lookup_order_status(order_id)

                print("\n--- PYTHON FUNCTION RESULT ---")
                print(json.dumps(result, indent=4))

                # Prepare result for Gemini
                function_results.append({
                    "type": "function_result",
                    "name": step.name,
                    "call_id": step.id,
                    "result": result
                })

            else:
                print("Unknown function requested:", step.name)


    # ==========================================
    # 6. SEND PYTHON RESULT BACK TO GEMINI
    # ==========================================

    if function_results:

        print("\nSending Python result back to Gemini...")

        final_interaction = client.interactions.create(
            model=MODEL,
            previous_interaction_id=interaction.id,
            input=function_results,
            tools=[order_tool]
        )

        # ==========================================
        # 7. DISPLAY FINAL ANSWER
        # ==========================================

        print("\n===================================")
        print("       TICKETPILOT FINAL ANSWER")
        print("===================================")

        print(final_interaction.output_text)

    else:

        print("\nGemini did not request the function.")

        print("Gemini response:")
        print(interaction.output_text)


except Exception as error:

    print("\n===================================")
    print("          ERROR OCCURRED")
    print("===================================")

    print("Error type:", type(error).__name__)
    print("Error message:", error)

    print("\nFull error details:")
    traceback.print_exc()
