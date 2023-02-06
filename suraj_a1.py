"""
Module for currency exchange

This module provides several string parsing functions to
implement a
simple currency exchange routine using an online currency
service.
The primary function in this module is exchange.

Author: SURAJ PRAJAPATI
Date: 30 DEC 2022
"""

def before_space(s):
	"""
	Returns a copy of s up to, but not including,the first space
	
	examples:

	>>> before_space('2.34 USD')
	'2.34'
	>>> before_space('2.34  usd')
	'2.34'
	>>> before_space('4.45 doller ')
	'4.45'
	>>> before_space(' 4.45 doller')
	''


	Parameter s: the string to slice
	Precondition: s is a string with at least one space
	"""
	str_first=s.find(' ')
	first=s[:str_first]
	return first

def after_space(s):
	"""
	Returns a copy of s after the first space

	examples:

	>>> after_space('4 doller')
	'doller'
	>>> after_space('4 doller ')
	'doller'
	>>> after_space('4   doller')
	'doller'
	>>> after_space(' 4 doller')
	'4 doller'
	


	Parameter s: the string to slice
	Precondition: s is a string with at least one space
	"""	
	str_last=s.find(' ')
	last=s[str_last+1:].strip()
	return last


def first_inside_quotes(s):
	"""
	Returns the first substring of s between two (double) quotes

	A quote character is one that is inside a string, not one that
	delimits it. We typically use single quotes (') to delimit a
	string if we want to use a double quote character (") inside of
	it.
	Examples:
	first_inside_quotes('A "B C" D') returns 'B C'
	first_inside_quotes('A "B C" D "E F" G') returns 'B C',
	because it only picks the first such substring

	>>> first_inside_quotes('hello "geek" for shows')
	'geek'
	>>> first_inside_quotes('hello " brother" ')
	' brother'
	>>> first_inside_quotes('hello "brotheer" for "help"')
	'brotheer'
	>>> first_inside_quotes('"hii" brother')
	'hii'

	Parameter s: a string to search

	Precondition: s is a string containing at least two double quotes
	"""
	x=s.find('"')
	# print(x)
	y=s[x+1:]
	# print(y)
	z=y.find('"')
	# print(z)
	w=y[:z]
	# print(w)
	return w



def get_lhs(json):
	'''
	Returns the lhs value in the response to a currency query

	Given a JSONresponse to a currency query, this returns the
	string inside double quotes (") immediately following the keyword

	"lhs". For example, if the JSON is '{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'
	 then this function returns '1 Bitcoin' (not '"1 Bitcoin"'). This function returns the empty string 
	 if the JSON response contains an error message.

	>>> get_lhs('{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }')
	'1 Bitcoin'
	>>> get_lhs('{ "lhs" : "", "rhs" : "", "err" : "Currency amount is invalid." }')
	''

	 Parameter json: a json string to parse 
	 Precondition: json is the response to a currency query
	 '''
	lhs=json[11:]
	# print(lhs)
	lhs_cut=lhs.find('"')
	# print(lhs_cut)
	get_lhs=lhs[:lhs_cut]
	#print(return_lhs)
	return get_lhs




def get_rhs(json):
	"""
	Returns the rhs value in the response to a currency query

	 Given a JSON response to a currency query, this returns the
	"rhs". For example, if the JSON is

	'{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'
	then this function returns '19995.85429186 Euros' (not '"38781.518240835 Euros"').

	examples:
	>>> get_rhs('{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }')
	'19995.85429186 Euros'
	>>> get_rhs('{ "lhs" : "", "rhs" : "", "err" : "Currency amount is invalid." }')
	''

	This function returns the empty string if the JSON response contains an error message.
	Parameter json: a json string to parse Precondition: json is the response to a currency query
	"""
	cut1=json.find(',')
	# print(cut1)
	cut2=json[cut1+11:]
	# print(cut2)
	cut3=cut2.find('"')
	# print(cut3)
	get_rhs=cut2[:cut3]
	# print(return_rhs)

	return get_rhs



def has_error(json):
	"""
	Returns True if the query has an error; False otherwise.

	Given a JSON response to a currency query, this returns True if there
	is an error message. For example, if the JSON is 
	'{ "lhs" : "", "rhs" : "", "err" : "Currency amount is invalid." }'
	then the query is not valid, so this function returns True (It does NOT return the message 'Currency amount is invalid.').

	examples:
	>>> has_error('{ "lhs" : "", "rhs" : "", "err" : "Currency amount is invalid." }')
	True
	>>> has_error('{ "lhs" : "", "rhs" : "", "err" : "Exchange currency code is invalid." }')
	True
	>>> has_error('{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }')
	False
	
	Parameter json: a json string to parse
	Precondition: json is the response to a currency query
	"""
	return get_lhs(json)==''

	
def query_website(old, new, amt):
	"""
	Returns the amount of currency received in the given
	exchange. In this exchange, the user is changing amt money in
	currency old to the currency new. The value returned represents
	the amount in currency new

	>>> query_website('USD','CUP',2.5)
	'{ "lhs" : "2.5 United States Dollars", "rhs" : "64.375 Cuban Pesos", "err" : "" }'
	>>> query_website('USD','INR',2.5)
	'{ "lhs" : "2.5 United States Dollars", "rhs" : "199.4700325 Indian Rupees", "err" : "" }'
	>>> query_website('USD','ABC',4.5)
	'{ "lhs" : "", "rhs" : "", "err" : "Exchange currency code is invalid." }'
	>>> query_website('US','ABC',4.5)
	'{ "lhs" : "", "rhs" : "", "err" : "Source currency code is invalid." }'
	>>> query_website('SSS','USD',4.5)
	'{ "lhs" : "", "rhs" : "", "err" : "Source currency code is invalid." }'


	The value returned has type float.

	Parameter old: the currency on hand
	Precondition: old is a string for a valid currency code

	Parameter new: the currency to convert to
	Precondition: new is a string for a valid currency code

	Parameter amt: amount of currency to convert
	Precondition: amt is a float
	"""
	import requests
	json=(requests.get('http://cs1110.cs.cornell.edu/2022fa/a1?old={0}&new={1}&amt={2}'.format(old,new,amt))).text
	return json


def	is_currency(code):
	"""
	Returns: True if code is a valid (3 letter code for a) currency It returns False otherwise.

	>>> is_currency('USD')
	True
	>>> is_currency('CUP')
	True
	>>> is_currency('ZEE')
	False

	Parameter code: the currency code to verify 
	Precondition: code is a string with no spaces or non-letters.
	"""
	return has_error(query_website(code,'INR',2.5))==False

def exchange(old, new, amt):
	"""
	Returns the amount of currency received in the given exchange

	In this exchange, the user is changing amt money in
	currency old to the currency new. The value returned represents the amount in currency new.
	The value returned has type float.


	Parameter old: the currency on hand
	Precondition: old is a string for a valid currency code Parameter new: the currency to convert to
	Precondition: new is a string for a valid currency code Parameter amt: amount of currency to convert Precondition: amt is a float
	"""
	json=query_website(old,new,amt)
	exchange_amount=get_rhs(json)
	return before_space(exchange_amount)
	
if __name__=='__main__':
	import doctest
	doctest.testmod()