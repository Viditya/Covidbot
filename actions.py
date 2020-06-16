# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import ast
from rasa_sdk.events import SlotSet


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

class ActionCoronaDistrictTracker(Action):

    def name(self) -> Text:
        return "action_corona_district_tracker"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get('https://api.covid19india.org/state_district_wise.json').json()

        entities = tracker.latest_message['entities']
        print('Last Message Now ', entities)
        district = None

        lat_long = []
        if len(entities) == 1:
            for e in entities:
                if len(entities) == 1:
                    district = e['value']
                    print(district)
                    message = "Please enter correct district name"

                    for data in response:
                        states = response[data]
                        # print(states)
                        # if data["state"] == state.title():
                        for state in states:
                            districts = states[state]
                            # print(districts)

                            for districtname in districts:
                                if districtname == district.title():
                                    print(districtname)
                                    districtstatus = districts[districtname]
                                    print(districtstatus)

                                    message = "Thanks for sharing you location. " + districtname + " is pretty place.\n\n The latest status for " + districtname + " is => " + "Active: " \
                                              + str(districtstatus["active"]) + " Confirmed: " + str(
                                        districtstatus["confirmed"]) + \
                                              " Recovered: " + str(districtstatus["recovered"]) + " Deceased: " \
                                              + str(
                                        districtstatus["deceased"]) + "\n\nDo you know the state in which your location" \
                                                                      " lies? No worries, we are just checking you were paying attention in your geography classes 😉" \
                                              + "\n\nPlease help us with the state you are living in"
                                    #print("Message: " + message)

        elif len(entities) == 2:
            for e in entities:
                district = e['value']
                print(district)
                lat_long.append(district.split(":")[1])
                print(lat_long)
        #
            lat = lat_long[1]
            long = lat_long[0]
            print(lat,long)
        #
            url = 'https://api.bigdatacloud.net/data/reverse-geocode-client?latitude=' + lat + '&longitude=' + long + '&localityLanguage=en'
            print(url)
            res_data = requests.get(url).json()
            #district_gl = res_data["locality"]
            print("Locality: " + res_data["locality"])
            state_gl = res_data["principalSubdivision"]
            txt = res_data["localityInfo"]["administrative"][2]["name"]
            sep = txt.split()[-1]
            dist = ' district'
            dist2 = ' District'

            if sep == dist.split()[-1]:
                district_gl = txt.split(dist)[0]
            elif sep == dist2.split()[-1]:
                district_gl = txt.split(dist2)[0]
            elif sep == txt:
                district_gl = txt

            #district_gl = res_data["localityInfo"]["administrative"][2]["name"].split(' district')[0]
            #print(district_gl == res_data["locality"])
            print("District: " + district_gl)
            if district_gl == "Gautam Buddh Nagar":
                district_gl = "Gautam Buddha Nagar"
            elif district_gl == "Thoothukudi":
                district_gl = "Thoothukkudi"
            elif district_gl == "Bagpat":
                district_gl = "Baghpat"
            elif district_gl == "Tirupur":
                district_gl = "Tiruppur"
            print(state_gl)

            for data in response:
                states = response[data]
                # print(states)
                # if data["state"] == state.title():
                for state in states:
                    districts = states[state]
                    # print(districts)

                    for districtname in districts:
                        if districtname == district.title() or districtname == district_gl:
                            #print(districtname)
                            districtstatus = districts[districtname]
                            #print(districtstatus)

                            message1 = "Thanks for sharing you location. " + districtname + " is pretty place.\n\n The latest status for " + districtname + " is => " + "Active: " \
                                      + str(districtstatus["active"]) + " Confirmed: " + str(
                                districtstatus["confirmed"]) + \
                                      " Recovered: " + str(districtstatus["recovered"]) + " Deceased: " \
                                      + str(
                                districtstatus["deceased"])
                            print("Message 1: " + message1)

            response = requests.get('https://api.covid19india.org/data.json').json()

            # entities = tracker.latest_message['entities']
            # print('Last Message Now ', entities)
            # state = None

            for e in entities:
                message = "Please enter correct state name"
                for data in response["statewise"]:
                    #print(state_gl)
                    if data["state"] == state_gl:
                        #print(data)

                        message2 = "\n\nThe status for " + data["state"] + " is => " + "Active: " + data[
                                "active"] + " Confirmed: " + data["confirmed"] + " Recovered: " + data["recovered"] \
                                      + " Deceased: " + data["deaths"] + " On " + data["lastupdatedtime"]
                        #print("Message 2: " + message2)

                        message = message1 + message2
                        print(message)

        dispatcher.utter_message(message)

        #return [SlotSet("url", url)]
        return  []

class ActionCoronaTracker(Action):

    def name(self) -> Text:
        return "action_corona_tracker"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get('https://api.covid19india.org/data.json').json()

        entities = tracker.latest_message['entities']
        print('Last Message Now ', entities)
        state = None

        for e in entities:
             if e['entity'] == "state":
                state = e['value']

        message = "Please enter correct state name"
        for data in response["statewise"]:
            if data["state"] == state.title():
                print(data)


                message = "The status for " + data["state"] + " is => " + "Active: " + data["active"] + " Confirmed: " + data["confirmed"] + " Recovered: " + data["recovered"] \
                          + " Deceased: " + data["deaths"] + " On " + data["lastupdatedtime"]
                print("Message: " + message)

        dispatcher.utter_message(message)

        return []

