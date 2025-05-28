
def main():
    names = ['nakib', 'mario', 'luna']

#    for i in names:
#       print(letter("tahfim", i))

    greet = " ".join(names)
    print(greet)


def letter(sender, reciever):
    return f"""
    +~~~~~~~~~~~~~~====~~~~~~~~~~~~~~~~~~+

    Hello {reciever},
    welcome to the party

                            from
                            {sender}
    +~~~~~~~~~~~~~~====~~~~~~~~~~~~~~~~~~+
    """



main()
