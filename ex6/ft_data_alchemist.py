#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_data_alchemist.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jmesa-ci <jmesa-ci@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/05 15:58:44 by jmesa-ci            #+#    #+#            #
#   Updated: 2026/06/16 12:03:54 by jmesa-ci           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import random


PLAYERS: tuple[str, ...] = (
    "Alberto",
    "juan Carlos",
    "Guillermo",
    "maría",
    "Marcela",
    "miguel",
    "Leon",
    "cristian",
    "jorge",
    "alejandro"
)


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    all_players: list[str] = list(PLAYERS)
    print(f"Initial list of players: {all_players}\n")

    capt: list[str] = [name.capitalize() for name in PLAYERS]
    print(f"New list with all names capitalized: {capt}\n")

    minus: list[str] = [name for name in PLAYERS if name[0].isupper()]
    print(f"New list of capitalized names only: {minus}\n")

    scores: dict[str, int] = {name: random.randint(0, 1000) for name in capt}
    print(f"Score dict: {scores}\n")

    total: int = sum(scores.values())
    players_capitalized: int = len(scores)
    avg: float = round((total / players_capitalized), 2)
    print(f"Score average is {avg}")
    high_scores: dict[str, int] = {name: value for name, value in
                                   scores.items() if value > avg}

    print(f"High scores: {high_scores}")
