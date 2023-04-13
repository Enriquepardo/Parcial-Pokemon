#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This Python method contains the application of the Game.

@contents :  This module contains the complete implementation of the application
             of the Game.
@project :  N/A
@program :  N/A
@file :  main.py
@author :  Antonio Artes Garcia (antonio.artesgarcia@ceu.es)
           Francisco Hernando Gallego (francisco.hernandogallego@ceu.es)
           Ruben Juarez Cadiz (ruben.juarezcadiz@ceu.es)

@version :  0.0.1, 08 November 2021
@information :  The Zen of Python
                  https://www.python.org/dev/peps/pep-0020/
                Style Guide for Python Code
                  https://www.python.org/dev/peps/pep-0008/
                Example NumPy Style Python Docstrings
                  http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html
                doctest – Testing through documentation
                  https://pymotw.com/2/doctest/

@copyright :  Copyright 2021 GNU AFFERO GENERAL PUBLIC.
              All rights are reserved. Reproduction in whole or in part is
              prohibited without the written consent of the copyright owner.
"""


# Source packages.

import csv
from pokemon import Pokemon
from weapon_type import WeaponType
import random




def get_data_from_user(name_file):
    """Function to obtain data from each user.


    This function obtains data from each user in order to set the configuration
    of the Game.

    Syntax
    ------
      [ ] = get_data_from_user(name_file)

    Parameters
    ----------
      name_file str Name of the CSV file.

    Returns
    -------
      list_pokemons List of Pokemons obtained from CSV .

    Example
    -------
      >>> list_pokemons = get_data_from_user("file.csv")
    """
    
    list_of_pokemons = []
    with open(name_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            id_pokemon = int(row[0])
            pokemon_name = row[1]
            weapon_type = WeaponType[row[2].upper()]
            health_points = int(row[3])
            attack_rating = int(row[4])
            defense_rating = int(row[5])
            pokemon = Pokemon(id_pokemon, pokemon_name, weapon_type, health_points, attack_rating, defense_rating)
            list_of_pokemons.append(pokemon)
    return list_of_pokemons


def get_pokemon_in_a_list_of_pokemons(coach_to_ask, list_of_pokemons):
    """Function to know the list of Pokemons that are associated to the Coach.

    This function is used in order to know the list of Pokemos that are
    associated to the coach. This function prints the result of this list, so
    the user can select a Pokemon.

    Syntax
    ------
       [ ] = get_pokemon_in_a_list_of_pokemons(coach_to_ask, list_of_pokemons):

    Parameters
    ----------
       [in] coach_to_ask Coach to ask for her/his list of Pokemons.
       [in] list_of_pokemons List of the Pokemons that are associated to the
                             coach.

    Returns
    -------
       List List of the Pokemons associaated to the coach that are undefeated.

    Example
    -------
       >>> get_pokemon_in_a_list_of_pokemons(1, list_of_pokemons)
    """
    
    print("------------------------------------------------------------------")
    print("Coach " + str(coach_to_ask) + " select your Pokemon.")
    print("------------------------------------------------------------------")
    print("List of Pokemons:")
    for pokemon in list_of_pokemons:
        print(pokemon)
    print("------------------------------------------------------------------")
    pokemon_id = int(input("Select the ID of the Pokemon: "))
    pokemon = None
    for p in list_of_pokemons:
        if p.get_id() == pokemon_id:  
            pokemon = p
            break
    if pokemon is None:
        print("Invalid Pokemon ID selected.")
    else:
        print("------------------------------------------------------------------")
        print("Coach " + str(coach_to_ask) + " selected the Pokemon: " + str(pokemon))
        print("------------------------------------------------------------------")
    return pokemon


def coach_is_undefeated(list_of_pokemons):
    """Function to know if the Coach is still undefeated.

    This function is used in order to know if the Coach is still undefeated.

    Syntax
    ------
       [ ] = coach_is_undefeated(list_of_pokemons)

    Parameters
    ----------
       [in] list_of_pokemons List of the Pokemons that are associated to the
                             coach.

    Returns
    -------
       Boolean True if the coach has all her/his Pokemons defeated.
               False if the coach has any Pokemon that is undefeated.

    Example
    -------
       >>> coach_is_undefeated(list_of_pokemons)
    """
    
    


def main():
    """Function main of the module.

    The function main of this module is used to perform the Game.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """

    print("Welcome to the Game.")
    print("Let's start to set the configuration of each game user. \n")

    # Get configuration for Game User 1.
    coach_1 = get_data_from_user('coach_1_pokemons.csv')


    # Get configuration for Game User 2.
    coach_2 = get_data_from_user('coach_2_pokemons.csv')

    print("------------------------------------------------------------------")
    print("The Game starts...")
    print("------------------------------------------------------------------")

    # Get a copy of the list of pokemons:
    
    list_of_pokemons_1 = coach_1.copy()
    list_of_pokemons_2 = coach_2.copy()
    print(list_of_pokemons_1)
    
    # Choose first pokemons
    get_pokemon_in_a_list_of_pokemons(1, list_of_pokemons_1)
    get_pokemon_in_a_list_of_pokemons(2, list_of_pokemons_2)

    # Main loop.



    print("------------------------------------------------------------------")
    print("The Game has end...")
    print("------------------------------------------------------------------")


    print("------------------------------------------------------------------")
    print("Statistics")
    print("------------------------------------------------------------------")
    print("Game User 1:")


    print("Game User 2:")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
