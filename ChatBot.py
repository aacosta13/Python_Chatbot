# Chatbot Assignment
# CPSC 362-05
# Armando Acosta
'''
TODO: RETRIEVE/UPLOAD/ETC FROM DATABASE
'''

import sys
from random import *


# Default class for user of service
class User:
    def __init__(self, name, sub_status):
        self.name = name
        self.sub = sub_status


# Default class for producer
class Producer:
    def __init__(self, name):
        self.name = name


# Class to hold/update tech support information
class TechSupport:
    def __init__(self, ticket):
        self.video_name = 'name'
        self.purchase_date = 'date'
        self.devices = 'tablet'
        self.ticket = ticket
        # Status level of 0 is solved, 1 is not solved
        self.__status = 0

    def get_status_level(self):
        return self.__status

    def set_status_level(self, level):
        self.__status = level


# Class to hold payment information
class ManagePayments:
    def __init__(self, name, subscription):
        self.name = name
        self.date = '10-10-10'
        self.__subscription = subscription
        self.__price = '0.00'

    def get_subscription(self):
        return self.__subscription

    def set_subscription(self, subscription):
        self.__subscription = subscription

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price


# Function to walk user through troubleshooting
def user_trouble_func():
    print("Trouble with our services? No worries!\n")
    resolved = False

    while not resolved:
        issue = input("Please provide a brief description of your issue.\n")

        if 'access' in issue:
            if 'content' in issue:
                confirm = input("You are having issues accessing your content, correct? (y|n)\n")
                if confirm == 'y':
                    print('Okay. Please provide the name of the video you purchased followed by the date.\n')
                    vid_name = input("Video Name: ")
                    vid_date = input("Purchase Date: ")
                    ticket = randint(1, 100)
                    support_status.ticket = ticket
                    support_status.video_name = vid_name
                    support_status.purchase_date = vid_date
                    support_status.set_status_level(1)
                    mockDB[support_status.ticket] = support_status.get_status_level()

                    print("Thank you. Your issue has been filed. For reference, your support ticket # is: ", ticket)
                    resolved = True
                else:
                    print("Sorry, let's try this again.\n")
                    continue
        elif 'videos' in issue:
            if 'devices' in issue:
                confirm = input("You are having issues playing videos on certain devices, correct? (y|n)\n")
                if confirm == 'y':
                    devices = input("Okay. Please list the devices you are having issues with, separated by a comma.\n")
                    ticket = randint(1, 100)
                    support_status.ticket = ticket
                    support_status.devices = devices
                    support_status.set_status_level(1)
                    mockDB[support_status.ticket] = support_status.get_status_level()

                    print("Thank you. Your issue has been filed. For reference, your support ticket # is: ", ticket)
                    resolved = True
                else:
                    print("Sorry, let's try this again.\n")
                    continue
        elif 'check' in issue:
            if 'ticket' in issue:
                confirm = input("You want to check up on your support ticket, correct? (y|n)\n")
                if confirm == 'y':
                    string_num = input("Please enter your support ticket #: ")

                    while not string_num.isdigit():
                        string_num = input("I'm sorry, please enter a valid number.\n")

                    number = int(string_num)
                    if number in mockDB:
                        if mockDB[number] == 0:
                            print("Your issue has been resolved. Please check your registration e-mail for a response.")
                            resolved = True
                        else:
                            print("I'm sorry, your issue is still being reviewed. Please allow 1-2 business days for a"
                                  "response. Taking you back to main menu.")
                            main_func('user')
                    else:
                        print("I'm sorry that support ticket is not in our system. Please try another number or run our"
                              "troubleshoot system again.\n")
                        main_func('user')
                else:
                    print("Sorry, let's try this again.\n")
        else:
            repeat = input("Sorry, I'm not sure I can solve that. Want to ask another question? (y|n)\n")

            if repeat == 'y':
                continue
            else:
                print('No worries, returning to main menu.\n')
                main_func('user')

    return resolved


