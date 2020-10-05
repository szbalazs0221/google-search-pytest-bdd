Feature: Google search

    As a user,
    I want to be able to find information online,
    So I can learn new things

    Scenario: Simple search
        Given the Google Search page is displayed
        When the user search for the phrase car
        Then the results are shown for car

