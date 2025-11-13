# Information for compiling

## Pandas 
I created these files to be run in a virtual environment to get around the pip3 "externally-managed-environment" error.
You can run them the same way I did by following these steps.

1. Set up the virtual environment. Within your project directory, open terminal and enter:

```python3 -m venv <your_project_name>  ```

2. Activate the environment, telling your computer to "look there" for the files.

```source <your_project_name>/bin/activate ```

3. Install pandas in the new virtual environment

```pip3 install pandas```

4. Check your install

```pip3 list```

5. When you're done, deactivate the virtual environment

```deactivate```

6. To restart the environment, repeat step 2 within your project directory.


## matplotlib

To run the matplotlib exercises in this folder, the same setup can be used with one change.
Repeating the steps above, set up and activate the Virtual Environment.

For step 3, install matplotlib.

```pip3 install pandas```

Follow the rest of the steps, double checking your install. 