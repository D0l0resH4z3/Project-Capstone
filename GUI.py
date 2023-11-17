import Password_Generator
import string
#import hypercli
from hypercli import hypercli

# create an instance of hypercli
cli = hypercli()

# configure the instance
cli.config["banner_text"] = "CyberSuite Tools"
cli.config["intro_title"] = "Intro"
cli.config["intro_content"] = "The Ultimate tools for your needs!"
cli.config["show_menu_table_header"] = True

# add navigation options to the menu
#cli.link("Main Menu", "String Encoder/Decoder")
#cli.link("Main Menu", "String Menu")
@cli.entry(menu="Main Menu", option="Password Generator")
def passgenexec():
# main_script.py
    with open("Password_Generator.py", "r") as file:
        script_contents = file.read()
    #debugging - remove
    print("Script contents:")
    print(script_contents)
    exec(script_contents, globals(), locals())


@cli.entry(menu="Main Menu", option="String Encoder/Decoder")
def stringexec():
    with open("encoderdecoder.py", "r") as file:
        script_contents2 = file.read()
    #debugging
    #print("Script contents2:")
    #print(script_contents2)

@cli.entry(menu="Main Menu", option="Image Metadata Remover")
def execs3():
    with open("metedata_removal.py", "r") as file:
        script_contents3 = file.read()

@cli.entry(menu="Main Menu", option="Key Logger")
def execs4():
    with open("keylogger.py", "r") as file:
        script_contents4 = file.read()

@cli.entry(menu="Main Menu", option="Port Scanner")
def execs5():
    with open("port_scanner.py", "r") as file:
        script_contents5 = file.read

@cli.entry(menu="Main Menu", option="Web Scraper")
def execs6():
    with open("Web_scraper.py", "r") as file:
        script_contents6 = file.read

@cli.entry(menu="Main Menu", option="Anti-Virus Scan")
def execs7():
    with open("virus_scan", "r") as file:
        script_contents7 = file.read
#This is testing methods of executing other scripts in a .py file.
#@cli.entry(menu="String Encoder/Decoder", option="Decode String")
#def sub(num1=1, num2=1):
    #a = int(input(f"Enter first number (default {num1}): ") or num1)
    #b = int(input(f"Enter second number (default {num2}): ") or num2)
    #print(f"{a} - {b} = {a - b}")


#@cli.entry(menu="String Menu", option="Reverse a string")
#def reverse():
    #string = input("Enter a string: ")
    #print(string[::-1])


#@cli.entry(menu="String Menu", option="Show length of a string")
#def str_length():
    #string = input("Enter a string: ")
    #print(f"Length of string is {len(string)}")


# run the cli
cli.run()