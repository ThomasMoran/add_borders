- Little script to add borders to all photos in a folder
- Output files will be added to a new sub folder "with_borders"

Make executable and add to $PATH:
```
cd add_borders
chmod +x add_borders.py
ln -s /path/to/repo/add_borders.py /path/to/executable/folder
```

I use oh-my-zsh so I add an alias
```
echo $ZSH_CUSTOM
alias add_borders="~/path/to/executable/folder/add_borders.py"
```
