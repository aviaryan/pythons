# NameOrderFix

Fixes a folder with contents ordered by numbers. It's hard to explain by words so let's take an example of a folder which has - 

```
ABC 1
ABC 2
..
..
ABC 10
ABC 11
```

Now some application you want to play all the files/folders in detects it in this order - 

```
ABC 1
ABC 10
ABC 11
ABC 2
ABC 3
..
```

The way to fix this is padding zeros in numbers such that all numbers are of uniform length.

```
ABC 01
ABC 02
ABC 03
..
ABC 10
ABC 11
```

The script does this. (Arghh)

And it works for both files and folders.

**NOTE** - It's safe to try the script, it asks a confirmation before actually renaming the files.