import csv

rows = []

with open("final.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader: 
    rows.append(row)

headers = rows[0]
star_data_rows = rows[1:]
print(headers)
print(star_data_rows[0])

headers[0] = "row_num"

solar_system_star_count = {}
for star_data in star_data_rows:
  if solar_system_star_count.get(star_data[2]):
    solar_system_star_count[star_data[2]] += 1
  else:
    solar_system_star_count[star_data[2]] = 1

max_solar_system = max(solar_system_star_count, key=solar_system_star_count.get)
print("Solar system {} has maximum stars {} out of all the solar systems we have discovered so far!".format(max_solar_system, solar_system_star_count[max_solar_system]))

temp_star_data_rows = list(star_data_rows)
for star_data in temp_star_data_rows:
  star_mass = star_data[4]
  if star_mass.lower() == "?":
    star_data_rows.remove(star_data)
    continue
  else:
    star_mass_value = star_mass.split(" ")[0]
    star_mass_ref = star_mass.split(" ")
    if star_mass_ref == "Sun":
      star_mass_value = float(star_mass_value) * 317.8
    star_data[3] = star_mass_value

  star_radius = star_data[5]
  if star_radius.lower() == "?":
    star_data_rows.remove(star_data)
    continue
  else:
    star_radius_value = star_radius.split(" ")[0]
    star_radius_ref = star_radius.split(" ")
    if star_radius_ref == "Sun":
      star_radius_value = float(star_radius_value) * 11.2
    star_data[5] = star_radius_value

print(len(star_data_rows))

import plotly.express as px

star_masses = []
star_names = []
for star_data in star_data_rows:
  star_masses.append(star_data[4])
  star_names.append(star_data[2])

star_masses.append(2)
star_names.append("Sun")

print(star_names)

fig = px.bar(x=star_names, y=star_masses)
fig.show()