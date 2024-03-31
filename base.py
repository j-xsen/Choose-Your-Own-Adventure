class Response:
    def __init__(self, _display_text, _destination_node):
        self.display_text = _display_text
        self.destination_node = _destination_node

    def __str__(self):
        return self.display_text


class Node:
    def __init__(self, _print_message, _response_list):
        self.print_message = _print_message
        self.response_list = _response_list

    def display(self):
        print(self.print_message)

    def reply(self, _user_input):
        pass


class StoryNode(Node):
    def __init__(self, _print_message, _destination_node):
        Node.__init__(self, _print_message, None)
        self.destination_node = _destination_node

    def display(self):
        Node.display(self)
        print("[press enter to continue]")

    def reply(self, _user_input=None):
        return self.destination_node


class ChoiceNode(Node):
    def __init__(self, _print_message, _response_list):
        Node.__init__(self, _print_message, _response_list)

    def display(self):
        Node.display(self)
        counter = 0
        while counter < len(self.response_list):
            print(f"{counter}: {self.response_list[counter]}")
            counter += 1

    def reply(self, _user_input):
        return self.response_list[int(_user_input)].destination_node


class DataNode(Node):
    def __init__(self, _print_message, _variable_name, _destination_node):
        Node.__init__(self, _print_message, None)
        self.variable_name = _variable_name
        self.destination_node = _destination_node

    def reply(self, _user_input):
        setattr(new_player, self.variable_name, _user_input)
        return self.destination_node


class Player:
    name = ""
    week = ""

    def __init__(self):
        self.alive = True


new_player = Player()


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


nodes = [
    # 0
    StoryNode("ERROR NODE!!", 1),
    # 1
    StoryNode("You are in heaven", 2),
    # 2
    DataNode("What is your name?", 'name', 3),
    # 3
    DataNode("What week of class is it?", 'week', 4),
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
    ChoiceNode("You walk up to the desk and greet the Professor. She turns to you, asking, \"How are you doing?\"",
               [
                   Response("Horrible", 0),
                   Response("Lost", 0),
                   Response("Great", 0)
               ]),
    # 7
    StoryNode("You explore the halls endlessly, becoming lost in the labyrinth of corridors.",
              8),
    # 8
    StoryNode("You fail all your classes and die.", 1),
    # 9
    ChoiceNode(VariableString("You look to your right and see a classmate staring at you.\n" +
                              "\"Saw you asleep the whole class. Today we learned about %.\"", "week"),
               [
                   Response("Go see the teacher", 6)
               ]
               )
]

current_node = 1

while new_player.alive:
    current_node_object = nodes[current_node]
    current_node_object.display()

    user_response = input()

    current_node = current_node_object.reply(user_response)
