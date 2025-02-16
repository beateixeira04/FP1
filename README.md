# FP1
Primeiro projeto da cadeira de fundamentos de programação - 1º ano de faculdade

Parking Management System (IAED Project 1 - 2023/24)
Overview

This project implements a Parking Management System designed to manage parking lots, vehicle entries and exits, as well as billing calculations. The system handles creating parking lots, registering vehicle movements, querying vehicle history, displaying parking lot billing, and removing parking lots.
Features:

    Parking Lot Creation: Define parking lots with a name, capacity, and billing rates.
    Vehicle Entry & Exit: Record vehicle entries and exits with specific timestamps.
    Vehicle Usage History: Query the entry and exit history of a vehicle.
    Billing System: Calculate and display parking fees, either by specific date or overall for a parking lot.
    Remove Parking Lots: Safely remove parking lots and their associated data.

Grade

Grade: 19.75/20
Commands

    q: Exit the program.
    p [<name> <capacity> <rate1> <rate2> <max_daily>]: Create or list parking lots.
    e <lot> <license_plate> <date> <time>: Register a vehicle entry.
    s <lot> <license_plate> <date> <time>: Register a vehicle exit.
    v <license_plate>: List all entries and exits of a vehicle.
    f <lot> [<date>]: Show the billing for a parking lot (daily or by date).
    r <lot>: Remove a parking lot from the system.

Requirements

    C language with standard libraries: stdio.h, stdlib.h, ctype.h, string.h
    GCC compiler with flags: -O3 -Wall -Wextra -Werror -Wno-unused-result

Compilation

To compile the program, run:

gcc -O3 -Wall -Wextra -Werror -Wno-unused-result -o proj1 *.c

Running the Program

Execute the program with:

./proj1 < input_file > output_file

To test the output, use:

diff expected_output_file output_file

