JavaScript can change HTML content.
<button type="button" onclick='document.getElementById("demo").innerHTML = "Hello JavaScript!"'>Click Me!</button>


In this case JavaScript changes the value of the src (source) attribute of an image
<button onclick="document.getElementById('myImage').src='pic_bulbon.gif'">Turn on the light</button>


var have global scope
let have block scope


var can be redeclared, it reset the value
let can not be redeclare


using var Redeclaring a variable inside a block will also redeclare the variable outside the block:
using let Redeclaring a variable inside a block will not redeclare the variable outside the block:

JavaScript Hoisting refers to the process whereby the interpreter appears to move the declaration of functions, variables, classes, or imports to the top of their scope, prior to execution of the code.


"this" in JavaScript refers to the current execution context. In a browser environment, this typically refers to the global object (window) in the global scope, but inside a function, it depends on how the function is called.


JavaScript const variables must be assigned a value when they are declared:

Redeclaring an existing var or let variable to const, in the same scope, is not allowed:


There are different types of JavaScript operators:

Arithmetic Operators
Assignment Operators
Comparison Operators
String Operators
Logical Operators
Bitwise Operators
Ternary Operators
Type Operators


==	equal to
===	equal value and equal type


The Nullish coalescing assignment operator is used between two values.
If the first value is undefined or null, the second value is assigned.

JavaScript has 8 Datatypes
1. String
2. Number
3. Bigint
4. Boolean
5. Undefined
6. Null
7. Symbol
8. Object

The Object Datatype
The object data type can contain:

1. An object
2. An array
3. A date

// Object: 
const person = {firstName:"John", lastName:"Doe"};

// Array object:
const cars = ["Saab", "Volvo", "BMW"];

// Date object:
const date = new Date("2022-03-25");

Javascript numbers are always one type:
double (64-bit floating point).



The typeof operator returns the type of a variable or an expression:
typeof "John" 

car = undefined;    // Value is undefined, type is undefined


# Function
function toCelsius(fahrenheit) {
  return (5/9) * (fahrenheit-32);
}

let value = toCelsius(77);




# declare object
const person = {
  firstName: "John",
  lastName : "Doe",
  id       : 5566,
  fullName : function() {
    return this.firstName + " " + this.lastName;
  }
};

name = person.fullName();

# this
In an object method, this refers to the object.
Alone, this refers to the global object.
In a function, this refers to the global object.
In a function, in strict mode, this is undefined.
In an event, this refers to the element that received the event.
Methods like call(), apply(), and bind() can refer this to any object.


this is not a variable. It is a keyword. You cannot change the value of this.




Do Not Declare Strings, Numbers, and Booleans as Objects!. It will create object type rather than it's respective type ie. string, number, boolean

x = new String();        // Declares x as a String object
y = new Number();        // Declares y as a Number object
z = new Boolean();       // Declares z as a Boolean object
Avoid String, Number, and Boolean objects. They complicate your code and slow down execution speed.


# Event
HTML events are "things" that happen to HTML elements.
When JavaScript is used in HTML pages, JavaScript can "react" on these events.

<element event='some JavaScript'>
eg. <button onclick="document.getElementById('demo').innerHTML = Date()">The time is?</button>

list of events
https://www.w3schools.com/jsref/dom_obj_event.asp


# string
Templates were introduced with ES6 (JavaScript 2016).
Templates allow single and double quotes inside a string:

let text = `He's often called "Johnny"`;


let text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
let length = text.length;

Escape character '\'
let text = "We are the so-called \"Vikings\" from the north.";


Escape character

Code	Result
\b	Backspace
\f	Form Feed
\n	New Line
\r	Carriage Return
\t	Horizontal Tabulator
\v	Vertical Tabulator


Templates allow multiline strings:

let text =
`The quick
brown fox
jumps over
the lazy dog`;


mystr = new String('vis') # it will create with type object not string


# String Methods
String length
String charAt()
String charCodeAt()
String at()
String [ ]
String slice()
String substring()
String substr()

String toUpperCase()
String toLowerCase()
String concat()
String trim()
String trimStart()
String trimEnd()
String padStart()
String padEnd()
String repeat()
String replace()
String replaceAll()
String split()

String indexOf()
String lastIndexOf()
String search()
String match()
String matchAll()
String includes()
String startsWith()
String endsWith()

https://www.w3schools.com/jsref/jsref_obj_string.asp


Property access might be a little unpredictable:

It makes strings look like arrays (but they are not)
If no character is found, [ ] returns undefined, while charAt() returns an empty string.
It is read only. str[0] = "A" gives no error (but does not work!)


slice(start, end)
substring(start, end)
substr(start, length) - if first parameter is negative, position counts from the end of the string


All string methods return a new string. They don't modify the original string. Strings are immutable: Strings cannot be changed, only replaced.


