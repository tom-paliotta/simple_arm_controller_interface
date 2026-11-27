import time
import pygame

# 1. Start pygame and look for controllers
pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No controller detected! Plug it in and run again.")
else:
    # Grab the first controller plugged in
    controller = pygame.joystick.Joystick(0)
    controller.init()
    print(f"Connected to: {controller.get_name()}")
    print("Move the sticks and pull the triggers (Press Ctrl+C to stop)...\n")

    try:
        while True:
            # Refresh controller state
            pygame.event.pump()

            # Read all joysticks/triggers (axes) and buttons
            axes = [
                round(controller.get_axis(i), 2)
                for i in range(controller.get_numaxes())
            ]
            buttons = [
                controller.get_button(i)
                for i in range(controller.get_numbuttons())
            ]

            print(f"Axes: {axes} | Buttons: {buttons}")
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        pygame.quit()
