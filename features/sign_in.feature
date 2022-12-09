Feature: Check to Sign_In Jules App

  Background:
    Given signin: I am a user on Jules sign-in page

  @test1
  Scenario: Check validation error message when password is empty and login button is disabled
    When signin: I fill in a email "abc@gmail.com"
    When signin: I check the password error message is not displayed
    Then signin: I check the button login is disabled