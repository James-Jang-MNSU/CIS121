"""
2024/11/30
David Hamilton, Owen Dunken, James Jang

This program is a PC version of the popular childrens game hangman.
The python asciimatics package was used to build the UI of the game,
and we used input files to generate random words for each round of hangman.
"""

from asciimatics.widgets import Frame, Layout, Label, Button, ListBox, \
    Text, Divider, VerticalDivider, MultiColumnListBox, PopUpDialog
from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.exceptions import ResizeScreenError, StopApplication
from asciimatics.event import KeyboardEvent, MouseEvent
from asciimatics.widgets.utilities import _get_offset
import sys
from game_engine import GameRound

class StartMenu(Frame):
    """
    This is a class represents the scene of the start menu.
    It inherits the Frame class to set the frame height, width, etc.
    Widgets are created and added to layouts, and multiple layouts are created and added to the frame.  
    The start menu contains the title, a list box to choose a theme, and two buttons -- play and quit.
    """
    def __init__(self, screen):
        super(StartMenu, self).__init__(screen,
                                       height=20,
                                       #screen.height * 2 // 3,
                                       width=80,
                                       #screen.width * 3 // 4,
                                       hover_focus=True,
                                       can_scroll=False,
                                       title="")
        
        # Title text of the start menu. Written in the figlet font
        self._title_text =  (" _    _          _   _  _____ __  __          _   _ \n"
                            " | |  | |   /\\   | \\ | |/ ____|  \\/  |   /\\   | \\ | |\n"
                            " | |__| |  /  \\  |  \\| | |  __| \\  / |  /  \\  |  \\| |\n"
                            " |  __  | / /\\ \\ | . ` | | |_ | |\\/| | / /\\ \\ | . ` |\n"
                            " | |  | |/ ____ \\| |\\  | |__| | |  | |/ ____ \\| |\\  |\n"
                            " |_|  |_/_/    \\_\\_| \\_|\\_____|_|  |_/_/    \\_\\_| \\_|\n\n")
        
        #layout1 - start menu title
        layout1 = Layout([100])
        self.add_layout(layout1)
        layout1.add_widget(Label("", height=1))
        self._title_section = Label(self._title_text, height=8, align="^")
        layout1.add_widget(self._title_section)
        
        #layout2 - list box for selecting theme of hangman
        layout2 = Layout([3, 14, 3])
        self.add_layout(layout2)
        layout2.add_widget(Divider(), 1)
        self._theme_select_list = ListBox(
            4,
            [
                (" Cities", "cities"), 
                (" Colors", "colors"), 
                (" Fruit", "fruit"), 
                (" Sports teams", "teams")
            ],
            label="Choose your theme: ",
            name="game theme",
            add_scroll_bar=True,
            on_select=self._set_theme
            )
        layout2.add_widget(self._theme_select_list, 1)
        layout2.add_widget(Divider(), 1)

        #layout3 - empty label for spacing between the list box and buttons 
        layout3 = Layout([100])
        self.add_layout(layout3)
        layout3.add_widget(Label('', height=1, align="^"))

        #layout4 - buttons start and quit
        layout4 = Layout([1, 1, 1, 1])
        self.add_layout(layout4)
        layout4.add_widget(Button('Start', self._play), 1)
        layout4.add_widget(Button('Quit', self._quit), 2)

        #fix position of widgets
        self.fix()

    def _set_theme(self):
        """
        A function that is called when an option is selected in the list box.
        Saves the data of the list box widget so it can be used when initiating a new round of hangman. 
        """
        self.save()

    def _play(self):
        """
        A function that is called when the user clicks the play button.
        Calls the load_round function to render the next scene of a current/new round.
        """
        self.save()
        print('Play')
        theme = self.data["game theme"]
        print(f"Theme: {theme}")
        game_obj = GameRound(theme)
        load_round(create_game_screen(game_obj))

    @staticmethod
    def _quit():
        """
        A function that is called when the user clicks the quit button.
        Stops the asciimatics application. 
        """
        print("Quit")
        raise StopApplication("User pressed quit")
    
