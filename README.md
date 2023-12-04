# FOOD TRUCK FINDER


This project uses docker and docker compose, make sure you have installed them.

1. Clone the repository: `git clone git@github.com:guibeira/food-truck-finder.git`
2. Navigate to the project directory: `cd food-truck-finder`
3. build docker image: `make build`

## Run

Before you run, make sure you import the CSV data, to do this first launch the bash with this command:
```bash
make bash
```
then import the file using this command:
```bash
python manage.py import_foodtrucks food-truck-data.csv
```
With all the data ingested, now you can run the project
```bash
make run
```
## Getting food trucks
with the project up and running, you can grab the truck in this endpoint:
```bash
curl --location 'http://localhost:8000/api/food-trucks'
```
To get the near trucks, just send the `longitude`, `latitude` and `distance` filters: 
```bash
curl --location 'http://localhost:8000/api/food-trucks/?distance=1000&longitude=-122.4035462541838&latitude=37.77102199924369'
```
## Test
For tests, the project has this command:
```bash
make test
```