Feature: Google search with calculation

    As a user,
    I want to be able to do some basic calculation
    Using the Google search engine

    Scenario: Basic calculation
        Given the Google Search page is displayed
        When the user types a simple mathmematical phrase in the search page
        Then the Google should return the correct results