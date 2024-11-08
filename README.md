# Overview
Creates an IoT carpark system [AT3 Project (PRJ) - V2.1 - Reference(C-IP4RIoT-PRJ-V2-OOP.docx)]

## Business Case
### Overview

The system will consist of a car park, sensors, and displays to track the cars entering and exiting and the availability of parking bays.
 
The programming language should be Python and should be using Object Oriented Programming(OOP) concept.

 - The car park opens every day at 5:00 am and closes at 12:00 am.
 - Display the 'OPEN' sign in green during operating hours and the 'CLOSE' sign in red when closed.

### Pseudo Code
1	Import CarPark, Sensor and Display classes
2	Initiate parking sensors
3	xxx number of parking bay sensors read current status and each parking bay sensor return signal(True)
4	Count available parking bay sensors and display the number on the sign
5	Count how many cars in the parking bay and update car_count variable.
6	If a car enters the car parking, record the number plate and find the colours from the list.
7	If the colour is not recognised by the sensor, assign 'Unknown'
8	car_count variable add 1
9	Once the car parked on a parking bay, the parking bay sensor will return signal(True) but it doesn't change car_count variable because it's already updated when the car entered.
10	If a car leave a parking bay, the sensor will return signal(False) but it doesn't change car_count variable.
11	If a car leave the car parking, remove the car detail and reduce car_count variable by 1.


### Workflow
Link: https://tafewa-my.sharepoint.com/:u:/r/personal/j173025_tafe_wa_edu_au1/_layouts/15/doc2.aspx?sourcedoc=%7BD6C7F846-5A5A-4B01-B2E8-677E550AC6CB%7D&file=Drawing%201.vsdx&action=edit&mobileredirect=true&wdTpl=TM89860103&wdlcid=1033&wdnewandopenct=0&ct=1731063766839&wdOrigin=OFFICECOM-WEB.START.NEW&wdPreviousSessionSrc=HarmonyWeb&wdPreviousSession=6e5473f5-1715-4696-874e-65ff342eb44f&cid=e7c43c68-b8bf-41b3-b8f5-86b0fad58520&or=PrevCreateNew