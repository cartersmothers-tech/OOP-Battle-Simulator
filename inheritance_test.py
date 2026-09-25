from goblin import Goblin
from boss import Boss


enemies = [
    Goblin("Jim"),
    Boss("Jim's Boss"),
]

for enemy in enemies:
    print(f"\n{enemy.name} enters with {enemy.health} health.")

    damage = enemy.attack()
    print(f"{enemy.name} attacks for {damage} damage!")

    enemy.take_damage(20)
    print(f"Still alive: {enemy.is_alive()}")