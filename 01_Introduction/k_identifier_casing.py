#!/usr/bin/python3
"""
Purpose: Identifier Casing
    PEP (python Enhancement Proposal) 8 - Coding Style Guide
        - Class names should be 'camelCase'
        - Identifier names should be in snake( or Underscore) case .

    Article: https://ieeexplore.ieee.org/document/5521745?tp=&arnumber=5521745

"""

# Python is case-sensitive language
animal = "DWAG"
print(animal)

# print(Animal)
#NameError: name 'Animal' is not defined. Did you mean: 'animal'?

ANIMAL = "CHEETHA"
print(ANIMAL)

Animal = "Jaguar"
print(Animal)


# ------------------------
# Variable Casing
# 1.Snake Casing or Underscore Casing

gladiator = "Barca"
gladiator_earnings = 999897.19
cost_of_freedom = 97
selling_price_of_gladiator = 50

# 2. Camel casing
Gladiator = "Barca"
GladiatorEarnings = 999897.19
CostOfFreedom = 97
SellingPriceOfGladiator = 50