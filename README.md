## Project Description

This is an outstanding web application that helps us to track down cute squirrel in Central Park. With imported data, users can keep track of all the known squirrels and be able to add, update, and view squirrel data into our database.

## Group Information
- Project Group 35
- UNIs: [ss6125, ns3535]

## Command
1. Import command:
```
$ python manage.py import_squirrel_data 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv
```
2. Export command:
```
$ python manage.py export_squirrel_data export_data.csv
```
3. View the location of squirrel sightings on a map:
   - Locate at: ```/map```
4. View the list of all squirrel sightings:
   - Locate at: ```/sightings```
5. Update a particular squirrel sighting:
   - Locate at: ```/sightings/<unique-squirrel-id>```
6. Add a new squirrel sighting:
   - Locate at: ```/sightings/add```
7. View the general stats of squirrel sightings:
   - Locate at: ```/sightings/stats```

## Links
- Deployed Link: https://moonlit-buckeye-303409.ue.r.appspot.com
- [To view map](https://moonlit-buckeye-303409.ue.r.appspot.com/map)
- [To view all squirrel sightings](https://moonlit-buckeye-303409.ue.r.appspot.com/sightings)
- [To add a new squirrel sighting](https://moonlit-buckeye-303409.ue.r.appspot.com/sightings/add)
- [To view general stats of squirrel sightings](https://moonlit-buckeye-303409.ue.r.appspot.com/sightings/stats)
