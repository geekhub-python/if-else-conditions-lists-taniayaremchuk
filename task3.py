#!/usr/bin/env python3

print("Ввод")
first_number = int(input())
second_number = int(input())
third_number = int(input())
if first_number == second_number == third_number:
	print("3")
elif first_number == second_number or first_number == third_number or second_number == third_number:
	print("2")
else:
	print("0")


