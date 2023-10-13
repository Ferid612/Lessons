# Ders 2

https://www.tutorialspoint.com/python/python_data_types.htm
## Data Types 
<table class="w3-table">
  <tbody><tr>
    <td style="width:160px;">Text Type:</td>
    <td><code class="w3-codespan">str</code></td>
  </tr>
  <tr>
    <td>Numeric Types:</td>
    <td><code class="w3-codespan">int</code>, <code class="w3-codespan">float</code>,
    <code class="w3-codespan">complex</code></td>
  </tr>
  <tr>
    <td>Sequence Types:</td>
    <td><code class="w3-codespan">list</code>, <code class="w3-codespan">tuple</code>, 
    <code class="w3-codespan">range</code></td>
  </tr>
  <tr>
    <td>Mapping Type:</td>
    <td><code class="w3-codespan">dict</code></td>
  </tr>
  <tr>
    <td>Set Types:</td>
    <td><code class="w3-codespan">set</code>, <code class="w3-codespan">frozenset</code></td>
  </tr>
  <tr>
    <td>Boolean Type:</td>
    <td><code class="w3-codespan">bool</code></td>
  </tr>
  <tr>
    <td>Binary Types:</td>
    <td><code class="w3-codespan">bytes</code>, <code class="w3-codespan">bytearray</code>, 
    <code class="w3-codespan">memoryview</code></td>
  </tr>
  <tr>
    <td>None Type:</td>
    <td><code class="w3-codespan">NoneType</code></td>
  </tr>
</tbody></table>
<br/>
<br/>

## Nümunələr  
<table id="dtref" class="ws-table-all notranslate">
<tbody><tr>
<th style="min-width:350px">Example</th>
<th>Data Type</th>
<!-- <th style="width:90px">Try it</th> -->
</tr>
<tr>
<td>x = str("Hello World")</td>
<td>str</td>

</tr>
<tr>
<td>x = int(20)</td>
<td>int</td>

</tr>
<tr>
<td>x = float(20.5)</td>
<td>float</td>

</tr>
<tr>
<td>x = complex(1j)</td>
<td>complex</td>

</tr>
<tr>
<td>x = list(("apple", "banana", "cherry"))</td>
<td>list</td>

</tr>
  <tr>
<td>x = tuple(("apple", "banana", "cherry"))</td>
<td>tuple</td>

  </tr>
  <tr>
<td>x = range(6)</td>
<td>range</td>

  </tr>
  <tr>
<td>x = dict(name="John", age=36)</td>
<td>dict</td>

  </tr>
  <tr>
<td>x = set(("apple", "banana", "cherry"))</td>
<td>set</td>

  </tr>
  <tr>
<td>x = frozenset(("apple", "banana", "cherry"))</td>
<td>frozenset</td>

  </tr>
  <tr>
<td>x = bool(5)</td>
<td>bool</td>

  </tr>
  <tr>
<td>x = bytes(5)</td>
<td>bytes</td>

  </tr>
  <tr>
<td>x = bytearray(5)</td>
<td>bytearray</td>

  </tr>
<tr>
<td>x = memoryview(bytes(5))</td>
<td>memoryview</td>

</tr>
</tbody></table>

<br>
<br>

## Nümunələr 3

