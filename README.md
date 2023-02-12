# mimir - `/ˈmiːmɪə(ɹ)/`
mimir is a software following the goal of boosting your productivity. The name derives from the norse god of wisdom "Mimir". 
Some may consider this program a virus, but I wish to digress.

## 📥 Installation
As of right now the installation requires git. Simply clone the repository using:
```
git clone https://github.com/Just5MoreMinutes/mimir.git
```
Once my website is done (whenever that will happen - if it even ever happens) there will be an installer for all my projects including this one.

## ❓ Usage
mimir is a Windows (linux WIP) command-line tool which can be controlled with a variety of commands. These are mostly used at runtime, and do not have to be passed as start arguments! Some, however, can be used as such arguments.


⚠ ***mimir requires Python `3.9+`*** ⚠

### ✔️ Starting the program
There are 2 main ways to start mimir as of right now, both of which will be reworked.
- *The good old `cmd` way*


Open the `./src` folder and type `cmd` in the address bar of your explorer. This will open a new terminal in the correct directory. Once the window is opened type:
```
python3 main.py
```
This will then start mimir. Check out [the commands](#commands) to see how to actually use mimir.
- *The other way*


Open the `./src` folder and find the `main.py` file. Then right-click it and find "Open with". Then select `Python 3.9`. This will automatically open a functioning instance of mimir in a new python terminal. Check out [the commands](#commands) to check how to use mimir.

### ⌨️ Commands
To actually make use of mimir, you will have to use some commands. There are some arguments which can be passed as starting arguments, the others will have to be used at runtime.

#### Starting arguments
```
C:/User/mimir> python3 main.py -<command>

OR

C:/User/mimir> python3 main.py --<command>
```
- `-h`/`--help`: The help command. This displays all commands and how to use them. *USAGE*: 
- `-s`/`--settings`: Displays the settings page where you can alter the behaviours of mimir.

#### Other commands


If you want to use other commands besides the help and settings command, you will be using them at runtime. They are indicated by either a `!` or a `?`, followed by the command and the argument:
```
│ 
├  !<command> [program-name]

OR

│ 
├  ?<command> [program-name]
```
*(Everything between `<>` is required. Everything in `[]` are not required in every command.)*
You can use the following commands as of right now:
- `a`/`add`: Add a program to the list of blocked programs. If it already is added, it will not be added again. (requires `[program-name]`)
- `r`/`remove`: Remove a program from the list of blocked programs. If it doesn't exist in the list, nothing will happen. (requires `[program-name]`)
- `c`/`clear`: Clear the list of blocked programs. No programs will be blocked once the program is started again.
- `s`/`start`: Start the program and block all instances of the programs in the blocked list.
- `exit`: End all processes and exit mimir.

## ⚙️ How does it work?
it doesn't. 


(section ***WIP***)