
 a = b = c = 300
<br> list_a = [2,3,4]
<br> a,b,c = list_a

<br> age = 1
<br> Age = 2
<br> aGe = 3
<br> AGE = 4
<br> a_g_e = 5
<br> _age = 6
<br> age_ = 7
<br> _AGE_ = 8

<br> [A-Z]  [a-z] [0-9]  _ 
<br> print(age, Age, aGe, AGE, a_g_e, _age, age_, _AGE_)


### camelCase
### PascalCase
### snake_case
### kabab-case
<br><br><br>



<div class="table-responsive">
<table class="table table-hover">
<thead>
<tr>
<th>Python    Keywords</th>
<th>&nbsp;</th>
<th>&nbsp;</th>
<th>&nbsp;</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>False</code></td>
<td><code>def</code></td>
<td><code>if</code></td>
<td><code>raise</code></td>
</tr>
<tr>
<td><code>None</code></td>
<td><code>del</code></td>
<td><code>import</code></td>
<td><code>return</code></td>
</tr>
<tr>
<td><code>True</code></td>
<td><code>elif</code></td>
<td><code>in</code></td>
<td><code>try</code></td>
</tr>
<tr>
<td><code>and</code></td>
<td><code>else</code></td>
<td><code>is</code></td>
<td><code>while</code></td>
</tr>
<tr>
<td><code>as</code></td>
<td><code>except</code></td>
<td><code>lambda</code></td>
<td><code>with</code></td>
</tr>
<tr>
<td><code>assert</code></td>
<td><code>finally</code></td>
<td><code>nonlocal</code></td>
<td><code>yield</code></td>
</tr>
<tr>
<td><code>break</code></td>
<td><code>for</code></td>
<td><code>not</code></td>
<td></td>
</tr>
<tr>
<td><code>class</code></td>
<td><code>from</code></td>
<td><code>or</code></td>
<td></td>
</tr>
<tr>
<td><code>continue</code></td>
<td><code>global</code></td>
<td><code>pass</code></td>
<td></td>
</tr>
</tbody>
</table>
</div>

<br>

## help("keywords")

<br><br>

###  >>> 2 == "2" <br> False

<br><br><br>


5 < "7" <br>
Traceback (most recent call last):
    ... <br>
TypeError: '<' not supported between instances of 'int' and 'str'


<h3> 
<br><br><br>

 x = 1.1 + 2.2 <br>
 x == 3.3 <br>
False

<br><br><br>
 1.1 + 2.2 <br>
3.3000000000000003


<br>
from math import isclose

x = 1.1 + 2.2

isclose(x, 3.3)

</h3>

<br><br><br>


<div class="highlight python repl" len="906"><span class="repl-toggle" title="Toggle REPL prompts and output" len="12">&gt;&gt;&gt;</span><pre len="811"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="nb">ord</span><span class="p">(</span><span class="s2">"A"</span><span class="p">)</span>
<span class="go">65</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">ord</span><span class="p">(</span><span class="s2">"a"</span><span class="p">)</span>
<span class="go">97</span>

<span class="gp">&gt;&gt;&gt; </span><span class="s2">"A"</span> <span class="o">==</span> <span class="s2">"a"</span>
<span class="go">False</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s2">"A"</span> <span class="o">&gt;</span> <span class="s2">"a"</span>
<span class="go">False</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s2">"A"</span> <span class="o">&lt;</span> <span class="s2">"a"</span>
<span class="go">True</span>
</code></pre></div>


<br><br><br>


<div class="highlight python repl" len="615"><span class="repl-toggle" title="Toggle REPL prompts and output" len="12">&gt;&gt;&gt;</span><pre len="520"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="s2">"Hello"</span> <span class="o">&gt;</span> <span class="s2">"HellO"</span>
<span class="go">True</span>

<span class="gp">&gt;&gt;&gt; </span><span class="nb">ord</span><span class="p">(</span><span class="s2">"o"</span><span class="p">)</span>
<span class="go">111</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">ord</span><span class="p">(</span><span class="s2">"O"</span><span class="p">)</span>
<span class="go">79</span>
</code></pre></div>

<br><br><br>


<div class="highlight python repl" len="2573"><span class="repl-toggle" title="Toggle REPL prompts and output" len="12">&gt;&gt;&gt;</span><pre len="2478"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="p">[</span><span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">]</span> <span class="o">==</span> <span class="p">[</span><span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">]</span>
<span class="go">True</span>
<span class="gp">&gt;&gt;&gt; </span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">)</span> <span class="o">==</span> <span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">)</span>
<span class="go">True</span>

<span class="gp">&gt;&gt;&gt; </span><span class="p">[</span><span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="mi">7</span><span class="p">]</span> <span class="o">&lt;</span> <span class="p">[</span><span class="mi">7</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">]</span>
<span class="go">True</span>
<span class="gp">&gt;&gt;&gt; </span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="mi">7</span><span class="p">)</span> <span class="o">&lt;</span> <span class="p">(</span><span class="mi">7</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">)</span>
<span class="go">True</span>

<span class="gp">&gt;&gt;&gt; </span><span class="p">[</span><span class="mi">4</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">2</span><span class="p">]</span> <span class="o">&lt;</span> <span class="p">[</span><span class="mi">4</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">2</span><span class="p">]</span>
<span class="go">False</span>
<span class="gp">&gt;&gt;&gt; </span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span> <span class="o">&lt;</span> <span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span>
<span class="go">False</span>
</code></pre></div>

<br><br><br>

<div class="highlight python repl" len="1896"><span class="repl-toggle" title="Toggle REPL prompts and output" len="12">&gt;&gt;&gt;</span><pre len="1801"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="p">[</span><span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">]</span> <span class="o">==</span> <span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">)</span>
<span class="go">False</span>
<span class="gp">&gt;&gt;&gt; </span><span class="p">[</span><span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">]</span> <span class="o">!=</span> <span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">)</span>
<span class="go">True</span>

<span class="gp">&gt;&gt;&gt; </span><span class="p">[</span><span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">]</span> <span class="o">&gt;</span> <span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">)</span>
<span class="gt">Traceback (most recent call last):</span>
<span class="w">    </span><span class="o">...</span>
<span class="gr">TypeError</span>: <span class="n">'&gt;' not supported between instances of 'list' and 'tuple'</span>

<span class="gp">&gt;&gt;&gt; </span><span class="p">[</span><span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">]</span> <span class="o">&lt;=</span> <span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">)</span>
<span class="gt">Traceback (most recent call last):</span>
<span class="w">    </span><span class="o">...</span>
<span class="gr">TypeError</span>: <span class="n">'&lt;=' not supported between instances of 'list' and 'tuple'</span>
</code></pre></div>


<br><br><br>



<pre len="2081"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="p">[</span><span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="mi">7</span><span class="p">]</span> <span class="o">&lt;</span> <span class="p">[</span><span class="mi">8</span><span class="p">]</span>
<span class="go">True</span>
<span class="gp">&gt;&gt;&gt; </span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="mi">7</span><span class="p">)</span> <span class="o">&lt;</span> <span class="p">(</span><span class="mi">8</span><span class="p">,)</span>
<span class="go">True</span>

