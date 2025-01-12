# simple-account-system
This repository contains a basic Python program that simulates an account creation and login system. Users can create an account by entering a username and password, and later log in using their credentials. The program validates the login information and provides appropriate feedback.

## Features

Allows users to create an account by providing a username and password.

Validates login credentials to ensure they match the created account.

Provides user-friendly messages for account creation, login success, or login failure.

## How It Works

Account Creation:

The user is prompted to enter a username and password.

A message confirms that the account has been created successfully.

Account Login:

The user is asked to enter their username and password.

The program checks if the entered credentials match the previously created account.

Validation:

If the credentials are correct, a success message is displayed.

If the credentials are incorrect, an error message is shown.

## Example Output

Account Creation:

Create your account
Enter your username: user123
Enter your password: pass123
Account created successfully!

Account Login:

Please sign into your account.
Account Login:
Enter your username: user123
Enter your password: pass123
Account logged in successfully!
Welcome to your account! You are logged in successfully

Login Failure:

Please sign into your account.
Account Login:
Enter your username: user123
Enter your password: wrongpass
Invalid username or password!

## Requirements

Python 3.x

## Usage

Clone the repository:

git clone https://github.com/your-username/simple-account-system.git

Navigate to the project directory:

cd simple-account-system

Run the program:

python account_system.py

Follow the prompts to create an account and log in.

## File Structure

account_system.py: The main script containing the account creation and login logic.

Repository Name Suggestion

simple-account-system

basic-authentication-python

account-login-script

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests for improvements.

## License

This project is licensed under the MIT License.