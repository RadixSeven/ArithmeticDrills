# Overview

Generate html speed drills for practice taking arithmetic tests.

Since arithmetic tests also test speed in writing the answers, it is
best to improve both at once. Thus we need a printed medium. HTML is
easy to generate, so this program outputs HTML.

This generates html containing 2 pages of mixed addition and
subtraction problems. Some day I may expand it, but for now you simply
go to the directory where the code is located and type at the
command-line:

    ./generate_tests.py > my_dest_file.html

Then print it and there will be 160 problems divided into 80 problems
per page.