<div class="w3-code notranslate pythonHigh" style="background-color:white; padding:20px;"><span class="pythoncolor" style="color:black"><span class="pythonnumbercolor" style="color:red">
</span>  x = <span class="pythonnumbercolor" style="color:red">1</span>&nbsp;&nbsp;&nbsp; <span class="commentcolor" style="color:green"># int<br></span>y = <span class="pythonnumbercolor" style="color:red">2.8</span>&nbsp; <span class="commentcolor" style="color:green"># float<br></span>z = 1j&nbsp;&nbsp; <span class="commentcolor" style="color:green"># complex<br></span><br><span class="commentcolor" style="color:green">#convert from int to float:<br></span><span class="pythonnumbercolor" style="color:red">
</span>  a = <span class="pythonkeywordcolor" style="color:mediumblue">float</span>(x)<br><br><span class="commentcolor" style="color:green">#convert from float to int:<br></span><span class="pythonnumbercolor" style="color:red">
</span>  b = <span class="pythonkeywordcolor" style="color:mediumblue">int</span>(y)<br><br><span class="commentcolor" style="color:green">#convert from int to complex:<br></span>c = <span class="pythonkeywordcolor" style="color:mediumblue">complex</span>(x)<br><br><span class="pythonkeywordcolor" style="color:mediumblue">print</span>(a)<br><span class="pythonkeywordcolor" style="color:mediumblue">print</span>(b)<br><span class="pythonnumbercolor" style="color:red">
</span>  <span class="pythonkeywordcolor" style="color:mediumblue">print</span>(c)<br><br><span class="pythonkeywordcolor" style="color:mediumblue">print</span>(<span class="pythonkeywordcolor" style="color:mediumblue">type</span>(a))<br><span class="pythonkeywordcolor" style="color:mediumblue">print</span>(<span class="pythonkeywordcolor" style="color:mediumblue">type</span>(b))<br><span class="pythonnumbercolor" style="color:red">
</span>  <span class="pythonkeywordcolor" style="color:mediumblue">print</span>(<span class="pythonkeywordcolor" style="color:mediumblue">type</span>(c)) </span>
<a href="https://www.w3schools.com/python/trypython.asp?filename=demo_numbers_convert"> TRY </a>
</div>
<br>
<br>
<br>

<h1>Random Function</h1>
<div style="color:black; background-color:white; padding:20px;">
<div class="w3-code notranslate pythonHigh"><span class="pythoncolor" style="color:black"><span class="pythonnumbercolor" style="color:red">
</span>  <span class="pythonkeywordcolor" style="color:mediumblue">import</span> random<br><br><span class="pythonkeywordcolor" style="color:mediumblue">print</span>(random.randrange(<span class="pythonnumbercolor" style="color:red">1</span>, <span class="pythonnumbercolor" style="color:red">10</span>)) </span></div>
</div>


<br>
<br>
<br>

# STRİNGS

<div class="w3-code notranslate pythonHigh" style="background-color:white; padding:20px;"><span class="pythoncolor" style="color:black">
<span class="pythonkeywordcolor" style="color:mediumblue">print</span>(<span class="pythonstringcolor" style="color:brown">"Hello"</span>)<br>
<span class="pythonkeywordcolor" style="color:mediumblue">print</span>(<span class="pythonstringcolor" style="color:brown">'Hello'</span>)<span class="pythonnumbercolor" style="color:red">
</span> </span></div>

<br>
<h2>Multiline Strings</h2>
<div class="w3-code notranslate pythonHigh" style="background-color:white; padding:20px;"><span class="pythoncolor" style="color:black"><span class="pythonnumbercolor" style="color:red">
</span>  a = <span class="pythonstringcolor" style="color:brown">""</span><span class="pythonstringcolor" style="color:brown">"Lorem ipsum dolor sit amet,<br>consectetur adipiscing elit,<br>sed do 
  eiusmod tempor incididunt<br>ut labore et dolore magna aliqua."</span><span class="pythonstringcolor" style="color:brown">""</span><br><span class="pythonkeywordcolor" style="color:mediumblue">print</span>(a) </span></div>
<br>
<br>

<h2>Strings are Arrays</h2>
<div style="background-color:white; padding:20px;" class="w3-code notranslate pythonHigh"><span class="pythoncolor" style="color:black">
a = <span class="pythonstringcolor" style="color:brown">"Hello, World!"</span><br>
<span class="pythonkeywordcolor" style="color:mediumblue">print</span>(a[<span class="pythonnumbercolor" style="color:red">1</span>])<span class="pythonnumbercolor" style="color:red">
</span> </span></div>