def producer_trouble_func():
    print('Trouble with running your account? No problem!\n')
    resolved = False

    while not resolved:
        issue = input("Please provide a brief description of your issue.\n")

        if 'video' in issue:
            if 'online' in issue:
                confirm = input("You are having trouble with one of your videos appearing online, correct? (y|n)\n")
                if confirm == 'y':
                    print("Okay. Please provide the name of the video and the date from when it was uploaded.\n")
                    vid_name = input("Video Name: ")
                    vid_date = input("Upload Date: ")
                    ticket = randint(1, 100)
                    support_status.ticket = ticket
                    support_status.video_name = vid_name
                    support_status.purchase_date = vid_date
                    support_status.set_status_level(1)
                    mockDB[support_status.ticket] = support_status.get_status_level()

                    print("Thank you. Your issue has been filed. For reference, your support ticket # is: ", ticket)
                    resolved = True
                else:
                    print("Sorry, let's try that again.")
                    continue
        elif 'page' in issue:
            if 'showing' in issue:
                if 'videos' in issue:
                    confirm = input("You are having trouble with your page showing certain videos, correct? (y|n)\n")
                    if confirm == 'y':
                        print("Okay. Please provide the name of the video and the date it was uploaded.\n")
                        vid_name = input("Video Name: ")
                        vid_date = input("Upload Date: ")
                        ticket = randint(1, 100)
                        support_status.ticket = ticket
                        support_status.video_name = vid_name
                        support_status.purchase_date = vid_date
                        support_status.set_status_level(1)
                        mockDB[support_status.ticket] = support_status.get_status_level()
                        # Here, we are to look through the database of videos in a more fleshed out environment to see
                        # if the video actually exists, and to sort it properly
                        mockDB[vid_name] = vid_date

                        print("Thank you. Our team will search through and properly organize the video by date.\n"
                              "You may inquire about the status of this update with this ticket #: ", ticket)
                        resolved = True
                    else:
                        print("Sorry, let's try that again.")
                        continue
        elif 'video' in issue:
            if 'cut' in issue:
                confirm = input("You are inquiring about why one of your videos was cut short, correct? (y|n)\n")
                if confirm == 'y':
                    query = input("Okay. It is actually in our policy to allow only up to 10 minutes of video time.\n"
                                  "Did you have further questions on the topic? (y|n)\n")
                    if query == 'y':
                        ticket = randint(1, 100)
                        support_status.ticket = ticket
                        support_status.set_status_level(1)
                        mockDB[support_status.ticket] = support_status.get_status_level()
                        print("Okay. We have issued a ticket for you to discuss this in a live chat with a support"
                              "member. Please provide the following ticket # to discuss suggestions/concerns: ", ticket)
                        resolved = True
                    else:
                        resolved = True
                else:
                    print("Sorry, let's try that again.")
                    continue
        else:
            repeat = input("Sorry, I'm not sure I can solve that. Want to ask another question? (y|n)\n")

            if repeat == 'y':
                continue
            else:
                print('No worries, returning to main menu.\n')
    return resolved