<span class="gp">&gt;&gt;&gt; </span><span class="p">[</span><span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="mi">7</span><span class="p">]</span> <span class="o">==</span> <span class="p">[</span><span class="mi">5</span><span class="p">]</span>
<span class="go">False</span>
<span class="gp">&gt;&gt;&gt; </span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="mi">7</span><span class="p">)</span> <span class="o">==</span> <span class="p">(</span><span class="mi">5</span><span class="p">,)</span>
<span class="go">False</span>

<span class="gp">&gt;&gt;&gt; </span><span class="p">[</span><span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="mi">7</span><span class="p">]</span> <span class="o">&gt;</span> <span class="p">[</span><span class="mi">5</span><span class="p">]</span>
<span class="go">True</span>
<span class="gp">&gt;&gt;&gt; </span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="mi">7</span><span class="p">)</span> <span class="o">&gt;</span> <span class="p">(</span><span class="mi">5</span><span class="p">,)</span>
<span class="go">True</span>
</code></pre>

<br><br><br>

<h2> Instance İşləmi</h2>
<h3>
<br> isinstance(number, int)
<br> isinstance("string", str)
<br> isinstance(float.value, float)
<h3>
<br><br><br>



<pre len="1258"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="n">number</span> <span class="o">=</span> <span class="mi">42</span>

<span class="gp">&gt;&gt;&gt; </span><span class="n">validation_conditions</span> <span class="o">=</span> <span class="p">(</span>
<span class="gp">... </span>    <span class="nb">isinstance</span><span class="p">(</span><span class="n">number</span><span class="p">,</span> <span class="nb">int</span><span class="p">),</span>
<span class="gp">... </span>    <span class="n">number</span> <span class="o">%</span> <span class="mi">2</span> <span class="o">==</span> <span class="mi">0</span><span class="p">,</span>
<span class="gp">... </span><span class="p">)</span>

<span class="gp">&gt;&gt;&gt; </span><span class="nb">all</span><span class="p">(</span><span class="n">validation_conditions</span><span class="p">)</span>
<span class="go">True</span>

<span class="gp">&gt;&gt;&gt; </span><span class="nb">callable</span><span class="p">(</span><span class="n">number</span><span class="p">)</span>
<span class="go">False</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">callable</span><span class="p">(</span><span class="nb">print</span><span class="p">)</span>
<span class="go">True</span>
</code></pre>



<br><br><br>
#  Logical Operator Details

<div class="table-responsive" len="733">
<table class="table table-hover" len="690">
<thead len="73">
<tr len="62">
<th len="8" lang="tr" style="">Operatör</th>
<th len="17" lang="tr" style="">Örnek İfade</th>
<th len="6" lang="tr">Sonuç</th>
</tr>
</thead>
<tbody len="584">
<tr len="184">
<td len="16"><code len="3">and</code></td>
<td len="20"><code len="7">x and y</code></td>
<td len="117"><font lang="tr">• <code len="4">True</code> <code len="1">x</code> hem de <code len="1">y</code> Doğru ise <code len="4">True</code></font><br len="0"><font lang="tr">• <code len="5">False</code></font></td>
</tr>
<tr len="182">
<td len="15"><code len="2">or</code></td>
<td len="19"><code len="6">x or y</code></td>
<td len="117"><font lang="tr">• <code len="1">x</code> veya <code len="1">y</code> Doğru ise <code len="4">True</code> <code len="4">True</code></font><br len="0"><font lang="tr">• <code len="5">False</code></font></td>
</tr>
<tr len="187">
<td len="16"><code len="3">not</code></td>
<td len="18"><code len="5">not x</code></td>
<td len="122"><font lang="tr" style="">• <code len="1">x</code> <code len="5">False</code> ise <code len="4">True</code></font><br len="0"><font lang="tr" style="">• <code len="1">x</code> <code len="4">True</code> ise <code len="5">False</code></font></td>
</tr>
</tbody>
</table>
</div>


<br><br><br>
<br><br><br>


# Hansı ifadələr False qaytarır 
<blockquote len="928">
<p len="437"><font lang="tr">Varsayılan olarak, sınıfı <code len="5">False</code> döndüren bir __bool__() yöntemi veya nesneyle birlikte çağrıldığında sıfır döndüren bir <a href="https://docs.python.org/3/reference/datamodel.html#object.__bool__" len="23"><code>__bool__()</code></a><a href="https://docs.python.org/3/reference/datamodel.html#object.__len__" len="22"><code>__len__()</code></a> yöntemi tanımlamadığı sürece nesne true olarak kabul edilir. </font><font lang="tr">Yanlış olarak kabul edilen yerleşik nesnelerin çoğu şunlardır:</font></p>
<ul len="374">
<li len="72"><font lang="tr" style="" len="87">False olarak tanımlanan sabitler: <code len="4">None</code> ve <code len="5">False</code></font>.</li>
<li len="129" lang="tr" style="">herhangi bir sayısal türde sıfır: <code len="1">0</code>0, 0,0, <code len="2">0j</code>, <code len="10">Decimal(0)</code>(0), <code len="14">Fraction(0, 1)</code> <code len="3">0.0</code></li>
<li len="142" lang="tr" style="">Boş diziler ve koleksiyonlar: '<code len="2">''</code>, (), <code len="2">[]</code>, <code len="2">{}</code>, <code len="5">set()</code>(), <code len="8">range(0)</code> <code len="2">()</code></li>
</ul>
<p len="90">(<a href="https://docs.python.org/3/library/stdtypes.html#truth-value-testing" len="6" lang="tr">Kaynak</a>)</p>
</blockquote>


