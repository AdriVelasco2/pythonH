Feature: Online store
  @login
  Scenario Outline: Login with different users
    Given the user opens the login page
    When they enter the username <username> and password <password>
    Then they should see the expected result <expected_result>

    Examples:
      | username       | password       | expected_result  |
      | standard_user  | secret_sauce   | success          |
      | invalid_user   | wrong_pass     | error            |
  @otras
  Scenario Outline: Product search
    Given the user is on the products page
    When they search for a product named <product_name>"
    Then they should see the search results

    Examples:
      | product_name         |
      | Sauce Labs Backpack  |
      | Bike Light           |
      | T-Shirt              |

  
  @cart
  Scenario Outline: Adding products to the cart
    Given the user is already on the products page
    When they add the product <product_name> to the cart
    Then the cart icon should display <expected_count>

    Examples:
      | product_name         | expected_count |
      | Sauce Labs Backpack  | 1             |
      | Bike Light           | 2             |
      | T-Shirt              | 3              |
  
  @checkout
  Scenario Outline: Checkout process
    Given the user has products in the cart
    When they complete the checkout process with <first_name>, <last_name>, and <zip_code>
    Then they should see the confirmation message "Thank you for your order!"

    Examples:
      | first_name | last_name | zip_code |
      | Adri        | Velasco       | 12345    |
      | Paco       | Paquito     | 67890    |
