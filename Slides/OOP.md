<p> Əşya yönümlü proqramlaşdırma, əlaqəli xüsusiyyətləri və davranışları fərdi obyektlərə birləşdirərək proqramları strukturlaşdırmağın bir yolu olan bir proqramlaşma paradigmasıdır.
</p>
<img src="/Pictures/oop.png">


For example, an object could represent a person with properties like a name, age, and address and behaviors such as walking, talking, breathing, and running. Or it could represent an email with properties like a recipient list, subject, and body and behaviors like adding attachments and sending.



<pre len="637"><span></span><code><span class="k">class</span> <span class="nc">Employee</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">age</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span>  <span class="n">name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">age</span> <span class="o">=</span> <span class="n">age</span>
</code></pre>

<br/>
<br/>
 
### Bütün obyektlərə aid atribut
<pre len="794"><span></span><code><span class="c1"># dog.py</span>

<span class="k">class</span> <span class="nc">Dog</span><span class="p">:</span>
<span class="hll">    <span class="n">species</span> <span class="o">=</span> <span class="s2">"Canis familiaris"</span>
</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">age</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="n">name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">age</span> <span class="o">=</span> <span class="n">age</span>
</code></pre>


### Fərqli obyektlər
<pre len="447"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">=</span> <span class="n">Dog</span><span class="p">()</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">b</span> <span class="o">=</span> <span class="n">Dog</span><span class="p">()</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">==</span> <span class="n">b</span>
<span class="go">False</span>
</code></pre>


### Metodlar

<pre len="1966"><span></span><code><span class="c1"># dog.py</span>

<span class="k">class</span> <span class="nc">Dog</span><span class="p">:</span>
    <span class="n">species</span> <span class="o">=</span> <span class="s2">"Canis familiaris"</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">age</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="n">name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">age</span> <span class="o">=</span> <span class="n">age</span>

    <span class="c1"># Instance method</span>
    <span class="k">def</span> <span class="nf">description</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s2"> is </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">age</span><span class="si">}</span><span class="s2"> years old"</span>

    <span class="c1"># Another instance method</span>
    <span class="k">def</span> <span class="nf">speak</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sound</span><span class="p">):</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s2"> says </span><span class="si">{</span><span class="n">sound</span><span class="si">}</span><span class="s2">"</span>
</code></pre>

<br/>
<br/>

### Metodları çağırılması

<pre len="964"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="n">miles</span> <span class="o">=</span> <span class="n">Dog</span><span class="p">(</span><span class="s2">"Miles"</span><span class="p">,</span> <span class="mi">4</span><span class="p">)</span>

<span class="gp">&gt;&gt;&gt; </span><span class="n">miles</span><span class="o">.</span><span class="n">description</span><span class="p">()</span>
<span class="go">'Miles is 4 years old'</span>

<span class="gp">&gt;&gt;&gt; </span><span class="n">miles</span><span class="o">.</span><span class="n">speak</span><span class="p">(</span><span class="s2">"Woof Woof"</span><span class="p">)</span>
<span class="go">'Miles says Woof Woof'</span>

<span class="gp">&gt;&gt;&gt; </span><span class="n">miles</span><span class="o">.</span><span class="n">speak</span><span class="p">(</span><span class="s2">"Bow Wow"</span><span class="p">)</span>
<span class="go">'Miles says Bow Wow'</span>
</code></pre>

<br/>
<br/>


### Meta str metodu 
\_\_str__

<pre len="750"><span></span><code><span class="c1"># dog.py</span>

<span class="k">class</span> <span class="nc">Dog</span><span class="p">:</span>
    <span class="c1"># ...</span>

<span class="hll">    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span>        <span class="k">return</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s2"> is </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">age</span><span class="si">}</span><span class="s2"> years old"</span>
</code></pre>



### repr vs str
\_\_repr__ vs \_\_str__


<pre><span></span><code><span class="c1"># book.py
</span>
<span class="k">class</span> <span class="nc">Book</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">title</span><span class="p">,</span> <span class="n">author</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">title</span> <span class="o">=</span> <span class="n">title</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">author</span> <span class="o">=</span> <span class="n">author</span>

    <span class="k">def</span> <span class="fm">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">class_name</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">class_name</span><span class="si">}</span><span class="s2">(title=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">title</span><span class="si">!r}</span><span class="s2">, author=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">author</span><span class="si">!r}</span><span class="s2">)"</span>