<br><br><br>
# Logical Operatorlar Nümunə 1
<pre len="988"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="nb">bool</span><span class="p">(</span><span class="mi">0</span><span class="p">),</span> <span class="nb">bool</span><span class="p">(</span><span class="mf">0.0</span><span class="p">),</span> <span class="nb">bool</span><span class="p">(</span><span class="mf">0.0</span><span class="o">+</span><span class="mi">0</span><span class="n">j</span><span class="p">)</span>
<span class="go">(False, False, False)</span>

<span class="gp">&gt;&gt;&gt; </span><span class="nb">bool</span><span class="p">(</span><span class="o">-</span><span class="mi">3</span><span class="p">),</span> <span class="nb">bool</span><span class="p">(</span><span class="mf">3.14159</span><span class="p">),</span> <span class="nb">bool</span><span class="p">(</span><span class="mf">1.0</span><span class="o">+</span><span class="mi">1</span><span class="n">j</span><span class="p">)</span>
<span class="go">(True, True, True)</span>
</code></pre>
<br><br><br>



# Logical Operatorlar Nümunə 2
<div class="highlight python repl" len="637"><span class="repl-toggle" title="Toggle REPL prompts and output" len="12">&gt;&gt;&gt;</span><pre len="542"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="nb">bool</span><span class="p">(</span><span class="s2">""</span><span class="p">)</span>
<span class="go">False</span>

<span class="gp">&gt;&gt;&gt; </span><span class="nb">bool</span><span class="p">(</span><span class="s2">" "</span><span class="p">)</span>
<span class="go">True</span>

<span class="gp">&gt;&gt;&gt; </span><span class="nb">bool</span><span class="p">(</span><span class="s2">"Hello"</span><span class="p">)</span>
<span class="go">True</span>
</code></pre></div>


<br><br><br>
# Logical Operatorlar Nümunə 3
<div class="highlight python repl" len="1966"><span class="repl-toggle" title="Toggle REPL prompts and output" len="12">&gt;&gt;&gt;</span><pre len="1871"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="nb">bool</span><span class="p">([])</span>
<span class="go">False</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">bool</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">])</span>
<span class="go">True</span>

<span class="gp">&gt;&gt;&gt; </span><span class="nb">bool</span><span class="p">(())</span>
<span class="go">False</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">bool</span><span class="p">((</span><span class="s2">"John"</span><span class="p">,</span> <span class="mi">25</span><span class="p">,</span> <span class="s2">"Python Dev"</span><span class="p">))</span>
<span class="go">True</span>

<span class="gp">&gt;&gt;&gt; </span><span class="nb">bool</span><span class="p">(</span><span class="nb">set</span><span class="p">())</span>
<span class="go">False</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">bool</span><span class="p">({</span><span class="s2">"square"</span><span class="p">,</span> <span class="s2">"circle"</span><span class="p">,</span> <span class="s2">"triangle"</span><span class="p">})</span>
<span class="go">True</span>

<span class="gp">&gt;&gt;&gt; </span><span class="nb">bool</span><span class="p">({})</span>
<span class="go">False</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">bool</span><span class="p">({</span><span class="s2">"name"</span><span class="p">:</span> <span class="s2">"John"</span><span class="p">,</span> <span class="s2">"age"</span><span class="p">:</span> <span class="mi">25</span><span class="p">,</span> <span class="s2">"job"</span><span class="p">:</span> <span class="s2">"Python Dev"</span><span class="p">})</span>
<span class="go">True</span>
</code></pre></div>

<br><br><br>


# And Operatorunun detalları 
## &ensp;  And operatoru nümunə 1
<pre><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="mi">5</span> <span class="o">&gt;</span> <span class="mi">3</span> <span class="ow">and</span> <span class="mi">5</span> <span class="o">==</span> <span class="mi">3</span> <span class="o">+</span> <span class="mi">2</span>
<span class="go">True</span>

<span class="gp">&gt;&gt;&gt; </span><span class="mi">5</span> <span class="o">&lt;</span> <span class="mi">3</span> <span class="ow">and</span> <span class="mi">5</span> <span class="o">==</span> <span class="mi">5</span>
<span class="go">False</span>

<span class="gp">&gt;&gt;&gt; </span><span class="mi">5</span> <span class="o">==</span> <span class="mi">5</span> <span class="ow">and</span> <span class="mi">5</span> <span class="o">!=</span> <span class="mi">5</span>
<span class="go">False</span>

<span class="gp">&gt;&gt;&gt; </span><span class="mi">5</span> <span class="o">&lt;</span> <span class="mi">3</span> <span class="ow">and</span> <span class="mi">5</span> <span class="o">!=</span> <span class="mi">5</span>
<span class="go">False</span>
</code></pre>

<br><br><br>
## &ensp;  And operatoru nümunə 2

<pre><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="mi">2</span> <span class="ow">and</span> <span class="mi">3</span>
<span class="go">3</span>

<span class="gp">&gt;&gt;&gt; </span><span class="mi">5</span> <span class="ow">and</span> <span class="mf">0.0</span>
<span class="go">0.0</span>

<span class="gp">&gt;&gt;&gt; </span><span class="p">[]</span> <span class="ow">and</span> <span class="mi">3</span>
<span class="go">[]</span>

<span class="gp">&gt;&gt;&gt; </span><span class="mi">0</span> <span class="ow">and</span> <span class="p">{}</span>
<span class="go">0</span>

<span class="gp">&gt;&gt;&gt; </span><span class="kc">False</span> <span class="ow">and</span> <span class="s2">""</span>
<span class="go">False</span>
</code></pre>


<br><br><br>



