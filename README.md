![](https://www.img.in.th/images/0e25a96fe1fb05de5da6ce944dc95221.jpg)

![](https://img.shields.io/badge/python-3.6-blue.svg)

### An example of typical input would be something like this
> user:  สวัสดี 

> bot: สวัสดีครับผมคือบอทให้ความรู้เรื่องหุ้นครับ ^^

> user: ราคาPTT 

> bot: ราคาหุ้น บริษัท ปตท. จำกัด (มหาชน) ขณะนี้ : ['PTT ', '44.50', '+0.25', '+0.56%', '21/12/2019 00:30:09']

# Line Chat Bot(SET)50
Chat Bot application helps analyze stocks (SET50). Developed for those who are interested and want to start looking for investment information. Analyze SET50 stocks, where users can query the meaning of stocks Stories about stocks and current stock prices, which stocks are interesting All of this information the user can access through the application line. Currently, Line application is very popular among Thai society. Therefore making the creators think that if the application of LINE is the part that pulls the user will be much more convenient because it is easy to use and easy to access More stable system
# How it works
An untrained instance of ChatterBot starts off with no knowledge of how to communicate. Each time a user enters a statement, the library saves the text that they entered and the text that the statement was in response to. As ChatterBot receives more input the number of responses that it can reply and the accuracy of each response in relation to the input statement increase. The program selects the closest matching response by searching for the closest matching known statement that matches the input, it then returns the most likely response to that statement based on how frequently each response is issued by the people the bot communicates with.
# Installation
     pip install Flask
     pip install virtualenv
     pip install requests
     pip install uncleengineer
# Basic Usage

     from flask import Flask, request
     import requests
    
     # Create a new server webhook for the chatbot
     @app.route('/webhook', methods=['POST','GET'])
     def webhook():
          if request.method == 'POST':
          payload = request.json
          
     # Create a new trainer for the chatbot
     if 'ราคาITD' in message :
            ITD = thaistock('ITD')
            Reply_messasge = 'ราคาหุ้น อิตาเลียนไทย ขณะนี้ : {}'.format(ITD)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
     
     # Get a response to an input statement
     def ReplyMessage(Reply_token, TextMessage, Line_Acees_Token):
      LINE_API = 'https://api.line.me/v2/bot/message/reply'

## This project is part of BC410 subject 
## Bachelor Degrees
## Term 1 year of education 2019
## University of the Thai Chamber of Commerce
