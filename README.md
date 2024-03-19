
# Restaurants Code Challenge

This project is a code challenge aimed at developing a simple command-line interface (CLI) application for managing restaurants, customers, and their reviews. The application allows users to perform various tasks such as adding restaurants and customers, leaving reviews, listing all reviews, and exiting the application.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

To run this application, you'll need Python 3 installed on your system. Follow these steps to set up the project:

1. Clone the repository to your local machine:
   git clone https://github.com/your_username/restaurants-code-challenge.git

2. Navigate to the project directory:
   cd restaurants-code-challenge

3. Install the required dependencies:
   pip install -r requirements.txt


## Usage

After completing the installation steps, you can use the command-line interface (CLI) to interact with the application. Here are the available commands:

- `python3 lib/cli.py`: Launches the CLI interface.
- `1`: Add a new restaurant.
- `2`: Add a new customer.
- `3`: Leave a review for a restaurant.
- `4`: List all restaurants.
- `5`: List all customers.
- `6`: List all reviews.
- `7`: Exit the application.

Follow the prompts displayed in the CLI to perform various tasks such as adding restaurants, customers, leaving reviews, and listing reviews.

## Features

- **Add Restaurants**: Users can add new restaurants to the database with a name and price range.
- **Add Customers**: Users can add new customers to the database with a first name and last name.
- **Leave Reviews**: Users can leave reviews for restaurants, specifying the customer, restaurant, and star rating.
- **List Restaurants**: Users can list all restaurants currently in the database.
- **List Customers**: Users can list all customers currently in the database.
- **List Reviews**: Users can list all reviews currently in the database, showing the associated restaurant, customer, and star rating.
- **Exit**: Users can exit the application at any time.

## File Structure

The project follows a simple file structure:

- `lib/`: Contains the main Python scripts for the CLI application.
  - `cli.py`: Main script for the command-line interface.
  - `helpers.py`: Helper functions for the CLI.
  - `seed.py`: Script for seeding the database with initial data.
- `models/`: Contains Python scripts defining the data models for restaurants, customers, and reviews.
  - `__init__.py`: Initializes the package.
  - `restaurant.py`: Defines the `Restaurant` class.
  - `customer.py`: Defines the `Customer` class.
  - `review.py`: Defines the `Review` class.
- `README.md`: Detailed documentation for the project.

## Contributing

Contributions to this project are welcome. Feel free to submit bug reports, feature requests, or pull requests to help improve the application.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to customize the README according to your project's specific requirements and details. This template provides a starting point for documenting your project.