<br>
<br>
<h2>Looping Through a String</h2>
<div style="background-color:white; padding:20px;" class="w3-code notranslate pythonHigh"><span class="pythoncolor" style="color:black"><span class="pythonnumbercolor" style="color:red">
</span>  <span class="pythonkeywordcolor" style="color:mediumblue">for</span> x <span class="pythonkeywordcolor" style="color:mediumblue">in</span> <span class="pythonstringcolor" style="color:brown">"banana"</span>:<br>&nbsp; <span class="pythonkeywordcolor" style="color:mediumblue">print</span>(x)<span class="pythonnumbercolor" style="color:red">
</span> </span></div>

<br>
<br>
<h2>String Length</h2>
<div style="background-color:white; padding:20px;" class="w3-code notranslate pythonHigh"><span class="pythoncolor" style="color:black">
a = <span class="pythonstringcolor" style="color:brown">"Hello, World!"</span><br>
<span class="pythonkeywordcolor" style="color:mediumblue">print</span>(<span class="pythonkeywordcolor" style="color:mediumblue">len</span>(a))<span class="pythonnumbercolor" style="color:red">
</span> </span></div>

<br>
<br>
<h2>Check String</h2>
<div style="background-color:white; padding:20px;" class="w3-code notranslate pythonHigh"><span class="pythoncolor" style="color:black"><span class="pythonnumbercolor" style="color:red">
</span>  txt = <span class="pythonstringcolor" style="color:brown">"The best things in life are free!"</span><br><span class="pythonkeywordcolor" style="color:mediumblue">print</span>(<span class="pythonstringcolor" style="color:brown">"free"</span> <span class="pythonkeywordcolor" style="color:mediumblue">in</span> txt)<br><span class="pythonnumbercolor" style="color:red">
</span> </span></div>


<br>
<br>
<div style="background-color:white; padding:20px;" class="w3-code notranslate pythonHigh"><span class="pythoncolor" style="color:black"><span class="pythonnumbercolor" style="color:red">
</span>  txt = <span class="pythonstringcolor" style="color:brown">"The best things in life are free!"</span><br><span class="pythonkeywordcolor" style="color:mediumblue">print</span>(<span class="pythonstringcolor" style="color:brown">"expensive"</span> not <span class="pythonkeywordcolor" style="color:mediumblue">in</span> txt)<span class="pythonnumbercolor" style="color:red">
</span>   </span></div>

<br>
<br>
<br>
<h1>Python - <span class="color_h1">Slicing Strings</span></h1>
<h2>Slicing</h2>
<div style="background-color:white; padding:20px;" class="w3-code notranslate pythonHigh"><span class="pythoncolor" style="color:black">
b = <span class="pythonstringcolor" style="color:brown">"Hello, World!"</span><br><span class="pythonnumbercolor" style="color:red">
</span>  <span class="pythonkeywordcolor" style="color:mediumblue">print</span>(b[<span class="pythonnumbercolor" style="color:red">2</span>:<span class="pythonnumbercolor" style="color:red">5</span>])<span class="pythonnumbercolor" style="color:red">
</span> </span></div>

<br>
<br>
<h2>Slice From the Start</h2>
<div style="background-color:white; padding:20px;" class="w3-code notranslate pythonHigh"><span class="pythoncolor" style="color:black">
b = <span class="pythonstringcolor" style="color:brown">"Hello, World!"</span><br><span class="pythonnumbercolor" style="color:red">
</span>  <span class="pythonkeywordcolor" style="color:mediumblue">print</span>(b[:<span class="pythonnumbercolor" style="color:red">5</span>])<span class="pythonnumbercolor" style="color:red">
</span> </span></div>

<br>
<br>
<h2>Slice To the End</h2>
<div style="background-color:white; padding:20px;" class="w3-code notranslate pythonHigh"><span class="pythoncolor" style="color:black">
b = <span class="pythonstringcolor" style="color:brown">"Hello, World!"</span><br><span class="pythonnumbercolor" style="color:red">
</span>  <span class="pythonkeywordcolor" style="color:mediumblue">print</span>(b[<span class="pythonnumbercolor" style="color:red">2</span>:])<span class="pythonnumbercolor" style="color:red">
</span> </span></div>

