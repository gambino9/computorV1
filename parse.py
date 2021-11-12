# regex for a monomial : "^\s*[+-]?\s*(\d+(?:\.\d+)?)?\s*(([\*]?)\s*(([X]\s*)(?(4)(\^)(\s*(\d+(?!\.)))|)?))?\s*"
# split whitespaces
# https://regex101.com/r/pC4Aud/1

# Without spaces : "^([+-])?(\d+(?:\.\d+)?)?([\*]?)(([X])(?(5)(\^)(\d+(?!\.))|)?)?"

# 1st capturing group : ([+-])?
# 1st character may be a "-" or "+", but it is optional

# 2nd capturing group : (\d+(?:\.\d+)?)?
# May be an int (\d+) or a float, or nothing. (\.\d+)
# (?:...) matches everything enclosed

# 3rd capturing group : ([\*]?)
# A single "*" can be match, but is also optional

# 4th capturing group : (([X])(?(5)(\^)((\d+(?!\.)))|)?)?
# 5th capturing group : ([X])
# 6th capturing group : (\^)
# 7th capturing group : (\d+(?!\.))

# 4th capturing group : a conditional statement enclosing 5th, 6th, 7th
# groups. If 5th group returns a match, the pattern before the "|" is matched
# otherwise, the pattern after the "|" is matched. Here, it allows us to check
# that an "X" character is matched before we try to match 6th capturing
# group "^" char and what comes after. In other words, "^\d" is dependant on
# a "X" char presence to be matched.

# 7th capturing group : Only accepts a int after the "^" char. Float are
# explicitly forbidden with the negative lookahead(?!...), that ensures that
# the float pattern will not match
