from datetime import datetime as dt

from pyscript import document
from pyweb import pydom

tasks = []

def q(selector, root=document):
    return root.querySelector(selector)

meta_template = """\
<h1> Meta Data Template </h1>
<pre>
%s
%s
%s
</pre>
"""

meta_container = pydom["#meta-container"][0]

new_task_content = pydom["#meta-1"][0]
meta_2 = pydom["#meta-2"][0]
meta_3 = pydom["#meta-3"][0]

def add_meta(e):
    first = new_task_content.value
    second = meta_2.value
    third = meta_3.value
    meta_html = meta_template % (first, second, third)
    meta_container.html = meta_html




