*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  validname
    Set Password  validpw123
    Set Password confirmation  validpw123
    Submit Credentials
    Register Should Succeed    

Register With Too Short Username And Valid Password
    Set Username  a
    Set Password  validpw123
    Set Password confirmation  validpw123
    Submit Credentials
    Register Should Fail With Message  Incorrect username  

Register With Valid Username And Too Short Password
    Set Username  validname
    Set Password  k
    Set Password confirmation  k
    Submit Credentials
    Register Should Fail With Message  Incorrect password

Register With Nonmatching Password And Password Confirmation
    Set Username  validname
    Set Password  validpw123
    Set Password confirmation  validpw12
    Submit Credentials
    Register Should Fail With Message  Password and confirmation does not match

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}