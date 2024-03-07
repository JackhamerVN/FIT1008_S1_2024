from enum import Enum

class PokeType(Enum):
    """
    This class contains all the different types that a Pokemon could belong to
    """
    FIRE = 0
    WATER = 1
    GRASS = 2
    BUG = 3
    DRAGON = 4
    ELECTRIC = 5
    FIGHTING = 6
    FLYING = 7
    GHOST = 8
    GROUND = 9
    ICE = 10
    NORMAL = 11
    POISON = 12
    PSYCHIC = 13
    ROCK = 14

def get_effectiveness(attack_type: PokeType, defend_type: PokeType) -> float:
    """
    Returns the effectiveness of one Pokemon type against another, as a float.

    Parameters:
        attack_type (PokeType): The type of the attacking Pokemon.
        defend_type (PokeType): The type of the defending Pokemon.

    Returns:
        float: The effectiveness of the attack, as a float value between 0 and 4.
    """
    effectiveness_table = {}

    with open('type_effectiveness.csv', 'r') as file:
        # Skip the header line
        file.readline()
        for line in file:
            data = line.strip().split(',')
            attacker_type = PokeType[data[0]]  # Convert CSV value to enum
            effectiveness_table[attacker_type] = {defender_type: float(effectiveness) for defender_type, effectiveness in zip(PokeType, data[1:])}

    return effectiveness_table[attack_type][defend_type]

# Example usage
print(get_effectiveness(PokeType.FIRE, PokeType.WATER))  # Output: 0.5

# Example usage
print(get_effectiveness(PokeType.FIRE, PokeType.WATER))  # Output: 0.5