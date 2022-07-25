# AutoZipper

## Introduction

This is the tool that can recursively zip/unzip your file with encryption.

* Zip 
    Create `n` layers of zip files, each layer has only one file XXXXXXXX.zip. The compressed file of each layer except the last layer are encrypted, and the password is the name of the compressed file of the next layer.

    For example, suppose we have created a two layers zip files by this tool to zip two files (a.txt & b.txt)
    The file structure will be like this:
    
    ```
    .
    └── AutoZipper_of_layer2.zip  ──────> pwd = 94857162    : layer 0
        └── 94857162.zip  ──────────────> pwd = 21435264    : layer 1
            └── 21435264.zip  ──────────> pwd = NONE        : layer 2
                ├── a.txt
                └── b.txt
    ```
    
    
* Unzip
    Extract the `n` layers of zip files recursively and leave files that are compressed in last layer.
    
    For example, we extract the `AutoZipper_of_layer2.zip` file above.
    The file structure will be like this:
    
    ```
    .
    ├── a.txt
    └── b.txt
    ```


## Usage
For windows user, there is a executable file `AutoZipper.exe` in the `Windows_Executable_File` folder.

If you don't want to execute the program by executing exe file, you can execute `main_window.py` to start the program.

```
python main_window.py
```

Notice : You may need to download the `pyzipper` package if you don't have it.

```
pip install pyzipper
```


## Screenshots

* Main Window

    ![](https://i.imgur.com/FkxatEi.png)

* Zip Window

    ![](https://i.imgur.com/XcoWV4U.png)

* Unzip Window

    ![](https://i.imgur.com/BLEuNox.png)