<span class="hll">    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span class="hll">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">title</span>
</span>
<span class="n">odyssey</span> <span class="o">=</span> <span class="n">Book</span><span class="p">(</span><span class="s2">"The Odyssey"</span><span class="p">,</span> <span class="s2">"Homer"</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="nb">repr</span><span class="p">(</span><span class="n">odyssey</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">odyssey</span><span class="p">))</span>
</code></pre>

### Inheritance 

<pre len="506"><span></span><code><span class="c1"># inheritance.py</span>

<span class="k">class</span> <span class="nc">Parent</span><span class="p">:</span>
    <span class="n">hair_color</span> <span class="o">=</span> <span class="s2">"brown"</span>

<span class="k">class</span> <span class="nc">Child</span><span class="p">(</span><span class="n">Parent</span><span class="p">):</span>
<span class="hll">    <span class="n">hair_color</span> <span class="o">=</span> <span class="s2">"purple"</span>
</span></code></pre>


### How to work?

<pre len="2083"><span></span><code><span class="c1"># dog.py</span>

<span class="k">class</span> <span class="nc">Dog</span><span class="p">:</span>
    <span class="n">species</span> <span class="o">=</span> <span class="s2">"Canis familiaris"</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">age</span><span class="p">,</span> <span class="n">breed</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="n">name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">age</span> <span class="o">=</span> <span class="n">age</span>
<span class="hll">        <span class="bp">self</span><span class="o">.</span><span class="n">breed</span> <span class="o">=</span> <span class="n">breed</span>
</span>
    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s2"> is </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">age</span><span class="si">}</span><span class="s2"> years old"</span>

    <span class="k">def</span> <span class="nf">speak</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sound</span><span class="p">):</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s2"> says </span><span class="si">{</span><span class="n">sound</span><span class="si">}</span><span class="s2">"</span>
</code></pre>


<br>
Obyektlər
<pre len="1255"><span></span><code><span class="gp jsREPLOutputHidden" style="display: none;"> </span><span class="n">miles</span> <span class="o">=</span> <span class="n">Dog</span><span class="p">(</span><span class="s2">"Miles"</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="s2">"Jack Russell Terrier"</span><span class="p">)</span>
<span class="gp jsREPLOutputHidden" style="display: none;"> </span><span class="n">buddy</span> <span class="o">=</span> <span class="n">Dog</span><span class="p">(</span><span class="s2">"Buddy"</span><span class="p">,</span> <span class="mi">9</span><span class="p">,</span> <span class="s2">"Dachshund"</span><span class="p">)</span>
<span class="gp jsREPLOutputHidden" style="display: none;"> </span><span class="n">jack</span> <span class="o">=</span> <span class="n">Dog</span><span class="p">(</span><span class="s2">"Jack"</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="s2">"Bulldog"</span><span class="p">)</span>
<span class="gp jsREPLOutputHidden" style="display: none;"> </span><span class="n">jim</span> <span class="o">=</span> <span class="n">Dog</span><span class="p">(</span><span class="s2">"Jim"</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="s2">"Bulldog"</span><span class="p">)</span>
</code></pre>
<br>
<br>

Çağırıldığında
<pre len="734"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="n">buddy</span><span class="o">.</span><span class="n">speak</span><span class="p">(</span><span class="s2">"Yap"</span><span class="p">)</span>
<span class="go">'Buddy says Yap'</span>

<span class="gp">&gt;&gt;&gt; </span><span class="n">jim</span><span class="o">.</span><span class="n">speak</span><span class="p">(</span><span class="s2">"Woof"</span><span class="p">)</span>
<span class="go">'Jim says Woof'</span>

<span class="gp">&gt;&gt;&gt; </span><span class="n">jack</span><span class="o">.</span><span class="n">speak</span><span class="p">(</span><span class="s2">"Woof"</span><span class="p">)</span>
<span class="go">'Jack says Woof'</span>
</code></pre>

<br/>
<br/> 

### Miras alsaq bəs?
<pre len="610"><span></span><code><span class="c1"># dog.py</span>