<br>
<br>

<h2>Negative Indexing</h2>
<div style="background-color:white; padding:20px;" class="w3-code notranslate pythonHigh"><span class="pythoncolor" style="color:black">
b = <span class="pythonstringcolor" style="color:brown">"Hello, World!"</span><br><span class="pythonnumbercolor" style="color:red">
</span>  <span class="pythonkeywordcolor" style="color:mediumblue">print</span>(b[-<span class="pythonnumbercolor" style="color:red">5</span>:-<span class="pythonnumbercolor" style="color:red">2</span>])<span class="pythonnumbercolor" style="color:red">
</span> </span></div>

<br>
<br>
<br>
<br>

<h1>Python - <span class="color_h1">Modify Strings</span></h1>

<h2>Upper Case</h2>
<div style="background-color:white; padding:20px;" class="w3-code notranslate pythonHigh"><span class="pythoncolor" style="color:black">
a = <span class="pythonstringcolor" style="color:brown">"Hello, World!"</span><br>
<span class="pythonkeywordcolor" style="color:mediumblue">print</span>(a.upper())<span class="pythonnumbercolor" style="color:red">
</span> </span></div>

<br>
<br>

<h2>Lower Case</h2>
<div style="background-color:white; padding:20px;" class="w3-code notranslate pythonHigh"><span class="pythoncolor" style="color:black">
a = <span class="pythonstringcolor" style="color:brown">"Hello, World!"</span><br>
<span class="pythonkeywordcolor" style="color:mediumblue">print</span>(a.lower())<span class="pythonnumbercolor" style="color:red">
</span> </span></div>

<br>
<br>
<h2>Remove Whitespace</h2>
<div style="background-color:white; padding:20px;" class="w3-code notranslate pythonHigh"><span class="pythoncolor" style="color:black">
a = <span class="pythonstringcolor" style="color:brown">" Hello, World! "</span><br>
<span class="pythonkeywordcolor" style="color:mediumblue">print</span>(a.strip()) <span class="commentcolor" style="color:green"># returns "Hello, World!"
 </span></span></div>

<br>
<br>

 <h2>Replace String</h2>
<div style="background-color:white; padding:20px;" class="w3-code notranslate pythonHigh">
 <span class="pythoncolor" style="color:black">
a = <span class="pythonstringcolor" style="color:brown">"Hello, World!"</span><br>
<span class="pythonkeywordcolor" style="color:mediumblue">print</span>(a.replace(<span class="pythonstringcolor" style="color:brown">"H"</span>, <span class="pythonstringcolor" style="color:brown">"J"</span>))<span class="pythonnumbercolor" style="color:red">
</span> </span></div>
<br>
<br>


 <h2>Split String</h2>

<div  style="background-color:white; padding:20px;" class="w3-code notranslate pythonHigh"><span class="pythoncolor" style="color:black">
a = <span class="pythonstringcolor" style="color:brown">"Hello, World!"</span><br>
<span class="pythonkeywordcolor" style="color:mediumblue">print</span>(a.split(<span class="pythonstringcolor" style="color:brown">","</span>)) <span class="commentcolor" style="color:green"># 
  returns ['Hello', ' World!']
 </span></span></div>
<br>
<br>


 <h2>String Concatenation</h2>
 <div  style="background-color:white; padding:20px;" class="w3-code notranslate pythonHigh"><span class="pythoncolor" style="color:black"><span class="pythonnumbercolor" style="color:red">
</span>  a = <span class="pythonstringcolor" style="color:brown">"Hello"</span><br>b = <span class="pythonstringcolor" style="color:brown">"World"</span><br>c = a + b<br>
<span class="pythonkeywordcolor" style="color:mediumblue">print</span>(c)<span class="pythonnumbercolor" style="color:red">
</span> </span></div>



