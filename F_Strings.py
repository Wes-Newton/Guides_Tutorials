# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 15:27:35 2022

@author: Wes User

Excerpts and examples from 

'A Guide to f-string Fromatting in Python' by
Jacqueline Masloff



To use formatted string literals, begin a string with f or F before the
opening quotation mark.  Inside this string, you can wrtie a Python 
expression between { } characters that can refer to variables or literal
values.

f-strings support modifiers to control appearance.
Expressions in f-strings can be modified by a format specification.

Alignments:
    < - Forces the field to be left aligned with the space available,
        default for most objects.
    > - Forces the field to be right aligned within the available
        space, default for numbers.
    = -  Forces the padding to be places after the sign if any but before 
        the digits in the form '+0000000120'. Valid for numeric types only.
        Default when '0' precedes the field width.
    ^ - Forces the field to be centered within the available space.
    
Data Types:
    s - String format.
    d - Decimal integer.
    n - Number, same as d but using locale separtor, i.e. 100,000
    e - Exponent notation, default precision is 6.
    f - Fixed-point notation, default precision is 6.
    % - Percentage.  Multiplies by 100 and display using f format.
    

"""

import os

# # Basic

def pause():
    input('Press return to continue')
    print()

    
x = 4.5
print(f'This will print out the variable x: {x}')
pause()

print(f'This prints x with 3 decimal points precision : {x:.3f}')
# notice the colon after the variable
pause()

# Field Width

# Passing an integer after the ':' will cause that field to be a minimum
# number of characters wide.  Useful for lining up columns.

table =  ['Sjoerd', 'Jack', 'Pat', 'William']
for name in table:
    print(f'Name in the table list, left justified: {name:10}')
pause()

for name in table:
    print(f'Name in the table list, right justified: {name:>10}')
pause()

for name in table:
    print(f'Name in the table list, centered: {name:^10}')
pause()

table2 = [4127, 4098, 7678, 998, 10103]
for num in table2:
    print(f'Number in table: {num:10}')
pause()

# fixed-point notation
for num in table2:
    print(f'Number in table: {num:.1f}')
pause()

# with alignment
for num in table2:
    print(f'Number in table: {num:10,.1f}')
pause()

print('Number\tSquare\tCube')
for x in range(1,11):
    print(f'{x:2d}\t\t{x*x:3d}\t\t{x*x*x:4d}')
pause()

print('Number\t\tSquare\t\tCube')
numbers = [1.2, 2.1, 3.3, 4.5, 5.4, 6.3, 7.6, 8.7, 9.9]         
for x in numbers:
    print(f'{x:2.2f}\t\t{x*x:3.2f}\t\t{x*x*x:4.2f}')
pause()


Apples = .50
Bread = 1.50
Cheese = 2.25

numApples = 3
numBread = 4
numCheese = 2

strApples = 'Apples'
strBread = 'Bread'
strCheese = 'Cheese'

prcApples = numApples * Apples
prcBread = numBread * Bread
prcCheese  = numCheese * Cheese

total = prcApples + prcBread + prcCheese
print(f'{"My Grocery List":^30s}')
print(f'{"="*30}')
print(f'{strApples}\t{numApples:10d}\t\t${prcApples:>5.2f}')
print(f'{strBread}\t{numBread:10d}\t\t${prcBread:>5.2f}')
print(f'{strCheese}\t{numCheese:10d}\t\t${prcCheese:>5.2f}')
print(f'{"Total:":>19s}\t\t${total:>4.2f}')

# Formatting with Commas
number = 10145236
print(f'The number, 10145236, formatted with a comma {number:,.2f}')
print(f'The number, 10145236, formatted with a comma and right aligned in a width of 15 {number:>15,.2f}')
print(f'The number, 10145236, formatted with a comma as a dollar amount ${number:,.2f}')

# Conclusion
# Basic procedure:
#     Place between the quotation marks after 'f' the text to display
#     Enclosing the variables to display between curly braces { }
#     Within the curly braces place a colon after the variable
#     Use format specifications - width, alignment, data tyoe after the colon
    

# From wilkipedia
# in all versions
apples = 4
bananas = 3
print("I have %d apples and %d bananas" % (apples, bananas))  # no longer recommended
print("I have %(apples)d apples and %(bananas)d bananas" % locals())  # no longer recommended
# with Python 2.6+
print("I have {0} apples and {1} bananas".format(apples, bananas))
print("I have {a} apples and {b} bananas".format(b=bananas, a=apples))
# with Python 2.7+
print("I have {} apples and {} bananas".format(apples, bananas))
# or with Python 3.6+
print(f"I have {apples} apples and {bananas} bananas")  


'''
https://docs.python.org/3/library/string.html#template-strings

The available string presentation types are:

Type    Meaning

's'     String format. This is the default type for strings and may be omitted.

None    The same as 's'.



The available integer presentation types are:

Type    Meaning

'b'     Binary format. Outputs the number in base 2.

'c'     Character. Converts the integer to the corresponding unicode character 
        before printing.

'd'     Decimal Integer. Outputs the number in base 10.

'o'     Octal format. Outputs the number in base 8.

'x'     Hex format. Outputs the number in base 16, using lower-case letters 
        for the digits above 9.

'X'     Hex format. Outputs the number in base 16, using upper-case letters 
        for the digits above 9. In case '#' is specified, the prefix '0x' 
        will be upper-cased to '0X' as well.

'n'     Number. This is the same as 'd', except that it uses the current 
        locale setting to insert the appropriate number separator characters.
None    The same as 'd'. 

In addition to the above presentation types, integers can be formatted with 
the floating point presentation types listed below (except 'n' and None). 
When doing so, float() is used to convert the integer to a floating point 
number before formatting. 

The available presentation types for float and Decimal values are:

Type    Meaning

'e'     Scientific notation. For a given precision p, formats the number in 
        scientific notation with the letter ‘e’ separating the coefficient 
        from the exponent. The coefficient has one digit before and p digits 
        after the decimal point, for a total of p + 1 significant digits. 
        With no precision given, uses a precision of 6 digits after the 
        decimal point for float, and shows all coefficient digits for Decimal.
        If no digits follow the decimal point, the decimal point is also 
        removed unless the # option is used.

'E'     Scientific notation. Same as 'e' except it uses an upper case ‘E’ as 
        the separator character.

'f'     Fixed-point notation. For a given precision p, formats the number as 
        a decimal number with exactly p digits following the decimal point. 
        With no precision given, uses a precision of 6 digits after the 
        decimal point for float, and uses a precision large enough to show 
        all coefficient digits for Decimal. If no digits follow the decimal 
        point, the decimal point is also removed unless the # option is used.

'F'     Fixed-point notation. Same as 'f', but converts nan to NAN and inf 
        to INF.

'g'     General format. For a given precision p >= 1, this rounds the number 
        to p significant digits and then formats the result in either 
        fixed-point format or in scientific notation, depending on its 
        magnitude. A precision of 0 is treated as equivalent to a 
        precision of 1.  
        
        The precise rules are as follows: suppose that the 
        result formatted with presentation type 'e' and precision p-1 would 
        have exponent exp. Then, if m <= exp < p, where m is -4 for floats 
        and -6 for Decimals, the number is formatted with presentation 
        type 'f' and precision p-1-exp. Otherwise, the number is formatted 
        with presentation type 'e' and precision p-1. In both cases 
        insignificant trailing zeros are removed from the significand, and 
        the decimal point is also removed if there are no remaining digits 
        following it, unless the '#' option is used. 
        
        With no precision given, uses a precision of 6 significant digits 
        for float. For Decimal, the coefficient of the result is formed 
        from the coefficient digits of the value; scientific notation 
        is used for values smaller than 1e-6 in absolute value and values 
        where the place value of the least significant digit is larger 
        than 1, and fixed-point notation is used otherwise.  
        
        Positive and negative infinity, positive and negative zero, and nans, 
        are formatted as inf, -inf, 0, -0 and nan respectively,regardless of 
        the precision.

'G'     General format. Same as 'g' except switches to 'E' if the number 
        gets too large. The representations of infinity and NaN are 
        uppercased, too.

'n'     Number. This is the same as 'g', except that it uses the current 
        locale setting to insert the appropriate number separator characters.

'%'     Percentage. Multiplies the number by 100 and displays in fixed ('f') 
        format, followed by a percent sign.

None    For float this is the same as 'g', except that when fixed-point 
        notation is used to format the result, it always includes at least 
        one digit past the decimal point. The precision used is as large as 
        needed to represent the given value faithfully.

        For Decimal, this is the same as either 'g' or 'G' depending on the 
        value of context.capitals for the current decimal context.

        The overall effect is to match the output of str() as altered by the 
        other format modifiers.

'''


'''

https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals

Unless an 'r' or 'R' prefix is present, escape sequences in string and bytes 
literals are interpreted according to rules similar to those used by 
Standard C. The recognized escape sequences are:

Escape Sequence     Meaning                                 Notes

\newline            Backslash and newline ignored

\\                  Backslash (\)

\'                  Single quote (')

\"                  Double quote (")

\a                  ASCII Bell (BEL)

\b                  ASCII Backspace (BS)

\f                  ASCII Formfeed (FF)

\n                  ASCII Linefeed (LF)

\r                  ASCII Carriage Return (CR)

\t                  ASCII Horizontal Tab (TAB)

\v                  ASCII Vertical Tab (VT)

\ooo                Character with octal value ooo      (1,3)

\xhh                Character with hex value hh         (2,3)

Escape sequences only recognized in string literals are:

Escape Sequence     Meaning                             Notes

\N{name}            Character named name in the 
                    Unicode database                    (4)

\uxxxx              Character with 16-bit hex 
                    value xxxx                          (5)

\Uxxxxxxxx          Character with 32-bit hex 
                    value xxxxxxxx                      (6)

Notes:

1 - As in Standard C, up to three octal digits are accepted.

2 - Unlike in Standard C, exactly two hex digits are required.

3 - In a bytes literal, hexadecimal and octal escapes denote the byte 
    with the given value. In a string literal, these escapes denote a 
    Unicode character with the given value.

4 - Changed in version 3.3: Support for name aliases 1 has been added.

5 - Exactly four hex digits are required.

6 - Any Unicode character can be encoded this way. Exactly eight hex 
    digits are required.
    
    
'''
