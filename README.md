# Maestro Uninstallation Script Documentation

This script is responsible for uninstalling the Maestro software versions (Maestro BPM, Maestro ERP, Maestro MCA, Maestro Nest) present on the system. It searches for directories where Maestro products may be installed, deletes the found files and folders, and logs the removal in a log file.

## Features

1. **Search for Maestro installation directories**: The script checks standard directories where Maestro products might be installed.
2. **File deletion**: The script iterates through the found directories and deletes all files and subfolders within them.
3. **Removal logging**: If the file removal is successful, the message "Maestro successfully removed" is recorded in the log file.
4. **Logs**: The log file is stored at `C:\Windows\Temp\Maestro_Uninstall_Log.txt`.

## Code Structure

### 1. Library Imports

```python
import os
import shutil
import time
```

These libraries are used for file and directory operations:
- **`os`**: For checking the existence of directories and file handling.
- **`shutil`**: For removing files and folders.
- **`time`**: For recording the date and time of the removal in the log.

### 2. Configuration Variables

#### Maestro product paths

```python
maestro_paths = [
    r"C:\Program Files\Maestro BPM",
    r"C:\Program Files (x86)\Maestro BPM",
    r"C:\Users\Public\Maestro BPM",
    r"C:\Program Files\Maestro ERP",
    r"C:\Program Files (x86)\Maestro ERP",
    r"C:\Users\Public\Maestro ERP",
    r"C:\Program Files\Maestro MCA",
    r"C:\Program Files (x86)\Maestro MCA",
    r"C:\Users\Public\Maestro MCA",
    r"C:\Program Files\Maestro Nest",
    r"C:\Program Files (x86)\Maestro Nest",
    r"C:\Users\Public\Maestro Nest"
]
```

These are the directories the script will check for installed Maestro products. The list covers several possible locations, including both 32-bit and 64-bit systems, as well as public folders.

#### Log file path

```python
log_path = r"C:\Windows\Temp\Maestro_Uninstall_Log.txt"
```

This is the path to the log file where the removal of Maestro will be recorded, if successful.

### 3. Functions

#### `log_remocao()`

```python
def log_remocao():
    """Logs only the message 'Maestro successfully removed' in the log file"""
    try:
        with open(log_path, "a") as log_file:
            log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Maestro successfully removed\n")
        print("Maestro successfully removed")  # Displays in the terminal
    except Exception:
        pass  # Ignores errors when writing to the log
```

This function is responsible for recording in the log file that Maestro was successfully removed, including the date and time of the removal. If an error occurs while writing to the log, it is silently ignored.

#### `excluir_arquivos(directory)`

```python
def excluir_arquivos(directory):
    """Deletes all files and folders within the provided directory"""
    removed = False
    for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            try:
                os.remove(os.path.join(root, name))
                removed = True
            except Exception:
                pass
        for name in dirs:
            try:
                shutil.rmtree(os.path.join(root, name))
                removed = True
            except Exception:
                pass
    return removed
```

This function walks through the given directory and deletes all files and folders inside. It returns `True` if any file or folder was successfully removed, otherwise `False`.

#### `desinstalar_maestro()`

```python
def desinstalar_maestro():
    """Uninstalls all detected versions of Maestro"""
    something_removed = False
    for path in maestro_paths:
        if os.path.exists(path):
            if excluir_arquivos(path):
                something_removed = True

    if something_removed:
        log_remocao()
    else:
        print("No Maestro version found.")  # No log is created
```

This function checks if any of the default directories contain installed Maestro products. If found, it calls the `excluir_arquivos()` function to delete the files. If at least one directory is removed, the `log_remocao()` function is called to log the removal. If no Maestro products are found, a message is displayed in the terminal.

### 4. Script Execution

```python
if __name__ == "__main__":
    desinstalar_maestro()
```

This line ensures that the script will only run when executed directly (not when imported as a module). It calls the `desinstalar_maestro()` function to start the uninstallation process.

## Usage

1. **Run the script**: Simply execute the script in a Python environment. It will attempt to locate and remove Maestro installations and log the removal.
2. **Check the log**: After execution, the log file at `C:\Windows\Temp\Maestro_Uninstall_Log.txt` can be checked to confirm the removals performed.

## Possible Improvements

- **More robust error handling**: In case of failure during file deletion or log writing, the script could log more detailed error information.
- **Additional checks**: The script could be modified to search other locations or perform permission checks before attempting deletion.

## Conclusion

This script was designed to streamline the removal of Maestro versions and ensure the process is recorded in a simple and effective way.
