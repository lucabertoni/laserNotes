# laserNotes

Take your notes with laserNotes and share them on all your devices

## Directory structure
```
.
├── classes
│   ├── Database.py
│   ├── LaserNotes.py
│   ├── LogBuffer.py
│   ├── Server.py
│   └── Socket.py
├── laserNotes-server.log
├── provaProcessi.py
├── provaSock.py
├── README.md
├── server.py
└── settings.py

```  

_classes_: It contains all the classes used in the server, like: LaserNotes, Database, Server, ...  
_server.py_: This is the **main** file.

## Requirements
* Linux  
* Python3  
* PyMySQL ([github repo here](https://github.com/PyMySQL/PyMySQL))  
* Mysql (server)

## How to run the server
An installer will be ready soon. Until it is not ready, follow this steps to have your server running:  
1. Download and install requirements.  
2. Clone/Download this repository or download server package from releases  
3. Import the database from database/ directory using mysql  
4. If you have downloaded all the repository, "cd" into src/server/.  
5. Run "python3 server.py"  

## Contributors
Luca Bertoni

## Info/Contacts:
**Authors**: Luca Bertoni, Andrea Lucchini  
**Version**: 0.9-unstable  
**Contacts**:  

	Email: luca.bertoni24@gmail.com

	Facebook: https://www.facebook.com/LucaBertoniLucaBertoni