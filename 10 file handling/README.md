# Files and directories

Files and directories is a very important topic in general. Most of us work with files and directories on a daily basis. We use files to store data and directories to organize our files.

There are many different types of files and things to consider when working with files.

Python has a lot of built-in functionality to work with files and directories. We will cover the most important ones in this chapter.

## Introduction

In this chapter you'll be able to:

- Understand why files and directories are important.
- Explain the difference between files and directories.
- Create and read files and directories.
- Work with different types of files.

## Narrative: Captain's log?

_ As you board the derelict Arkship, you're trying to figure out what happened to the crew. You find its logs, but they're corrupted. You need to rebuild the logs to find out the fate of the crew._

<div>
    <img src="./assets/Chapter4.jpeg" width="600" alt="File vault">
</div>

## What is a file and a directory?

**Tabitha**: "I've just boarded the Arkship, the readings I have says oxygen levels are low but stable"

**Ship**: "Great, next step is to find a way to interface with the ship mainframe, then try to access the logs"

**Tabitha**: "I'm on it, how do I access the logs?"

**Ship**: "The logs are stored in files, so we need to have a crash course in files and directories"

- **File**: A file is a named location on disk to store related information. It is used to permanently store data in a non-volatile memory (e.g. hard disk).
- **Directory**: A directory is a location for storing files on a computer. In most operating systems, directories are known as folders.

Files and directories are important because they allow us to store data in a structured way. We can use files to store data and directories to organize our files.

## Working with files and directories

**Ship**: "Now that you know what files and directories are, let's see how you can work with them."

Here's the most common operations you're likely to carry out when working with files and directories.

- **Open**, this one of the most common operations you'll do when working with files. You open a file so that you then can read or write to it.
- **Read**, reading a file is a common operation. Things like reading a configuration file or reading a log file are common operations. 
- **Write**, writing to a file means you're adding content to existing content or you're overwriting existing content.
- **Close**, when you're done with a file, you should close it. This is to ensure that the file is not locked and that other processes can access it.
- **Create**, creating a file is a common operation. You might want to create a file to store data.
- **Delete**, deleting a file is a common operation. You might want to delete a file to remove data.

**Tabitha**: "Got it, I guess I need to mainly need to focus on reading files and directories to find the logs?"

**Ship**: "Yes, that's correct. However, depending on the state of the logs, you might need to write to the files as well."

## Open a file

**Ship**: To open a file, you use the built-in function `open()`. The `open()` function takes two arguments, the first argument is the path to the file you want to open and the second argument is the mode you want to open the file in. However, it's possible to open a file without specifying the mode. If you don't specify the mode, the file will be opened in read-only mode.

Here's code that opens a file in read-only mode:

```python
f = open('logs.txt') # open with no mode specified, defaults to read-only mode

f = open('logs.txt', 'r') # open with read-only mode specified
```

**Tabitha**: "What if the file doesn't exist?"

**Ship**: The above code opens a file called `file.txt` in read-only mode. The file must exist, otherwise you'll get an error.

The `f` variable is a file object. From a file object you can read the contents of the file but you can also write to the file, providing the file is opened in write mode. Other information you can get from a file object is the name of the file, the mode the file is opened in and the encoding of the file.

**Tabitha**: "I'm accessing a data port here, looks like it's listing some files:"

```text
backup.zip
logs.txt
.config
```

**Tabitha**: "How to read its contents?"

**Ship**: "There's a few things to consider when reading a file, let's go through them."

## Reading a file

**Ship**: So far, we've learned to open a file.Once you have a file open you can read the contents of the file. At this point, there's a few approaches to choose from:

- **Read the entire file at once**. This is a good approach if the file is small, but terrible if the file is large that is larger than the available memory.
- **Read the file line by line**. A probably safer approach than reading the entire file at once, but still not great if the file is large.
- **Read the file character by character or word by word**. You want to read the file this way if you want to process the file in a specific way.
- **Read the file in chunks**. So far we covered common approached reading text files, but what if you want to read a binary file? In that case, you want to read the file in chunks. A chunk is a part of the file, usually a fixed size in bytes. This is also a good approach for text files, especially if the file is large.

