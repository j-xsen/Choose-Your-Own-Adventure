import enum
import the_hunger_games


class Player:
    name = ""
    week = ""

    def __init__(self):
        self.alive = True


new_player = Player()


class Response:
    """
    The choices presented to players

    _display_text = What will be shown in the terminal
    _destination_node = What Node should the code jump to if chosen
    """
    def __init__(self, _display_text, _destination_node):
        self.display_text = _display_text
        self.destination_node = _destination_node

    def __str__(self):
        return self.display_text


class Node:
    """
    The base class for Nodes

    _print_message = The message to be displayed in the terminal
    _response_list = Response objects available for this Node
    """
    def __init__(self, _print_message, _response_list):
        self.print_message = _print_message
        self.response_list = _response_list

    def display(self):
        print(self.print_message)

    def reply(self, _user_input):
        pass


class StoryNode(Node):
    """
    Node that will display a single message then prompt the user to press enter to continue

    _print_message = Message displayed in terminal
    _destination_node = Subsequent Node
    """
    def __init__(self, _print_message, _destination_node):
        Node.__init__(self, _print_message, None)
        self.destination_node = _destination_node

    def display(self):
        Node.display(self)
        print("[press enter to continue]")

    def reply(self, _user_input=None):
        return self.destination_node


class ChoiceNode(Node):
    """
    Node that will present that user with a choice

    _print_message = Message displayed in terminal
    _response_list = List of Responses that the player can select from
    """
    def __init__(self, _print_message, _response_list):
        Node.__init__(self, _print_message, _response_list)

    def display(self):
        Node.display(self)
        counter = 0
        while counter < len(self.response_list):
            print(f"{counter}: {self.response_list[counter]}")
            counter += 1

    def reply(self, _user_input):
        if _user_input.isnumeric() and len(self.response_list) > int(_user_input):
            dest = self.response_list[int(_user_input)].destination_node
            if dest == -1:
                the_hunger_games.run()
                exit(1)
            return dest
        return False


class DeathNode(Node):
    """
    Node that ends game

    _print_message = Message to display in terminal
    _player = Player object to kill
    """
    def __init__(self, _print_message):
        Node.__init__(self, _print_message, None)

    def display(self):
        Node.display(self)
        print("[press enter to end]")

    def reply(self, _user_input=None):
        new_player.alive = False


class TestNode(Node):
    """
    Node that checks if the answer is correct

    _print_message = Message to display in terminal
    _expected = Expected response
    """
    def __init__(self, _print_message, _expected, _success, _fail):
        Node.__init__(self, _print_message, None)
        self.expected = _expected
        self.success = _success
        self.fail = _fail

    def reply(self, _user_input):
        if _user_input == weeks[int(getattr(new_player, self.expected))-1]:
            return self.success
        return self.fail


class VerifyMethod(enum.Enum):
    NONEMPTY = 0,
    INTEGER = 1,
    VALID_WEEK = 2,


class DataNode(Node):
    """
    Node that will take and store a variable from the player

    _print_message = The message displayed in the terminal
    _variable_name = What the variable name will be stored as in the Player object
    _destination_node = What Node to go to after this one
    _method = VerifyMethod to use when verifying an input
    """
    def __init__(self, _print_message, _variable_name, _destination_node, _method):
        Node.__init__(self, _print_message, None)
        self.variable_name = _variable_name
        self.destination_node = _destination_node
        self.method = _method

    def reply(self, _user_input):
        if self.verify_input(_user_input):
            setattr(new_player, self.variable_name, _user_input)
        else:
            return False
        return self.destination_node

    def verify_input(self, _user_input):
        if self.method == VerifyMethod.NONEMPTY:
            if _user_input != "":
                return True
            print("Invalid input; Please enter a value.")
        elif self.method == VerifyMethod.INTEGER:
            if _user_input.isnumeric():
                return True
            print("Invalid input; Please enter an integer.")
        elif self.method == VerifyMethod.VALID_WEEK:
            if _user_input.isnumeric() and 1 <= int(_user_input) <= 14:
                return True
            print("Invalid input; Please enter a number 1 - 14.")
        return False


class VariableString:
    """
    Replaces a symbol in a string with a variable from the Player object

    _string = string to store, with a % placed where you want the variable placed
    _variable_name = Name of the variable within the Player object to be put into the text
    """
    def __init__(self, _string, _variable_name):
        self.string = _string
        self.variable_name = _variable_name

    def __str__(self):
        if self.variable_name == "week":
            return self.string.replace("%", weeks[int(getattr(new_player, "week"))-1])
        return self.string.replace("%", getattr(new_player, self.variable_name))


