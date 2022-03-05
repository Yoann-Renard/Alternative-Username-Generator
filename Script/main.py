from importlib.resources import read_text
import os

from matplotlib.style import use
from numpy import outer
from utils.char_list import char_list_wide

def pross(username: str,start: int, output: list) -> list:

    i=start

    for char in username:

        for letters in char_list_wide:
            if char in letters:
                for letter in letters:
                    if char == letter:
                        continue
                    newUN = username.replace(char, letter)
                    if newUN not in output and newUN != username:
                        output.append(newUN)
                        print(newUN)
    if i+1 <= len(username):
        return pross(username.replace(char, letter), i+1, output)
    else:
        return output


if __name__ == "__main__":
    username = input("Enter username: ").strip()

    output_list = pross(username,0 , [])

    print(output_list)