<br>
<br>
<br>
<h2>String Format</h2>
<div class="w3-example w3-pale-red" style="padding: 8px 20px;
    margin: 24px -20px;
    box-shadow: none!important;     color: #000!important;
    background-color: #ffdddd!important;">
<div class="w3-code notranslate pythonHigh w3-border-red"><span class="pythoncolor" style="color:black"><span class="pythonnumbercolor" style="color:red">
</span>  age = <span class="pythonnumbercolor" style="color:red">36</span><br>txt = <span class="pythonstringcolor" style="color:brown">"My name is John, I am "</span> + age<br><span class="pythonkeywordcolor" style="color:mediumblue">print</span>(txt)<span class="pythonnumbercolor" style="color:red">
</span> </span></div>
<a target="_blank" class="w3-btn w3-margin-bottom" href="trypython.asp?filename=demo_string_format_error">Try it Yourself »</a>
</div>


<br>
<br>
<h2 _msttexthash="94211" _msthash="833">Example 1</h2>
<div  style="background-color:white; padding:20px;"  class="w3-code notranslate pythonHigh"><span class="pythoncolor" style="color:black"><span class="pythonnumbercolor" style="color:red">
</span>  age = <span class="pythonnumbercolor" style="color:red">36</span><br>txt = <span class="pythonstringcolor" style="color:brown">"My name is John, and I am {}"</span><br><span class="pythonkeywordcolor" style="color:mediumblue">print</span>(txt.<span class="pythonkeywordcolor" style="color:mediumblue">format</span>(age))<span class="pythonnumbercolor" style="color:red">
</span> </span></div>


<br>
<br>

<h2 _msttexthash="94211" _msthash="833">Example 2</h2>
<div  style="background-color:white; padding:20px;"  class="w3-code notranslate pythonHigh"><span class="pythoncolor" style="color:black"><span class="pythonnumbercolor" style="color:red">
</span>  quantity = <span class="pythonnumbercolor" style="color:red">3</span><br>itemno = <span class="pythonnumbercolor" style="color:red">567</span><br>price = <span class="pythonnumbercolor" style="color:red">49.95</span><br>myorder = <span class="pythonstringcolor" style="color:brown">"I want {} 
  pieces of item {} for {} dollars."</span><br><span class="pythonkeywordcolor" style="color:mediumblue">print</span>(myorder.<span class="pythonkeywordcolor" style="color:mediumblue">format</span>(quantity, <span class="pythonnumbercolor" style="color:red">
</span>  itemno, price))<span class="pythonnumbercolor" style="color:red">
</span> </span></div>


<br>
<br>
<h2 _msttexthash="94211" _msthash="833">Example 3</h2>

<div  style="background-color:white; padding:20px;"  class="w3-code notranslate pythonHigh"><span class="pythoncolor" style="color:black"><span class="pythonnumbercolor" style="color:red">
</span>  quantity = <span class="pythonnumbercolor" style="color:red">3</span><br>itemno = <span class="pythonnumbercolor" style="color:red">567</span><br>price = <span class="pythonnumbercolor" style="color:red">49.95</span><br>myorder = <span class="pythonstringcolor" style="color:brown">"I want to pay {2} 
  dollars for {0} pieces of item {1}."</span><br><span class="pythonkeywordcolor" style="color:mediumblue">print</span>(myorder.<span class="pythonkeywordcolor" style="color:mediumblue">format</span>(quantity, <span class="pythonnumbercolor" style="color:red">
</span>  itemno, price))<span class="pythonnumbercolor" style="color:red">
</span> </span></div>

<br>
<br>


<h1>Python - <span class="color_h1">Escape Characters</span></h1>

<h4>Error</h4>
<div  style="background-color:white; padding:20px;"  class="w3-code notranslate pythonHigh w3-border-red"><span class="pythoncolor" style="color:black">
txt = <span class="pythonstringcolor" style="color:brown">"We are the so-called "</span>Vikings<span class="pythonstringcolor" style="color:brown">" from the north."</span><span class="pythonnumbercolor" style="color:red">
</span> </span></div>


