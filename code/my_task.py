#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def calculate_shipping_cost(**items):
    shipping_rate_per_kg = 5

    total_weight = 0
    for item, weight in items.items():
        total_weight += weight

    shipping_cost = total_weight * shipping_rate_per_kg
    return shipping_cost

if __name__ == "__main__":
    items_to_ship = {'book': 0.5, 'laptop': 2, 'clothes': 1.5}
    total_cost = calculate_shipping_cost(**items_to_ship)
    print(f"Общая стоимость доставки: ${total_cost:.2f}")