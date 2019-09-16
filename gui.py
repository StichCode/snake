import thorpy

from snake import main

application = thorpy.Application(size=(500, 500), caption='ThorPy stupid Example')
thorpy.theme.set_theme('classic')

start_single = thorpy.make_button("Single game", func=main)
create_host = thorpy.make_button("Create server")
connect = thorpy.make_button("Connect to game")
settings = thorpy.make_button("Settings")
quit_button = thorpy.make_button("Quit")
quit_button.set_as_exiter()

central_box = thorpy.Box.make([start_single, create_host, connect, settings, quit_button])
central_box.set_main_color((200, 200, 200, 120))
central_box.center()

# background = thorpy.Background(elements=[central_box])

menu = thorpy.Menu(elements=central_box, fps=45)
menu.play()

application.quit()