<br>
<br>
<h3>Example</h3>
<div  style="background-color:white; padding:20px;"  class="w3-code notranslate pythonHigh"><span class="pythoncolor" style="color:black">
txt = <span class="pythonstringcolor" style="color:brown">"We are the so-called \"</span>Vikings\<span class="pythonstringcolor" style="color:brown">" from the north."</span><span class="pythonnumbercolor" style="color:red">
</span> </span></div>
<br>
<br>


<table style="    margin-top: 1.2em;
    margin-bottom: 1.2em;
    font-size: 15px;" class="ws-table-all notranslate">
<tbody><tr>
  <th width="25%">Code</th>
  <th>Result</th>
</tr>
<tr>
  <td>\'</td>
  <td>Single Quote</td>

</tr>
<tr>
  <td>\\</td>
  <td>Backslash</td>

</tr>
<tr>
  <td>\n</td>
  <td>New Line</td>

</tr>
<tr>
  <td>\r</td>
  <td>Carriage Return</td>

</tr>
<tr>
  <td>\t</td>
  <td>Tab</td>

</tr>
<tr>
  <td>\b</td>
  <td>Backspace</td>

</tr>
<tr>
  <td>\f</td>
  <td>Form Feed</td>
<td></td>
</tr>
<tr>
  <td>\ooo</td>
  <td>Octal value</td>

</tr>
<tr>
  <td>\xhh</td>
  <td>Hex value</td>

</tr>
</tbody></table>

<br>
<br>
<br>
<h1><a href="https://www.w3schools.com/python/python_strings_methods.asp"> String Methods Link <-- Click me </a></h1>


<br>
<br>


<h1><a href ="https://www.pythonmorsels.com/string-methods/#endswith">Important String Methods</a></h1>

<table class="table table-bordered">
<thead>
<tr>
<th>Method</th>
<th>Related Methods</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#join"><code>join</code></a></td>
<td></td>
<td>Join iterable of strings by a separator</td>
</tr>
<tr>
<td><a href="#split"><code>split</code></a></td>
<td><code>rsplit</code></td>
<td>Split (on whitespace by default) into list of strings</td>
</tr>
<tr>
<td><a href="#replace"><code>replace</code></a></td>
<td></td>
<td>Replace all copies of one substring with another</td>
</tr>
<tr>
<td><a href="#strip"><code>strip</code></a></td>
<td><code>rstrip</code> &amp; <code>lstrip</code></td>
<td>Remove whitespace from the beginning and end</td>
</tr>
<tr>
<td><a href="#casefold"><code>casefold</code></a></td>
<td><code>lower</code> &amp; <code>upper</code></td>
<td>Return a case-normalized version of the string</td>
</tr>
<tr>
<td><a href="#startswith"><code>startswith</code></a></td>
<td></td>
<td>Check if string starts with 1 or more other strings</td>
</tr>
<tr>
<td><a href="#endswith"><code>endswith</code></a></td>
<td></td>
<td>Check if string ends with 1 or more other strings</td>
</tr>
<tr>
<td><a href="#splitlines"><code>splitlines</code></a></td>
<td></td>
<td>Split into a list of lines</td>
</tr>
<tr>
<td><a href="#format"><code>format</code></a></td>
<td></td>
<td>Format the string (consider an f-string before this)</td>
</tr>
<tr>
<td><a href="#count"><code>count</code></a></td>
<td></td>
<td>Count how many times a given substring occurs</td>
</tr>
<tr>
<td><a href="#removeprefix"><code>removeprefix</code></a></td>
<td></td>
<td>Remove the given prefix</td>
</tr>
<tr>
<td><a href="#removesuffix"><code>removesuffix</code></a></td>
<td></td>
<td>Remove the given suffix</td>
</tr>
</tbody>
</table>

