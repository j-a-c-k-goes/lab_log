'''
    Context: A tool to achieve the automation & organization of lab notes/class notes
    Author: Neo Information Technology & Design

    log must include:
    • user (name, class, email, instructor, etc.) created and imported from user.py
    • date
    • summary of what is being worked on
    • major goal for current and future session
    • items completed
    • items incomplete
    • questions from the session
    • output of current session into parent .json data structure
    • output of current session into individual .txt file
'''

# imports
import json
from datetime import datetime
from user import *

# log class
class DayLog():
    def __init__(self):
        pass

    ''' functions for display data '''
    # date
    def date():
        day = datetime.now().day
        month = datetime.now().month
        year = datetime.now().year
        hour = datetime.now().hour
        minute = datetime.now().minute
        full = str(datetime.now())
        return {
            "day": day,
            "month": month,
            "year": year,
            "hour": hour,
            "minute": minute,
            "full": full
        }
    # basic welcome message
    def welcome_msg(self, date, user_json=".user.json"):
        with open(user_json, "r+") as file:
            print("loading file with user base data")
            user_creds = json.load(file)
        msg = f'''
        { user_creds["name"]["fname"] } { user_creds["name"]["lname"] }
        { user_creds["class"] }
        { user_creds["email"] }

        LOG DATE: { date["day"] } { date["month"] } { date["year"] } | { date["hour"] }:{ date["minute"] } 
        '''
        print(msg.upper())
        return msg.upper()

    ''' functions to input data '''
    # key topcis from series of inputs, returns an array
    def key_topics():
        topics = []
        entering_data = True
        print("\nKEY TOPICS:\n")
        while entering_data is True:
            topic = str(input("enter a topic covered during today's session (type STOP to stop): "))
            if topic.upper() == "STOP" or topic.upper() == "":
                print("triggering stop. breaking loop.")
                break
            else:
                print("adding: ", topic)
                topics.append(topic)
        return topics
    # questions from series of inputs, returns an array
    def questions():
        questions = []
        entering_data = True
        print("\nQUESTIONS:\n")
        while entering_data is True:
            question = str(input("enter a question you had during today's session (type STOP to stop): "))
            if question.upper() == "STOP" or question.upper() == "":
                print("triggering stop. breaking loop.")
                break
            else:
                print("adding: ", question)
                questions.append(question)
        return questions
    # major goal for next time is an input which returns a string
    def next_major_goal():
        print("\nMAJOR GOAL:\n")
        goal = str(input("enter a major goal to accomplish next time: "))
        return goal
    # log summary is an input which returns a string
    def summary():
        summaries = []
        entering_data = True
        print("\nSUMMARY:\n")
        while entering_data is True:
            summary = str(input("input summary relative to key topics (type STOP or press enter to stop): "))
            if summary.upper() == "STOP" or summary.upper() == "":
                print("triggering stop. breaking loop.")
                break
            else:
                print("adding:", summary)
                summaries.append(summary)
        return summary
    # completed items formed from input, returns an array
    def complete():
        entered_items = []
        entering_items = True
        print("\nITEMS COMPLETE\n")
        while entering_items is True:
            item = str(input("enter a completed task/element/item for today's work (type STOP to stop): "))
            if item.upper() == "STOP" or item.upper() == "":
                print("triggering stop. breaking loop.")
                break
            else:
                print("adding: ", item)
                entered_items.append(item)
        return entered_items   
    # incomplete items formed from input, returns an array
    def incomplete():
        incomplete_items = []
        entering_items = True
        print("\nITEMS COMPLETE\n")
        while entering_items is True:
            item = str(input("enter incomplete tasks/items for today (type STOP to stop): "))
            if item.upper() == "STOP" or item.upper() == "":
                print("triggering stop. breaking loop.")
                break
            else:
                print("adding: ", item)
                incomplete_items.append(item)
        return incomplete_items
    
    ''' functions to load/save data '''
    # export data to .json
    def save_to_json(self, data, filename):
        with open(filename, "r+") as file:
            print("writing log to .json data file")
            file_data = json.load(file)
            file_data.append(data)
            file.seek(0)
            json.dump(file_data, file, indent=4)  
    # export data to .txt file
    def log_to_txt(self, date, data, user_json=".user.json"):
        
        # get user data
        print("retrieving user data")
        with open(user_json, "r+") as file:
            user_creds = json.load(file)
        print("user data retrieved")

        # build accronym from user datapoint for file naming
        def build_accronym(obj, key_name ):
            to_accr = obj[key_name].split(" ")
            accr = ""
            print("creating accronym for: ", obj[key_name])
            for name in to_accr:
                accr += name[0].upper()
            print("accronym created!")
            return accr
        accronym = build_accronym(user_creds, "class")

        # name the file
        filename = f"{ accronym }_{ user_creds['name']['lname'] }_{ date['full'] }.txt"
        with open (f"../logs/{filename}", "w+") as file:
            for key, value in data.items():
                file.write(f"{key}: {value}\n")
      
    ''' functions to shape data '''
    def log(self, date):
        log = {
            "date": date["full"],
            "key_topics": DayLog.key_topics(),
            "summary": DayLog.summary(),
            "questions": DayLog.questions(),
            "complete": DayLog.complete(),
            "incomplete": DayLog.incomplete(),
            "next_major_goal": DayLog.next_major_goal(),
        }
        return log
        
# on run
if __name__ == "__main__":
    date = DayLog.date()
    msg = DayLog().welcome_msg(date)
    log = DayLog().log(date)
    save_json = DayLog().save_to_json(log, "../master/master_log.json")
    save_txt = DayLog().log_to_txt(date, log)