class GameScreen(Frame):
    """
    This is a class represents the scene of a screen during game play.
    Like the start menu, it inherits the Frame class to set the frame height, width, etc.
    the class 
    """
    def __init__(self, screen, game_obj):
        super(GameScreen, self).__init__(screen,
                                       height=20,
                                       #screen.height * 2 // 3,
                                       width=80,
                                       #screen.width * 3 // 4,                                    
                                       hover_focus=True,
                                       can_scroll=False,
                                       title="")
        self._game_obj = game_obj
        self.hangman_drawing = self._game_obj.get_hangman_drawing()       
        self._word_current_round = self._game_obj.get_user_word()

        #layout0 - label for selected theme of round
        layout0 = Layout([100])
        self.add_layout(layout0)
        layout0.add_widget(Label(f"Theme: {self._game_obj._theme.title()}", height=1, align="^"))
        layout0.add_widget(Divider())

        #layout1 - left: visual of available alphabets, right: canvas for hangman drawing
        layout1 = Layout([9, 22, 10, 2, 10, 20, 27])
        self.add_layout(layout1)
        self._available_alphas = MultiColumnListBox(
            height=5,
            columns=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            options=[
                ([], -1),
                ([], 0),
                (self._game_obj._alphabet_list[:10], 1), 
                (self._game_obj._alphabet_list[10:20], 2), 
                (self._game_obj._alphabet_list[20:], 3), 
                ],
            titles=[],
            name="available alphas",
            space_delimiter='  ')
        layout1.add_widget(self._available_alphas, 1)
        self._available_alphas.disabled=True
        layout1.add_widget(VerticalDivider(), 3)
        self._hangman_canvas = Label(self.hangman_drawing, height=8, align="<")
        layout1.add_widget(self._hangman_canvas, 5)
        self._game_word = MultiColumnListBox(
            height=5,
            columns=[1 for i in range(len(self._word_current_round))],
            options=[
                ([], -2),
                ([], -1),
                ([], 0),
                ([letter for letter in self._word_current_round], 1)
                ],
            titles=[],
            name="game word")
        self._game_word.disabled=True
        layout1.add_widget(self._game_word, 6)

        #layout2 - divider
        layout2 = Layout([100])
        self.add_layout(layout2)
        layout2.add_widget(Divider())

        #layout3 - left: text line for user guesses, right: empty
        layout3 = Layout([38, 62])
        self.add_layout(layout3)
        self._guess_line = Text("Guess:", "guess")
        layout3.add_widget(self._guess_line, 0)

        #layout4 - spacing
        layout4 = Layout([100])
        self.add_layout(layout4)
        self._spacing_line = Divider(line_char=" ")
        layout4.add_widget(self._spacing_line)
        layout4.add_widget(self._spacing_line)
        layout4.add_widget(self._spacing_line)

        #layout5 - left: buttons for new_round and exit to menu, right:
        layout5 = Layout([1, 1, 1, 1, 1])
        self.add_layout(layout5)
        layout5.add_widget(Button("New Game", self._new_game), 3)
        layout5.add_widget(Button("Back To Menu", self._exit), 4)

        self.fix()

    def __str__(self):
        return f"Round \"{self._game_obj._word}\" -- miss {str(self._game_obj._num_of_misses)}"

    def _new_game(self):
        game_obj = GameRound(current_round._game_obj._theme)
        load_round(create_game_screen(game_obj))

    def _exit(self):
        load_start_menu(start_menu)

def new_game(optional_arg = 0):
    game_obj = GameRound(current_round._game_obj._theme)
    load_round(create_game_screen(game_obj))
    
def read_guess():
    current_round.save()
    user_guess = current_round.data["guess"]
    result = current_round._game_obj.take_guess(user_guess)
    if result == "WIN":
        current_round._scene.add_effect(PopUpDialog(current_round._screen, "You Win", ["OK"], on_close=new_game))
    elif result == "GAME OVER":
        current_round._scene.add_effect(PopUpDialog(current_round._screen, "You Lose", ["OK"], on_close=new_game))
    else:
        load_round(create_game_screen(current_round._game_obj))

