## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

# greet_mood_great_tellingLocation
* greet
    - utter_greet
* mood_great
    - utter_ask_location
* corona_district
    - action_corona_district_tracker
* corona_state
    - action_corona_tracker
    - utter_goodbye
* goodbye

## greet_mood_great_tellingLocation_bye

* greet
    - utter_greet
* mood_great
    - utter_ask_location
* goodbye

## greet_tellingLocation

* greet
    - utter_greet
    - utter_ask_location
* corona_district
    - action_corona_district_tracker
* corona_state
    - action_corona_tracker
    - utter_goodbye

## greet_mood_great_denyLocation_tellingLocation

* greet
    - utter_greet
* mood_great
    - utter_ask_location
* deny
    - utter_location_denied
* corona_district
    - action_corona_district_tracker
* corona_state
    - action_corona_tracker
    - utter_goodbye

## greet_denyLocation_tellingLocation

* greet
    - utter_greet    
    - utter_ask_location
* deny
    - utter_location_denied
* corona_district
    - action_corona_district_tracker
* corona_state
    - action_corona_tracker
    - utter_goodbye
    
## greet_mood_greet_denyLocation_denyLocation_bye

* greet
    - utter_greet
* mood_great
    - utter_ask_location
* deny
    - utter_location_denied
* deny
    - utter_tryAfter_sometime
    - utter_goodbye

## get_corona_state
* corona_state
    - action_corona_tracker
    
## get_corona_district
* corona_district
    - action_corona_district_tracker