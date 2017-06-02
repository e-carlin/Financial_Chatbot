# Financial Chatbot
This is a texting based chatbot to set up time based financial goals.
A typical use case is someone who wants to spend $1500 over the course
of the next month. The bot will text them each time they make a purchase
to let the user know how much they spent and the change to their overall
budget. 

The app is written in Python using the Django framework. Messages are
recieved and sent through Twillio and incoming messages are parsed using
Wit.ai.