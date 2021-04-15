## Project Description
Users can keep track of all the known squirrels and plans to start with Central Park. 
It's an web application that can import the 2018 Central Park Squirrel Census data and allow his team to add, update, and view squirrel data.

## Group Information
- Project Group 34
- UNIs: [ss6125, ns3535]

## Command
1. Import command:
```
$ python manage.py import_squirrel_data /path/to/file.csv
```
2. Export command:
```
$ python manage.py export_squirrel_data /path/to/file.csv
```
3. View the location of squirrel sightings on a map:
   - Locate at: ```/map```
4. View the list of all squirrel sightings:
   - Locate at: ```/sightings```
5. Update a particular squirrel sighting:
   - Locate at: ```/sightings/<unique-squirrel-id>```
6. Add a new squirrel sighting:
   - Locate at: ```/sightings/add```

