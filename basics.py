# --------------------------------------------------------------------------- #
# IMMUTABLE DATATYPES ------------------------------------------------------- #
# --------------------------------------------------------------------------- #

string_type = 'blue' 
int_type = 22
bool_type = True
tuple_type = ('this', 'that')
bytes_type = b'vampires'
# See: realpython.com/python-mutable-vs-immutable-types/#immutable-built-in-data-types-in-python


# --------------------------------------------------------------------------- #
# MUTABLE DATATYPES --------------------------------------------------------- #
# --------------------------------------------------------------------------- #

list_type = ['this', 'that']
set_type = {'this', 'that'} # 👈 set items are immutable, tho
dict_type = { # 👈 reliably ordered since Python 3.6
  'key': 'value',
  'other_key': ['more', 'stuff'],
}


# --------------------------------------------------------------------------- #
# TYPE-CHECKING ------------------------------------------------------------- #
# --------------------------------------------------------------------------- #

print('type(None) evaluates to:', type(None))
print('type(22) evaluates to:', type(22))
print('type([1, 2, 3]) evaluates to:', type([1, 2, 3]))

# --------------------------------------------------------------------------- #
# FALSY VALUES -------------------------------------------------------------- #
# --------------------------------------------------------------------------- #

[]       # empty list
()       # empty tuple
{}       # empty dict
set()    # empty set
''       # empty string
range(0) # empty range
0        # 0 as integer
0.0      # 0 as float
0j       # 0 as complex
None     
False


# --------------------------------------------------------------------------- #
# .sort vs .sorted  --------------------------------------------------------- #
# --------------------------------------------------------------------------- #

numbers = [5, 2, 8, 1]
print('sorted(numbers) evaluates to:', sorted(numbers))
print('numbers evaluates to:', numbers)
print('numbers.sort() evaluates to:', numbers.sort())
print('numbers now evaluates to:', numbers)

# Built-in methods that mutate shall not return 'self':
# https://mail.python.org/pipermail/python-dev/2003-October/038855.html


# --------------------------------------------------------------------------- #
# LIST COMPREHENSIONS ------------------------------------------------------- #
# --------------------------------------------------------------------------- #

some_bikes = [
  {
    'brand': 'Gitane',
    'model': 'Tour de France',
    'color': 'French Racing Blue',
  },
  {
    'brand': 'Surly',
    'model': 'Steamroller',
    'color': 'Banana Candy Yellow',
  },
  {
    'brand': 'Kombi',
    'model': 'Lux',
    'color': 'Norwegian Blue',
  },
  {
    'brand': 'Surly',
    'model': 'Cross Check',
    'color': 'Dream Tangerine'
  }
]

# Can be used like .map:
bike_colors = [bike['color'] for bike in some_bikes]
print('bike_colors evaluates to:', bike_colors)

# Can be used like .filter:
surly_bikes = [bike for bike in some_bikes if bike['brand'] == 'Surly']
print('surly_bikes evaluates to:', surly_bikes)


# --------------------------------------------------------------------------- #
# FUNCTION INPUT MADNESS ---------------------------------------------------- #
# --------------------------------------------------------------------------- #

# Refresher: None in Python is the equivalent of undefined in JS.
def positional_vs_keyword(thing, bear = None):
  # Positional arguments are required:
  print('thing evaluates to:', thing)
  # Keyword arguments are optional:
  print('bear evaluates to:', bear)

# positional_vs_keyword(bear = 'Wish Bear')
  # TypeError: positional_vs_keyword() missing 1 required positional argument: 'thing'

# positional_vs_keyword(22)
  # thing evaluates to: 22
  # bear evaluates to: None

# positional_vs_keyword(22, 'Wish Bear')
  # thing evaluates to: 22
  # bear evaluates to: Wish Bear

# positional_vs_keyword(22, bear = 'Wish Bear')
  # thing evaluates to: 22
  # bear evaluates to: Wish Bear

def the_args_tuple(thing, *args):
  print('thing evaluates to:', thing)
  print('type(args) evaluates to:', type(args))
  print('args evaluates to:', args)

the_args_tuple('hi', 3, 2)
  # thing evaluates to: hi
  # type(args) evaluates to: <class 'tuple'>
  # args evaluates to: (3, 2)

def the_kwargs_object(thing, **kwargs):
  print('thing evaluates to:', thing)
  print('type(kwargs) evaluates to:', type(kwargs))
  print('kwargs evaluates to:', kwargs)

the_kwargs_object('hi', friend=True, score=22)
  # thing evaluates to: hi
  # type(kwargs) evaluates to: <class 'dict'>
  # kwargs evaluates to: {'friend': True, 'score': 22}

def clown_car(thing, *args, **kwargs):
  print('thing evaluates to:', thing)
  print('args evaluates to:', args)
  print('kwargs evaluates to:', kwargs)

clown_car('hi', 2, True, 2, two=(22, True), three='spicy')
  # thing evaluates to: hi
  # args evaluates to: (2, True, 2)
  # kwargs evaluates to: {'two': (22, True), 'three': 'spicy'}

# Unpacking iterables with * and dictionaries with **:
clown_car('good', *['grief', 'this'], **{'is': 'so', 'neato': '!'})
  # thing evaluates to: good
  # args evaluates to: ('grief', 'this')
  # kwargs evaluates to: {'is': 'so', 'neato': '!'}


# --------------------------------------------------------------------------- #
# if __name__ == '__main__': ------------------------------------------------ #
# --------------------------------------------------------------------------- #

if __name__ == '__main__':
  nice_poem = (
    "You've directly ran\n"
    "basics.py and that's nice\n"
    "this is a haiku\n"
  )
  print(nice_poem)

# AKA: If this specific file was ran with the python command.
  # `python basics.py` would cause the print statement to fire.
