# Python Dupcate Icon
- De-dupcate Icon in python
- the only file: dedup_icon.py
- the initial testing file: dedup_icon.py and dedupIcon.py for testing
- you need to modify additional database.py and config.json, which will not provided in public

# Front-end supoort function
- doing analysis all the session under the folder and is the status.json's status is ok, 
- if ok, then sort all the images name under the img foler and save to the list, 
- finally save both session_id and images_list to mongodb
- create_new_table.py: creat new tables with ObjectID and img_list
- with database.py and config.json

# Pyton Find Similar Icon
- similar_icon.py
- using pypuzzle lib
- take some sample and and located at each class folder, 
- then checking the random folder compare with all the icons in classes' folder
- if similar smaller than [value], then move (or copy) the icons to each class's folder
