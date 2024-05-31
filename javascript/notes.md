JavaScript can change HTML content.
```
<button type="button" onclick='document.getElementById("demo").innerHTML = "Hello JavaScript!"'>Click Me!</button>
```

In this case JavaScript changes the value of the src (source) attribute of an image
```
<button onclick="document.getElementById('myImage').src='pic_bulbon.gif'">Turn on the light</button>
```

var have global scope. let have block scope


var can be redeclared, it reset the value. let can not be redeclare


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


# loop
## for loop
for (let i = 0; i < cars.length; i++) {
  text += cars[i] + "<br>";
}


## for in loop
const person = {fname:"John", lname:"Doe", age:25}; // It is object but can iterate over loop too

let text = "";
for (let x in person) {
  text += person[x];
}

Do not use for in over an Array if the index order is important. The index order is implementation-dependent, and array values may not be accessed in the order you expect. It is better to use a for loop, a for of loop, or Array.forEach() when the order is important.

## Array.forEach()
The forEach() method calls a function (a callback function) once for each array element.

```
const numbers = [45, 4, 9, 16, 25];

let txt = "";
numbers.forEach(myFunction);

function myFunction(value, index, array) {
  txt += value;
}
```

## The For Of Loop
It lets you loop over iterable data structures such as Arrays, Strings, Maps, NodeLists, and more:
```
const cars = ["BMW", "Volvo", "Mini"];

let text = "";
for (let x of cars) {
  text += x;
}
```

## The While Loop
while (i < 10) {
  text += "The number is " + i;
  i++;
}

## The Do While Loop
do {
  text += "The number is " + i;
  i++;
}
while (i < 10);

# break and continue
The break statement "jumps out" of a loop. The continue statement "jumps over" one iteration in the loop.

for (let i = 0; i < 10; i++) {
  if (i === 3) { break; }
  text += "The number is " + i + "<br>";
}


for (let i = 0; i < 10; i++) {
  if (i === 3) { continue; }
  text += "The number is " + i + "<br>";
}

The continue statement (with or without a label reference) can only be used to skip one loop iteration.

The break statement, without a label reference, can only be used to jump out of a loop or a switch.

With a label reference, the break statement can be used to jump out of any code block:


# Home made iterable 
This return done too, so it can be used in for of loop too

// Create an Object
myNumbers = {};

// Make it Iterable
myNumbers[Symbol.iterator] = function() {
  let n = 0;
  done = false;
  return {
    next() {
      n += 10;
      if (n == 100) {done = true}
      return {value:n, done:done};
    }
  };
}


let iterator = myNumbers[Symbol.iterator]();

while (true) {
  const result = iterator.next();
  if (result.done) break;
  // Any Code Here
}

# set
you can create empty set and add value

Can pass array inside set constuctor to create new set
const letters = new Set(["a","b","c"]);

letters.add("a");


// add variable
const a = "a";
letters.add(a);

If you add equal elements, only the first will be saved:

Sets are Objects
typeof letters;      // Returns object
letters instanceof Set;  // Returns true

has("a") - to check "a" is present in set or not
The values() method returns an Iterator object with the values in a Set:
The keys() method returns an Iterator object with the values in a Set:
The entries() method returns an Iterator with [value,value] pairs from a Set.

# Map
A Map holds key-value pairs where the keys can be any datatype. A Map remembers the original insertion order of the keys.

## create
// Create a Map
const fruits = new Map([
  ["apples", 500],
  ["bananas", 300],
  ["oranges", 200]
]);

// Create a Map
const fruits = new Map();

// Set Map Values. Creating map using set() 
fruits.set("apples", 500);
fruits.set("bananas", 300);
fruits.set("oranges", 200);

The set() method can also be used to change existing Map values:
  fruits.set("apples", 200);
The get() method gets the value of a key in a Map:
  fruits.get("apples");    // Returns 500


// Returns object:
typeof fruits;

// Returns true:
fruits instanceof Map;


## Object	
Not directly iterable
Do not have a size property	
Keys must be Strings (or Symbols)	
Keys are not well ordered	
Have default keys	


## Map
Directly iterable
Have a size property
Keys can be any datatype
Keys are ordered by insertion
Do not have default keys


The size property returns the number of elements in a map:
The delete() method removes a map element:
The clear() method removes all the elements from a map:
The has() method returns true if a key exists in a map:
The forEach() method invokes a callback for each key/value pair in a map:
The entries() method returns an iterator object with the [key,values] in a map:
The keys() method returns an iterator object with the keys in a map:
The values() method returns an iterator object with the values in a map:


Being able to use objects as keys is an important Map feature.
// Create Objects
const apples = {name: 'Apples'};
const bananas = {name: 'Bananas'};
const oranges = {name: 'Oranges'};

