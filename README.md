# CS396 Final Project
Final project for CSCI 396 - Computer Networks

Author: Jiarong Li

## Introduction
This is a socket-programming based application. The program is written in Python3 and run on Mac.

My initial attempt is to build a gift recommendation APP based on the 3-tier architecture. The current version builds TCP connections between multiple clients with the server. Meanwhile, the server will record useful user information in the process of connection. For future development for this application, I will add the logic layer (some machine learning algorithm to generate recommendation from the database) and maybe try to use federated learning.

## To run
1. Open a terminal window and run `python3 homePage.py`.
2. Click `Run Server`.
3. Choose either `User Register` or `User Login`.
  * Choose `User Register`, input Email and Password.
      * Email must be in a valid format.
      * Password cannot be empty or a space.
  * Choose `User Login`, input requested information and the server will record the input information in the database.
      * If the input email and password are correct and the account is not already online, then you are successfully logged in.
      * If either email or password is invalid, then you will have to try again and you have three chances in total.
5. After logged in, you will choose a holiday, which helps the system to narrow the range of gift recommendation.
6. The server will reply if there is a matching answer from the current dataset. (This step will be handled by some machine learning algorithm in the future development)
7. After making choice, you can log out by clicking `Logout` or keep choosing holiday by clickig `Choose Holiday`.

## Collected Data
All user information will be recorded in `database/userList.csv`.
