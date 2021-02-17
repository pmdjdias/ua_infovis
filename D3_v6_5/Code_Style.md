# Code Style Guide

Partial code's evaluation for the pratical work will be done using this style guide. It was based on the [Idiomatic.js](https://github.com/rwaldron/idiomatic.js) manifesto and the [JQuery](https://contribute.jquery.org/style-guide/js/) style guide.  
__Summary: Be consistent, do not first comma format, chain with context, credit everything you did not write and modularize the code.__

## 1. Whitespaces and Indentation
* Never mix spaces and tabs. Choose one and keep consistency through the entire project.  
* `if/else/for/while/try` always have braces and always go on multiple lines.

``` javascript
// BAD
if(condition) doSomething();

while(condition) iterating++;

for(let i=0;i<100;i++) someIterativeFn();

map = { ready: 9,
    when: 4, "you are": 15 };
 
array = [ 9,
    4,
    15 ];
 
array = [ {
    key: val
} ];
 
array = [ {
    key: val
}, {
    key2: val2
} ];



// GOOD
let i = 0,
    length = 100;

for ( ; i < length; i++ ) {
  // statements
}

let prop;

for ( prop in object ) {
  // statements
}

if ( true ) {
  // statements
} else {
  // statements
}

map = { ready: 9, when: 4, "you are": 15 };
 
array = [ 9, 4, 15 ];
 
array = [ { key: val } ];
 
array = [ { key: val }, { key2: val2 } ];
 
array = [
    { key: val },
    { key2: val2 }
];
 
// Good as well
map = {
    ready: 9,
    when: 4,
    "you are": 15
};
 
array = [
    9,
    4,
    15
];
 
array = [
    {
        key: val
    }
];
 
array = [
    {
        key: val
    },
    {
        key2: val2
    }
];

```

* Each HTML tag must be properly indented following its parent. Exception: Textual content that involves tags like `<p>` and `<br/>`.
``` html
<!-- BAD -->
<div class="container"> <div class="vis_container"> 
        <button id="button_load"> <p class="text_button">Load Data</p> </button> </div> </div>

<!-- GOOD -->
<div class="container"> 
    <div class="vis_container">  
        <button id="button_load"> <p class="text_button">Load Data</p> </button>
    </div> 
</div>

```

* Indent the code by its control structures, and the chainings by its context:
``` javascript
// BAD
d3.select("svg").selectAll("rect") // changed selection
    .data(data1)
    .enter()
    .append("rect") // changed selection
    .attr("a","b")
    .selectAll("circle") // changed selection
    .attr("c","d")

// Good
d3.select("svg").selectAll("rect") // changed selection
    .data(data1)
    .enter()
    .append("rect") // changed selection
        .attr("a","b")
        .selectAll("circle") // changed selection
            .attr("c","d")

// Good as well
d3.select("svg").selectAll("rect") // changed selection
    .data(data1)
    .enter()
        .append("rect") // changed selection
    .attr("a","b")
        .selectAll("circle") // changed selection
    .attr("c","d")
```

* Comma first code formatting is prohibited
``` javascript
// Horrible
let a = "ape"
  , b = "bat"
  , c = "cat"
  , d = "dog"
  , e = "elf"
  , f = "fly"
  , g = "gnu"
  , h = "hat"
  , i = "ibu"
  ;

// Good
let a = "ape",
  b = "bat",
  c = "cat",
  d = "dog",
  e = "elf",
  f = "fly",
  g = "gnu",
  h = "hat",
  i = "ibu";
```

## 2. Naming Conventions and declarations
* Variable and function names should be full words, using camel case with a lowercase first letter. Names should be descriptive but not excessively so. Exceptions are allowed for iterators, such as the use of `i` to represent the index in a loop.

``` javascript
// From the Google Closure Library Style Guide
functionNamesLikeThis;
variableNamesLikeThis;
ConstructorNamesLikeThis;
EnumNamesLikeThis;
methodNamesLikeThis;
SYMBOLIC_CONSTANTS_LIKE_THIS;
```

* Use `let` in the place of `var` for declarations.  
* Any function with +50 lines or chaining with +10 commands must be accompanied by a comment indicating its purpose.

## 3. Code Reuse

* All libraries must be in the final version of your repository or must be loaded using the web.

* Libraries
    * Indicate with a comment above the HTML import tag the following:
        * The main purpose of the library in the project
        * If it uses a global object ($, _) 
        * If it do not uses a global object, indicate on the code the first usage of the library
``` html
<!-- 
    Used for <my purpose>, and <my other purpose>
    It uses the global object <GlobalObject>
-->
<script src="https://some.adress/library.js"> </script>
<script type="text/javascript">
    functionNotInGlobal() // Used from the library <library.js>
</script>
```

* Functions and excerpts
    * Indicate with a comment above function header or the excerpt usage
        * The main purpose of the code
        * Link from the where it was copied, and (if any) the modifications made
        * If it is a function, explain the parameters

``` html
<script type="text/javascript">
    // It does <thing1> by <way1>
    // param1 must be <restriction1> and param2 must <restriction2>
    // From: http://some.adress/example1.html
    function copiedFunction(param1, param2) {

    }

    // Generates <thing1> by <modification1>
    // From: http://some.adress/example2.html
    d3.select("svg").selectAll("rect") // changed selection
        .data(data1)
        .enter()
        .append("rect") // changed selection
            .attr("a","b")
            .selectAll("circle") // changed selection
                .attr("c","d")
</script>
```
* __Transgression of credit notes will impact very negatively the evaluation__.
* Expections for this section are made for D3.

## 4. InfoVis Pipeline
* Whenever possible, try to modularize the code to follow the InfoVis Pipeline
* Load data, preprocess, display, interaction
* D3 eases display + interaction together
* Meta-Example:
``` javascript

// display + interaction
function draw() {
    // draw everything needed
    // bind everything needed
}

// preprocess
function prepProcess(data) {
    // convert wherever needed
}

// Load Data
d3.csv("data.csv")
    .then((data) => {
        let newdata = preProcess(data);
        draw(newdata);
    })
    .catch(err => {console.log(err)});
```
