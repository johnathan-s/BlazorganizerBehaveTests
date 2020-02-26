from behave import *
from pages.ToDoList import ToDoList
import time
from _datetime import datetime, timedelta
import uuid

use_step_matcher("re")

todolist = ToDoList()
page_name = "todolist"
base_test_url = "https://localhost:44307/"
focused_row_due_date = ""
focused_row_description = ""


@given("The to-do list page is loaded")
def step_impl(context):
    if context.web.get_current_url() != base_test_url + page_name:
        context.web.open(base_test_url + page_name)
    time.sleep(10)
    print(context.web.get_current_url())
    print(base_test_url + page_name)
    assert (context.web.get_current_url() == base_test_url + page_name)


@then("the to-do item info has the default values")
def step_impl(context):
    todays_date_string = get_date_validation_string(0)
    label_value = context.web.get_element_text_by_id(todolist.labelDateDueInputValue)
    assert (todays_date_string in context.web.get_element_text_by_id(todolist.labelDateDueInputValue))
    assert (context.web.get_element_text_by_id(todolist.labelDescriptionInputValue) is None)
    assert (context.web.is_enabled_by_id(todolist.insertSaveButtonId) is True)
    assert (context.web.is_enabled_by_id(todolist.insertDeleteButtonId) is False)


@when("I enter a Date Due Date")
def step_impl(context):
    insert_due_date(context, 4)


@step("I enter a Description")
def step_impl(context):
    insert_description(context, str(uuid.uuid1()))
    assert (context.web.is_enabled_by_id(todolist.insertSaveButtonId) is True)


@step("click the upcert button")
def step_impl(context):
    assert (context.web.is_enabled_by_id(todolist.insertSaveButtonId) is True)
    context.web.click_element_by_id(todolist.insertSaveButtonId)


@then("the new to-do item is added to the list")
def step_impl(context):
    days_in_future = 10
    new_todo_item_description = str(uuid.uuid1())
    new_to_item_date = get_date_validation_string(days_in_future)
    create_new_todo_list_item(context, days_in_future, new_todo_item_description)
    table_rows = get_table_rows(context)
    found = False
    for row in table_rows:
        if new_todo_item_description in row.text and new_to_item_date in row.txt:
            found = True
            break
    assert (found is True)


@when("I click on an existing to-do list item row")
def step_impl(context):
    days_in_future = 14
    new_todo_item_description = str(uuid.uuid1())
    new_to_item_date = get_date_validation_string(days_in_future)
    create_new_todo_list_item(context, days_in_future, new_todo_item_description)
    table_rows = get_table_rows(context)
    found = False
    for row in table_rows:
        if new_todo_item_description in row.text and new_to_item_date in row.txt:
            context.web.click_element(row)
            found = True
            break
    assert (found is True)


@then("the edit Due date field has the to-do list item's date")
def step_impl(context):
    assert (focused_row_due_date in context.web.get_element_text_by_id(todolist.labelDateDueInputValue))


@step("the edit Description has the to-do list item's description")
def step_impl(context):
    assert (focused_row_description in context.web.get_element_text_by_id(todolist.labelDateDueInputValue))


@step("I click on the delete button")
def step_impl(context):
    assert (context.web.is_enabled_by_id(todolist.insertDeleteButtonId) is True)
    context.web.click_element_by_id(todolist.insertDeleteButtonId)


@then("the to-do item is deleted from the to-do list")
def step_impl(context):
    table_rows = get_table_rows(context)
    found = False
    for row in table_rows:
        if focused_row_description in row.text:
            found = True
            break
    assert (found is False)


@step("the to-do item due date is changed from its original due date")
def step_impl(context):
    insert_due_date(context, 7)


@step("the to-do item description is change from its original description")
def step_impl(context):
    insert_description(context, str(uuid.uuid1()))
    assert (context.web.is_enabled_by_id(todolist.insertSaveButtonId) is True)


@then("there are no console errors")
def step_impl(context):
    for entry in context.web.get_browser_errors():
        print(entry, '->', context.web.get_browser_errors()[entry])
        print(entry)
    assert (len(context.web.get_browser_errors()) == 0)


@then("the to-do item is updated in the to-do list to show the updated due date")
def step_impl(context):
    table_rows = get_table_rows(context)
    found = False
    for row in table_rows:
        if focused_row_description in row.text:
            found = True
            assert(focused_row_due_date in row.text)
            break
    assert (found is True)


@then("the to-do item is updated in the to-do list to show the updated description")
def step_impl(context):
    table_rows = get_table_rows(context)
    found = False
    for row in table_rows:
        if focused_row_description in row.text:
            found = True
            break
    assert (found is True)


@then("the to-do item is updated in the to-do list to show the updated due date and updated description")
def step_impl(context):
    table_rows = get_table_rows(context)
    found = False
    for row in table_rows:
        if focused_row_description in row.text and focused_row_due_date in row.text:
            found = True
            break
    assert (found is True)


def get_date_string(days_in_future):
    now = datetime.now()
    td = timedelta(days=days_in_future)
    future_date = now + td
    return "{:0>2}{:0>2}{:0>4}".format(future_date.month, future_date.day, future_date.year)


def get_date_validation_string(days_in_future):
    now = datetime.now()
    td = timedelta(days=days_in_future)
    future_date = now + td
    return "{:0>2}/{:0>2}/{:0>4}".format(future_date.month, future_date.day, future_date.year)


def get_table_rows(context):
    table_el = context.web.find_by_id(todolist.datagridTableId)
    # header_row = context.web.finds_by_tag_name_for_element(table_el, "th")  # get all of the rows in the table
    tbody = context.web.finds_by_tag_name_for_element(table_el, "tbody")
    tbody_rows = context.web.finds_by_tag_name_for_element(tbody[0], "tr")
    return tbody_rows


def insert_due_date(context, days_in_future):
    focused_row_due_date = get_date_validation_string(days_in_future)
    date_input = get_date_string(days_in_future)
    context.web.send_keys_by_id(todolist.insertDueDateId, date_input)


def insert_description(context, description):
    el = context.web.finds_by_id(todolist.insertDescriptionId)
    el.clear()
    context.web.send_keys_by_id(todolist.insertDescriptionId, description)
    focused_row_description = description


def create_new_todo_list_item(context, days_in_future, description):
    insert_due_date(context, days_in_future)
    insert_description(context, description)
    time.sleep(2)
    context.web.click_element_by_id(todolist.insertSaveButtonId)