## And operatoru cədvəli
<div class="table-responsive">
<table class="table table-hover">
<thead>
<tr>
<th class="text-left"><code>object1</code></th>
<th class="text-left"><code>object2</code></th>
<th class="text-left"><code>object1 and object2</code></th>
</tr>
</thead>
<tbody>
<tr>
<td class="text-left">False</td>
<td class="text-left">False</td>
<td class="text-left"><code>object1</code></td>
</tr>
<tr>
<td class="text-left">False</td>
<td class="text-left">True</td>
<td class="text-left"><code>object1</code></td>
</tr>
<tr>
<td class="text-left">True</td>
<td class="text-left">True</td>
<td class="text-left"><code>object2</code></td>
</tr>
<tr>
<td class="text-left">True</td>
<td class="text-left">False</td>
<td class="text-left"><code>object2</code></td>
</tr>
</tbody>
</table>
</div>
<br><br><br>



## &ensp;  And operatoru nümunə 4
<div class="highlight python repl"><span class="repl-toggle" title="Toggle REPL prompts and output">&gt;&gt;&gt;</span><pre><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="mi">2</span> <span class="o">&lt;</span> <span class="mi">4</span> <span class="ow">and</span> <span class="mi">2</span>
<span class="go">2</span>
<span class="gp">&gt;&gt;&gt; </span><span class="mi">2</span> <span class="ow">and</span> <span class="mi">2</span> <span class="o">&lt;</span> <span class="mi">4</span>
<span class="go">True</span>

<span class="gp">&gt;&gt;&gt; </span><span class="mi">2</span> <span class="o">&lt;</span> <span class="mi">4</span> <span class="ow">and</span> <span class="p">[]</span>
<span class="go">[]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="p">[]</span> <span class="ow">and</span> <span class="mi">2</span> <span class="o">&lt;</span> <span class="mi">4</span>
<span class="go">[]</span>

<span class="gp">&gt;&gt;&gt; </span><span class="mi">5</span> <span class="o">&gt;</span> <span class="mi">10</span> <span class="ow">and</span> <span class="p">{}</span>
<span class="go">False</span>
<span class="gp">&gt;&gt;&gt; </span><span class="p">{}</span> <span class="ow">and</span> <span class="mi">5</span> <span class="o">&gt;</span> <span class="mi">10</span>
<span class="go">{}</span>

<span class="gp">&gt;&gt;&gt; </span><span class="mi">5</span> <span class="o">&gt;</span> <span class="mi">10</span> <span class="ow">and</span> <span class="mi">4</span>
<span class="go">False</span>
<span class="gp">&gt;&gt;&gt; </span><span class="mi">4</span> <span class="ow">and</span> <span class="mi">5</span> <span class="o">&gt;</span> <span class="mi">10</span>
<span class="go">False</span>
</code></pre></div>
<br><br><br>




##  And operatoru nümunə 5
<div class="highlight python repl" len="673"><span class="repl-toggle" title="Toggle REPL prompts and output" len="12">&gt;&gt;&gt;</span><pre len="578"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="mi">5</span> <span class="ow">or</span> <span class="mi">2</span> <span class="ow">and</span> <span class="mi">2</span> <span class="o">&gt;</span> <span class="mi">1</span>
<span class="go">5</span>

<span class="gp">&gt;&gt;&gt; </span><span class="p">(</span><span class="mi">5</span> <span class="ow">or</span> <span class="mi">3</span><span class="p">)</span> <span class="ow">and</span> <span class="mi">2</span> <span class="o">&gt;</span> <span class="mi">1</span>
<span class="go">True</span>
</code></pre></div>

<br><br><br>

# OR - Operator Details
##  Or operatoru nümunə 1


<div class="highlight python repl" len="549"><span class="repl-toggle" title="Toggle REPL prompts and output" len="12">&gt;&gt;&gt;</span><pre len="454"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="mi">3</span> <span class="ow">or</span> <span class="mi">4</span>
<span class="go">3</span>

<span class="gp">&gt;&gt;&gt; </span><span class="mi">0</span> <span class="ow">or</span> <span class="mi">4</span>
<span class="go">4</span>

<span class="gp">&gt;&gt;&gt; </span><span class="mi">3</span> <span class="ow">or</span> <span class="mi">0</span>
<span class="go">3</span>
</code></pre></div>

<br><br><br>
##  Or operatoru nümunə 2

<pre len="169"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="mi">0</span> <span class="ow">or</span> <span class="p">[]</span>
<span class="go">[]</span>
</code></pre>
<br><br><br>

##  Or operatoru nümunə 3
<div class="highlight python repl" len="911"><span class="repl-toggle" title="Toggle REPL prompts and output" len="12">&gt;&gt;&gt;</span><pre len="816"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="n">f</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span> <span class="ow">or</span> <span class="n">f</span><span class="p">(</span><span class="kc">False</span><span class="p">)</span> <span class="ow">or</span> <span class="n">f</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span> <span class="ow">or</span> <span class="n">f</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span> <span class="ow">or</span> <span class="n">f</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
<span class="go">-&gt; f(0) = 0</span>
<span class="go">-&gt; f(False) = False</span>
<span class="go">-&gt; f(1) = 1</span>
<span class="go">1</span>
</code></pre></div>
<br><br><br>

## And operatoru ekstra nümunə
<pre len="1285"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="n">f</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span> <span class="ow">and</span> <span class="n">f</span><span class="p">(</span><span class="kc">False</span><span class="p">)</span> <span class="ow">and</span> <span class="n">f</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span> <span class="ow">and</span> <span class="n">f</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
<span class="go">-&gt; f(1) = 1</span>
<span class="go">-&gt; f(False) = False</span>
<span class="go">False</span>

<span class="gp">&gt;&gt;&gt; </span><span class="n">f</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span> <span class="ow">and</span> <span class="n">f</span><span class="p">(</span><span class="mf">0.0</span><span class="p">)</span> <span class="ow">and</span> <span class="n">f</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span> <span class="ow">and</span> <span class="n">f</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
<span class="go">-&gt; f(1) = 1</span>
<span class="go">-&gt; f(0.0) = 0.0</span>
<span class="go">0.0</span>
</code></pre>

<br><br><br>
## Or operator real nümunə
<div class="highlight python repl" len="901"><span class="repl-toggle" title="Toggle REPL prompts and output" len="12">&gt;&gt;&gt;</span><pre len="806"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="n">country</span> <span class="o">=</span> <span class="s2">"Canada"</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">default_country</span> <span class="o">=</span> <span class="s2">"United States"</span>

