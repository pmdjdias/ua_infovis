# Web technologies
The web today runs on a set of simple protocols and standards to create a powerful and stable platform. HTML, CSS, Javascript and SVG are the building blocks choosen for these lab classes and posterior assigments, and the Google Charts, D3 and Three.js libraries presents compliance with these standards. As this is a InfoVis course, we will not dive in in the particular workings of each one of these technologies, but offer some initial highlights of important 

## Serve files
For starters, we will see how to serve files in a secure way for the browser. Since the files for the classes are loaded from the disk, the browser blocks the loading for security reasons. You will need to run a local server to render the pages and visualizations. Here we will present some ways to do it. 

### Static server with script languages

#### Python
You can start a local server using Python natively. Navigate to the directory that contains your files  and then type 
``` bash
python -m SimpleHTTPServer
```
in the command line. If you type `localhost:8000` into the address bar of your browser, then you should see the files that you can display in the web page.
If you're in an environment running Python 3 instead of Python 2, you can use 
``` bash
python -m http.server
```
to start up the local server instead.

#### nodejs
For nodejs, you need to install a package with npm the command is:
```bash
npm install http-server -g
```
Navigate to the directory that contains all the files and then type 
``` bash
http-server
```
in the command line. If you type `localhost:8080` into the address bar of your browser, then you should see the files that you can display in the web page.

### Live server with Text Editors
While modifying code using a static server, like the python one, you'll need to reload the page to see the changes made. A live server from a editor or IDE reloads automatically the page, than you can see the changes in real time. [VSCode](https://code.visualstudio.com/) and [Atom](https://atom.io/) are lightweight text editors with some IDE functionalities for code, and both have a extension for a live server.

#### VSCode
![VSCode Live Server Extension](./images/vscode_liveserver.png)

From the initial screen, click on the Extensions tab (1), type "live server" on the search bar (2) and install the extension (3). The main shortcuts are _ALT+L, ALT+O_ to start the server and _ALT+L, ALT+C_ to stop it. You can also run a web page by right-clicking it on the outline view.   
For each new project, add the project folder to the workspace, than the root of the server can be started by the new directory. More details on how to use the extension on its installation page.

#### Atom
![Atom Live Server Extension](./images/atom_liveserver.png)

From the initial screen, click on File tab (1), settings (2) than install (3), type "live server" on the search bar (4) and install the extension (5). The main shortcuts are _CTRL+ALT+L_ to start the server and _CTRL+ALT+Q,_ to stop it. You can also run a web page by right-clicking it on the outline view.  
For each new project, add the project folder to the workspace, than the root of the server can be started by the new directory.  
More details on how to use the extension on its installation page.


## HTML and CSS
Now that we have a working server, it is time to create a site. HTML works based on nested tags that represent the document structure. The `<body>` tag renders all that is visible for the user. A simple HTML page is shown below.

``` html
<!DOCTYPE html>
<html>
   <head>
      <title>Hello HTML</title>
   </head>	
   <body>
      <p class="hello">Hello World!</p>
   </body>	
</html>
```

These tags can be identified by class or id (like in the `<p>` tag above), and have style properties that can be altered, and we control them using CSS. CSS can be injected directly on the tags, but the `<style>` tag can alter all instances of a determined selector, like:

``` css
selector { property : value }
```
The selector can be a tag, class or id, and property or values are element dependant. A example page with a blue centered text and gray background: 

``` html
<!DOCTYPE html>
<html>
   <head>
      <title>Hello CSS</title>
      <style> 
        p {
            text-align: center;
            color: red;
            font-size: 100px
        }
        body {
            background-color: gray
        }
      </style>
   </head>	
   <body>
      <p>Hello World!</p>
   </body>
</html>
```

## Javascript
The logic engine that powers up HTML and CSS is Javascript, a script language interpreted by the browser. A pge with some syntax example is shown below:

``` html
<!DOCTYPE html>
<html>
    <head>
        <title>Hello JS</title>
    </head>	
    <body>      
          
    </body>
    <script type = "text/javascript">
            let count_even = 0;
            document.write("Starting Loop" + "<br />");
         
            for(let count = 0; count < 10; count++) {
                document.write("Current Count : " + count );
                if (count % 2 == 0) {
                    count_even++;
                    document.write("<br /> Current Count is even <br />");   
                }
               document.write("<br />");
            }         
            document.write("Loop stopped with " + count_even + " even numbers!");
    </script>    
</html>
```


### Random tips
You can use debugger in javascript file to stop program.  
[Javascript Debugging in Chrome](https://developer.chrome.com/devtools/docs/javascript-debugging)  
Read from csv: [here](http://visual.yantrajaal.com/2013/12/google-charts-from-public-csv-datasets.html), [here](https://stackoverflow.com/questions/14211636/how-to-use-google-chart-with-data-from-a-csv) and [here](http://economistry.com/2013/07/easy-data-visualization-with-google-charts-and-a-csv/)
