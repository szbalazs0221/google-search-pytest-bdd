Feature: Google search with calculation

    As a user,
    I want to be able to do some basic calculation
    Using the Google search engine

    Scenario Outline: Basic calculation
        Given the Google Search page is displayed
        When the user types "<mathmematical_phrase>" in the search page
        Then Google should return "<result>"

        Examples: Math
            | mathmematical_phrase | result |
            | 5 + 5                | 10     |
            | 1 + 7                | 8      |
            | 5 - 5                | 0      |
            | 5 - 8                | -3     |
            | 5 * 8                | 40     |
            | -5 * 8               | -40    |
            | -2 * -5              | 10     |
            | 10 / 2               | 5      |