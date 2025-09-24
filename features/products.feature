Feature: Product Management
  As a user
  I want to manage products
  So that I can read, update, delete, and list them

  Background:
    Given the following products exist
      | name   | category    | price | availability |
      | Laptop | Electronics | 1200  | true         |
      | Shirt  | Clothing    | 500   | true         |

  Scenario: Read a product by ID
    When I send a GET request to "/products/1"
    Then the response status code should be 200
    And the response should contain the product with name "Laptop"
