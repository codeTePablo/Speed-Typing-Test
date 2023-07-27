import random


def programming():
    """generate a list with programming words"""
    # list of programming words
    words = [
        "python",
        "java",
        "javascript",
        "c",
        "c++",
        "c#",
        "php",
        "ruby",
        "perl",
        "go",
        "swift",
        "kotlin",
        "r",
        "sql",
        "matlab",
        "typescript",
        "scala",
        "groovy",
        "rust",
        "elixir",
        "haskell",
        "erlang",
        "clojure",
        "dart",
        "julia",
        "fortran",
        "cobol",
        "ada",
        "lisp",
        "prolog",
        "scheme",
        "smalltalk",
        "visual basic",
        "delphi",
        "pascal",
        "lua",
        "abap",
        "actionscript",
    ]
    lenght = len(words)
    # join all the words using a space
    ls = random.choices(words, k=lenght - 3)
    return " ".join(ls)


def space():
    """generate a list with space words"""
    # list of space words
    words = [
        "astronaut",
        "space",
        "spaceship",
        "rocket",
        "planet",
        "star",
        "galaxy",
        "universe",
        "alien",
        "comet",
        "asteroid",
        "milky way",
        "black hole",
        "supernova",
        "nebula",
        "quasar",
        "cosmos",
        "orbit",
        "gravity",
        "atmosphere",
        "astronomy",
        "telescope",
        "observatory",
        "astronomer",
        "cosmonaut",
        "eclipse",
        "meteorite",
        "meteoroid",
        "meteor shower",
        "solar system",
        "space station",
    ]
    lenght = len(words)
    # join all the words using a space
    ls = random.choices(words, k=lenght - 3)
    return " ".join(ls)


def text_python():
    random_text = "Hello World Python Programming is fun to learn and use in real life applications, especially when you are using it to build a real life application."
    return random_text


def random_subject():
    """generate a random subject"""
    # list of subjects
    subjects = [programming(), space(), text_python()]
    # randomly select a subject
    subject = random.choice(subjects)
    new_ls = subject.split()
    #  print(new_ls)
    return new_ls


random_subject()
print(type(random_subject()))
