Feature: Product Management
  As a user
  I want to manage products
  So that I can read, update, delete, and list them

  Background:
    Given the following products exist
      | name        | category     | price | availability |
      | Laptop      | Electronics | 1200  | true         |
      | Shirt       | Clothing    | 500   | true         |
      | Book        | Education   | 300   | false        |
      | Headphones  | Electronics | 800   | true         |

  # ---------------- 6a: READ ----------------
  Scenario: Read a product by ID
    When I send a GET request to "/products/1"
    Then the response status code should be 200
    And the response should contain the product with name "Laptop"

  # ---------------- 6b: UPDATE ----------------
  Scenario: Update a product
    When I send a PUT request to "/products/2" with JSON
      """
      {"name": "T-Shirt", "price": 550}
      """
    Then the response status code should be 200
    And the response should contain the updated product name "T-Shirt"

  # ---------------- 6c: DELETE ----------------
  Scenario: Delete a product
    When I send a DELETE request to "/products/3"
    Then the response status code should be 204

  # ---------------- 6d: LIST ALL ----------------
  Scenario: List all products
    When I send a GET request to "/products"
    Then the response status code should be 200
    And the response should contain at least 3 products

  # ---------------- 6e: SEARCH BY CATEGORY ----------------
  Scenario: Search products by category
    When I send a GET request to "/products?category=Electronics"
    Then the response status code should be 200
    And the response should contain products with category "Electronics"

  # ---------------- 6f: SEARCH BY AVAILABILITY ----------------
  Scenario: Search products by availability
    When I send a GET request to "/products?availability=true"
    Then the response status code should be 200
    And the response should contain products with availability "true"

  # ---------------- 6g: SEARCH BY NAME ----------------
  Scenario: Search product by name
    When I send a GET request to "/products?name=Laptop"
    Then the response status code should be 200
    And the response should contain product with name "Laptop"
