Personal Text

This basic script lets you write your personal text inside a textpad. It needs a password to enter into the text pad. The text is auto saved on closing (Alt+F4 in WINDOWS (OR) clicking close-'X' button (OR) CMD+Q in MAC).

The text is stored in the database in encrypted format. The encrypting here used is very basic encryption.
You can change the database storing path, password as you want inside the script. Then, convert it to the executable using "pyinstaller" with following command:

	pyinstaller --onefile --noconsole --windowed main.py --name <.exe file name>
	
The attached application is the test application (password - 1234). 
The application opens a bit slow.