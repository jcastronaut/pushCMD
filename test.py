import sys
print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])
print("testing python docker")
f = open("note.xml","r")
a =f.read()
a = a.replace("${PORT1}",sys.argv[1])
a = a.replace("${PORT2}",sys.argv[2])
a = a.replace("${PORT3}",sys.argv[3])
a = a.replace("${PORT4}",sys.argv[4])
print(a)
f = open("note2.xml","w")
f.write(a)
f.close()