// Create a Map
const fruits = new Map();

// Add new Elements to the Map
fruits.set(apples, 500);
fruits.set(bananas, 300);
fruits.set(oranges, 200);


The Map.groupBy() method groups elements of an object according to string values returned from a callback function. The Map.groupBy() method does not change the original object.

// Create an Array
const fruits = [
  {name:"apples", quantity:300},
  {name:"bananas", quantity:500},
  {name:"oranges", quantity:200},
  {name:"kiwi", quantity:150}
];

// Callback function to Group Elements
function myCallback({ quantity }) {
  return quantity > 200 ? "ok" : "low";
}

// Group by Quantity
const result = Map.groupBy(fruits, myCallback);



The difference between Object.groupBy() and Map.groupBy() is: Object.groupBy() groups elements into a JavaScript object. Map.groupBy() groups elements into a Map object.


# typeof
In JavaScript, null is a primitive value. However, typeof returns "object". This is a well-known bug in JavaScript and has historical reasons.

A complex data type can store multiple values and/or different data types together.

JavaScript has one complex data type:

object
All other complex types like arrays, functions, sets, and maps are just different types of objects.

The typeof operator returns only two types:

object
function


typeof {name:'John'}   // Returns object
typeof [1,2,3,4]       // Returns object
typeof new Map()       // Returns object
typeof new Set()       // Returns object

typeof function (){}   // Returns function


How to know if a variable is an array?

// Create an Array
const fruits = ["apples", "bananas", "oranges"];
Array.isArray(fruits);

The instanceof operator returns true if an object is an instance of a specified object type:
// Create a Date
const time = new Date();

(time instanceof Date);



The typeof of an undefined variable is undefined.
The typeof of a variable with no value is undefined. The value is also undefined.
Any variable can be emptied, by setting the value to undefined. The type will also be undefined.

An empty value has nothing to do with undefined. An empty string has both a legal value and a type.
let car = "";

The value is:
The type is: string


In JavaScript null is "nothing". It is supposed to be something that doesn't exist. Unfortunately, in JavaScript, the data type of null is an object. You can empty an object by setting it to null: You can also empty an object by setting it to undefined:

Difference Between Undefined and Null
undefined and null are equal in value but different in type:

typeof undefined      // undefined
typeof null           // object

null === undefined    // false
null == undefined     // true

The constructor property returns the constructor function for all JavaScript variables.
// Returns function Object() {[native code]}:
{name:'John',age:34}.constructor

// Returns function Array() {[native code]}:
[1,2,3,4].constructor

// Returns function Date() {[native code]}:
new Date().constructor

// Returns function Set() {[native code]}:
new Set().constructor

// Returns function Map() {[native code]}:
new Map().constructor

// Returns function Function() {[native code]}:
function () {}.constructor


With the constructor, you can check if an object is an Array:
(myArray.constructor === Array);  
(myDate.constructor === Date);

The data type of NaN (Not a Number) is number !


The void operator evaluates an expression and returns undefined. This operator is often used to obtain the undefined primitive value, using "void(0)" (useful when evaluating an expression without using the return value).

<a href="javascript:void(0);">
  Useless link
</a>

<a href="javascript:void(document.body.style.backgroundColor='red');">
  Click me to change the background color of body to red
</a>


JavaScript variables can be converted to a new variable and another data type:

By the use of a JavaScript function
Automatically by JavaScript itself


A non numeric string (like "John") converts to NaN (Not a Number).
Number("John")

Number()	Returns a number, converted from its argument
parseFloat()	Parses a string and returns a floating point number
parseInt()	Parses a string and returns an integer


The global method String() can convert numbers to strings.
String(x)         // returns a string from a number variable x
String(123)       // returns a string from a number literal 123

The Number method toString() does the same.
x.toString()
(123).toString()

## Date methods
getDate()	Get the day as a number (1-31)
getDay()	Get the weekday a number (0-6)
getFullYear()	Get the four digit year (yyyy)
getHours()	Get the hour (0-23)
getMilliseconds()	Get the milliseconds (0-999)
getMinutes()	Get the minutes (0-59)
getMonth()	Get the month (0-11)
getSeconds()	Get the seconds (0-59)
getTime()	Get the time (milliseconds since January 1, 1970)


Number(false)     // returns 0
Number(true)      // returns 1

String(false)      // returns "false"
String(true)       // returns "true"

false.toString()   // returns "false"
true.toString()    // returns "true"


## Automatic Type conversion
When JavaScript tries to operate on a "wrong" data type, it will try to convert the value to a "right" type. The result is not always what you expect:

5 + null    // returns 5         because null is converted to 0
"5" + null  // returns "5null"   because null is converted to "null"
"5" + 2     // returns "52"      because 2 is converted to "2"
"5" - 2     // returns 3         because "5" is converted to 5
"5" * "2"   // returns 10        because "5" and "2" are converted to 5 and 2

JavaScript automatically calls the variable's toString() function when you try to "output" an object or a variable:

https://www.w3schools.com/js/js_type_conversion.asp # see type conversion table

# Destructing assginment syntaxt
// Create an Object
const person = {
  firstName: "John",
  lastName: "Doe",
  age: 50
};

// Destructuring
let {firstName, lastName} = person;


It can also unpack arrays and any other iterables:
let [firstName, lastName] = person;

The order of the properties does not matter:

Object Property alias
// Destructuring
let {lastName : name} = person;


# Exception Handling
JavaScript will actually create an Error object with two properties: name and message.


# Scope
A variable declared outside a function, becomes GLOBAL.

let carName = "Volvo";
// code here can use carName

function myFunction() {
// code here can also use carName
}

Variables declared Globally (outside any function) have Global Scope.

Global variables can be accessed from anywhere in a JavaScript program. Variables declared with var, let and const are quite similar when declared outside a block. They all have Global Scope:


If you assign a value to a variable that has not been declared, it will automatically become a GLOBAL variable. This code example will declare a global variable carName, even if the value is assigned inside a function.

myFunction();

// code here can use carName

function myFunction() {
  carName = "Volvo";
}

In HTML, the global scope is the window object. Global variables defined with the var keyword belong to the window object:
var carName = "Volvo";
// code here can use window.carName


Global variables defined with the let keyword do not belong to the window object:

## warning
Do NOT create global variables unless you intend to.

Your global variables (or functions) can overwrite window variables (or functions).
Any function, including the window object, can overwrite your global variables and functions.



# Hoisting
Hoisting is JavaScript's default behavior of moving all declarations to the top of the current scope (to the top of the current script or the current function).

JavaScript only hoists declarations, not initializations.

To avoid bugs, always declare all variables at the beginning of every scope.

# Strict Mode
"use strict"; Defines that JavaScript code should be executed in "strict mode". It helps you to write cleaner code. JavaScript in strict mode does not allow variables to be used if they are not declared.

```
"use strict";
x = 3.14;       // This will cause an error because x is not declared
```

Strict mode changes previously accepted "bad syntax" into real errors.

As an example, in normal JavaScript, mistyping a variable name creates a new global variable. In strict mode, this will throw an error, making it impossible to accidentally create a global variable.

In normal JavaScript, a developer will not receive any error feedback assigning values to non-writable properties.

In strict mode, any assignment to a non-writable property, a getter-only property, a non-existing property, a non-existing variable, or a non-existing object, will throw an error.

Deleting a variable (or object) is not allowed
Deleting a function is not allowed.
Duplicating a parameter name is not allowed:
Octal numeric literals are not allowed:
  let x = 010;             // This will cause an error
Octal escape characters are not allowed:
  let x = "\010";            // This will cause an error
Writing to a read-only property is not allowed:

  "use strict";
const obj = {};
Object.defineProperty(obj, "x", {value:0, writable:false});

obj.x = 3.14;            // This will cause an error


# this
The this keyword refers to different objects depending on how it is used:

- In an object method, this refers to the object.
- Alone, this refers to the global object.
- In a function, this refers to the global object.
- In a function, in strict mode, this is undefined.
- In an event, this refers to the element that received the event.
- Methods like call(), apply(), and bind() can refer this to any object.


this is not a variable. It is a keyword. You cannot change the value of this.

In a browser window the global object is [object Window]:


# Arrow Function
Before Arrow:
hello = function() {
  return "Hello World!";
}

With Arrow Function:
hello = () => {
  return "Hello World!";
}

# class
A JavaScript class is not an object. It is a template for JavaScript objects.

class Car {
  constructor(name, year) {
    this.name = name;
    this.year = year;
  }
}

# JSON
use the JavaScript built-in function JSON.parse() to convert the string into a JavaScript object:
let text = '{ "employees" : [' +
'{ "firstName":"John" , "lastName":"Doe" },' +
'{ "firstName":"Anna" , "lastName":"Smith" },' +
'{ "firstName":"Peter" , "lastName":"Jones" } ]}';

const obj = JSON.parse(text);

// use object above
<p id="demo"></p>

<script>
document.getElementById("demo").innerHTML =
obj.employees[1].firstName + " " + obj.employees[1].lastName;
</script>


# recaptulate
Type Conversion
Destructuring
bitwise
Precedence
strict mode
class - on wards


# revise more from source
event
