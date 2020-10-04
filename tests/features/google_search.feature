Feature: Google search

    As a user,
    I want to be able to find information online,
    So I can learn new things

    Background:
        Given the Google Search page is displayed

    Scenario: Simple search
        When the user search for the phrase car
        Then the results are shown for car

    Scenario: Basic calculation
        When the user types a simple mathmematical phrase in the search page
        Then the Google should calculate the results