https://www.crio.do/blog/string-methods-in-python/
<br>
<br>




<h1 class="__web-inspector-hide-shortcut__">Python <span class="color_h1">Lists</span></h1>



<table class="ws-table-all notranslate">
<tbody><tr>
<th>Method</th>
<th>Description</th>
</tr>
<tr><td><a href="ref_list_append.asp">append()</a></td><td>Adds an element at 
  the end of the list</td></tr>
<tr><td><a href="ref_list_clear.asp">clear()</a></td><td>Removes all the 
  elements from the list</td></tr>
<tr><td><a href="ref_list_copy.asp">copy()</a></td><td>Returns a copy of the 
  list</td></tr>
<tr><td><a href="ref_list_count.asp">count()</a></td><td>Returns the number of 
  elements with the specified value</td></tr>
<tr><td><a href="ref_list_extend.asp">extend()</a></td><td>Add the elements of a 
  list (or any iterable), to the end of the current list</td></tr>
<tr><td><a href="ref_list_index.asp">index()</a></td><td>Returns the index of 
  the first element with the specified value</td></tr>
<tr><td><a href="ref_list_insert.asp">insert()</a></td><td>Adds an element at 
  the specified position</td></tr>
<tr><td><a href="ref_list_pop.asp">pop()</a></td><td>Removes the element at the 
  specified position</td></tr>
<tr><td><a href="ref_list_remove.asp">remove()</a></td><td>Removes the first 
  item with the specified value</td></tr>
<tr><td><a href="ref_list_reverse.asp">reverse()</a></td><td>Reverses the order 
  of the list</td></tr>
<tr><td><a href="ref_list_sort.asp">sort()</a></td><td>Sorts the list</td></tr>
</tbody></table>




<br>
<br>
<h3>
<ul>
<li><strong>List</strong> is a collection which is ordered and changeable. Allows duplicate members.</li>
<br>

<li><strong><a href="python_tuples.asp">Tuple</a></strong> is a collection which is ordered and unchangeable. Allows duplicate members.</li>
<br>

<li><strong><a href="python_sets.asp">Set</a></strong> is a collection which is unordered, 
unchangeable*, and unindexed. No duplicate members.</li>

<br>

<li><strong><a href="python_dictionaries.asp">Dictionary</a></strong> is a collection which is ordered** 
and changeable. No duplicate members.</li>
</ul>

<br>

</h3>

<br>
<br>




<h1 class="__web-inspector-hide-shortcut__">Python <span class="color_h1">Tuple</span></h1>


<table style="    -webkit-text-size-adjust: 100%;
    font-family: Verdana,sans-serif;
    font-size: 15px;
    line-height: 1.5;
    color: #white!important;
    box-sizing: inherit;
    border-collapse: collapse;
    border-spacing: 0;
    width: 100%;
    display: table;
    border: 1px solid #ccc;
    margin: 20px 0;"class="ws-table-all notranslate">
<tbody><tr>
<th style="width:20%">Method</th>
<th>Description</th>
</tr>
<tr><td><a href="ref_tuple_count.asp">count()</a></td><td>Returns the number of times a specified value occurs in a tuple</td></tr>
<tr><td><a href="ref_tuple_index.asp">index()</a></td><td>Searches the tuple for a specified value and returns the position of where it was found</td></tr>
</tbody></table>

<br>
<br>
<br>
<h1 class="__web-inspector-hide-shortcut__">Python <span class="color_h1">SET</span></h1>



<table class="ws-table-all notranslate">
<tbody><tr>
<th>Method</th>
<th>Description</th>
</tr>
<tr><td><a href="ref_set_add.asp">add()</a></td><td>Adds an element to the 
  set</td></tr>
<tr><td><a href="ref_set_clear.asp">clear()</a></td><td>Removes all the 
  elements from the set</td></tr>
