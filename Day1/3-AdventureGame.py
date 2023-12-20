print("Welcome to a choose your own adventure game.")
road_choice = input("You are at a crossroad. Which way to do want to go. Type 'left' or 'right' ")

if road_choice == "right":
    swim_or_wait = input("You are at a lake where you see an island in the middle do you wait for a boat or start swimming towards it. Type 'swim' or 'wait' ")
    if swim_or_wait == "swim":
        print("You get eaten by sharks. Game over.")
    else:
        door_color = input("You reach the island and see a big house with three door: red, blue and green. Which door do you choose. Type 'red', 'blue' or 'green' ")
        if door_color == "red":
            print("You get eaten by the lion inside the room. Game over.")
        elif door_color == "blue":
            print("Wow. You found some treasure. Nice!")
        else:
            print("You get killed by the chemicals inside the room. Game over")
else:
    print("The roads leads you to quicksand where you get trapped and die. Game over")