# Function to manage user's payment needs
def user_payments_func():
    print("Issues with paying for certain content? We're here to help!\n")
    resolved = False

    while not resolved:
        issue = input("Please describe your issue below.\n")

        if 'pay' in issue:
            if 'know' in issue:
                if 'how' in issue:
                    confirm = input("You want to know how to pay for some content, correct? (y|n)")
                    if confirm == 'y':
                        print("Paying for our videos is actually quite simple. Depending on the uploader, the user may"
                              "charge a single fee to own the video or charge by a subscription model. Simply visit"
                              "their homepage, and there will be a link detailing how to purchase their video.\n")
                        resolved = True
                    else:
                        print("Sorry, let's try that again.")
                        continue
        elif 'stop' in issue:
            if 'subscription' in issue:
                confirm = input("You want to stop a certain subscription you have, correct? (y|n)")
                if confirm == 'y':
                    print("To cancel your subscription, simply visit your profile page, and there will be a method to"
                          "unsubscribe from any of your listed subscriptions within.\n")
                    resolved = True
                else:
                    print("Sorry, let's try that again.")
                    continue
        elif 'still' in issue:
            if 'charged' in issue:
                confirm = input("You are asking about being incorrectly charged for something, correct?")
                if confirm == 'y':
                    print("Please provide the name of the channel and the date you unsubscribed.\n")
                    sub_name = input("Name: ")
                    unsub_date = input("Date: ")
                    plan.name = sub_name
                    plan.date = unsub_date
                    plan.set_subscription(0)
                    mockDB[sub_name] = plan.get_subscription()
                    ticket = randint(1, 100)
                    support_status.ticket = ticket
                    support_status.set_status_level(1)
                    mockDB[support_status.ticket] = support_status.get_status_level()

                    print("Thank you. You are entered in our database as unsubscribed. Our team will review this change"
                          "and will e-mail you a confirmation within 24 hours. For status updates, refer to our"
                          "troubleshooting section with this ticket #: ", ticket)
                    resolved = True
                else:
                    print("Sorry, let's try that again.")
                    continue
        elif 'much' in issue:
            if 'cost' in issue:
                confirm = input("You wish to know how much a video/subscription costs, correct? (y|n)\n")
                if confirm == 'y':
                    print("Prices for each video/subscription are set by the uploaders themselves. In order to find out"
                          "the exact cost, please visit their personal upload page where you can subscribe/purchase"
                          "any of their provided videos.")
                    resolved = True
                else:
                    print("Sorry, let's try that again.")
                    continue
        else:
            repeat = input("Sorry, I'm not sure I can solve that. Want to ask another question? (y|n)\n")

            if repeat == 'y':
                continue
            else:
                print('No worries, returning to main menu.\n')

    return resolved


def producer_payments_func():
    print("Issues with setting up payments for your content? No problem!\n")
    resolved = False

    while not resolved:
        issue = input("Please describe your issue below.\n")
        for word in issue:
            if word.isdigit():
                confirm = input("You want to charge a certain amount for a video/subscription, correct? (y|n)\n")
                if confirm == 'y':
                    print("Okay. Please provide the following info: \n")
                    sell = input("SUBSCRIPTION or VIDEO: \n")

                    if sell == 'subscription':
                        recurrence = input('MONTHLY/DAILY/YEARLY?')
                        plan.set_subscription(recurrence)
                        amount = input('How much would you like to charge?\n')
                        plan.set_price(amount)

                        mockDB[plan.get_subscription()] = plan.get_price()
                        print("Thank you. Your information has been uploaded to our database.")
                        resolved = True
                    elif sell == 'video':
                        recurrence = input("Will this be per-view or unlimited?")
                        plan.set_subscription(recurrence)
                        amount = input("How much would you like to charge?")
                        plan.set_price(amount)

                        mockDB[plan.get_subscription()] = plan.get_price()
                        print("Thank you. Your information has been uploaded to our database.")
                        resolved = True
                    else:
                        print("Sorry, let's try that again.")
                        continue
                else:
                    print("Sorry, let's try that again.")
                    continue

        if 'not' in issue:
            if 'paid' in issue:
                confirm = input("You're asking about not being paid for a certain video/subscription, correct? (y|n)\n")
                if confirm == 'y':
                    print("Sorry to hear that! Allow me to pull up the information from our database.\n")
                    # No database implemented, so test values printed. DB would pull info from producer table
                    print("VIDEOS/VIEWS: VIDEO1/100K\n")
                    # DB would pull pending payments here as well
                    print("You currently have X pending pay-outs.\n")
                    ticket = randint(1, 100)
                    support_status.ticket = ticket
                    support_status.set_status_level(1)
                    mockDB[support_status.ticket] = support_status.get_status_level()

                    print("A troubleshoot ticket has been issued for you. Please contact live support for further"
                          "support with the following ticket #: ", ticket)
                    resolved = True
                else:
                    print("Sorry, let's try that again.")
        else:
            repeat = input("Sorry, I'm not sure I can solve that. Want to ask another question? (y|n)\n")

            if repeat == 'y':
                continue
            else:
                print('No worries, returning to main menu.\n')

    return resolved


