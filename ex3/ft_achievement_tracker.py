#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_achievement_tracker.py                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jmesa-ci <jmesa-ci@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/03 16:13:15 by jmesa-ci            #+#    #+#            #
#   Updated: 2026/06/16 12:04:47 by jmesa-ci           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import random

my_set = {'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
          'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
          'First Steps', 'Collector Supreme', 'Untouchable',
          'Sharp Mind', 'Boss Slayer', 'Python master', '42 Seconds to Mars'
          'Pope', 'Radiant', 'Whops', 'World Champion', 'Craft Master'
          'Enlightned', 'Developer of tools', 'Apple eater', 'Wow!'
          'Cleaner', 'Horse whisper', 'Flying dog', 'Melendi', 'Olala',
          'Yes i can', 'Water pouring', 'Hash encrypter', 'MaestroPT'
          'GePeTo', 'Gemini', 'Cloude9', 'Alehop'}


def gen_player_achievements() -> set[str]:
    set_as_list: list[str] = list(my_set)
    rnd_int: int = random.randint(4, len(set_as_list))
    ach_list: list[str] = random.sample(set_as_list, rnd_int)
    ach_set = set(ach_list)
    return ach_set


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    set_alice = gen_player_achievements()
    print(f"Player Alice: {set_alice}")
    set_bob = gen_player_achievements()
    print(f"Plater Bob: {set_bob}")
    set_charlie = gen_player_achievements()
    print(f"Player Charlie: {set_charlie}")
    set_dylan = gen_player_achievements()
    print(f"Player Dylan: {set_dylan}")
    print()
    print(f"All distinct achievements:"
          f" {set_alice.union(set_bob).union(set_charlie).union(set_dylan)}")
    print()
    print(f"Common achievements: "
          f"{my_set.intersection(set_alice, set_bob, set_charlie, set_dylan)}")
    print()
    only_alice = set_alice.difference(set_bob, set_charlie, set_dylan)
    only_bob = set_bob.difference(set_alice, set_charlie, set_dylan)
    only_charlie = set_charlie.difference(set_bob, set_alice, set_dylan)
    only_dylan = set_dylan.difference(set_bob, set_charlie, set_alice)

    print(f"Only Alice has: {only_alice}")
    print(f"Only Bob has: {only_bob}")
    print(f"Only Charlie has: {only_charlie}")
    print(f"Only Dylan has: {only_dylan}")
    print()

    missing_alice = my_set.difference(set_alice)
    missing_bob = my_set.difference(set_bob)
    missing_charlie = my_set.difference(set_charlie)
    missing_dylan = my_set.difference(set_dylan)

    print(f"Alice is missing: {missing_alice}")
    print()
    print(f"Bob is missing: {missing_bob}")
    print()
    print(f"Charlie is missing: {missing_charlie}")
    print()
    print(f"Dylan is missing: {missing_dylan}")