Let's look at each of these approaches in more detail via code.

### Read the entire file at once

**Ship**: To read the entire file, you use a file object's `read` method, like so:

```python
f = open('logs.txt', 'r')
content = f.read()
```

At this point, the entire file is read into memory and stored in the `content` variable. You can then process the file in any way you want. The maximum size of the file you can read this way is limited by the amount of memory you have available.

**Tabitha**: "Trying that on *logs.txt*, let's see what we get:

```text
*** Arkship 7 ***

Captain's log, stardate 2083.10.01

I'm the only one awake, the rest of the crew is in cryosleep. The ship is on autopilot, heading to the nearest star system. I'm about to go into cryosleep myself, but before I do, I'll make a final entry in the log.

Captain out.

Captain's log, stardate 2084.02.11

I've just woken up from cryosleep. The ship is indicating intermittent power failures. I need to investigate.

Captain out.

** Corrupted data **
``` 

**Tabitha**: "Looks like they were struggling with power failures. It's all corrupted after that.  Ship, ideas?"

**Ship**: "See if you can locate ships logs, you might need to try reading that backup.zip file"

### Read the entire file into a list

**Ship**: "Let's learn another way to read the file, this time we'll read the entire file into a list, this is useful if you want to process the file line by line."

You can use to read the entire file is the `readlines()` method. `readlines()` reads the entire file into memory and stores it in a list, which could be great if you want to process the file line by line. It might even be preferred to use `readlines()` over `read()`. Here's an example:

```python
f = open('logs.txt', 'r')
lines = f.readlines()
for line in lines:
    print(line)
```

> [!WARNING]
> Be careful when reading large files, you might run out of memory.

**Tabitha**: "I'll remember that"

In below example, it's using `readline` to read the file line by line. It also performs a check to see if `line` is empty, which it will be when it reaches the end of the file.

```python
f = open('file.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)
```

There's also another way for us check if we've reached the end of the file, namely by using the `tell` method. Here's an example:

### Read the file character by character/word

**Ship**: It's entirely possible to read the file by specific units, like character, word, or paragraph. Here's an example:

```python
f = open('file.txt', 'r')
while True:
    char = f.read(1)
    if not char:
        break
    print(char)
```

Above we pass 1 as an argument to the `read` method. This means that we're reading the file character by character. 

**Tabitha**: "When would you want to read a file character by character in the context of spaceship logs?"

**Ship**: "Usually this is done when you want to process the file in a specific way, like for example if you want to count the number of characters in the file. It also doesn't read the entire file into memory, which is good if the file is large."

### Read the file word by word

**Ship**: To read the file in a different way like word by word, you need to split it into words, like so:

```python
f = open('file.txt', 'r')
while True:
    line = f.readline()
    words = line.split()
    for word in words:
        print(word)
    if not line:
        break
```

**Tabitha**: "Sounds like I should be using this approach to read the logs"

### Read the file in chunks

**Ship**: "As I said before, reading the entire file at once is not a good idea unless you know the file size is small"

**Tabitha**: "What if the file is large, what can happen?"

**Ship**: "If the file is large, you might run out of memory. A better approach is to read the file in chunks. A chunk is a part of the file, usually a fixed size in bytes. 

```python

# open image file in binary mode
f = open('image.jpg', 'rb')
list = []
while True:
    chunk = f.read(1024)
    if not chunk:
        break
    print(chunk)
    # store chunk in a list
    list.append(chunk)
    f.close()
# save chunks to a new file
with open('new_image.jpg', 'wb') as f:
    for chunk in list:
        f.write(chunk)

```

**Tabitha**: "I see, looks like a better approach if we're dealing with content that's images, videos and not text?"

**Ship**: "Exactly, you can also use this approach for text files, especially if the file is large."

In the above code:

- We open the image file in binary mode, `rb`.
- Then proceeded to read the file in chunks of 1024 bytes.
- Each chunk is stored in a list.
- Finally, we write the chunks to a new file.  

## Adding robustness

**Ship**: It's unfortunately not enough to just list files and reading them, many things can go wrong and we need to handle these errors. Here are some common errors you might encounter when working with files:

