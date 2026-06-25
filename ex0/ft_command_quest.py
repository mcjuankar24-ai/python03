#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_command_quest.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jmesa-ci <jmesa-ci@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/03 14:26:51 by jmesa-ci            #+#    #+#            #
#   Updated: 2026/06/16 11:17:29 by jmesa-ci           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def ft_command_quest(arg: str, index: int) -> None:
    print(f"Argument {index}: {arg}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    argc: int = len(sys.argv)
    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments recieved: {argc - 1}")
    if argc == 1:
        print("No arguments provided!")
    index: int = 1
    for argument in sys.argv[1:]:
        ft_command_quest(argument, index)
        index += 1
    print(f"Total arguments: {argc}")
