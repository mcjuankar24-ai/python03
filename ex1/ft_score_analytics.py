#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_score_analytics.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jmesa-ci <jmesa-ci@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/03 14:31:52 by jmesa-ci            #+#    #+#            #
#   Updated: 2026/06/16 11:38:47 by jmesa-ci           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def convert_to_int(args: list[str]) -> list[int]:
    scores_list: list[int] = []
    score: int
    for arg in args:
        try:
            score = int(arg)
            scores_list.append(score)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    return scores_list


def ft_score_analytics(str_list: list[str]) -> None:
    scores_list: list[int] = convert_to_int(str_list)
    if not scores_list:
        print("No scores provided. Usage: python3"
              "ft_score_analytics.py <score1> <score2> ...")
        return

    players: int = len(scores_list)
    print(f"Scores processed: {scores_list}")
    print(f"Number of players: {players}")
    print(f"Total score: {sum(scores_list)}")
    print(f"Average score: {sum(scores_list) / players}")
    print(f"High score: {max(scores_list)}")
    print(f"Low score: {min(scores_list)}")
    print(f"Score range: {max(scores_list)-min(scores_list)}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    argc: int = len(sys.argv)
    args: list[str] = sys.argv
    str_list: list[str] = args[1:]
    if argc == 1:
        print("No scores provided. Usage: python3"
              " ft_score_analytics.py <score1> <score2> ...")
    else:
        ft_score_analytics(str_list)