- **File not found**, if the file doesn't exist, you'll get an error.
- **Permission error**, if you don't have permission to open the file, you'll get an error.
- **File is locked**, if the file is locked by another process, you'll get an error.
- **File is too large**, if the file is too large, you might run out of memory.
- **File is corrupted**, if the file is corrupted, you might not be able to read it.

Let's address some of these errors.

**Ship**: We mentioned that if the file doesn't exist, you'll get an error. You can handle this error by using a `try` and `except` block. Here's an example:

```python
try:
    f = open('file.txt', 'r')
except FileNotFoundError:
    print('The file does not exist')
```

Here you see that we're using a `try` and `except` block to handle the error. If the file doesn't exist, we print a message to the user.

### Checking for file existence

**Ship**: It's possible to check for a file's existence before trying to open it. Doing so saves you from having to handle an error. Here's an example:

```python
import os

if os.path.exists('file.txt'):
    f = open('file.txt', 'r')
else:
    print('The file does not exist')
```

**Tabitha**: "Ok, noted"

### Permission error

**Ship**: However, there's another reason why might get an error from trying to open a file, namely if you don't have permission to open the file. Also this can be handled by using a `try` and `except` block. Here's an example:

```python
try:
    f = open('file.txt', 'r')
except PermissionError:
    print('You do not have permission to open the file')
```

You can check your permissions before trying to open a file. Use the `os.access` function to check if you have the rights to open it. Here's an example:

```python
import os

if os.access('file.txt', os.R_OK):
    print('You have permission to open the file')
else:
    print('You do not have permission to open the file')
```

**Tabitha**: "Yea that just happened when I tried to open the .conf file"

### Combining the two error handling approaches

**Ship**: Now that we've seen how to handle errors when opening a file, let's combine the two approaches. Here's the code for that:

```python
import os

file_name = 'logs.txt'

if not os.path.exists(file_name):
    print('The file does not exist')
elif not os.access(file_name, os.R_OK):
    print('You do not have permission to open the file')
else:
    f = open(file_name, 'r')
```

> [!NOTE]
> As you can see, you can't just assume that you'll be able to open a file, make your code robust by handling errors.

**Tabitha**: "I'm going to first copy the backup.zip file to my local device but I'll also try to locate other data ports to see if I can find the ships own logs"

## Write to a file

**Ship**: "Ok, meanwhile, let' learn how to write to a file. Writing to a file is similar to reading a file. You use a file object's `write` method.

You use a file object's `write` method, like so:

```python
f = open('logs.txt', 'w')
f.write('Captain\'s log, stardate 2083.10.01')
f.close()
```

As you can see from the above code:

- We're opening the file in write mode, `w`. 
- Then we write the string `Hello, World!` to the file.
- Finally, we close the file.

> [!NOTE]
> If the file doesn't exist, it will be created. If the file already exists, it will be overwritten.  

**Tabitha**: "Ok, seems I can destroy the logs if I'm not careful."

**Ship**: "Correct. So word of caution, if you're writing to a file, you need to be careful not to overwrite the file. If you do, you'll lose the contents of the file. To avoid this, you can use the `x` mode, which will raise an error if the file already exists. Here's an example":

```python
try:
    f = open('logs.txt', 'x')
    f.write('Captain\'s log, stardate 2083.10.01')
catch FileExistsError:
    print('File already exists')
```

The above approach, is one way of handling accidental overwrites. Another way is to append to a file.

## Append to a file

Appending to a file means that you're adding to the end of the file. Of you're trying to add to a file log for example, you don't want to overwrite the file, you want to append most likely.

To append to a file, you use a file object's `write` method, with the file mode set to `a`, like so:

```python
f = open('logs.txt', 'a')
f.write('Captains log, stardate 2083.10.01')
f.close()
```

**Tabitha**: "Definitely don't want to overwrite the logs, I'll remember this one"

## Close a file

**Ship**: You've seen so far that we're closing the file after we're done reading or writing to it by calling `close`. This is important, because if you don't close the file, you might run into issues. What can happen is that the file is still open, and you try to open it again, but you can't because it's already open. This is called a resource leak. 

