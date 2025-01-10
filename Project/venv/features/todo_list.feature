Feature: To-Do List Manager

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries" with description "Buy milk and eggs" due date "2025-01-10" and priority "High"
    Then the to-do list should contain "Buy groceries"

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task          | Description          | Due Date   | Priority |
      | Buy groceries | Buy milk and eggs    | 2025-01-10 | High     |
      | Pay bills     | Pay electricity bill | 2025-01-12 | Medium   |
    When the user lists all tasks
    Then the output should contain:
      | Task          |
      | Buy groceries |
      | Pay bills     |

  Scenario: Mark a task as completed
    Given the to-do list contains tasks:
      | Task          | Description       | Due Date   | Priority | Status   |
      | Buy groceries | Buy milk and eggs | 2025-01-10 | High     | Pending  |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Task          | Description          | Due Date   | Priority |
      | Buy groceries | Buy milk and eggs    | 2025-01-10 | High     |
      | Pay bills     | Pay electricity bill | 2025-01-12 | Medium   |
    When the user clears the to-do list
    Then the to-do list should be empty

  Scenario: Edit a task in the to-do list
    Given the to-do list contains tasks:
      | Task          | Description          | Due Date   | Priority |
      | Buy groceries | Buy milk and eggs    | 2025-01-10 | High     |
    When the user edits the task "Buy groceries" to change its description to "Buy bread and eggs" and priority to "Low"
    Then the to-do list should show task "Buy groceries" with description "Buy bread and eggs" and priority "Low"

  Scenario: Filter tasks by status
    Given the to-do list contains tasks:
      | Task          | Description          | Due Date   | Priority | Status    |
      | Buy groceries | Buy milk and eggs    | 2025-01-10 | High     | Completed |
      | Pay bills     | Pay electricity bill | 2025-01-12 | Medium   | Pending   |
    When the user filters tasks by status "Pending"
    Then the output should contain:
      | Task      |
      | Pay bills |
