# Order Placement and Tracking Chatbot

This repository contains the code for a **food order placement and tracking chatbot**, designed to assist users in ordering and tracking their food in a fast and efficient way. The chatbot integrates with a backend to process orders, update order statuses, and track real-time progress.

## Features

- **Natural Language Processing**: Built using **Dialogflow**, the chatbot understands customer inputs, including food items and quantities, and can process multiple orders at once.
- **Order Management**: Users can place orders for various items like *Chicken Tagine*, *Lamb Couscous*, and more. The chatbot processes orders, updates item quantities, and handles complex order requests.
- **Backend Integration**: Developed using **FastAPI**, the backend handles:
  - Inserting new orders and updating the database with food items and their quantities.
  - Calculating total prices for orders based on the selected items.
  - Tracking order status and allowing users to check the progress of their orders.
- **Database Operations**: A robust **SQL database** stores menu items, orders, and order statuses. Stored procedures are used to manage order insertion and price calculations.
- **Error Handling**: Ensures smooth user experience by catching and handling errors such as invalid food items or quantities.

## Technologies Used

- **Dialogflow**: For chatbot integration and natural language understanding.
- **FastAPI**: To create a high-performance backend for processing and managing orders.
- **MySQL**: For database operations, storing food items, and tracking orders.
- **HTML/CSS**: For creating a responsive and user-friendly interface for customers to interact with the menu.

## How It Works

1. The user interacts with the chatbot, providing their order information.
2. The chatbot processes the order and communicates with the backend via API calls to handle database transactions.
3. The order is stored, and the user is provided with updates on the order status (e.g., "in progress," "ready for delivery").
4. The user can inquire about the status of their order at any time.

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/chatbot-order-tracking.git
    cd chatbot-order-tracking
    ```

2. **Set up the MySQL database**:
    - Run the provided SQL scripts in the `/sql` directory to create the necessary tables and stored procedures.

3. **Install Python dependencies**:
    ```bash
    pip install uvicorn
    ```
    ```bash
    pip install mysql-connector-python

    ```

4. **Run the FastAPI backend server**:
    ```bash
    uvicorn main:app --reload
    ```

5. **Integrate with Dialogflow**:
    - Follow Dialogflow setup to link the backend API to the chatbot and handle user inputs.

## Contributing

Feel free to open issues or contribute to the project. Pull requests are welcome.


