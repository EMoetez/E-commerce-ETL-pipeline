# ETL Project: Customer Revenue Analysis

## Project Description

This project is an ETL (Extract, Transform, Load) pipeline designed to analyze customer revenue data for an e-commerce platform. The goal is to determine the top customers who have generated the most revenue and export this data to a MySQL database. The project follows best practices for data processing, including the use of environment variables for security, detailed logging, and unit testing.

## Features

- **Data Extraction**: Load customer and event data from a MySQL database.
- **Data Transformation**: Calculate total revenue for each customer and determine the top customers based on a specified quantile.
- **Data Loading**: Export the top customers to a new table in the MySQL database using mass insert.
- **Progress Tracking**: Use a progress bar to indicate the progress of data processing.
- **Unit Testing**: Includes unit tests to ensure the correctness of data extraction functions.
- **Logging**: Detailed logging with timestamps and standard classification (info, warning, etc.).


## Getting Started

### Prerequisites

- Python 3.6 or higher
- MySQL server
- `pip` package manager

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/EMoetez/E-commerce-ETL-pipeline.git
    cd E-commerce-ETL-pipeline
    ```

2. Create and activate a virtual environment:

    - On Windows:
        ```sh
        python -m venv etl
        etl\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        python3 -m venv etl
        source etl/bin/activate
        ```

3. Install the required Python packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Set up the [.env](http://_vscodecontentref_/9) file with your MySQL database credentials:

    ```properties
    MYSQL_HOST=localhost
    MYSQL_USER=root
    MYSQL_PASSWORD=your_password
    MYSQL_DATABASE=mydb
    ```

5. Populate the database with sample data:

    ```sh
    python populate_data.py
    ```

### Running the Scripts

1. Load data from the database:

    ```sh
    python load_data.py
    ```

2. Compute customer revenue and top customers:

    ```sh
    python compute.py
    ```

3. Export top customers to the database:

    ```sh
    python export.py
    ```

### Running Unit Tests

To run the unit tests, execute the following command:

    ```sh
    python -m unittest test_load_data.py
    ```

### Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

### License
This project is licensed under the MIT License.


### Summary

This `README.md` file provides a clear and comprehensive overview of your project, including its features, structure, and instructions for getting started. It also includes sections for running the scripts and unit tests, contributing, and the project license. This will help others understand and use your project effectively. If you encounter any issues or need further assistance, feel free to ask.
### Summary

This `README.md` file provides a clear and comprehensive overview of your project, including its features, structure, and instructions for getting started. It also includes sections for running the scripts and unit tests, contributing, and the project license. This will help others understand and use your project effectively. If you encounter any issues or need further assistance, feel free to ask.




