**Steganography** is a process of hiding a file, an image, a video, a text inside another file.

We can concatenate/hide files using the `cat` command.

for example, we want to hide script.zip and get.jpg into show.jpg

`cat script.zip get.jpg > show.jpg` 

In order to undo this concatenation. We can use the command:

`unzip show.jpg`

