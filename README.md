# CS396 Final Project
Answer to the final project for CSCI 396 - Computer Networks

## Introduction
This is a socket-programming based application. The program is written in Python3 and run on Mac.

My initial attempt is to build a gift recommendation APP based on the 3-tier architecture. The current version builds TCP connections between multiple clients with the server. Meanwhile, the server will record useful information in the process of connection. For future development for this application, I will seperate the logic part (some machine learning algorithm to generate recommendation) from the database and add the presentation layer.

## To run
1. Open a terminal window and run `python3 Server.py`.
2. Open another terminal window and run `python3 Client.py` to build connection with the server.
3. Choose either to Login(1) or Register(2).
⋅⋅* Choose 1, input Email and Password.
⋅⋅⋅⋅⋅* If the input email and password are correct and the account is not already online, then you are successfully logged in.
⋅⋅⋅⋅⋅* If either email or password is invalid, then you will have to try again and you have three chances in total.
⋅⋅* Choose 2, input requested information and the server will record the input information in the database.
4. After logged in, you will input the person who you want to buy a guft for and the holiday.
5. The server will reply if there is a matching answer.