To avoid resource leaks, you need to close the file after you're done with it like so:

```python
f.close()
```

There is a better approach however, using `with`.

## Using the "with" statement

**Ship**: We've established so far that using `close` function is important to do, but it's also easy to forget. To avoid you forgetting to call `close`, you can use the `with` statement. Here's an example:

```python
with open('logs.txt', 'r') as f:
    print(f.read())
```

> [!NOTE]
> What happens is that the file is opened, and the file object is assigned to the variable `f`. Then the `with` statement takes over, and when the `with` statement is done, the file is closed automatically. How this works internally is that the `with` statement calls the `__enter__` method of the file object, and when the `with` statement is done, it calls the `__exit__` method of the file object.

## Working with file paths

**Ship**: "I think we need to build a more general tool to help you locate the logs, let's see how we can work with file paths."

So far, you've seen how we access files by calling `open`. But what if the file is in a different directory? How can we locate the file correctly? Well, there are a few ways to do this:

- **Absolute path**. The absolute path is the exact location of the file. For example, `C:\Users\username\Documents\file.txt`.
- **Relative path**. A relative path is relative to the current working directory. For example, a file called `file.txt` in the current working directory. If said file would be located one level up, you would use `../file and for a subdirectory you would use`subdir/file.txt`.
- **Current working directory**. The current working directory is the directory from which you're running your script.

> [!NOTE]
> There's one thing to note about paths, and that is that they are different on different operating systems. On Windows, you use backslashes, `\`, and on Linux and macOS, you use forward slashes, `/`. You don't want to hardcode paths in your code, because it will break on different operating systems.

### Introducing the `os` module

To work with paths in safe way, we should be using the `os` module. This module contains functions that allow us to work with paths. Here's an example:

```python
os.path.join('path', 'to', 'logs.txt') # combines the paths into a single path, in this case 'path/to/logs.txt'
os.path.abspath('logs.txt') # returns the absolute path of the file, in this case '/home/user/logs.txt'
os.path.dirname('path/to/logs.txt') # returns the directory name of the path, 'path/to
os.path.basename('path/to/logs.txt') # the base name of the path, 'logs.txt'
os.path.exists('path/to/logs.txt') # returns True if the path exists, False otherwise
os.path.isfile('path/to/logs.txt') # returns True if the path is a file, False otherwise
```

Let's use the `os` module to open a file in a safe way. We try to open a file *config.json* in the `logs` subdirectory if it exists, otherwise rely on the default configuration:

```python
import os

log_file_path = os.path.join('logs', 'logs.txt')

# Read logs from the starship logs file if it exists
if os.path.exists(log_file_path):
    with open(log_file_path, 'r') as f:
        logs = f.read()

# Do something with the logs
print("Starship Logs:")
print(logs)
```

Above, you can see how we leverage several methods from the `os` module:

- `os.path.join` to combine the paths.
- `os.path.exists` to check if the file exists.
- `with` statement to open the file in a safe way.

## File info

**Tabitha**: "I've located the ships logs, but I could use some more information about file sizes and permissions, is that possible?"

**Ship**: "Of course, there are some common things you can get from a file, like file size, permissions, owner, etc.

- **File size**, file size can be useful to determine if the file is too large to process. It's also an interesting statistic to know, if you for example need to know how much space a directory takes up.
- **File permissions**, knowing beforehand if you can read, write or execute certain files can be useful.
- **File owner**, knowing who owns the file can be great to know, especially if you need to contact the owner.  
- **File creation date**, when something was created is something a user checks often.
- **File modification date**. Just like with creation date, knowing when something was modified is useful.
- **File access date**. Seeing when a file was last accessed could be to detect if a file is stale or not.
- **File type**, it's common to sort files by type, like text or image files.
- **File extension**, knowing the extension can help determine its type.     
- **File name**, it's quite often that we search for files by name.

**Tabitha**: "What about files specifically?"

**Ship**: "Yes, so you can use `os.stat` to get information about a file. This function returns a `stat_result` object, which contains all the information about the file. Here's some code demonstrating this:

```python
import os

