import gpxpy
import gpxpy.gpx
import json

FILE_NAME = 'track.gpx'
OUTPUT_FILE = 'track_prepared.txt'

def get_coordinates():
    gpx_file = open(FILE_NAME, 'r')
    gpx = gpxpy.parse(gpx_file)

    coordinates = []

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                coordinates.append((point.latitude, point.longitude))
    return coordinates


def write_json(coordinates):
    data = {}
    data['track'] = []
    for c in coordinates:
        data['track'].append({
            'latitude' : c[0],
            'longitude' : c[1]
        })
    with open(OUTPUT_FILE, 'w') as outfile:
        json.dump(data, outfile)


coordinates = get_coordinates()
write_json(coordinates)