The replace() method replaces only the first match. If you want to replace all matches, use a regular expression with the /g flag set. See examples below.


To replace case insensitive, use a regular expression with an /i flag (insensitive):
let text = "Please visit Microsoft!";
let newText = text.replace(/MICROSOFT/i, "W3Schools");


To replace all matches, use a regular expression with a /g flag (global match):
let text = "Please visit Microsoft and Microsoft!";
let newText = text.replace(/Microsoft/g, "W3Schools");


The search() method cannot take a second start position argument.
The indexOf() method cannot take powerful search values (regular expressions).


Template Strings allow variables, expression in strings:  (like f-string in python), Automatic replacing of expressions with real values is called string interpolation.
let text = `Welcome ${firstName}, ${lastName}!`;


# Numbers
JavaScript Numbers are Always 64-bit Floating Point
Integers (numbers without a period or exponent notation) are accurate up to 15 digits.

JavaScript will try to convert strings to numbers in all numeric operations:

This will work:
let x = "100";
let y = "10";
let z = x / y; // output: 10, like devision all other arithmetic operation will work


NaN - Not a Number
NaN is a JavaScript reserved word indicating that a number is not a legal number.
Trying to do arithmetic with a non-numeric string will result in NaN (Not a Number)

You can use the global JavaScript function isNaN() to find out if a value is a not a number:

NaN is a number: typeof NaN returns number:



Infinity (or -Infinity) is the value JavaScript will return if you calculate a number outside the largest possible number.
Infinity is a number: typeof Infinity returns number.


JavaScript interprets numeric constants as hexadecimal if they are preceded by 0x.
let x = 0xFF;


Never write a number with a leading zero (like 07).
Some JavaScript versions interpret numbers as octal if they are written with a leading zero.


By default, JavaScript displays numbers as base 10 decimals.
But you can use the toString() method to output numbers from base 2 to base 36.
Hexadecimal is base 16. Decimal is base 10. Octal is base 8. Binary is base 2.

let myNumber = 32;
myNumber.toString(32);
myNumber.toString(16);
myNumber.toString(12);
myNumber.toString(10);
myNumber.toString(8);
myNumber.toString(2);


# BigInt
To create a BigInt, append n to the end of an integer or call BigInt():

let x = 9999999999999999;
let y = 9999999999999999n;

let x = 1234567890123456789012345n;
let y = BigInt(1234567890123456789012345)


Arithmetic between a BigInt and a Number is not allowed (type conversion lose information).
Unsigned right shift (>>>) can not be done on a BigInt (it does not have a fixed width).


A BigInt can not have decimals.
BigInt can also be written in hexadecimal, octal, or binary notation:

## Minimum and Maximum Safe Integers
let x = Number.MAX_SAFE_INTEGER;


The Number.isInteger() method returns true if the argument is an integer.
A safe integer is an integer that can be exactly represented as a double precision number. The Number.isSafeInteger() method returns true if the argument is a safe integer.



Number() can also convert a date to a number.

Number(new Date("1970-01-01"))

The Date() method returns the number of milliseconds since 1.1.1970.


https://www.w3schools.com/jsref/jsref_obj_number.asp


# Array
An array is a special variable, which can hold more than one value:

const cars = ["Saab", "Volvo", "BMW"];


Adding elements with high indexes can create undefined "holes" in an array:

If you use named indexes, JavaScript will redefine the array to an object. After that, some array methods and properties will produce incorrect results.


The Difference Between Arrays and Objects
In JavaScript, arrays use numbered indexes.  

In JavaScript, objects use named indexes.

Arrays are a special kind of objects, with numbered indexes.


// Create an array with 40 undefined elements:
const points = new Array(40);  


The instanceof operator returns true if an object is created by a given constructor:


const fruits = ["Banana", "Orange", "Apple"];
fruits instanceof Array;


# array methods
Array length
Array toString()
Array at()
Array join()
Array pop()
Array push()
Array shift()
Array unshift()
Array delete()
Array concat()
Array copyWithin()
Array flat()
Array splice()
Array toSpliced()
Array slice()


Array indexOf()
Array lastIndexOf()
Array includes()
Array find()
Array findIndex()
Array findLast()
Array findLastIndex()


Array sort()
Array reverse()
Array toSorted()
Array toReversed()
Sorting Objects
Numeric Sort
Random Sort
Math.min()
Math.max()
Home made Min()
Home made Max()


Array forEach
Array map()
Array flatMap()
Array filter()
Array reduce()
Array reduceRight()
Array every() - The every() method checks if all array values pass a test.
Array some()
Array from()
Array keys()
Array entries()
Array with()
Array Spread (...)


# foreach example
const numbers = [45, 4, 9, 16, 25];
let txt = "";
numbers.forEach(myFunction);

function myFunction(value, index, array) {
  txt += value + "<br>";
}

