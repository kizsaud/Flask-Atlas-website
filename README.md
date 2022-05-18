# Flask-Atlas-website
This program uses python/HTML to take in user input from a form like site which stores the data and passes it to the Mongodb database, from the mongodb website, once you click submit on the first page it creates a table which lists all the non duplicate entries,anytime submit is entered there is also a log file which is generated

note: to use this correctly the localhost must enable access for there own unique IP


First i imported pymongo, i created a cluster called HTML which has the database for name,phone, and email, 
with that i had a HTML template which i created which can take in 3 data fields, name,email and phone number,
once the user presses submit, which is a post request, the app route calls a function called get data which stores the respective data into variables which passes it ultimitley to another function called pass data,using pass data next two things happen one is that a log file is created and it enters the information from the HTML site to the log file and it sends the information to the mongodb
i created a back button to continously keep adding more data into the database.
