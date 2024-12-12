# Test Cases for Search Functionality

```gherkin
Feature: Search Functionality
  As a user, I want to use the search functionality to find relevant information quickly and efficiently.

  Scenario: Search box accepts input of up to 50 characters
    Given the user is on the search page
    When the user enters a search query of 50 characters
    Then the search box should accept the input without any errors

  Scenario: System returns search results in under 2 seconds
    Given the user is on the search page
    When the user enters a search query
    Then the system should return the search results in under 2 seconds

  Scenario: Display 'No Results Found' message when no results are found
    Given the user is on the search page
    When the user enters a search query that has no matching results
    Then the system should display a 'No Results Found' message

  Scenario: Search box does not accept input over 50 characters
    Given the user is on the search page
    When the user enters a search query of more than 50 characters
    Then the search box should not accept the input and should display an error message

  Scenario: System handles empty search query gracefully
    Given the user is on the search page
    When the user submits an empty search query
    Then the system should display a message prompting the user to enter a search term

  Scenario: System handles special characters in search query
    Given the user is on the search page
    When the user enters a search query with special characters
    Then the system should return relevant search results without any errors

  Scenario: System returns relevant results for a common search query
    Given the user is on the search page
    When the user enters a common search query
    Then the system should return relevant search results

  Scenario: System maintains search query in the search box after search
    Given the user is on the search page
    When the user enters a search query and submits it
    Then the search query should remain in the search box after the results are displayed
```