stat = os.stat('logs.txt') # returns a stat_result object
# stat, st_size, st_mode, st_uid, st_gid, st_atime, st_mtime, st_ctime
```

When you called the above code, you got a `stat_result` object back. This object contains all the information about the file. Here's what response looks like:

- `st_size` is the size of the file in bytes.
- `st_mode` is the file mode, which contains the file permissions.
- `st_uid` is the user id of the owner.
- `st_gid` is the group id of the owner.
- `st_atime` is the last access time.
- `st_mtime` is the last modification time.
- `st_ctime` is the creation time.

**Tabitha**: "Trying this on the ships logs, let's see what we get"

```python
import os

stat = os.stat('ship-logs.txt') # returns a stat_result object

print(f'Size: {stat.st_size}') # 10MB
print(f'Permissions: {stat.st_mode}') # 0o100644 = -rw-r--r--
print(f'Owner: {stat.st_uid}') # Ship
print(f'Last modified: {stat.st_mtime}') # 2085-03-11 12:00:00
print(f'Last accessed: {stat.st_atime}') # 2085-03-11 12:00:00
print(f'Created: {stat.st_ctime}') # 2083-01-01 12:00:00
```

**Ship**: "Great, you can see that you can get a lot of information about a file. That's a large file, 10MB, I recommend not reading it all into memory at once."

**Tabitha**: "Noted, I'll be careful"

## Directories

**Ship**: "I've talked about files so far. But directories are also important, and you'll often need to work with them. In fact, directories and files are very similar, and you can use the same functions to work with them. The reason why that is is because directories are just a special type of file that contains other files."

**Ship**: "When I mentioned we needed a generic tool for you to locate the logs, I was also thinking we could be looking for images, videos, and other files and a program could efficiently locate them, as that may contain further evidence what happened to the ship and its crew. So let's learn about directories and then get to work on that tool."

### Working with directories

**Ship**: "Here are some common operations you can do with directories:

- Create a directory, you can create a directory using the `os.mkdir` function.

   ```python
    import os

    os.mkdir('directory') # creates a directory called directory
    ```

- Create a directory and subdirectory, you can create a directory and a subdirectory using the `os.makedirs` function.

   ```python
    import os

    os.makedirs('directory/subdirectory') # creates a directory called directory and a subdirectory called subdirectory
    ```

- Check if a directory exists, you can check if a directory exists using the `os.path.isdir` function.

   ```python
    import os

    os.path.isdir('directory') # returns True if directory exists, False otherwise
    ```
   
- Remove a directory, you can remove a directory using the `os.rmdir` function.

    ```python
     import os
    
     os.rmdir('directory') # removes directory
     ```

Now that we've seen some common operations for working with directories, we need to remember that the same rules apply as with files, meaning:

- Working with paths is the same as working with files. Construct paths using `os.path.join`, and check if a path exists using `os.path.exists`.
- The same errors can occur when working with directories. For example, if you try to create a directory that already exists, you'll get a `FileExistsError` exception. Check if a directory exists, or you have permission to create it, before creating it.

### Directory info

**Ship**: So far, you've seen how you can get information about a file. But what if you want to get information about a directory? Well, you can do that too:

```python
import os

stat = os.stat('directory') # returns a stat_result object
```

### A practical example - a CLI tool for a directory

**Tabitha**: "You mentioned a tool to help me locate the logs, how would that work?"

**Ship**: "Yes, so the idea is to search through directories and files for keywords and even name of files and directories, for things like \"logs\" \"images\" and so on. You can use the `os.listdir` function to get a list of all the files and directories in a directory. Here's an example:

```python
import os

os.listdir('directory') # returns a list of all the files and directories in directory
```

**Tabitha**: "I see, what about the search part?"

**Ship**: "You can use the `os.walk` function to search through directories and files. Here's an example:

```python
import os

for root, dirs, files in os.walk('directory'):
    for file in files:
        if 'logs' in file:
            print(file)
