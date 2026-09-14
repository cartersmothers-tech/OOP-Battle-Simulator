from goblin import Goblin
from hero import Hero


ARENA_NAME = "The Diamond Circle"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Big Bean")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    goblinTwo = Goblin("Little Bean")
    
    print(f"{goblinTwo.name} enters the arena with {goblin.health} health.")
    print("But no hero has answered the call... yet.")

    print("... Wait What is That I hear?")
    print("?!?")

   

    hero = Hero("Cali")

    print(f"{hero.name} enters the arena with {hero.health} health.")



    # Cali attacks should return a number
    print (f"The hero attacks {goblinTwo.name}")
    CaliAttackNumber = hero.attack()
    goblin.take_damage=CaliAttackNumber
    
    




if __name__ == "__main__":
    main()
