from mailer import Mailer

mail = Mailer(email="epiccodewizard@gmail.com", password="password1234!")
mail.send(receiver=input("Please enter your email. "), subject="Positive Message", message="You are very special, have a nice day!")
