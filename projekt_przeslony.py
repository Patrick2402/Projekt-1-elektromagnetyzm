from random import uniform
from math import sqrt,log10
import argparse

frequency = 4.28e9
c = 3.0e8
wave_len = c/frequency
data = []

def generating_params(itterations):
    for it in range(itterations):
        shape_size        = round(uniform(0.0000001 , wave_len / 2),8)
        #separation_size  = round(uniform(0.0000001 , wave_len / 10), 8)
        separation_size   = wave_len / 10
        neighbors         = getNeighbor(shape_size=shape_size, separation_size=separation_size)
        infos             = {"shape_size": shape_size, "separation_size": separation_size, "neighbors": neighbors,"sn":count_s(shape_size=shape_size,neighbors=neighbors), "sps": for_50_cm(shape_size=shape_size,separation_size=separation_size),"quality":shape_size*for_50_cm(shape_size=shape_size,separation_size=separation_size)}
        data.append(infos)
    score = (find_project_req(data))
    print('Shape size: ',score["shape_size"]*100)
    print('Separation size: ',score["separation_size"])
    print('Neighbors: ',score["neighbors"])
    print('Sn: ',score["sn"])
    print('All holes: ',score["sps"]**2)
    print('Quality: ',score["quality"])

def find_project_req(data):
    try:
        min_sn = 22.
        data = list(filter(lambda x: x["sn"] >= min_sn, data))
        return max(data, key=lambda x: x["quality"])
    except ValueError:
        print("Any Candidate pass project requirements")
        exit(0)
    
def getNeighbor(shape_size, separation_size):
    overallsize = shape_size/2
    n = 0 
    while overallsize <= wave_len / 2:
        overallsize += separation_size + shape_size
        n += 1
    return n

def for_50_cm(shape_size,separation_size):
    x = 0
    xn = 0
    while x < 0.5:
        x += separation_size + shape_size
        xn += 1
    return xn

def count_s(shape_size,neighbors):
    s = 20*log10((wave_len/(2*shape_size))) - 20*log10(sqrt(neighbors))
    return s


parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-i', '--iterations', type=int,   default=1,      help='Number of interations')
args = parser.parse_args()

generating_params(args.iterations)