```

The preceding code will search through all the files in the directory, including sub directories, and print the file if it contains the word 'logs'.
  
## Compression

**Ship**: We have one more topci to cover before we can start building the tool, and that is compression. Some files might be compressed, and in some other cases you might need to compress a set of files to a single file, when you're creating a backup for example.

There are a few different formats for compressing. Here are some of the most common ones:

- **gzip, zip**, is a compression algorithm that uses the DEFLATE algorithm. It's a lossless compression algorithm, meaning that the original data can be reconstructed from the compressed data. It's a good choice for compressing text files.
- **bzip2**, is a compression algorithm that uses the Burrows-Wheeler algorithm. It's also a lossless compression algorithm. 
- **lzma**, is a compression algorithm that uses the LZMA algorithm. It's also a lossless compression algorithm.  
- **tar**, is not a compression algorithm, but a file format that combines multiple files into a single file. It's often used in combination with gzip or bzip2 to compress the files.  

**Tabitha**: "I see, so how do I compress a file?"

## Working with zip files

**Ship**: "Right, let's start with zip files. Zip is a common compression format, and Python has a built-in module to work with zip files. With this module, you can create zip files, extract files from zip files, and more. Let's see how we can create a zip file:

### Creating a zip file


```python
import zipfile

zipfile.ZipFile('all-logs.zip', 'w').write('logs.txt') # creates a zip file called file.zip and adds file.txt to it
```

Above, you can see how we:

- Import `zipfile` module.
- Call `zipfile.ZipFile` to create a zip file called `all-logs.zip`.
- Finally, we call `write` to add `logs.txt` to the zip file.

It's possible to add multiple files to the zip file by calling `write` multiple times.

**Tabitha**: "Ok, I see where you're going with this, I can take all the log files and put it into a zip file, that makes for easier transportation and smaller size right?"

**Ship**: "Yes, exactly that. However, it could be good to learn about how to extract these compressed so you can search them"

### Extracting files from a zip file

**Ship**: The other interesting use case is to extract files from a zip file. To extract files from a zip file, we can use the `extractall()` method:

```python
import zipfile

zipfile.ZipFile('all-logs.zip', 'r').extractall('path/to/extract') # extracts all files from file.zip to path/to/extract
```

**Tabitha**: "Ok, so call this to extract a file into many files and then we search through them?"

**Ship**: "Correct. You can also extract a single file from a zip file by calling `extract`.

### Adding and removing files from a zip file

**Ship**: What else can we do with zip files? Well, we can also add files to an existing zip file, and we can also remove files from a zip file. Let's see how we can add files to an existing zip file:

```python   
import zipfile

with zipfile.ZipFile('all-logs.zip', 'a') as zip_file:
    zip_file.write('file.txt')

# or
zipfile.ZipFile('all-log.zip', 'a').write('logs.txt')

# remove
zipfile.ZipFile('file.zip', 'a').remove('logs.txt')
```

**Ship**: What if we just want to see what's in a zip file? We can use the `namelist` method to get a list of all the files in a zip file:

```python
import zipfile

zipfile.ZipFile('file.zip', 'r').namelist() # returns a list of all the files in file.zip
```

**Tabitha**: "Now can I start building the tool?"

**Ship**: "Yes, we've covered all the basics you need to know to build the tool." 

## Assignment

This tool will need to work in the following way:

- You should be able to specify what you're looking for, like logs, images, videos, etc. It should be able to take more than one keyword.
- It should search through a given directory and its subdirectories for the keywords.
- You should be able to compress a search results into a file. For example if the key word is found in files log.txt and ship.txt you should be able to save that in all-files.zip

## Solution

[Solution](./solution.py)

## Quiz

**Question**: What do you need to consider when creating directories?

1. The same rules apply as when working with files. You need to check if the directory exists, and you need to check if you have permission to create it.
2. You need to check if the directory exists.
3. You need to check if you have permission to create the directory.

[Solution quiz](./solutions/solution-quiz.md)

## Summary

In this chapter, we covered how to work with files. We saw how to read and write files and also how to find out information about files.

We also looked into directories and how they were similar to files in that they had some operations and rules in common as directories are just a special type of file that contains other files.

Finally, we saw how to work with zip files and how to add and remove files from them.

In the next chapter, we'll look into classes and objects, which are the building blocks of object-oriented programming. If you want to structure your code in a way that makes it easier to maintain and extend, it's a good idea to learn about classes and objects.

 