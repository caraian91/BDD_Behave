Feature: Jules sign_up tests

  Background:
    Given signin: I am a user on Jules sign-in page


  @test2
  Scenario: Check the Sign up and Login link
    When signin: I will click on sign_up link
    Then singup: I check if I'm on the right url sign-up
    When singup: I will click on login link
    Then singup: I check if I'm on the right url sign-in

  @test3
  Scenario: Check email input error
    When signin: I will click on sign_up link
    When signup: I select the Personal button ratio
    When signup: I click on continue button
    When signup: I enter my first name "Cristian"
    When signup: I click on continue button
    When signup: I enter my last name "Popescu"
    When signup: I click on continue button
    When signup: I enter email "abc1"
    When signup: I verify the email error message is diplayed "Please enter a valid email address."
    When signup: I clear the input email
    When signup: I enter the correct email "abc1@gmail.com"
    Then signup: I verify the email error message is not diplayed "None"


