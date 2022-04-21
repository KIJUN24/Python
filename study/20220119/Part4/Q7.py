f = open("test3.txt", 'r')
body = f.read()
f.close()

body = body.replace("java", "python")

f = open("test3.txt", 'w')
f.write(body)
f.close()