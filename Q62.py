'''3.     Assume a file city.txt with details of 5 cities in given format (cityname population(in lakhs) area(in sq KM) ):
Example:
Dehradun 5.78 308.20
Delhi 190 1484
……………
Open file city.txt and read to:
a.     Display details of all cities
b.     Display city names with population more than 10Lakhs
c.     Display sum of areas of all cities
 
'''
with open("city.txt", "w") as file:
    file.write("Dehradun 5.78 308.20\n")
    file.write("Delhi 190 1484\n")
    file.write("Mumbai 124 603\n")
    file.write("Chandigarh 11 114\n")
    file.write("Jaipur 30 467\n")
with open("city.txt", "r") as file:
    lines = file.readlines()
cities = []
for line in lines:
    parts = line.strip().split()
    name = parts[0]
    population = float(parts[1])
    area = float(parts[2])
    
    cities.append((name, population, area))
print("All City Details:")
for city in cities:
    print(city[0], city[1], city[2])
print("\nCities with population more than 10 lakhs:")
for city in cities:
    if city[1] > 10:
        print(city[0])


total_area = sum(city[2] for city in cities)

print("\nTotal area of all cities:", total_area)