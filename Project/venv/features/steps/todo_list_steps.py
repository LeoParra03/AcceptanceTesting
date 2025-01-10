from behave import given, when, then
from datetime import datetime

# Una lista global para simular el to-do list
to_do_list = []

@given('the to-do list is empty')
def step_given_list_is_empty(context):
    global to_do_list
    to_do_list = []  # Aseguramos que la lista esté vacía

@when('the user adds a task "{task}" with description "{description}" due date "{due_date}" and priority "{priority}"')
def step_when_user_adds_task(context, task, description, due_date, priority):
    global to_do_list
    to_do_list.append({
        'task': task,
        'description': description,
        'due_date': datetime.strptime(due_date, '%Y-%m-%d'),
        'priority': priority,
        'status': 'Pending'
    })

@then('the to-do list should contain "{task}"')
def step_then_list_should_contain_task(context, task):
    global to_do_list
    tasks = [t['task'] for t in to_do_list]
    assert task in tasks, f"Task '{task}' not found in the to-do list"

@given('the to-do list contains tasks')
def step_given_list_contains_tasks(context):
    global to_do_list
    to_do_list = []
    for row in context.table:
        to_do_list.append({
            'task': row['Task'],
            'description': row['Description'],
            'due_date': datetime.strptime(row['Due Date'], '%Y-%m-%d'),
            'priority': row['Priority'],
            'status': row.get('Status', 'Pending')
        })

@when('the user lists all tasks')
def step_when_user_lists_all_tasks(context):
    global to_do_list
    context.output = [task['task'] for task in to_do_list]

@then('the output should contain')
def step_then_output_should_contain(context):
    expected_tasks = [row['Task'] for row in context.table]
    actual_tasks = context.output
    assert all(task in actual_tasks for task in expected_tasks), \
        f"Some tasks are missing. Expected: {expected_tasks}, Got: {actual_tasks}"

@when('the user marks task "{task}" as completed')
def step_when_user_marks_task_completed(context, task):
    global to_do_list
    for t in to_do_list:
        if t['task'] == task:
            t['status'] = 'Completed'

@then('the to-do list should show task "{task}" as completed')
def step_then_task_should_be_completed(context, task):
    global to_do_list
    for t in to_do_list:
        if t['task'] == task:
            assert t['status'] == 'Completed', f"Task '{task}' is not marked as completed"

@when('the user clears the to-do list')
def step_when_user_clears_list(context):
    global to_do_list
    to_do_list = []

@then('the to-do list should be empty')
def step_then_list_should_be_empty(context):
    global to_do_list
    assert len(to_do_list) == 0, "The to-do list is not empty"

@when('the user edits the task "{task}" to change its description to "{description}" and priority to "{priority}"')
def step_when_user_edits_task(context, task, description, priority):
    global to_do_list
    for t in to_do_list:
        if t['task'] == task:
            t['description'] = description
            t['priority'] = priority

@then('the to-do list should show task "{task}" with description "{description}" and priority "{priority}"')
def step_then_task_should_be_updated(context, task, description, priority):
    global to_do_list
    for t in to_do_list:
        if t['task'] == task:
            assert t['description'] == description, f"Description mismatch for task '{task}'"
            assert t['priority'] == priority, f"Priority mismatch for task '{task}'"

@when('the user filters tasks by status "{status}"')
def step_when_user_filters_by_status(context, status):
    global to_do_list
    context.output = [task['task'] for task in to_do_list if task['status'] == status]

@then('the output should contain tasks with status "{status}"')
def step_then_output_should_contain_tasks_with_status(context, status):
    expected_tasks = [row['Task'] for row in context.table]
    actual_tasks = context.output
    assert all(task in actual_tasks for task in expected_tasks), \
        f"Some tasks are missing for status {status}. Expected: {expected_tasks}, Got: {actual_tasks}"
