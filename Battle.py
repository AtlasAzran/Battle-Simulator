import random
import time

def attack():
    print("\nYou attack the enemy!")
    time.sleep(0.5)
    return 15

def defend():
    print("\nYou defend against the enemy's attack!")
    time.sleep(0.5)
    return 10

def heal():
    print("\nYou heal yourself!")
    time.sleep(0.5)
    return 20

def enemy():
    enemyatk = random.randint(1, 3)
    if enemyatk == 1:
        print("The enemy attacks you!")
        time.sleep(1)
        return 20
    elif enemyatk == 2:
        print("The enemy defends against your attack!")
        time.sleep(1)
        return 10
    else:
        print("The enemy heals itself!")
        time.sleep(1)
        return 20

def info():
    print("attack: Deal 15 damage to the enemy.")
    time.sleep(0.5)
    print("defend: Reduce incoming damage.")
    time.sleep(0.5)
    print("heal: Restore health.")
    time.sleep(0.5)

def fight():
    player_health = 100
    enemy_health = 100

    while player_health > 0 and enemy_health > 0:
        print(f"\nYour health: {player_health}")
        print(f"Enemy health: {enemy_health}")
        time.sleep(1)
        action = input("\nActions: \n(1)attack \n(2)defend \n(3)heal \n(4)information \nEnter your number: \n").lower()
        

        if action == "1":
            damage = attack()
            enemy_health -= damage
        elif action == "2":
            damage = defend()
            player_health -= damage
        elif action == "3":
            heal_amount = heal()
            player_health += heal_amount
        elif action == "4":
            info()
            continue
        else:
            print("Invalid action. Please choose again.")
            time.sleep(1)
            continue

        enemy_damage = enemy()
        player_health -= enemy_damage

    if player_health <= 0:
        print("You have been defeated!")
        time.sleep(1)
    else:
        print("You have defeated the enemy!")
        time.sleep(1)

fight()