<span class="gp">&gt;&gt;&gt; </span><span class="n">country</span> <span class="ow">or</span> <span class="n">default_country</span>
<span class="go">'Canada'</span>

<span class="gp">&gt;&gt;&gt; </span><span class="n">country</span> <span class="o">=</span> <span class="s2">""</span>
<span class="hll"><span class="gp">&gt;&gt;&gt; </span><span class="n">country</span> <span class="ow">or</span> <span class="n">default_country</span>
</span><span class="hll"><span class="go">'United States'</span>
</span></code></pre></div>
<br><br><br>

# Or operatoru Real nümunə 2
<div class="highlight python" len="210"><pre len="199"><span></span><code><span class="n">data_is_clean</span> <span class="ow">or</span> <span class="n">clean_data</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</code></pre></div>
<br><br><br>

# And operatoru Real nümunə 
<div class="highlight python" len="215"><pre len="204"><span></span><code><span class="n">data_is_updated</span> <span class="ow">and</span> <span class="n">process_data</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</code></pre></div>


<br><br><br>

## If operatoruna aid bəzi qaydalar
<div class="highlight python" len="253"><pre len="242"><span></span><code><span class="n">variable</span> <span class="o">=</span> <span class="n">expression_1</span> <span class="k">if</span> <span class="n">condition</span> <span class="k">else</span> <span class="n">expression_2</span>
</code></pre></div>

<pre len="355"><span></span><code><span class="k">if</span> <span class="n">condition</span><span class="p">:</span>
    <span class="n">variable</span> <span class="o">=</span> <span class="n">expression_1</span>
<span class="k">else</span><span class="p">:</span>
    <span class="n">variable</span> <span class="o">=</span> <span class="n">expression_2</span>
</code></pre>

<div class="highlight python" len="254"><pre len="243"><span></span><code><span class="n">variable</span> <span class="o">=</span> <span class="n">condition</span> <span class="ow">and</span> <span class="n">expression_1</span> <span class="ow">or</span> <span class="n">expression_2</span>
</code></pre></div>

<br><br><br>
<div class="highlight python repl" len="1159"><span class="repl-toggle" title="Toggle REPL prompts and output" len="12">&gt;&gt;&gt;</span><pre len="1064"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="n">day</span> <span class="o">=</span> <span class="s2">"Sunday"</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">open_time</span> <span class="o">=</span> <span class="s2">"11AM"</span> <span class="k">if</span> <span class="n">day</span> <span class="o">==</span> <span class="s2">"Sunday"</span> <span class="k">else</span> <span class="s2">"9AM"</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">open_time</span>
<span class="go">'11AM'</span>

<span class="gp">&gt;&gt;&gt; </span><span class="n">day</span> <span class="o">=</span> <span class="s2">"Monday"</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">open_time</span> <span class="o">=</span> <span class="s2">"11AM"</span> <span class="k">if</span> <span class="n">day</span> <span class="o">==</span> <span class="s2">"Sunday"</span> <span class="k">else</span> <span class="s2">"9AM"</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">open_time</span>
<span class="go">'9AM'</span>
</code></pre></div>

<br><br><br>

# Əlavələr
### Diqqət sıfıra bölmək olmaz!
<div class="highlight python repl" len="758"><span class="repl-toggle" title="Toggle REPL prompts and output" len="12">&gt;&gt;&gt;</span><pre len="663"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">=</span> <span class="mi">0</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">b</span> <span class="o">=</span> <span class="mi">1</span>

