# Extract phone numbers & email ids

This script accepts data either directly from the *clipboard* or from the *user* and extracts all the **India-format phone numbers and email ids** from the data. It then stores the extracted information in a **text file** (in the same folder as the scripts) along with a date and time stamp. This is done by using the regular expressions module.

Make sure you have the ```pyperclip``` module installed before running this script.

````
pip install pyperclip
````

You can read more about this module in its [official documentation](https://pyperclip.readthedocs.io/en/latest/) or the [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/2e/chapter7/) book.

Read more about using *pip* for different operating systems [here](https://pip.pypa.io/en/stable/user_guide/).

### Further modifications

If you want to change the code for your country, a change of expression only in the ``phoneRegex`` object is required. You can try out regular expressions for better understanding [here](https://regex101.com/).

