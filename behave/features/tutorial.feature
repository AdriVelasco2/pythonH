# # Feature: showing off behave

# #   Scenario: run a simple test
# #      Given we have behave installed
# #       When we implement a test
# #       Then behave will test it for us!


# Feature: Cucumber basket

#     Scenario Outline: Add cucumbers to a basket
#     Given the basket has <number> baskets
#     When <add> cucumbers are added to the basket
#     Then the basket contains <total> cucumbers


#     Examples:
#         | number | add | total |
#         |   2    |  3  |   5   |
#         |   5    |  5  |  10   |
#         |   3    |  6  |   9   |
#         |  10    |  6  |  16   |