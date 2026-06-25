#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_data_stream.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jmesa-ci <jmesa-ci@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/05 15:10:37 by jmesa-ci            #+#    #+#            #
#   Updated: 2026/06/16 12:05:01 by jmesa-ci           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import typing
import random

PLAYERS: tuple[str, ...] = (
    "Alberto",
    "Juan Carlos",
    "Guillermo",
    "María",
    "Marcela",
    "Miguel",
    "Leon",
    "Cristian",
    "Jorge",
    "Alejandro"
)

ACTIONS: tuple[str, ...] = (
    "Hardcodea",
    "Programa",
    "GPTea",
    "Come",
    "Baila",
    "Juega",
    "Duerme"
)


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while (True):
        name = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (name, action)


def consume_event(
    events: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while events:
        index = random.randrange(len(events))
        yield events.pop(index)


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    g: typing.Generator[tuple[str, str], None, None] = gen_event()
    name: str
    action: str
    name, action = next(g)

    print("\n1000 loops")
    i: int = 1
    while i < 1001:
        name, action = next(g)
        print(f"Event {i}: player {name} '{action}'")
        i += 1
    list_events: list[tuple[str, str]] = []
    i = 0
    print("=== Creating a list of 10 events")
    while i < 10:
        list_events.append(next(g))
        i += 1
    print(f"{list_events}")
    print("=== Consuming the list of 10 events")
    for event in consume_event(list_events):
        name, action = event
        left: int = len(list_events)
        print(f"Event: player {name} '{action}'")
        print(f"{left} players/actions left")
        left -= 1
    print("=== End of program")
