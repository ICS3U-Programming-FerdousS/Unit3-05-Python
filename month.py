#!/usr/bin/env python3
# Created By: Ferdous Sediqi
# Date: March 29, 2022
# This program asks the user for the month
# number and display the months' name.
# if they enter 0 or higher than 12 display an
# error.

# function for displaying months number
def display_month(month):
    months = {
      1: "{} represent January.". format(month),
      2: "{} represent February.". format(month),
      3: "{} represent March.". format(month),
      4: "{} represent April.". format(month),
      5: "{} represent May.". format(month),
      6: "{} represent June.". format(month),
      7: "{} represent July.". format(month),
      8: "{} represent August.". format(month),
      9: "{} represent September.". format(month),
      10: "{} represent October.". format(month),
      11: "{} represent November.". format(month),
      12: "{} represent Decemebr.". format(month),
      }
    return months.get(month, "Error!. {} is not month number".format(month))


if __name__ == "__main__":
    user_month = int(input("Enter the month number "))
    print(display_month(user_month))
