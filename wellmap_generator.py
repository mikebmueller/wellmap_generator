import folium
import csv

# Set tileset and starting map location and zoom
tileset = r'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
wellmap = folium.Map(location=[51, -102], zoom_start=5, tiles=tileset,
    attr=' ')

markercluster = folium.MarkerCluster().add_to(wellmap)

# Open and read welllist.csv
with open('welllist.csv', 'rb') as f:
    wellDict= csv.DictReader(f)

# Loop through welllist.csv (or wherever the dataset is) to insert markers
    for row in wellDict:
        popuptemplate = '<strong>Well Name: </strong>' + row['Well Name'] + '<br><strong>Operator: </strong>' + row['Company'] + '<br><strong>Target Formation: </strong>' + row['Target Formation']
        popuphtml = folium.Html(popuptemplate, script=True)
        iframe = folium.Popup(popuphtml, max_width=650)
        if row['Target Formation'] == 'Bakken':
            popuphtml = folium.Html(popuptemplate, script=True)
            iframe = folium.Popup(popuphtml, max_width=500)
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                popup=iframe,
                icon=folium.Icon(color='beige'),
            ).add_to(markercluster)
        elif row['Target Formation'] == 'Upper Shaunavon B':
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                popup=iframe,
                icon=folium.Icon(color='blue'),
            ).add_to(markercluster)
        elif row['Target Formation'] == 'Lower Shaunavon':
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                popup=iframe,
                icon=folium.Icon(color='purple'),
            ).add_to(markercluster)
        elif row['Target Formation'] == 'Viking':
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                popup=iframe,
                icon=folium.Icon(color='orange'),
            ).add_to(markercluster)
        else:
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                popup=iframe,
                icon=folium.Icon(color='lightgray')
            ).add_to(markercluster)
    wellmap.save('wellmap.html')
