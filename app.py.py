#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__) 
# double underscore


# In[3]:


from flask import request, render_template
import joblib

@app.route("/", methods=["GET", "POST"])
#post: get html from front end to back end , post back end to front end which is DBS share price. Going from front to back and vice versa is called post
#get : front end to backend 


def index(): 
    if request.method == "POST": 
        rates = request.form.get("rates")
        print(rates)
        model=joblib.load("DBS")
        pred = model.predict([[float(rates)]])
        print(pred)
        s = "The predicted DBS share price is " + str(pred[0][0]) #remove the 2 squared brackets 
        return(render_template("index.html", result = s))
    else: 
        return(render_template("index.html", result="2"))


# In[ ]:


if __name__ =="__main__":
    app.run()


# In[ ]:




