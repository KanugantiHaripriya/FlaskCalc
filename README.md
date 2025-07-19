

# FlaskCalc

## Overview

FlaskCalc is a simple web application built with Flask. It provides a user interface for performing basic arithmetic operations: addition, subtraction, multiplication, and division. The application includes a homepage, an index page, and a login form.

## Features

-   Homepage: Serves as the entry point to the application.
-   Index Page: (Optional, can be customized)
-   Login Form: Allows users to input two numbers and calculate their sum.
-   Arithmetic Operations: Dedicated routes and forms for addition, subtraction, multiplication, and division.

## Prerequisites

-   Python 3.x
-   Flask

## Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2.  Create a virtual environment (recommended):

    ```bash
    python -m venv venv
    ```

3.  Activate the virtual environment:

    -   On Windows:

        ```bash
        venv\Scripts\activate
        ```

    -   On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4.  Install dependencies:

    ```bash
    pip install Flask
    ```

## Running the Application

1.  Navigate to the project directory in your terminal.
2.  Run the application:

    ```bash
    python app2.py
    ```

    (or the name of your main Python file)

3.  Open your web browser and go to `http://127.0.0.1:5000/` (or the address shown in your terminal).

## Usage

1.  Homepage: Access the application's main page.
2.  Index Page: (Optional, can be customized)
3.  Login Form: Enter two numbers and click the "Calculate Sum" button.
4.  Arithmetic Operations: Navigate to the respective routes (e.g., `/add`, `/subtract`) and use the forms to perform the desired calculations.

## Project Structure

```
flaskcalc/
│
├── app2.py          # Main application file
├── templates/       # Directory for HTML templates
│   ├── index.html   # Example index page
│   ├── home.html    # Example home page
│   ├── add.html     # Template for addition
│   ├── subtract.html # Template for subtraction
│   ├── multiply.html # Template for multiplication
│   └── divide.html   # Template for division
│
└── static/          # Directory for static files (CSS, JavaScript, images)
```
