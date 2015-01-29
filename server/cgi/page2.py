#!/usr/bin/env python
import cgi
form = cgi.FieldStorage()
val1 = form.getvalue('name')
val2 = form.getvalue('family')
print "Content-type:text/html"
print
print "my name is:"
print val1+"<br/>"
print "my family is:"
print val2+"<br/>"

print """
<form method="post" action ="page1.py">
<textarea name='birthday' cols="100" rows="1">
pls enter your birthday
</textarea>
<textarea name="hobby" cols="100" rows="1">
pls enter your hobby
</textarea>
<br/>
<input type="submit" value="Submit">
</form>"""
