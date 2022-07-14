# Rick and Morty Projet

## <span style="color:orange">Authors</span>
Boris Le Bon

## <span style="color:orange">Project description</span>

Creating an API REST that allow users to do commentary on the characters and episodes of the univers of Rick&Morty.

## <span style="color:orange">What is needed/what is used</span>

Python 3.9+ is needed (i use python 3.9.7).  
fastapi  
uvicorn  
pydantic  
passlib  
bcrypt  
python-jose  
python-multipart  
pandas  
sqlalchemy  

SQLite need to be installed follow the download and install process at this link https://www.sqlite.org
or follow https://www.servermania.com/kb/articles/install-sqlite/

## <span style="color:orange">Comment about my work</span>

<span style="color:Cyan">1 create database, table and import json to the database (started at 18h30 monday 27 july, over at 23h the same day)</span>  
    - found mysql, install it and start to create a localhost database  
    - found mysql way to import and create the file to create table  
    - difficulty : table episodes have a column that seems to be a date, but the format is not.  
    - solution : right now just created as varchar  
    - found a way to import json in internet and create the file to import the json file to import it in the database.  
        - difficulty : there is apostrophy in the database ! the code understand it like the end of the varchar  
        - solution : found on internet a way to avoid that adding another apostrophy near exemple : ''  
    - created the readme file.  
    -overhall mysql allow me to do the job except it won't work in other computer who don't have the database, replace
    mysql solution by SQLite to have the database in the project directly. code remains the same for the biggest part.  
    - found harder to install SQLite on a mac when never used before.  

<span style="color:Cyan">2. create path listing episodes and a path listing the characters. ( started 18h20, finished 19h tuesday)</span>  
    - difficulty : again SQLite create an error (same thread) while using it with the dal/characters_dal  
    - solution : searching on internet to avoid this error and found check_same_thread = False   

<span style="color:Cyan">3. brainstorming about architecture tables of the crud comment :</span>  
    - will create a table user ( with id and user_name)  
    - will create a table comment linked to user_id foreign key, column character id, column episode_id, will index  
    - the CRUD will need to link all but if even if the character_id or episode_id can be null, both can't be null

<span style="color:Cyan">4. Creation of the comment table and user table, creation of the path and the post creation of the comment</span>  
    - Difficulty : needed more documentation about pydantic (validator)  
    when return None, the database doesn't understand  
    concerning the edit i pass for now, we need user authentification so the SQL can remain it in order to do so. ( code is still written for futur modification)  
    - solution : learn pydantic validator's syntaxe
                 add or "Null" value for creation
                
<span style="color:Cyan">5. create page was not difficult, create a filter with LIKE was easy to find.</span>

<span style="color:Cyan">6. took the time to read documentation, and decide to modify the path to get_comment_by_chatacter_in_episode
by a query ( just to know that well, i know)</span>
                 
## <span style="color:orange">How to use this API</span>

WARNING : the data has been git in 3 Branch.
- the main branch is only the mandatory part
- the second branch continue the work adding the optional part
- the 3dn and final branch is THE COMPLETE WORK where I decide to refactor the code using alchemy orm

### <span style="color:orange">create env folder to install everything</span>

1. to create the env folder, in the terminal enter :  
`python -m venv env`

2. to activate the env environement, in the terminal enter :  
`cd env`  
`source bin/activate`

3 go back to the previous folder, in the terminal enter :  
`cd ..`

4. to install everything from the file requirement.txt, in the terminal 
- for mac enter :  
    `pip3 install -r requirement.txt`
- for pc enter :  
    `pip install -r requirements.txt`

05. if needed, update the env folder, in the terminal enter :  
`pip install --upgrade pip`

### <span style="color:orange">the import folder</span>

01. in VSCODE: 
        open the folder "importation" and open the file "create_table.py" and execute it
        - this will create the database at the root of the project and import table on it
    OR
    in the terminal enter:  
        `cd importation`
        `python3 create_table.py`

02. in VSCODE:
        open the file import_to_db.py (same folder) and execute it
        - this will import the json file in the table of the database.
        - if you need to see manually the database you can open the link :
        http://inloop.github.io/sqlite-viewer/ or use the module sqlite explorer on vscode.
    in the terminal enter:
        `cd ..`
        `python3 importation/import_to_db.py`

### <span style="color:orange">general use</span>

you can run the api using uvicorn, on the terminal enter :
`uvicorn __init__:app --reload`  

by default it should be accessible using the link: http://127.0.0.1:8000  
and you should see the root path. for the next route, enter that same url then /nameoftheroute (exemple: http://127.0.0.1:8000/nameoftheroute)

### <span style="color:orange">searching the route characters and episodes</span>

- enter in the URL "http://127.0.0.1:8000/characters" to see the characters  
- enter in the URL "http://127.0.0.1:8000/episodes" to see the episodes

### <span style="color:orange">Create/edit/delete comment</span>

go to the URL : http://127.0.0.1:8000/docs and select the apropriate link :  
- post/Comments to create the comment:  
    click on "try it out"  
    enter the information in the request body and click on execute
- put/comments/{comment_id}
    click on "try it out"  
    enter the id of the comment you want to edit ( it will of course return an error if that id doesn't exist).  
    enter the information in the request body and click on execute.
- delete/comments/{comment_id}
    click on "try it out"  
    enter the id of the comment you want to delete ( it will of course return an error if that id doesn't exist).  
    click on execute

### <span style="color:orange">searching the route comments</span>

- enter in the URL "http://127.0.0.1:8000/comments" to see the comments

- enter in the URL "http://127.0.0.1:8000/comments/ch=idOfTheCharacter" to see the comment by character

- enter in the URL "http://127.0.0.1:8000/comments/ep=idOfTheEpisode" to see the comment by episode

- enter in the URL "http://127.0.0.1:8000/comments/filter=typeWhatYouWant" to filter the comment by what you want
