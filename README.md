# Reminder App

## Video Demo

[https://youtu.be/Zun1Wrg4WJU](https://youtu.be/Zun1Wrg4WJU)


## Description

The **Reminder App** is a task management application designed to help users keep track of their to-do lists by providing task creation, reading, updating, and deletion (CRUD) functionality. It also sends **notifications** to users’ phones at task due times through the `ntfy.sh` service, ensuring that they never miss an important deadline.

This project is divided into two main components:

* **Backend:** Powered by **FastAPI**, the backend handles task operations, database interactions, and scheduling notifications. FastAPI ensures high performance and seamless task management.
* **Frontend:** Built using **Streamlit**, the frontend offers a user-friendly, interactive interface for managing tasks with ease.

The project also includes `project.py` and `test_project.py` files to fulfill **CS50P** final project requirements, with the primary functionality contained in the frontend and backend directories.

## Key Features

* **Task Management:** Create, read, update, and delete tasks directly through the user interface.
* **Notifications:** Receive task due date reminders sent to your phone via **ntfy.sh**.
* **Frontend Interface:** A clean, intuitive interface for interacting with your tasks built with **Streamlit**.
* **Backend API:** A fast and efficient backend powered by **FastAPI** that handles business logic and data persistence.
* **Modular Architecture:** The frontend and backend are cleanly separated, making the app easy to maintain and scale.

## Technologies and Libraries Used

* **Python 3.12**
* **FastAPI** (backend)
* **Streamlit** (frontend)
* **ntfy.sh** (for sending notifications)
* **SQLite** (or another database for task storage)
* **uvicorn** (for running the FastAPI server)
* **pytest** (for testing)

## Project Structure

```
reminder-cs50-python/
│
├── backend/                 # Backend code (FastAPI)
│   ├── app/
│   ├── config.py
│   ├── database/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│
├── frontend/                # Frontend code (Streamlit)
│   ├── app.py
│   ├── pages/
│   ├── utils/
│
├── project.py               # CS50P project structure file
├── test_project.py          # CS50P test file
├── requirements.txt         # Project dependencies
└── README.md                # This file
```

## How to Run the Project

Follow the steps below to get the project up and running locally.

### 1. Clone the repository:

```bash
git clone https://github.com/rudraa19/reminder-cs50-python.git
cd reminder-cs50-python
```

### 2. Setup and run the backend:

1. Navigate to the `backend/` directory:

   ```bash
   cd backend/
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the `backend/` folder and add the following environment variables:

   ```
   NTFY_ID=your_ntfy_id_here
   DATABASE_URL=your_database_url_here
   ```

   * Replace `your_ntfy_id_here` with your ntfy.sh ID (you can get one by registering at [ntfy.sh](https://ntfy.sh)).
   * Replace `your_database_url_here` with the URL for your SQLite or chosen database.

5. Start the FastAPI server:

   ```bash
   uvicorn app.main:app --reload
   ```

   The backend server will be running at [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

### 3. Setup and run the frontend:

1. Open a **new terminal** and navigate to the `frontend/` directory:

   ```bash
   cd frontend/
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the `frontend/` folder and add the following environment variable:

   ```
   BACKEND_URL=http://127.0.0.1:8000
   ```

   This ensures the frontend knows where to make requests to the backend.

5. Start the Streamlit frontend:

   ```bash
   streamlit run app.py
   ```

   The app will be available at [http://localhost:8501](http://localhost:8501).

---

### 4. Run Tests:

1. Navigate back to the root of the project:

   ```bash
   cd ..
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the tests:

   ```bash
   pytest test_project.py
   ```

---

## Design Choices

* **Separation of Frontend and Backend:** The frontend and backend are developed as separate components. This enables greater flexibility and scalability. **FastAPI** handles the backend logic, while **Streamlit** provides an intuitive interface for interacting with tasks.
* **Notifications via `ntfy.sh`:** Using `ntfy.sh` for notifications simplifies the process of sending push notifications to users’ phones. It doesn’t require additional configuration or the complexity of integrating other notification services.
* **Modular Utility Functions:** The project is designed with maintainability in mind. All CRUD operations and backend logic are encapsulated in dedicated modules.
* **Testing Compliance:** The `project.py` and `test_project.py` files satisfy **CS50P’s** final project requirements, including placeholder functions and unit tests.

---

## CS50P Final Project

This project was developed as part of **CS50’s Introduction to Programming with Python** (**CS50P**), a Harvard course that teaches Python fundamentals, including working with APIs, building web applications, and integrating third-party services. The **Reminder App** serves as the final project, showcasing skills in backend development with **FastAPI** and frontend development with **Streamlit**, along with practical use of notifications via **ntfy.sh**.

---

## Acknowledgments

* **ntfy.sh** for providing an easy-to-use notification service.
* **FastAPI** for building a fast, robust backend.
* **Streamlit** for offering a simple framework to create interactive frontends.
* **Harvard’s CS50P** for providing the foundational knowledge to complete this project.