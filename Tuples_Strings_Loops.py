#---------------------------------------Start of the Lessons----------------------------------------------------------

#Tuples, Strings, Loops

#Variable
#Everything in Python is just an object, this is Technically a "Tuple"
programming_languages = "Python", "Java", "C++",  "C#"

#If you are ever wondering what kind of variable you are dealing with you can just use the word type
print(type(programming_languages))

#Loops, "For Loops"
#Somewhat of a literal language. When looking a the tuple 'programming_language' you see the tuple is storing words or a language. 
#With a For look you literally can make a temporary variable calledn language as say IN programming_languages
#just print out the language within programming_languages
for language in programming_languages:
    print(language)


