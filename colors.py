from PIL import Image

img = Image.open("provinces.bmp")

max_colors = 1000

print(img.getcolors(max_colors))


file = open('output.txt',"w")

count = 1

file.write(f'{img.getcolors(max_colors)}')

with open('output.txt', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('), ', '\n')
filedata = filedata.replace('[', '')
filedata = filedata.replace(']', '')

# Write the file out again
with open('output.txt', 'w') as file:
  file.write(filedata)

with open('output.txt', 'r') as file:
    x = len(file.readlines())
    print('\nTotal lines:', x) # 8

f = open('output.txt','r+')
lines = f.readlines() # read old content
f.seek(0) # go back to the beginning of the file
f.write("Output: (pixels, (R, G, B)); Unique colors: {}\n".format(x)) # write new content at the beginning
for line in lines: # write old content after new
    f.write(line)
f.close()

file.close()