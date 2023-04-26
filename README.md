# README
This repo is my place for storing examples I use in demos for AI workshops, screencasts, etc.

To run the examples, you NEED to create an .env file in the root and add whatever of these keys you want to work in the various scripts and notebooks.
```
OPEN_API_KEY=sk_XXXXXXXXXXX
```
# Python
Setting up Python. Lots of this stuff can be used in ways other than running it directly on your computer. I do some of those things, but pretty much every one of those other ways comes with some restriction or thing that I do that doesn't work. So, I run this stuff that way.

## Pyenv
I use pyenv to manage the versions of Python. Some things work in one version that don't in another. For most of these demos, I'm running the latest version of Python 3.10.
### Windows
On Windows, set up pyenv using this: https://github.com/pyenv-win/pyenv-win

### Mac/Linux/Etc
On Mac and other UNIX systems, install https://github.com/pyenv/pyenv

# Tools
How I work with these things is in VSCode. I use the Python and Jupyter notebooks plugins, but also the following additional plugins you'll likely see me use in demos/workshops:

* Rubberduck - https://github.com/rubberduck-ai/rubberduck-vscode
    This puts ChatGPT chat window directly into VSCode
* AI Genie - https://github.com/ai-genie/chatgpt-vscode
    This puts ChatGPT in VSCode in a slightly different way, including the ability to highlight code and ask for an explanation of what it does, find problems, optimize, etc.