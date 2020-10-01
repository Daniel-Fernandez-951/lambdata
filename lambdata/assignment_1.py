"""Assignment 1- a Collection of Helper Functions"""
import pandas as pd
import numpy as np
import random

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

abbrev_us_state = dict(map(reversed, us_state_abbrev.items()))

def state_cleaner(state_name):
     return us_state_abbrev[state_name]


def date_cleaner(date):
    
    df['day'] = date.dt.day
    df['month'] = date.dt.month
    df['year'] = date.dt.year

    return(date)


print(state_cleaner('Illinois'))

"""Class Based Programming"""

class ExoticAnimals:
    def __init__(self, name,  height, weight, color, legs, species, mammal=True):
        self.name = name
        self.height = height
        self.weight = weight
        self.color = color
        self.legs = legs
        self.species = species
        self.mammal = mammal
        
    def move(self, distance, direction):
        return f"{self.name} travels {distance} meters in {direction} direction!"
    
    def eat(self, food):
        return f"Yum, yum! I love {food}!"

"""Inheritance Class"""

names = ["Roger", "Stuart", "Buddy", "Johnson", "Tommy"]
colors = ["Red", "Green", "Yellow", "Blue"]
species_names = ["Bird", "Rodent", "Reptile", "Fish", "Canine"]

class Anaconda(ExoticAnimals):
    """height and weight is an int"""
    def __init__(self, name,  height, weight, constrictor, color, legs=0, species="snake", mammal=False):
        super().__init__(name, height, weight, color, legs, species, mammal)
        self.constrictor = constrictor
    
    def move(self, distance, direction):
        return f"{self.name} sliters {distance} meters in {direction} direction!"


def create_animal():
    print("Welcome to the program! Please provdie the following info:")
    n = input("What is your animal's name?")
    h = input("What is your animal's height?")
    w = input("What is your animal's weight?")
    c = input("What is your animal's color?")
    l = input("What is your animal's number of legs?")
    s = input("What is your animal's species?")
    m = input("Is your animal a mammal? True or False")
    dist = input("How far will your animal travel?")
    dirc = input("Which direction will your animal go?")
    user_animal = ExoticAnimals(name=n, height=h, weight=w, color=c, legs=l, species=s, mammal=m)
   
    print(user_animal.move(dist, dirc))

def lots_of_animals(n):
    animals = []
    while n > 0:
        a_name = random.choice(names)
        a_height = random.randint(5, 501)
        a_weight = random.randint(2, 2001)
        a_color = random.choice(colors)
        a_legs = random.ranint(0, 5)
        a_specices = random.choice(species_names)
        if a_specices == "Rodents" or a_species == "Canine":
            a_mammal = True
        else:
            a_mammal = False

        a_animal = ExoticAnimals(a_name, a_height, a_weight, a_color, a_legs, a_specices, a_mammal)
        animals.append(a_animal)
        n = n-1
    return animals

