# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import csv
from csv import reader
from csv import DictReader
from rasa_sdk.events import SlotSet
import pandas as pd

#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_do_sth"

    # def run(self, dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    #     with open('addresses.csv', newline='', encoding="cp437") as csvfile:
    #         spamreader = csv.reader(csvfile, delimiter='.', quotechar='|')
    #         for row in spamreader:
    #             msg = ''.join(row)
    #             dispatcher.utter_message(text=msg)
    #
    #     return []

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        prenom = tracker.get_slot("first_name")
        nom = tracker.get_slot("last_name")
        with open('Clients.csv', 'r') as csvfile:
            csv_dict_reader = DictReader(csvfile)
            for row in csv_dict_reader:
                if(row['NOM'] == nom and row['PRENOM'] == prenom ):
                    with open('Banques.csv', 'r') as Ncsvfile:
                        csv_dict_reader_2 = DictReader(Ncsvfile)
                        for row2 in csv_dict_reader_2:
                            if (row2['CODE'] == row['BANQUE']):
                                print('Vous êtes ', row['NOM'] , row['PRENOM'] , ' de la banque ' , row2['LIBELLE LONG'] , ' avec la version AMPLITUDE:  ' , row2['VERSION EMPLITUDE'])
                                # msg = ''.join(row)
                                msg = 'Vous êtes '+ row['NOM'] + ' ' + row['PRENOM'] + ' de la banque ' + row2['LIBELLE LONG'] + ' avec la version AMPLITUDE:  ' + row2['VERSION EMPLITUDE']
                                # tracker.slots["Bank_name"] = row2['LIBELLE LONG']
                                # tracker.slots["Amplitude_version"] = row2['VERSION EMPLITUDE']
                                # SlotSet("Bank_name",testBnk)
                                # bank = tracker.get_slot("Bank_name")
                                # print('La banque est:', bank)
                                dispatcher.utter_message(text=msg)
                                break
                    break
        return [SlotSet("Bank_name", row2['LIBELLE LONG']), SlotSet("Amplitude_version", row2['VERSION EMPLITUDE'])]