<span class="gp">&gt;&gt;&gt; </span><span class="p">(</span><span class="n">b</span> <span class="o">/</span> <span class="n">a</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span>
<span class="gt">Traceback (most recent call last):</span>
<span class="w">    </span><span class="o">...</span>
<span class="gr">ZeroDivisionError</span>: <span class="n">division by zero</span>
</code></pre></div>
<br><br><br>





<section class="section2" len="8144"><h2 id="identity-operators-and-expressions-in-python" len="146"><font lang="tr" len="44" style="">Identity Operators and Expressions in Python</font><a class="headerlink" href="#identity-operators-and-expressions-in-python" title="Permanent link" len="0"></a></h2>
<p len="360">Python provides two operators, <code len="2">is</code> and <code len="6">is not</code>, that allow you to determine whether two operands have the same <strong len="8">identity</strong>. In other words, they let you check if the operands refer to the same object. Note that identity isn’t the same thing as equality. The latter aims to check whether two operands contain the same data.</p>
<div class="alert alert-primary" role="alert" len="234">
<p len="225"><font len="241"><strong len="5">Note:</strong> To learn more about the difference between identity and equality, check out <a href="https://realpython.com/python-is-identity-vs-equality/" len="56">Python ‘!=’ Is Not ‘is not’: Comparing Objects in Python</a></font>.</p>
</div>
<p len="129">Here’s a summary of Python’s identity operators. Note that <code len="1">x</code> and <code len="1">y</code> are variables that point to objects:</p>
<div class="table-responsive" len="735">
<table class="table table-hover" len="692">
<thead len="73">
<tr len="62">
<th len="8" lang="tr">Operator</th>
<th len="17" lang="tr" style="">Sample Expression</th>
<th len="6" lang="tr" style="">Result</th>
</tr>
</thead>
<tbody len="586">
<tr len="271">
<td len="85"><a href="https://docs.python.org/3/reference/expressions.html#is" len="15"><code>is</code></a></td>
<td len="19"><code len="6">x is y</code></td>
<td len="136"><font lang="tr" len="126" style="">• <code len="4">True</code> if <code len="1">x</code> and <code len="1">y</code> hold a reference to the same in-memory object</font><br len="0"><font lang="tr" len="38">• <code len="5">False</code> otherwise</font></td>
</tr>
<tr len="294">
<td len="93"><a href="https://docs.python.org/3/reference/expressions.html#is-not" len="19"><code>is not</code></a></td>
<td len="23"><code len="10">x is not y</code></td>
<td len="147"><font lang="tr" len="137" style="">• <code len="4">True</code> if <code len="1">x</code> points to an object different from the object that <code len="1">y</code> points to</font><br len="0"><font lang="tr" len="38">• <code len="5">False</code> otherwise</font></td>
</tr>
</tbody>
</table>
</div>
<p len="132">These two Python operators are keywords instead of odd symbols. This is part of Python’s goal of favoring readability in its syntax.</p>
<p len="126" lang="tr" style="">Here’s an example of two variables, <code len="1">x</code> and <code len="1">y</code>, that refer to objects that are equal but not identical:</p>
<div class="highlight python repl" len="641"><span class="repl-toggle" title="Toggle REPL prompts and output" len="12">&gt;&gt;&gt;</span><pre len="546"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="n">x</span> <span class="o">=</span> <span class="mi">1001</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">y</span> <span class="o">=</span> <span class="mi">1001</span>

<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span> <span class="o">==</span> <span class="n">y</span>
<span class="go">True</span>

<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span> <span class="ow">is</span> <span class="n">y</span>
<span class="go">False</span>
</code></pre></div>
<p len="317">In this example, <code len="1">x</code> and <code len="1">y</code> refer to objects whose value is <code len="4">1001</code>. So, they’re equal. However, they don’t reference the same object. That’s why the <code len="2">is</code> operator returns <code len="5">False</code>. You can check an object’s identity using the built-in <code len="4">id()</code> function:</p>
<div class="highlight python repl" len="464"><span class="repl-toggle" title="Toggle REPL prompts and output" len="12">&gt;&gt;&gt;</span><pre len="369"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="nb">id</span><span class="p">(</span><span class="n">x</span><span class="p">)</span>
<span class="go">4417772080</span>

<span class="gp">&gt;&gt;&gt; </span><span class="nb">id</span><span class="p">(</span><span class="n">y</span><span class="p">)</span>
<span class="go">4417766416</span>
</code></pre></div>
<p len="372">As you can conclude from the <code len="4">id()</code> output, <code len="1">x</code> and <code len="1">y</code> don’t have the same identity. So, they’re different objects, and because of that, the expression <code len="6">x is y</code> returns <code len="5">False</code>. In other words, you get <code len="5">False</code> because you have two different instances of <code len="4">1001</code> stored in your computer’s memory.</p>
<p len="203">When you make an assignment like <code len="5">y = x</code>, Python creates a second reference to the same object. Again, you can confirm that with the <code len="4">id()</code> function or the <code len="2">is</code> operator:</p>
<div class="highlight python repl" len="852"><span class="repl-toggle" title="Toggle REPL prompts and output" len="12">&gt;&gt;&gt;</span><pre len="757"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">=</span> <span class="s2">"Hello, Pythonista!"</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">b</span> <span class="o">=</span> <span class="n">a</span>

<span class="gp">&gt;&gt;&gt; </span><span class="nb">id</span><span class="p">(</span><span class="n">a</span><span class="p">)</span>
<span class="go">4417651936</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">id</span><span class="p">(</span><span class="n">b</span><span class="p">)</span>
<span class="go">4417651936</span>

<span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="ow">is</span> <span class="n">b</span>
<span class="go">True</span>
</code></pre></div>
<p len="324"><font len="388">In this example, <code len="1">a</code> and <code len="1">b</code> hold references to the same object, the string <code len="20">"Hello, Pythonista!"</code>. Therefore, the <code len="4">id()</code> function returns the same identity when you call it with <code len="1">a</code> and <code len="1">b</code>. Similarly, the <code len="2">is</code> operator returns <code len="4">True</code></font>.</p>
<div class="alert alert-primary" role="alert" len="263">
<p len="254"><font len="285"><strong len="5">Note:</strong> You should note that, on your computer, you’ll get a different identity number when you call <code len="4">id()</code> in the example above. The key detail is that the identity number will be the same for <code len="1">a</code> and <code len="1">b</code></font>.</p>
</div>
<p len="180">Finally, the <code len="6">is not</code> operator is the opposite of <code len="2">is</code>. So, you can use <code len="6">is not</code> to determine if two names <em len="5">don’t</em> refer to the same object:</p>
<div class="highlight python repl" len="941"><span class="repl-toggle" title="Toggle REPL prompts and output" len="12">&gt;&gt;&gt;</span><pre len="846"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="n">x</span> <span class="o">=</span> <span class="mi">1001</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">y</span> <span class="o">=</span> <span class="mi">1001</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span> <span class="ow">is</span> <span class="ow">not</span> <span class="n">y</span>
<span class="go">True</span>

<span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">=</span> <span class="s2">"Hello, Pythonista!"</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">b</span> <span class="o">=</span> <span class="n">a</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="ow">is</span> <span class="ow">not</span> <span class="n">b</span>
<span class="go">False</span>
</code></pre></div>
<p len="338"><font len="401">In the first example, because <code len="1">x</code> and <code len="1">y</code> point to different objects in your computer’s memory, the <code len="6">is not</code> operator returns <code len="4">True</code>. In the second example, because <code len="1">a</code> and <code len="1">b</code> are references to the same object, the <code len="6">is not</code> operator returns <code len="5">False</code></font>.</p>
<div class="alert alert-primary" role="alert" len="281">
<p len="272"><strong len="5">Note:</strong> The syntax <code len="10">not x is y</code> also works the same as <code len="10">x is not y</code>. However, the former syntax looks odd and is difficult to read. That’s why Python recognizes <code len="6">is not</code> as an operator and encourages its use for readability.</p>
</div>
<p len="168">Again, the <code len="6">is not</code> operator highlights Python’s readability goals. In general, both identity operators allow you to write checks that read as plain English.</p>
<div len="415"><div class="rounded border border-light" style="display:block;position:relative;" len="191"><div style="display:block;width:100%;padding-top:12.5%;" len="0"></div><div class="rpad rounded border" data-unit="8x1" style="position:absolute;left:0;top:0;right:0;bottom:0;overflow:hidden;" len="0"></div></div><a class="small text-muted" href="/account/join/" rel="nofollow" len="67"><i aria-hidden="true" class="fa fa-info-circle mr-1" len="0"></i></section>
<br><br><br>
<section class="section2" len="5879"><h2 id="membership-operators-and-expressions-in-python" len="150"><font lang="tr" len="46" style="">Membership Operators and Expressions in Python</font><a class="headerlink" href="#membership-operators-and-expressions-in-python" title="Permanent link" len="0"></a></h2>
<p len="399"><font len="431">Sometimes you need to determine whether a value is present in a container data type, such as a list, tuple, or set. In other words, you may need to check if a given value <em len="2">is</em> or <em len="6">is not</em> a <strong len="6">member</strong> of a collection of values. Python calls this kind of check a <a href="https://docs.python.org/3/reference/expressions.html#membership-test-operations" len="15">membership test</a></font>.</p>
<div class="alert alert-primary" role="alert" len="215">
<p len="206"><font len="222"><strong len="5">Note:</strong> For a deep dive into how Python’s membership tests work, check out <a href="https://realpython.com/python-in-operator/" len="58">Python’s “in” and “not in” Operators: Check for Membership</a></font>.</p>
</div>
<p len="226">Membership tests are quite common and useful in programming. As with many other common operations, Python has dedicated operators for membership tests. The table below lists the <strong len="20">membership operators</strong> in Python:</p>
<div class="table-responsive" len="844">
<table class="table table-hover" len="801">
<thead len="109">
<tr len="98">
<th class="text-left" len="8" lang="tr">Operator</th>
<th len="17" lang="tr" style="">Sample Expression</th>
<th class="text-left" len="6" lang="tr">Result</th>
</tr>
</thead>
<tbody len="659">
<tr len="306">
<td class="text-left" len="85"><a href="https://docs.python.org/3/reference/expressions.html#in" len="15"><code>in</code></a></td>
<td len="32"><code len="19">value in collection</code></td>
<td class="text-left" len="122"><font lang="tr" len="121">• <code len="4">True</code> if <code len="5">value</code> <em len="2">is</em> present in <code len="10">collection</code></font><br len="0"><font lang="tr" len="38">• <code len="5">False</code> otherwise</font></td>
</tr>
<tr len="332">
<td class="text-left" len="93"><a href="https://docs.python.org/3/reference/expressions.html#not-in" len="19"><code>not in</code></a></td>
<td len="36"><code len="23">value not in collection</code></td>
<td class="text-left" len="136"><font lang="tr" len="135">• <code len="4">True</code> if <code len="5">value</code> <em len="6">is not</em> present in <code len="10">collection</code> of values</font><br len="0"><font lang="tr" len="38">• <code len="5">False</code> otherwise</font></td>
</tr>
</tbody>
</table>
</div>
<p len="140" lang="tr">As usual, Python favors readability by using English words as operators instead of potentially confusing symbols or combinations of symbols.</p>
<div class="alert alert-primary" role="alert" len="290">
<p len="281"><strong len="5">Note:</strong> The syntax <code len="23">not value in collection</code> also works in Python. However, this syntax looks odd and is difficult to read. So, to keep your code clean and readable, you should use <code len="23">value not in collection</code>, which almost reads as plain English.</p>
</div>
<p len="257">The Python <code len="2">in</code> and <code len="6">not in</code> operators are binary. This means that you can create membership expressions by connecting two operands with either operator. However, the operands in a membership expression have particular characteristics:</p>
<ul len="205">
<li len="92" lang="tr"><strong len="12">Left operand</strong>: The value that you want to look for in a collection of values</li>
<li len="92" lang="tr" style=""><strong len="13">Right operand</strong>: The collection of values where the target value may be found</li>
</ul>
<p len="148" lang="tr">To better understand the <code len="2">in</code> operator, below you have two demonstrative examples consisting of determining whether a value is in a list:</p>
<div class="highlight python repl" len="909"><span class="repl-toggle" title="Toggle REPL prompts and output" len="12">&gt;&gt;&gt;</span><pre len="814"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="mi">5</span> <span class="ow">in</span> <span class="p">[</span><span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">9</span><span class="p">,</span> <span class="mi">7</span><span class="p">]</span>
<span class="go">True</span>

<span class="gp">&gt;&gt;&gt; </span><span class="mi">8</span> <span class="ow">in</span> <span class="p">[</span><span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">9</span><span class="p">,</span> <span class="mi">7</span><span class="p">]</span>
<span class="go">False</span>
</code></pre></div>
<p len="187">The first expression returns <code len="4">True</code> because <code len="1">5</code> is in the list of numbers. The second expression returns <code len="5">False</code> because <code len="1">8</code> isn’t in the list.</p>
<p len="190">The <code len="6">not in</code> membership operator runs the opposite test as the <code len="2">in</code> operator. It allows you to check whether an integer value <em len="6">is not</em> in a collection of values:</p>
<div class="highlight python repl" len="965"><span class="repl-toggle" title="Toggle REPL prompts and output" len="12">&gt;&gt;&gt;</span><pre len="870"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="mi">5</span> <span class="ow">not</span> <span class="ow">in</span> <span class="p">[</span><span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">9</span><span class="p">,</span> <span class="mi">7</span><span class="p">]</span>
<span class="go">False</span>

<span class="gp">&gt;&gt;&gt; </span><span class="mi">8</span> <span class="ow">not</span> <span class="ow">in</span> <span class="p">[</span><span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">9</span><span class="p">,</span> <span class="mi">7</span><span class="p">]</span>
<span class="go">True</span>
</code></pre></div>
<p len="391">In the first example, you get <code len="5">False</code> because <code len="1">5</code> is in the target list. In the second example, you get <code len="4">True</code> because <code len="1">8</code> isn’t in the list of values. This may sound like a tongue twister because of the negative logic. To avoid confusion, remember that you’re trying to determine if the value <em len="6">is not</em> part of a given collection of values.</p>
</section>

<br><br><br>


# Birləşdirmə və ya çoxaltma idadələri 
<div class="highlight python repl" len="1275"><span class="repl-toggle" title="Toggle REPL prompts and output" len="12">&gt;&gt;&gt;</span><pre len="1180"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="s2">"Hello, "</span> <span class="o">+</span> <span class="s2">"World!"</span>
<span class="go">'Hello, World!'</span>

<span class="gp">&gt;&gt;&gt; </span><span class="p">(</span><span class="s2">"A"</span><span class="p">,</span> <span class="s2">"B"</span><span class="p">,</span> <span class="s2">"C"</span><span class="p">)</span> <span class="o">+</span> <span class="p">(</span><span class="s2">"D"</span><span class="p">,</span> <span class="s2">"E"</span><span class="p">,</span> <span class="s2">"F"</span><span class="p">)</span>
<span class="go">('A', 'B', 'C', 'D', 'E', 'F')</span>

<span class="gp">&gt;&gt;&gt; </span><span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">]</span> <span class="o">+</span> <span class="p">[</span><span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">]</span>
<span class="go">[0, 1, 2, 3, 4, 5, 6]</span>
</code></pre></div>
<div class="highlight python repl" len="1103"><span class="repl-toggle" title="Toggle REPL prompts and output" len="12">&gt;&gt;&gt;</span><pre len="1008"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="s2">"Hello"</span> <span class="o">*</span> <span class="mi">3</span>
<span class="go">'HelloHelloHello'</span>
<span class="gp">&gt;&gt;&gt; </span><span class="mi">3</span> <span class="o">*</span> <span class="s2">"World!"</span>
<span class="go">'World!World!World!'</span>

<span class="gp">&gt;&gt;&gt; </span><span class="p">(</span><span class="s2">"A"</span><span class="p">,</span> <span class="s2">"B"</span><span class="p">,</span> <span class="s2">"C"</span><span class="p">)</span> <span class="o">*</span> <span class="mi">3</span>
<span class="go">('A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C')</span>

<span class="gp">&gt;&gt;&gt; </span><span class="mi">3</span> <span class="o">*</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">]</span>
<span class="go">[1, 2, 3, 1, 2, 3, 1, 2, 3]</span>
</code></pre></div>

<br><br><br>
# Bəzi əlavələr daha
## &emsp; Əmrlər sırası
<div class="highlight python repl" len="315"><span class="repl-toggle" title="Toggle REPL prompts and output" len="12">&gt;&gt;&gt;</span><pre len="220"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="mi">20</span> <span class="o">+</span> <span class="mi">4</span> <span class="o">*</span> <span class="mi">10</span>
<span class="go">60</span>
</code></pre></div>

<pre len="271"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="mi">2</span> <span class="o">*</span> <span class="mi">3</span> <span class="o">**</span> <span class="mi">4</span> <span class="o">*</span> <span class="mi">5</span>
<span class="go">810</span>
</code></pre>
<div class="highlight python repl" len="665"><span class="repl-toggle" title="Toggle REPL prompts and output" len="12">&gt;&gt;&gt;</span><pre len="570"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="p">(</span><span class="mi">20</span> <span class="o">+</span> <span class="mi">4</span><span class="p">)</span> <span class="o">*</span> <span class="mi">10</span>
<span class="go">240</span>

<span class="gp">&gt;&gt;&gt; </span><span class="mi">2</span> <span class="o">*</span> <span class="mi">3</span> <span class="o">**</span> <span class="p">(</span><span class="mi">4</span> <span class="o">*</span> <span class="mi">5</span><span class="p">)</span>
<span class="go">6973568802</span>
</code></pre></div>
<br><br><br>
# Özünü artırma əməliyyatı
<div class="highlight python repl" len="475"><span class="repl-toggle" title="Toggle REPL prompts and output" len="12">&gt;&gt;&gt;</span><pre len="380"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="n">total</span> <span class="o">=</span> <span class="mi">10</span>
<span class="hll"><span class="gp">&gt;&gt;&gt; </span><span class="n">total</span> <span class="o">+=</span> <span class="mi">5</span>
</span><span class="gp">&gt;&gt;&gt; </span><span class="n">total</span>
<span class="go">15</span>
</code></pre></div>
<div class="table-responsive" len="1683">
<table class="table table-hover" len="1640">
<thead len="109">
<tr len="98">
<th len="8" lang="tr" style="">Operator</th>
<th len="11" lang="tr">Description</th>
<th len="17" lang="tr">Sample Expression</th>
<th len="21" lang="tr">Equivalent Expression</th>
</tr>
</thead>
<tbody len="1498">
<tr len="181">
<td len="15"><code len="2">+=</code></td>
<td len="84" lang="tr" style="">Adds the right operand to the left operand and stores the result in the left operand</td>
<td len="19"><code len="6">x += y</code></td>
<td len="22"><code len="9">x = x + y</code></td>
</tr>
<tr len="188">
<td len="15"><code len="2">-=</code></td>
<td len="91" lang="tr" style="">Subtracts the right operand from the left operand and stores the result in the left operand</td>
<td len="19"><code len="6">x -= y</code></td>
<td len="22"><code len="9">x = x - y</code></td>
</tr>
<tr len="189">
<td len="15"><code len="2">*=</code></td>
<td len="92" lang="tr" style="">Multiplies the right operand with the left operand and stores the result in the left operand</td>
<td len="19"><code len="6">x *= y</code></td>
<td len="22"><code len="9">x = x * y</code></td>
</tr>
<tr len="184">
<td len="15"><code len="2">/=</code></td>
<td len="87" lang="tr" style="">Divides the left operand by the right operand and stores the result in the left operand</td>
<td len="19"><code len="6">x /= y</code></td>
<td len="22"><code len="9">x = x / y</code></td>
</tr>
<tr len="280">
<td len="16"><code len="3">//=</code></td>
<td len="180" lang="tr" style="">Performs <a href="https://docs.python.org/3/glossary.html#term-floor-division" len="14">floor division</a> of the left operand by the right operand and stores the result in the left operand</td>
<td len="20"><code len="7">x //= y</code></td>
<td len="23"><code len="10">x = x // y</code></td>
</tr>
<tr len="208">
<td len="15"><code len="2">%=</code></td>
<td len="111" lang="tr" style="">Finds the remainder of dividing the left operand by the right operand and stores the result in the left operand</td>
<td len="19"><code len="6">x %= y</code></td>
<td len="22"><code len="9">x = x % y</code></td>
</tr>
<tr len="197">
<td len="16"><code len="3">**=</code></td>
<td len="99" lang="tr">Raises the left operand to the power of the right operand and stores the result in the left operand</td>
<td len="20"><code len="7">x **= y</code></td>
<td len="21"><code len="8">x = x**y</code></td>
</tr>
</tbody>
</table>
</div>
<br><br><br>
<br><br><br>
<br><br><br>
<br><br><br>