#override the Text.process_event module to make it react to the "Enter-key" keyboardEvent
def process_event_text(self, event):
        if isinstance(event, KeyboardEvent):
            if event.key_code == Screen.KEY_BACK and not self._readonly:
                if self._column > 0:
                    # Delete character in front of cursor.
                    self._set_and_check_value("".join([self._value[:self._column - 1],
                                                       self._value[self._column:]]))
                    self._column -= 1
            elif event.key_code == Screen.KEY_DELETE and not self._readonly:
                if self._column < len(self._value):
                    self._set_and_check_value("".join([self._value[:self._column],
                                                       self._value[self._column + 1:]]))
            elif event.key_code == Screen.KEY_LEFT:
                self._column -= 1
                self._column = max(self._column, 0)
            elif event.key_code == Screen.KEY_RIGHT:
                self._column += 1
                self._column = min(len(self._value), self._column)
            elif event.key_code == Screen.KEY_HOME:
                self._column = 0
            elif event.key_code == Screen.KEY_END:
                self._column = len(self._value)
            elif event.key_code >= 32 and not self._readonly:
                # Enforce required max length - swallow event if not allowed
                if self._max_length is None or len(self._value) < self._max_length:
                    # Insert any visible text at the current cursor position.
                    self._set_and_check_value(chr(event.key_code).join([self._value[:self._column],
                                                                        self._value[self._column:]]))
                    self._column += 1
            elif event.key_code == 13:
                read_guess()
                return None
            else:
                # Ignore any other key press.
                return event
        elif isinstance(event, MouseEvent):
            # Mouse event - rebase coordinates to Frame context.
            if event.buttons != 0:
                if self.is_mouse_over(event, include_label=False):
                    self._column = (self._start_column +
                                    _get_offset(self._value[self._start_column:],
                                                event.x - self._x - self._offset,
                                                self._frame.canvas.unicode_aware))
                    self._column = min(len(self._value), self._column)
                    self._column = max(0, self._column)
                    return None
            # Ignore other mouse events.
            return event
        else:
            # Ignore other events
            return event

        # If we got here, we processed the event - swallow it.
        return None 
Text.process_event = process_event_text

def join_alpha_list(alpha_list):
    for index, line in enumerate(alpha_list):
        alpha_list[index] = ' '.join(line)
    return '\n'.join(alpha_list)

def start_menu(screen, scene):
    """
    This is a function for the start menu.
    The variable scenes is a list containing a Scene instance for the start menu.
    The funciton load_start_menu below will take this function as an argument to render the start menu.
    """
    scenes = [
        Scene([StartMenu(screen)], -1, name="start menu")
    ]
    screen.play(scenes, stop_on_resize=True, start_scene=scene, allow_int=True)

def create_game_screen(game_obj):
    """
    This function takes the current game's game_obj for as the argument.
    It returns a function that will be passed into the load_round function below.
    A game_obj is an instance of the GameRound class which holds the data for the current round of hangman. (see definition of GameRound)
    """
    def game_screen(screen, scene):
        global current_round
        current_round = GameScreen(screen, game_obj)
        print(current_round)
        scenes = [
            Scene([current_round], -1, name="game screen")
        ]
        screen.play(scenes, stop_on_resize=True, start_scene=scene, allow_int=True)
    return game_screen

def load_start_menu(scene):     
    """A function that takes the start_menu function as an argument to render the start menu on the screen"""   
    last_scene = None
    while True:
        try:
            Screen.wrapper(scene, catch_interrupt=True, arguments=[last_scene])
            sys.exit(0)
        except ResizeScreenError as e:
            last_scene = e.scene

def load_round(scene):
    """Loads the (next) game screen for a round of hangman"""        
    last_scene = None
    while True:
        try:
            Screen.wrapper(scene, catch_interrupt=True, arguments=[last_scene])
            sys.exit(0)
        except ResizeScreenError as e:
            last_scene = e.scene

# create a global variable that will save 
current_round = None

if __name__ == '__main__':
    # load the start menu
    load_start_menu(start_menu)
