# Write a Python program to accept a filename from the user and print the extension of that. Go to the editor Sample filename
filename = input("Input the Filename: \n")
f= filename.split(".")
print(f)
print((f[1]))