<span class="c1"># ...</span>

<span class="k">class</span> <span class="nc">JackRussellTerrier</span><span class="p">(</span><span class="n">Dog</span><span class="p">):</span>
    <span class="k">pass</span>

<span class="k">class</span> <span class="nc">Dachshund</span><span class="p">(</span><span class="n">Dog</span><span class="p">):</span>
    <span class="k">pass</span>

<span class="k">class</span> <span class="nc">Bulldog</span><span class="p">(</span><span class="n">Dog</span><span class="p">):</span>
    <span class="k">pass</span>
</code></pre>

<br>
<br>

### Fərqli obyektlər
<pre len="1037"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="n">miles</span> <span class="o">=</span> <span class="n">JackRussellTerrier</span><span class="p">(</span><span class="s2">"Miles"</span><span class="p">,</span> <span class="mi">4</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">buddy</span> <span class="o">=</span> <span class="n">Dachshund</span><span class="p">(</span><span class="s2">"Buddy"</span><span class="p">,</span> <span class="mi">9</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">jack</span> <span class="o">=</span> <span class="n">Bulldog</span><span class="p">(</span><span class="s2">"Jack"</span><span class="p">,</span> <span class="mi">3</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">jim</span> <span class="o">=</span> <span class="n">Bulldog</span><span class="p">(</span><span class="s2">"Jim"</span><span class="p">,</span> <span class="mi">5</span><span class="p">)</span>
</code></pre>

<br>
<br>

<pre len="761"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="n">miles</span><span class="o">.</span><span class="n">species</span>
<span class="go">'Canis familiaris'</span>

<span class="gp">&gt;&gt;&gt; </span><span class="n">buddy</span><span class="o">.</span><span class="n">name</span>
<span class="go">'Buddy'</span>

<span class="gp">&gt;&gt;&gt; </span><span class="nb">print</span><span class="p">(</span><span class="n">jack</span><span class="p">)</span>
<span class="go">Jack is 3 years old</span>

<span class="gp">&gt;&gt;&gt; </span><span class="n">jim</span><span class="o">.</span><span class="n">speak</span><span class="p">(</span><span class="s2">"Woof"</span><span class="p">)</span>
<span class="go">'Jim says Woof'</span>
</code></pre>
<br>
<br>
<h4> Test edək </h4>

<pre len="254"><span></span><code><span class="gp" style="">&gt;&gt;&gt; </span><span class="nb">isinstance</span><span class="p">(</span><span class="n">miles</span><span class="p">,</span> <span class="n">Dog</span><span class="p">)</span>
<span class="go" style="">True</span>
</code></pre>


<pre len="494"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="nb">isinstance</span><span class="p">(</span><span class="n">miles</span><span class="p">,</span> <span class="n">Bulldog</span><span class="p">)</span>
<span class="go">False</span>

<span class="gp">&gt;&gt;&gt; </span><span class="nb">isinstance</span><span class="p">(</span><span class="n">jack</span><span class="p">,</span> <span class="n">Dachshund</span><span class="p">)</span>
<span class="go">False</span>
</code></pre>



### Override

<pre len="868"><span></span><code><span class="c1"># dog.py</span>

<span class="c1"># ...</span>

<span class="k">class</span> <span class="nc">JackRussellTerrier</span><span class="p">(</span><span class="n">Dog</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">speak</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sound</span><span class="o">=</span><span class="s2">"Arf"</span><span class="p">):</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s2"> says </span><span class="si">{</span><span class="n">sound</span><span class="si">}</span><span class="s2">"</span>

<span class="c1"># ...    </span>
</code></pre>

<br>

<pre len="472"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="n">miles</span> <span class="o">=</span> <span class="n">JackRussellTerrier</span><span class="p">(</span><span class="s2">"Miles"</span><span class="p">,</span> <span class="mi">4</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">miles</span><span class="o">.</span><span class="n">speak</span><span class="p">()</span>
<span class="go">'Miles says Arf'</span>
</code></pre>


<pre len="264"><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="n">miles</span><span class="o">.</span><span class="n">speak</span><span class="p">(</span><span class="s2">"Grrr"</span><span class="p">)</span>
<span class="go">'Miles says Grrr'</span>
</code></pre>

#isinistance