# map example
const numbers1 = [45, 4, 9, 16, 25];
const numbers2 = numbers1.map(myFunction);

function myFunction(value, index, array) {
  return value * 2;
}

# filter example
const numbers = [45, 4, 9, 16, 25];
const over18 = numbers.filter(myFunction);

function myFunction(value, index, array) {
  return value > 18;
}

# reduce example
const numbers = [45, 4, 9, 16, 25];
let sum = numbers.reduce(myFunction);

function myFunction(total, value, index, array) {
  return total + value;
}

# every Example
const numbers = [45, 4, 9, 16, 25];
let allOver18 = numbers.every(myFunction);

function myFunction(value, index, array) {
  return value > 18;
}


The difference between toSorted() and sort() is that the first method creates a new array, keeping the original array unchanged, while the last method alters the original array.
The difference between toReversed() and reverse() is that the first method creates a new array, keeping the original array unchanged, while the last method alters the original array.


The ... operator expands an iterable (like an array) into more elements:

const q1 = ["Jan", "Feb", "Mar"];
const q2 = ["Apr", "May", "Jun"];
const q3 = ["Jul", "Aug", "Sep"];
const q4 = ["Oct", "Nov", "May"];

const year = [...q1, ...q2, ...q3, ...q4];



# Dates
Date objects are created with the new Date() constructor.

There are 9 ways to create a new date object:

new Date()
new Date(date string)

new Date(year,month)
new Date(year,month,day)
new Date(year,month,day,hours)
new Date(year,month,day,hours,minutes)
new Date(year,month,day,hours,minutes,seconds)
new Date(year,month,day,hours,minutes,seconds,ms)

new Date(milliseconds)


# date methods
getFullYear()	Get year as a four digit number (yyyy)
getMonth()	Get month as a number (0-11)
getDate()	Get day as a number (1-31)
getDay()	Get weekday as a number (0-6)
getHours()	Get hour (0-23)
getMinutes()	Get minute (0-59)
getSeconds()	Get second (0-59)
getMilliseconds()	Get millisecond (0-999)
getTime()	Get time (milliseconds since January 1, 1970)

above methods with "getUTC" will return utc date data

Date.now();


The getTimezoneOffset() method returns the difference (in minutes) between local time an UTC time:



setDate()	Set the day as a number (1-31)
setFullYear()	Set the year (optionally month and day)
setHours()	Set the hour (0-23)
setMilliseconds()	Set the milliseconds (0-999)
setMinutes()	Set the minutes (0-59)
setMonth()	Set the month (0-11)
setSeconds()	Set the seconds (0-59)
setTime()	Set the time (milliseconds since January 1, 1970)

# Math
Unlike other objects, the Math object has no constructor. The Math object is static. All methods and properties can be used without creating a Math object first.

Math.E        // returns Euler's number
Math.PI       // returns PI
Math.SQRT2    // returns the square root of 2
Math.SQRT1_2  // returns the square root of 1/2
Math.LN2      // returns the natural logarithm of 2
Math.LN10     // returns the natural logarithm of 10
Math.LOG2E    // returns base 2 logarithm of E
Math.LOG10E   // returns base 10 logarithm of E


Math.round(x)	Returns x rounded to its nearest integer
Math.ceil(x)	Returns x rounded up to its nearest integer
Math.floor(x)	Returns x rounded down to its nearest integer
Math.trunc(x)	Returns the integer part of x (new in ES6)

https://www.w3schools.com/jsref/jsref_obj_math.asp

# Random
Math.random() returns a random number between 0 (inclusive),  and 1 (exclusive):

=> Proper random function
function getRndInteger(min, max) {
  return Math.floor(Math.random() * (max - min) ) + min;
}


# Boolean
You can use the Boolean() function to find out if an expression (or a variable) is true:

Boolean(10 > 9)
(10 > 9)
10 > 9


Everything With a "Value" is True

100

3.14

-15

"Hello"

"false"

7 + 1 + 3.14


Everything Without a "Value" is False

Comparing two JavaScript objects always return false.


variablename = (condition) ? value1:value2 
let voteable = (age < 18) ? "Too young":"Old enough";

To secure a proper result, variables should be converted to the proper type before comparison:


The Nullish Coalescing Operator (??)
The ?? operator returns the first argument if it is not nullish (null or undefined). Otherwise it returns the second argument.

The Optional Chaining Operator (?.)
The ?. operator returns undefined if an object is undefined or null (instead of throwing an error).

// Create an object:
const car = {type:"Fiat", model:"500", color:"white"};
// Ask for car name:
document.getElementById("demo").innerHTML = car?.name;


Switching Details
If multiple cases matches a case value, the first case is selected.

If no matching cases are found, the program continues to the default label.

If no default label is found, the program continues to the statement(s) after the switch.
















# revise more from source
event
