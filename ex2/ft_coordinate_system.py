#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_coordinate_system.py                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jmesa-ci <jmesa-ci@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/03 00:00:00 by jmesa-ci            #+#    #+#            #
#   Updated: 2026/06/16 12:06:31 by jmesa-ci           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import math


def distance_to_zero(xyz: tuple[float, float, float]) -> float:
    distance = math.sqrt((xyz[0] - 0.0)**2 + (xyz[1] - 0.0)**2
                         + (xyz[2] - 0.0)**2)
    return distance


def distance_between_points(xyz: tuple[float, float, float],
                            xyz2: tuple[float, float, float]) -> float:
    distance = math.sqrt((xyz[0] - xyz2[0])**2 + (xyz[1] - xyz2[1])**2
                         + (xyz[2] - xyz2[2])**2)
    return distance


def convert_to_float(coords_list: list[str]) -> list[float]:
    coords: list[float] = []
    invalid_coords: list[str] = []
    for coord in coords_list:
        try:
            coords.append(float(coord))
        except (ValueError, TypeError):
            invalid_coords.append(coord)
    for invalid_coord in invalid_coords:
        print(f"Error on parameter '{invalid_coord}': could not convert"
              f" string to float: '{invalid_coord}'")
    return coords


def get_player_pos() -> None:
    while True:
        str_coords = str(input("Enter new coordinates"
                               " as floats in format 'x,y,z': "))
        coords_list = str_coords.split(",")
        if len(coords_list) != 3:
            print("Invalid syntax")
        else:
            coords = convert_to_float(coords_list)
            if (len(coords) == 3):
                # ensure a fixed-length 3-tuple for type checkers
                t_coords = (coords[0], coords[1], coords[2])
                print(f"Got a first tuple: {t_coords}")
                print(f"It includes: X={t_coords[0]}, Y={t_coords[1]} "
                      f"Z={t_coords[2]}")
                d2zero = distance_to_zero(t_coords)
                print(f"Distance to center: {round(d2zero, 4)}")
                break

    while True:
        str_coords2 = str(input("Enter new coordinates"
                                " as floats in format 'x,y,z': "))
        coords_list2 = str_coords2.split(",")
        if len(coords_list2) != 3:
            print("Invalid syntax")
        else:
            coords2 = convert_to_float(coords_list2)
            if (len(coords2) == 3):
                t_coords2 = (coords2[0], coords2[1], coords2[2])
                print(f"Got a second tuple: {t_coords2}")
                print(f"It includes: X={t_coords2[0]}, Y={t_coords2[1]} "
                      f"Z={t_coords2[2]}")
                d2points = distance_between_points(t_coords, t_coords2)
                print(f"Distance between points: {round(d2points, 4)}")
                break


if __name__ == "__main__":
    get_player_pos()
