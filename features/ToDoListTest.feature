# Created by johnathan at 2/21/2020
Feature: ToDoList Functionality


   Scenario: The User Loads the ToDoList page
    Given  The to-do list page is loaded
    Then the to-do item info has the default values

   Scenario: The user enters in a new To-do List Item
    Given  The to-do list page is loaded
    When I enter a Date Due Date
     And I enter a Description
     And click the upcert button
    Then the new to-do item is added to the list
    And there are no console errors

   Scenario: The edit field is propagated with a to-do items information once the row is clicked
    Given  The to-do list page is loaded
    When I click on an existing to-do list item row
    Then the edit Due date field has the to-do list item's date
    And the edit Description has the to-do list item's description
    And there are no console errors

   Scenario: The user deletes an existing To-do List Item
    Given  The to-do list page is loaded
    When I click on an existing to-do list item row
     And I click on the delete button
    Then the to-do item is deleted from the to-do list
    And the to-do item info has the default values
    And there are no console errors

   Scenario: The user updates the due date on an existing To-do List Item
    Given  The to-do list page is loaded
    When I click on an existing to-do list item row
     And the to-do item due date is changed from its original due date
     And click the upcert button
    Then the to-do item is updated in the to-do list to show the updated due date
    And the to-do item info has the default values
    And there are no console errors

   Scenario: The user updates the description on an existing To-do List Item
    Given  The to-do list page is loaded
    When I click on an existing to-do list item row
     And the to-do item description is change from its original description
     And click the upcert button
    Then the to-do item is updated in the to-do list to show the updated description
    And the to-do item info has the default values
    And there are no console errors

   Scenario: The user updates the due date and description on an existing To-do List Item
    Given  The to-do list page is loaded
    When I click on an existing to-do list item row
     And the to-do item due date is changed from its original due date
     And the to-do item description is change from its original description
     And click the upcert button
    Then the to-do item is updated in the to-do list to show the updated due date and updated description
    And the to-do item info has the default values
    And there are no console errors

