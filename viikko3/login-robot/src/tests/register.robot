*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  nalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  validpw123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  k  validpw123
    Output Should Contain  Incorrect username

Register With Valid Username And Too Short Password
    Input Credentials  validusername  short1
    Output Should Contain  Incorrect password  

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  validusername  longenoughpw
    Output Should Contain  Incorrect password   

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123
