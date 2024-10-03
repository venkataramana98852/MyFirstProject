*** Settings ***
Library    SeleniumLibrary


*** Variables ***





*** Test Cases ***
LoginTest
    Open Browser    https://robotframework.org/    chrome
#    ${dummy} =    SeleniumLibrary.Input Text    Press Enter to close the browser.
#    Close Browser

*** Keywords ***