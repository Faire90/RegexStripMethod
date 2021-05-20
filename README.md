# RegexStripMethod
Regex Version of the strip() Method from Chapter 7 of Automate the Boring Stuff

Solves the project by using the ^ to address the beginning of the string and $ to
address the end.  Each of those target white space with \s.  To be able to pass specific
characters to strip, it uses a for loop to loop through the passed string and removes each
character individually.