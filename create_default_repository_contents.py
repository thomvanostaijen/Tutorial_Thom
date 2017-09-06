"""
Author: Floris Kroon
Date: 2016-12-23
Description: Python file to create default directories and files for git
repositories. Make sure that the default .gitignore and .gitattributes have
been copied with this file.

Run:
$ python create_default_repository_contents.py

"""

from os import mkdir
from os.path import exists


def create_default_repository_contents():
    print("Creating default directories and files...")

    if exists(".gitignore") and exists(".gitattributes"):
        f = open(".gitignore")
        for line in f:
            # [:-1] to get rid of the newline at the end of the line.
            if line[:-1] != "## MICOMPANY GIT TUTORIAL EXAMPLE .gitignore":
                print("Make sure that you copied the .gitignore and "
                      ".gitattributes files " + "from the example repository!")
                return
            break
        f.close()

        f = open(".gitattributes")
        for line in f:
            if line[:-1] != "## MICOMPANY GIT TUTORIAL EXAMPLE .gitattributes":
                print("Make sure that you copied the .gitignore and "
                      ".gitattributes files " + "from the example repository!")
                return
            break
        f.close()

    else:
        print("Make sure that you copied the .gitignore and .gitattributes "
              "files from the example repository!")
        return

    # Use a try-except block for all attempts to create files/directories, as
    # they may already exist.
    try:
        f = open("requirements.txt", 'w')
        f.close()
    except:
        pass

    try:
        f = open("README.md", 'w')
        f.write(readme)
        f.close()
    except:
        pass

    try:
        f = open("setup.cmd", 'w')
        f.close()
    except:
        pass

    try:
        mkdir("Apps")
    except:
        pass

    try:
        mkdir("Databases")
    except:
        pass

    try:
        mkdir("Integration")
    except:
        pass

    try:
        mkdir("Reports")
    except:
        pass

    try:
        mkdir("Scripts")
    except:
        pass

    print("Done!")
    print("Add additional directories that you need, and make sure to " +
          "change the default files to suit your project.")


create_default_repository_contents()
