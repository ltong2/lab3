#!/usr/bin/env python
import cgi
form = cgi.FieldStorage()
val1 = form.getvalue('birthday')
val2 = form.getvalue('hobby')
print """Content-type:text/html

<form method="post" action ="page2.py">
<textarea name='name' cols="100" rows="1">
pls enter the name
</textarea>
<textarea name="family" cols="100" rows="1">
pls enter the family
</textarea>
<br/>
<input type="submit" value="Submit">
</form>
My birthday is: %s <br/>
My hobby is: %s <br/>
""" %(val1, val2)
