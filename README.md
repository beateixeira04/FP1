# FP1
Primeiro projeto da cadeira de fundamentos de programação - 1º ano de faculdade

Mountains and Valleys Project
Overview

This project, completed as part of the Fundamentals of Programming course (2023-24), focuses on simulating the state of a rectangular territory formed by vertical and horizontal paths. The goal is to work with intersections in this territory, some of which may be occupied by mountains, forming chains of mountains and valleys.

The project involves writing a Python program to analyze and retrieve information about the state of a territory, including the identification of mountains, valleys, and connected intersections.
Key Features

    Territory Representation: A territory is represented as a tuple of vertical paths, where each vertical path contains a series of intersections (either free or occupied by mountains).
    Intersections: Each intersection is represented by a tuple containing a vertical path (letter) and a horizontal path (number).
    Mountain Chains & Valleys: The program identifies connected chains of mountains and the valleys surrounding them.

Functions Implemented
Territory Functions:

    eh_territorio: Checks if an input corresponds to a valid territory.
    obtem_ultima_intersecao: Retrieves the top-rightmost intersection of the territory.
    eh_intersecao: Validates if an argument is a valid intersection.
    eh_intersecao_valida: Checks if an intersection exists in the territory.
    eh_intersecao_livre: Checks if an intersection is free of mountains.
    obtem_intersecoes_adjacentes: Returns valid adjacent intersections.
    ordena_intersecoes: Sorts intersections based on the reading order of the territory.
    territorio_para_str: Converts a territory to a human-readable string format.

Mountain and Valley Functions:

    obtem_cadeia: Returns the chain of connected intersections, either occupied or free, starting from a given intersection.
    obtem_vale: Identifies the valley connected to a given mountain intersection.
    verifica_conexao: Verifies if two intersections are connected.
    calcula_numero_montanhas: Counts the number of mountain intersections in the territory.
    calcula_numero_cadeias_montanhas: Counts the number of distinct mountain chains.
    calcula_tamanho_vales: Calculates the total number of intersections forming all valleys in the territory.

Example
Input:

territory = ((1,1,1,0),(0,1,0,0),(0,0,1,0),(0,0,0,0),(0,0,0,0))
print(territory_to_str(territory))

Output:

 A B C D E
4 . . . . . 4
3 X . X . . 3
2 X X . . . 2
1 X . . . . 1
A B C D E

Project Evaluation

The project was evaluated with a score of 19.75/20.
Requirements

    Python 3.x
    The code is encapsulated in a single .py file.
