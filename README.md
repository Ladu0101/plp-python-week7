# Assignment: Shopping List Manager

This assignment practices Python lists, list operations, loops, conditions, and user interaction.

## Files

- `list_warmup.py` — # List Warmup

`list_warmup.py` is a simple Python program that practices creating a list, accessing items using indexes, adding and removing fruits, and counting list items using `len()`.
- 
`shopping_list.py` — A menu-based shopping list program that allows the user to add, remove, show, and finish shopping items.


`list_report.py` practices looping through a list, numbering items, counting items with more than four letters, and finding the longest item using a loop comparison.
- `screenshots/` — Contains screenshots showing each Python program running successfully.
- `README.md` — Provides information about the assignment, its files, and why checking `in` before `.remove()` is safer.

## Why check `in` before calling `.remove()`?

It is safer to check `in` before calling `.remove()` because `.remove()` causes an error if the item does not exist in the list. Checking first allows the program to handle the situation safely and display a helpful message instead of stopping with an error.
