# Import modules for CGI handling
import cgi, cgitb

# Create Instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
province = form.getvalue("province")
income = form.getvalue("income")


# Form Output to HTML
print "Content-type:text/html\r\n\r\n"
print("<html>")
print("<head>")
print("<title>Personal Tax Calculator</title>")
print("</head>")
print("<body>")
print ("<h2>Your personal income is %s</h2>" % income)
print("</body>")
print("</html>")