# Function to provide user with list of products offered
def inquire_func():
    inquiry = input("Want to know about our products? Ask away!\n")
    resolved = False

    while not resolved:
        if 'videos' in inquiry:
            if 'kids' in inquiry:
                print("If you would like to know about our videos for children, there are plenty that our users have"
                      "uploaded! Please search relatable keywords such as 'kids videos' to search our wide array of"
                      "videos!\n")
                resolved = True

        if 'videos' in inquiry:
            if 'music' in inquiry:
                print("If you would like to know about our music videos, we have plenty of user-uploaded music and"
                      "professional music videos as well! Please use the site searchbar to find any genre you like!\n")
                resolved = True

        if 'videos' in inquiry:
            if 'cosplay' in inquiry:
                print("If you would like to know about any videos revolving cosplayers, we have a growing userbase"
                      "uploading these videos! You may find links on the homepage under the category 'Cosplay' or"
                      "you can even search for them using the search bar!\n")
                resolved = True

        if 'video' in inquiry:
            if 'user' in inquiry:
                # Here we would search for the user in our DB to pull up the results
                user_name = input("Please enter the full name of the user below:\n")
                print("Here are the following videos by ", user_name)
                print(mockDB[user_name])

    return resolved


# Main ChatBot Process
def main_func(user_type):
    requirement = input("What would you like to do today? Please pick a number:\n"
                        "1. Troubleshooting Help\n"
                        "2. Manage Payments\n"
                        "3. Inquire about Content\n"
                        "4. Exit\n")

    while (requirement != '1') and (requirement != '2') and (requirement != '3') and (requirement != '4'):
        requirement = input("Sorry, please enter a valid number between 1-3:\n"
                            "1. Troubleshooting Help\n"
                            "2. Manage Payments\n"
                            "3. Inquire about Content\n"
                            "4. Exit\n")

    if requirement == '1':
        if user_type == 'user':
            user_trouble_func()
        else:
            producer_trouble_func()
    elif requirement == '2':
        if user_type == 'user':
            user_payments_func()
        else:
            producer_payments_func()
    elif requirement == '3':
        inquire_func()
    elif requirement == '4':
        print("Thank you for using TechBot Support! Goodbye!")
        sys.exit()

    final_check = input("Would you like to perform another action? (y|n)\n")
    if final_check == 'y':
        main_func(user_type)
    else:
        print("Thank you for using TechBot Support! Goodbye!")
        sys.exit()


# Program begins here
if __name__ == "__main__":
    # Here, we initialize ticket and class to 000. In a more fleshed out version, this info is grabbed from a database
    # This means that check ticket request only works if a different troubleshoot function has been performed already
    mockDB = {}
    response = input("Welcome to Tech Inc Support!\nMy name is TechBot! Before we start, are you a user or producer?\n")

    while (response != 'user') and (response != 'producer'):
        response = input("Sorry, I didn't get that. Are you a user or producer?\n")

    if response == 'user':
        user = User('John', 'Yearly')
        print("Welcome back, John!\n")
        support_status = TechSupport(000)
        plan = ManagePayments('Test', 0)
        main_func('user')

    if response == 'producer':
        producer = Producer('Jane')
        print("Welcome back, Jane!\n")
        support_status = TechSupport(000)
        plan = ManagePayments('Test', 0)
        main_func('producer')
