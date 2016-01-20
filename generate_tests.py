#!/usr/bin/env python3
import random

add_min = 0
add_max = 10

class Fact:
    def __init__(self, first, operator, second):
        self.first = first
        self.operator = operator
        self.second = second
    def __repr__(self):
        return "Fact({},{},{})".format(repr(self.first),repr(self.operator),
                                       repr(self.second))
    def __str__(self):
        return "{} {} {} =".format(str(self.first), str(self.operator),
                                   str(self.second))


# Generate the facts

facts = set()

for first in range(add_min, add_max+1):
    for second in range(add_min, add_max+1):
        facts.add(Fact(first, "+", second))
        s = first + second
        facts.add(Fact(s,"-",first))
        facts.add(Fact(s,"-",second))


# Shuffle them
facts = list(facts)
random.shuffle(facts)


# Create HTML

# Headers and footers
doc_header=r"""
<html>
<head>
<style>
@media all {
	.page-break	{ display: none; }
}

@media print {
	.page-break	{ display: block; page-break-before: always; }
}

table {
    width: 100%;
}

td {
    font-size: 0.345in;
}

</style>
<body>
"""
doc_footer=r"""
</body>
</html>
"""
table_head="""
<table>
"""
table_foot="""
</table>
<div class="page-break"></div>
"""
last_table_foot="""
</table>
"""
row_head="""<tr>"""
row_foot="""</tr>
"""

# Print tables
print(doc_header)

tables_per_printing = 2
facts_per_row = 4
rows_per_table = 20
facts_per_table = facts_per_row * rows_per_table

num_tables = 0
num_in_current_table = 0
num_in_current_row = 0
for f in facts:
    if num_in_current_table == 0:
        print(table_head)
    if num_in_current_row == 0:
        print(row_head)
    print("<td>{}</td>".format(str(f)))
    num_in_current_table += 1
    num_in_current_row += 1
    if num_in_current_row == facts_per_row:
        print(row_foot)
        num_in_current_row = 0
    if num_in_current_table == facts_per_table:
        num_in_current_table = 0
        num_tables += 1
        if num_tables == tables_per_printing:
            print(last_table_foot)
            break
        else:
            print(table_foot)

if num_in_current_row > 0:
    print(row_foot)
if num_in_current_table > 0:
    print(last_table_foot)

print(doc_footer)
