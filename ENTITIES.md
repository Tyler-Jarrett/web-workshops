# Entities

## News
### Article
Model which contains the meta data for a given article
- author
- creation_date
- creation_time
- last_change_date
- last_change_time
- title
- image
- category

### Section
There are many different ways to handle sections for an article, but I like this one
This allows you to map several distinct sections to a given article
 - article
 - heading
 - text
 - order


 ## Events
 ### Event
 The main model for managing events
 - title
 - description
 - start_date
 - start_time
 - end_date
 - end_time
 - registration_limit

### Registration
The intermediary table for users to register for an event
 - event
 - user
 