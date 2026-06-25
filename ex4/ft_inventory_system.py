#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_inventory_system.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jmesa-ci <jmesa-ci@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/04 12:36:52 by jmesa-ci            #+#    #+#            #
#   Updated: 2026/06/16 11:58:55 by jmesa-ci           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


class DuplicatedItem(Exception):
    def __init__(self, message: str = "Redundant item. Discarding") -> None:
        super().__init__(message)


class InvalidParameter(Exception):
    def __init__(self, message: str = "Invalid parameter") -> None:
        super().__init__(message)


def inventory_show(inventory: dict[str, int]) -> None:
    inv_size: int = len(inventory)
    if (inv_size == 0):
        print("Your inventory is empty!")
    else:
        print(f"Got inventory: {inventory}")
        list_items: list[str] = list(inventory.keys())
        list_values: list[int] = list(inventory.values())
        total_quantity: int = sum(list_values)

        print(f"Item list: {list_items}")
        print(f"Total quantity of the {len(list_items)} "
              f"items: {total_quantity}")

        for item, qty in inventory.items():
            porcentage: float = round((int(qty) / total_quantity * 100), 1)
            print(f"Item '{item}' represents {porcentage}%")

        most_item, most_qty = max(inventory.items(), key=lambda itm: itm[1])
        least_item, least_qty = min(inventory.items(), key=lambda itm: itm[1])

        print(f"Item most abundant: {most_item} with quantity {most_qty}")
        print(f"Item least abundant: {least_item} with quantity {least_qty}")


def inventory_parse(args: list[str],
                    dictionary: dict[str, int]) -> dict[str, int]:
    for obj in args:
        try:
            if ":" not in obj:
                raise InvalidParameter(f"Error - invalid parameter '{obj}'")

            item, quantity = obj.split(":", 1)
            if item in dictionary:
                raise DuplicatedItem(f"Redundant item '{item}' - discarding")

            dictionary[item] = int(quantity)
        except InvalidParameter as error:
            print(error)
        except DuplicatedItem as error:
            print(error)
        except ValueError as error:
            print(f"Quantity error for '{item}': {error}")

    return dictionary


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    args_input: list[str] = sys.argv[1:]
    inventory: dict[str, int] = {}
    if (len(sys.argv) < 2):
        print("Empty inventory")
    else:
        inventory = inventory_parse(args_input, inventory)
        inventory_show(inventory)
    inventory = inventory_parse(["magic item:2"], inventory)
    print(f"Updated inventory: {inventory}")
