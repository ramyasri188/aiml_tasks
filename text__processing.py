#!/usr/bin/env python
# coding: utf-8

# In[27]:


def remove_punc(input_text):
    puncuation_marks = ['.',',','%','&','?','@','#','$','^','*','(',')','~','/','!','"']
    output_text = ""
    for char in input_text:
        if char not in puncuation_marks:
            output_text += char
    return output_text
    


# In[34]:


remove_punc('''Hello!, "How are you?"''')


# In[36]:


def remove_stopwords(input_text):
    stop_words=['is','and','or','am','we','the','a','an','in','on','at','it','up','was','be']
    #Split the text into words
    words=input_text.split()
    #remove stopwords using a for loop
    filtered_words=[]
    for word in words:
        if word.lower() not in stop_words:
            filtered_words.append(word)
    #Join the filtered words back into a sentence
    output_text = ' '.join(filtered_words)
    return(output_text)


# In[40]:


remove_stopwords("It is an apple")


# 
