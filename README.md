# Rick and Morty Projet

## Authors
Boris Le Bon

## Project description

Creating an API REST that allow users to do commentary on the characters and episodes of the univers of 
Rick&Morty.

## What is needed/what is used

Python 3.7+ is needed (i use python 3.9.7).
FastAPI
uvicorn
pydantic

SQLite need to be installed follow the download and install process at this link https://www.sqlite.org
or follow https://www.servermania.com/kb/articles/install-sqlite/ 

## Comment about my work

01 create database, table and import json to the database (started at 18h30 monday 27 july, over at 23h the same day)
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

02. create path listing episodes and a path listing the characters. ( started 18h20, finished 19h tuesday)
    - difficulty : again SQLite create an error (same thread) while using it with the dal/characters_dal
    - solution : searching on internet to avoid this error and found check_same_thread = False 

03. brainstorming about architecture tables of the crud comment : 
    - will create a table user ( with id and username)
    - will create a table comment linked to user_id foreign key, column character id, column episode_id, will index
    - the CRUD will need to link all but if even if the character_id or episode_id can be null, both can't be null

04. Creation of the comment table and user table, creation of the path and the post creation of the comment
    - Difficulty : needed more documentation about pydantic (validator),
                   when return None, the database doesn't understand
                   concerning the edit i pass for now, we need user authentification so the SQL can remain it in order to do so. ( code is still written for futur modification)
    - solution : learn pydantic validator's syntaxe
                 add or "Null" value for creation
                
05. create page was not difficult, create a filter with LIKE was easy to find.

06. took the time to read documentation, and decide to modify the path to get_comment_by_chatacter_in_episode
by a query ( just to know that well, i know)

07. added security login, this part is definitively the most complicated part

08. added export route (easy), a simple search on google show me the way

09. just discovered sqlalchemy and decide to refactor with it 
                 
## How to use this API

### the import folder

01. open the folder "database" and open the file create_table.py and execute it
    - this will create the database at the root of the project and import table on it
02. open the file import_to_db (same folder) and execute it
    - this will import the json file in the table of the database.
    - if you need to see manually the database you can open the link :
    http://inloop.github.io/sqlite-viewer/ or use the module sqlite explorer on vscode.

### installing all module

01. don't hesitate to install the requirement creating a virtual environnement

02. depending on where the API is tested, enter the host of the API and then
    - enter the route "/" to see the root

03.searching the route
- enter in the URL "/characters" to see the characters
- enter in the URL "/episodes" to see the episodes
- enter in the URL "/comment" to see the comment
- enter in the URL "/comment/idOfTheComment" to see the comment by id
- enter in the URL "/comments/ch=idOfTheCharacter" to see the comment by character
- enter in the URL "/comments/ch=idOfTheCharacter?episode_id=idOfTheEpisode" to see the comment by character in episode
- enter in the URL "/comments/filter=typeWhatYouWant" to filter the comment by what you want

04. adding, deleting or update
- use /docs to do so