Feature: User Registration
As a new user, I want to register an account with my email, password, first name, and last name so that I can access the system.

Scenario: Successful registration with valid details
Given the user is on the registration page
When the user enters a valid email, password, first name, and last name
And the password is at least 8 characters long and includes one uppercase letter, one lowercase letter, and one number
And clicks the "Register" button
Then the user should see a confirmation message
And a confirmation email should be sent to the user's email address

Scenario: Registration with an invalid email
Given the user is on the registration page
When the user enters an invalid email, a valid password, first name, and last name
And clicks the "Register" button
Then the user should see an error message indicating the email is invalid
And the user should not be registered

Scenario: Registration with a password that does not meet the criteria
Given the user is on the registration page
When the user enters a valid email, a password that does not meet the criteria, first name, and last name
And clicks the "Register" button
Then the user should see an error message indicating the password requirements
And the user should not be registered

Scenario: Registration with missing first name
Given the user is on the registration page
When the user enters a valid email, valid password, and last name but leaves the first name field empty
And clicks the "Register" button
Then the user should see an error message indicating the first name is required
And the user should not be registered

Scenario: Registration with missing last name
Given the user is on the registration page
When the user enters a valid email, valid password, and first name but leaves the last name field empty
And clicks the "Register" button
Then the user should see an error message indicating the last name is required
And the user should not be registered

Scenario: Registration with an already registered email
Given the user is on the registration page
And the email is already registered in the system
When the user enters the already registered email, a valid password, first name, and last name
And clicks the "Register" button
Then the user should see an error message indicating the email is already in use
And the user should not be registered

Scenario: Registration with all fields empty
Given the user is on the registration page
When the user leaves all fields empty
And clicks the "Register" button
Then the user should see error messages indicating all fields are required
And the user should not be registered