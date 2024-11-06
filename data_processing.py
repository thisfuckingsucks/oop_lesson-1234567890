import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

countries = []
with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries.append(dict(r))

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print all cities in Italy
temps = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        temps.append(city['city'])
print("All the cities in", my_country, ":")
print(temps)
print()

# Print the average temperature for all the cities in Italy
# Write code for me
temps = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        temps.append(float(city['temperature']))
print("The average temperature of all the cities in", my_country, ":")
print(sum(temps)/len(temps))
print()

# Print the max temperature for all the cities in Italy
# Write code for me
temps = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        temps.append(float(city['temperature']))
print("The max temperature of all the cities in", my_country, ":")
print(max(temps))
print()

# Let's write a function to filter out only items that meet the condition
def filter(condition, dict_list):
    filtered_list = []
    for item in dict_list:
        if condition(item):
            filtered_list.append(item)
    return filtered_list


# Let's write a function to do aggregation given an aggregation function and an aggregation key
def aggregate(aggregation_key, aggregation_function, dict_list):
    agg_list = [float(x[aggregation_key]) for x in dict_list]
    return aggregation_function(agg_list)



# Let's write code to
# - print the average temperature for all the cities in Italy
print(aggregate('temperature',lambda x: sum(x)/len(x),(filter(lambda x: x['country'] == 'Italy', cities))))
# - print the average temperature for all the cities in Sweden
print(aggregate('temperature',lambda x: sum(x)/len(x),(filter(lambda x: x['country'] == 'Sweden', cities))))
# - print the min temperature for all the cities in Italy
print(aggregate('temperature',lambda x: min(x),(filter(lambda x: x['country'] == 'Italy', cities))))
# - print the max temperature for all the cities in Sweden
print(aggregate('temperature',lambda x: max(x),(filter(lambda x: x['country'] == 'Sweden', cities))))