<tr><td><a href="ref_set_copy.asp">copy()</a></td><td>Returns a copy of the set</td></tr>
  <tr>
    <td><a href="ref_set_difference.asp">difference()</a></td><td>Returns a set 
    containing the difference between two or more sets</td>
  </tr>
  <tr>
    <td><a href="ref_set_difference_update.asp">difference_update()</a></td><td>Removes the 
    items in this set that are also included in another, specified set</td>
  </tr>
<tr><td><a href="ref_set_discard.asp">discard()</a></td><td>Remove the specified 
  item</td></tr>
  <tr>
    <td><a href="ref_set_intersection.asp">intersection()</a></td><td>Returns a set, 
    that is the intersection of two other sets</td>
  </tr>
<tr><td><a href="ref_set_intersection_update.asp">intersection_update()</a></td><td>
  Removes the items in this set that are not present in other, specified set(s)</td></tr>
  <tr>
    <td><a href="ref_set_isdisjoint.asp">isdisjoint()</a></td><td>Returns whether 
    two sets have a intersection or not</td>
  </tr>
  <tr>
    <td><a href="ref_set_issubset.asp">issubset()</a></td><td>Returns whether 
    another set contains this set or not</td>
  </tr>
<tr><td><a href="ref_set_issuperset.asp">issuperset()</a></td><td>Returns whether 
  this set contains another set or not</td></tr>
<tr><td><a href="ref_set_pop.asp">pop()</a></td><td>Removes an element from the 
  set</td></tr>
<tr><td><a href="ref_set_remove.asp">remove()</a></td><td>Removes the specified element</td></tr>
  <tr>
    <td><a href="ref_set_symmetric_difference.asp">symmetric_difference()</a></td><td>Returns 
    a set with the symmetric differences of two sets</td>
  </tr>
<tr><td><a href="ref_set_symmetric_difference_update.asp">symmetric_difference_update()</a></td><td>
  inserts the symmetric differences from this set and another</td></tr>
  <tr>
    <td><a href="ref_set_union.asp">union()</a></td><td>Return a set containing 
    the union of sets</td>
  </tr>
<tr><td><a href="ref_set_update.asp">update()</a></td><td>Update the set with the 
  union of this set and others</td></tr>
</tbody></table>

<br>
<br>
<br>
<h1 class="__web-inspector-hide-shortcut__">Python <span class="color_h1">DICTIONARY</span></h1>




<table class="ws-table-all notranslate">
<tbody><tr>
<th>Method</th>
<th>Description</th>
</tr>
<tr><td><a href="ref_dictionary_clear.asp">clear()</a></td><td>Removes all the elements from the dictionary</td></tr>
<tr><td><a href="ref_dictionary_copy.asp">copy()</a></td><td>Returns a copy of the dictionary</td></tr>
<tr><td><a href="ref_dictionary_fromkeys.asp">fromkeys()</a></td><td>Returns a dictionary with the specified keys and value</td></tr>
<tr><td><a href="ref_dictionary_get.asp">get()</a></td><td>Returns the value of the specified key</td></tr>
<tr><td><a href="ref_dictionary_items.asp">items()</a></td><td>Returns a list containing a tuple for each key value pair</td></tr>
<tr><td><a href="ref_dictionary_keys.asp">keys()</a></td><td>Returns a list containing the dictionary's keys</td></tr>
<tr><td><a href="ref_dictionary_pop.asp">pop()</a></td><td>Removes the element with the specified key</td></tr>
<tr><td><a href="ref_dictionary_popitem.asp">popitem()</a></td><td>Removes the last 
  inserted key-value pair</td></tr>
<tr><td><a href="ref_dictionary_setdefault.asp">setdefault()</a></td><td>Returns the value of the specified key. If the key does not exist: insert the key, with the specified value</td></tr>
<tr><td><a href="ref_dictionary_update.asp">update()</a></td><td>Updates the dictionary with the specified key-value pairs</td></tr>
<tr><td><a href="ref_dictionary_values.asp">values()</a></td><td>Returns a list of all the values in the dictionary</td></tr>
</tbody></table>