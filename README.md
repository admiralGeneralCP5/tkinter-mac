# Get Tkinter to Work on Mac
* If your python program using Tkinter fails on mac,  your python may not be configured for Tkinter. This can be resolved by installing a package through HomeBrew. 
* If you're using graphics.py you will need Tkinter installed becuase graphics.py imports Tkinter. 

---

#### Note:
```pip3 install tk``` **DOES NOT** install Tkinter. It will install TensorKit which is a completely different package. 

---

## Step 1: First Check if Homebrew is Installed
In the terminal type the following command to see the version of brew (homebrew) is installed. 
```
brew --version
```
If the version is returned, like below, then brew is installed. [Go to Step 2.](#step-2-update-brew) 
```txt
Homebrew 4.2.9
```
If the command is not found, install brew with:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
For more info on brew: [Homebrew](https://brew.sh)

---

## Step 2: Update Brew
Updating brew will give brew an updated list of packages that can be installed or upgraded.
```
brew update
```

---

## Step 3: Install Tkinter with Brew
```
brew install python-tk
```
After brew finishes installing python-tk, Tkinter should work. 

"test_file.py" is a simple program to convert a value in inches into meters and can be used to find out if Tkinter is functioning.

---
<br>

---

## Working with graphics.py
There are two ways to access the graphics module, through pip or manually creating the file.

Using pip is a much easier way to install and use python modules and is the recommended option. Manually creating the file requires you to keep a copy of the file in each directory, of every program, that accesses the graphics.py module. This will work with MacOS and Windows, but just use pip instead of pip3 for Windows. 


### Using pip:
```
pip3 install graphics.py
```
Now graphics.py can be imported into your program. A separate graphics.py file in the same direcory as your main file is not necessary.

"test_file_graphics.py" can be used to find out if graphics.py and Tkinter are functioning.
