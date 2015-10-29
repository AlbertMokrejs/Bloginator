# Bloginator2.0

By Ari, Rong, and Albert. 

The majority of mongo code refactoring was done by running the website and using it until evident errors were found, at which point a small change would be pushed and retested. This is the reason for the slew of tiny, rapid, commits by one person as we'd get about a commit a minute from tiny changes in the code as everyone suggested solution to test.

Usernames and passwords are stored on a local text file and are lightly encrypted (we think). 

A mongo database called Main is used to store all posts, each of which also stores its comments. 
