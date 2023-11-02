#!/usr/bin/env python3
"""
Main file
"""

filter_datum = __import__('filtered_logger').filter_datum

fields = ["password", "date_of_birth"]
messages = ["name=egg;email=eggmin@gmail.com;password=eggcellent;date_of_birth=03/11/1988;", "name=bob;email=bobyahoo.com;password=bobbycool;date_of_birth=083/064/19903;"]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))
