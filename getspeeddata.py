import csv
import os
import toolz as tz


def CSVfileGrabber(dirname):
    """Step 1 : Grab CSV files from a directory """
    for filename in os.listdir(dirname):
        if filename.endswith('.csv'):
            print('Working on: {}'.format(filename[:5]))  # Print name of fish
            yield os.path.join(dirname, filename)


def readxy(filename):
    """Step 2 : read the csv files line by line """
    with open(filename) as f:
        csvreader = csv.reader(f)
        for i, line in enumerate(csvreader):
            # Skip a few lines
            if i < 10:
                continue
            else:
                # x and y coordinates
                x = int(line[2])
                y = int(line[3])
                yield (x, y)


def consecutivexy1(linearray):
    """Step 4: get consecutive xy values"""
    # Here we want to get two consecutive xy to get speed/frame
    # Make use of the next keyword
    for i, line in enumerate(linearray):
        if i == 0:
            prevxy = line
            nextxy = next(linearray)
        else:
            prevxy = nextxy
            nextxy = line
        yield prevxy, nextxy


import math


def getdist(xy):
    # Calculate euclidean distance
    for prevxy, nextxy in xy:
        # zip allows you to iterate two lists parallely
        dist = [(a - b) ** 2 for a, b in zip(prevxy, nextxy)]
        dist = math.sqrt(sum(dist))
        yield dist


@tz.curry
def getframes(dist, threshold=10, frames_per_sec=30):
    dist_count = 0
    for i, d in enumerate(dist):
        if d < threshold:
            dist_count += 1
    print('Of {:0.3f} seconds recording time, time spent with speed less than {} is {:0.3f} seconds'.format(
        i / frames_per_sec, threshold, dist_count / frames_per_sec))