weeks = [
    "Pycharm and Error Handling",
    "Data Types",
    "Conditions and Loops",
    "Sets/Tuple",
    "1D and 2D Arrays/Lists and Functions",
    "Midterm",
    "Dictionaries",
    "Files",
    "Files",
    "Classes, Structures, and Inheritance",
    "Recursion",
    "Recursion, Pip/Modules, and Pandas",
    "Matplotlib and PyGame",
    "Final Project due"
]


# list of all Nodes
nodes = [
    # 0
    DeathNode("ERROR NODE!!"),
    # 1
    StoryNode("You are in heaven", 2),
    # 2
    DataNode("What is your name?", 'name', 3,
             VerifyMethod.NONEMPTY),
    # 3
    DataNode("What week of class is it?", 'week', 4,
             VerifyMethod.VALID_WEEK),
    # 4
    StoryNode("You wake up at the end of class.", 5),
    # 5
    ChoiceNode(VariableString("\"Thanks for coming to class today!\" the Professor announces to the class " +
                              "before turning to you.\n\"%, please come see me in my office.\"", 'name'),
               [
                   Response("Leave the room", 7),
                   Response("Go see teacher", 6),
                   Response("Talk to classmate", 9)
               ]),
    # 6
    ChoiceNode("You walk up to the desk and greet the Professor. She turns to you, asking,"
               " \"How are you doing?\"",
               [
                   Response("Horrible", 10),
                   Response("Lost", 14),
                   Response("Great", 20)
               ]),
    # 7
    StoryNode("You explore the halls endlessly, becoming lost in the labyrinth of corridors.",
              8),
    # 8
    DeathNode("You fail all your classes and die."),
    # 9
    ChoiceNode(VariableString("You look to your right and see a classmate staring at you.\n" +
                              "\"Saw you asleep the whole class. Today we learned about %.\"", "week"),
               [
                   Response("Go see the teacher", 6)
               ]
               ),
    # 10
    ChoiceNode("\"Is there anything I can do to help?\" she asks.",
               [
                   Response("Yes", 12),
                   Response("No", 11)
               ]),
    # 11
    StoryNode("\"I need to make sure you are understanding the topics we are covering in class.\"",
              24),
    # 12
    StoryNode("She calls the police and you are swiftly arrested.", 13),
    # 13
    DeathNode("You die in prison."),
    # 14
    ChoiceNode("\"You're... lost? Do you need to leave?\"",
               [
                   Response("Yes", 19),
                   Response("No", 10),
                   Response("Do you hear that?", 15),
               ]),
    # 15
    StoryNode("You are abducted by aliens.", 16),
    # 16
    StoryNode("They look exactly as they are depicted in popular media from your childhood."
              " You giggle at them.", 17),
    # 17
    StoryNode("They murmur in response and your vision goes black.", 18),
    # 18
    DeathNode("You never wake up."),
    # 19
    StoryNode("You leave the classroom.", 7),
    # 20
    ChoiceNode("She looks confused. \"I could not help but notice you were asleep the whole class.\"",
               [
                   Response("Say nothing", 11),
                   Response("I stayed up late playing video games", 21)
               ]),
    # 21
    StoryNode("The Professor looks at you, confused.", 22),
    # 22
    StoryNode("You see a shift in her eyebrows only seen in people seething with rage.", 23),
    # 23
    StoryNode("In a calm, but tense, voice she states,"
              " \"I think it's best if you leave my classroom now.\"", 19),
    # 24
    TestNode("\"What did we talk about today?\" she asks.", 'week', 26, 25),
    # 25
    StoryNode("She rolls her eyes.", 28),
    # 26
    StoryNode("Before the words even escape your mouth,"
              " your Professor has jumped to her feet with a shriek of positivity.", 27),
    # 27
    DeathNode("You are raptured."),
    # 28
    StoryNode("\"You are... Obviously not paying attention. Please see yourself out.\"", 19),
    # 29
    ChoiceNode("Choose your narrative:", [
        Response("The Hunger Games", -1),
        Response("Classroom", 1)
    ]),
]

current_node = 29

while new_player.alive:
    current_node_object = nodes[current_node]
    current_node_object.display()

    user_response = input()

    next_node = current_node_object.reply(user_response)
    if next_node is not False:
        current_node = current_node_object.reply(user_response)
exit(1)
