#!/usr/bin/env python
# coding: utf-8

# <a><img src="https://ibm.box.com/shared/static/ugcqz6ohbvff804xp84y4kqnvvk3bq1g.png" width="200" align="center"></a>

# <h1>Analyzing US Economic Data and  Building a Dashboard  </h1>
# <h2>Description</h2>
# 

# Extracting essential data from a dataset and displaying it is a necessary part of data science; therefore individuals can make correct decisions based on the data. In this assignment, you will extract some essential economic indicators from some data, you will then display these economic indicators in a Dashboard. You can then share the dashboard via an URL.
# <p>
# <a href="https://en.wikipedia.org/wiki/Gross_domestic_product"> Gross domestic product (GDP)</a> is a measure of the market value of all the final goods and services produced in a period. GDP is an indicator of how well the economy is doing. A drop in GDP indicates the economy is producing less; similarly an increase in GDP suggests the economy is performing better. In this lab, you will examine how changes in GDP impact the unemployment rate. You will take screen shots of every step, you will share the notebook and the URL pointing to the dashboard.</p>

# <h2>Table of Contents</h2>
# <div class="alert alert-block alert-info" style="margin-top: 20px">
#     <ul>
#         <li><a href="#Section_1"> Define a Function that Makes a Dashboard </a></li>
#     <li><a href="#Section_2">Question 1: Create a dataframe that contains the GDP data and display it</a> </li>
#     <li><a href="#Section_3">Question 2: Create a dataframe that contains the unemployment data and display it</a></li>
#     <li><a href="#Section_4">Question 3: Display a dataframe where unemployment was greater than 8.5%</a></li>
#     <li><a href="#Section_5">Question 4: Use the function make_dashboard to make a dashboard</a></li>
#         <li><a href="#Section_6"><b>(Optional not marked)</b> Save the dashboard on IBM cloud and display it</a></li>
#     </ul>
# <p>
#     Estimated Time Needed: <strong>180 min</strong></p>
# </div>
# 
# <hr>

# <h2 id="Section_1"> Define Function that Makes a Dashboard  </h2>

# We will import the following libraries.

# In[1]:


import pandas as pd
from bokeh.plotting import figure, output_file, show,output_notebook
output_notebook()


# In this section, we define the function <code>make_dashboard</code>. 
# You don't have to know how the function works, you should only care about the inputs. The function will produce a dashboard as well as an html file. You can then use this html file to share your dashboard. If you do not know what an html file is don't worry everything you need to know will be provided in the lab. 

# In[2]:


def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% unemployed")
    show(p)


# The dictionary  <code>links</code> contain the CSV files with all the data. The value for the key <code>GDP</code> is the file that contains the GDP data. The value for the key <code>unemployment</code> contains the unemployment data.

# In[3]:


links={'GDP':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',       'unemployment':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}


# <h3 id="Section_2"> Question 1: Create a dataframe that contains the GDP data and display the first five rows of the dataframe.</h3>

# Use the dictionary <code>links</code> and the function <code>pd.read_csv</code> to create a Pandas dataframes that contains the GDP data.

# <b>Hint: <code>links["GDP"]</code> contains the path or name of the file.</b>

# In[4]:


# Type your code here
import pandas as pd
csv_path = links["GDP"]
df = pd.read_csv(csv_path)


# Use the method <code>head()</code> to display the first five rows of the GDP data, then take a screen-shot.

# In[5]:


# Type your code here
df.head()


# <h3 id="Section_2"> Question 2: Create a dataframe that contains the unemployment data. Display the first five rows of the dataframe. </h3>

# Use the dictionary <code>links</code> and the function <code>pd.read_csv</code> to create a Pandas dataframes that contains the unemployment data.

# In[6]:


# Type your code here
import pandas as pd
csv_data = links["unemployment"]
df = pd.read_csv(csv_data)


# Use the method <code>head()</code> to display the first five rows of the GDP data, then take a screen-shot.

# In[7]:


# Type your code here
df.head()


# <h3 id="Section_3">Question 3: Display a dataframe where unemployment was greater than 8.5%. Take a screen-shot.</h3>

# In[8]:


# Type your code here
import pandas as pd
links={'GDP':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',       'unemployment':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}
csv_path=links['unemployment']
df=pd.read_csv(csv_path)
df=df[df['unemployment']>8.5]
df


# <h3 id="Section_4">Question 4: Use the function make_dashboard to make a dashboard</h3>

# In this section, you will call the function  <code>make_dashboard</code> , to produce a dashboard. We will use the convention of giving each variable the same name as the function parameter.

# Create a new dataframe with the column <code>'date'</code> called <code>x</code> from the dataframe that contains the GDP data.

# In[9]:


# Create your dataframe with column date
import pandas as pd
links={'GDP':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',      'unemployment':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}
csv_path=links['GDP']
gdp_dataframe=pd.read_csv(csv_path)
x = pd.DataFrame(gdp_dataframe, columns=['date'])
x.head()


# Create a new dataframe with the column <code>'change-current' </code> called <code>gdp_change</code>  from the dataframe that contains the GDP data.

# In[10]:


# Create your dataframe with column change-current

import pandas as pd
links={'GDP':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',      'unemployment':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}
csv_path = links['GDP']
df = pd.read_csv(csv_path)
gdp_change = pd.DataFrame(df, columns=['change-current'])
gdp_change.head()


# Create a new dataframe with the column <code>'unemployment' </code> called <code>unemployment</code>  from the dataframe that contains the  unemployment data.

# In[11]:


# Create your dataframe with column unemployment
import pandas as pd
links={'GDP':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',      'unemployment':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}
csv_path = links['unemployment']
df = pd.read_csv(csv_path)
unemployment = pd.DataFrame(df, columns = ['unemployment'])
unemployment.head()


# Give your dashboard a string title, and assign it to the variable <code>title</code>

# In[12]:


# Give your dashboard a string title
title = "Unemployement statistics according to GDP"


# Finally, the function <code>make_dashboard</code> will output an <code>.html</code> in your direictory, just like a <code>csv</code> file. The name of the file is <code>"index.html"</code> and it will be stored in the varable  <code>file_name</code>.

# In[13]:


file_name = "index.html"


# Call the function <code>make_dashboard</code> , to produce a dashboard.  Assign the parameter values accordingly take a the <b>, take a screen shot of the dashboard and submit it</b>.

# In[14]:


# Fill up the parameters in the following function:
# make_dashboard(x=, gdp_change=, unemployment=, title=, file_name=)


# <h3 id="Section_5"> <b>(Optional not marked)</b>Save the dashboard on IBM cloud and display it  </h3>

# From the tutorial <i>PROVISIONING AN OBJECT STORAGE INSTANCE ON IBM CLOUD</i> copy the JSON object containing the credentials you created. You’ll want to store everything you see in a credentials variable like the one below (obviously, replace the placeholder values with your own). Take special note of your <code>access_key_id</code> and <code>secret_access_key</code>. <b>Do not delete <code># @hidden_cell </code> as this will not allow people to see your credentials when you share your notebook. </b>

# <code>
# credentials = {<br>
#  &nbsp; "apikey": "your-api-key",<br>
#  &nbsp; "cos_hmac_keys": {<br>
#  &nbsp;  "access_key_id": "your-access-key-here", <br>
#  &nbsp;   "secret_access_key": "your-secret-access-key-here"<br>
#  &nbsp; },<br>
# </code>
# <code>
#    &nbsp;"endpoints": "your-endpoints",<br>
#  &nbsp; "iam_apikey_description": "your-iam_apikey_description",<br>
#  &nbsp; "iam_apikey_name": "your-iam_apikey_name",<br>
#  &nbsp; "iam_role_crn": "your-iam_apikey_name",<br>
#  &nbsp;  "iam_serviceid_crn": "your-iam_serviceid_crn",<br>
#  &nbsp;"resource_instance_id": "your-resource_instance_id"<br>
# }
# </code>

# You will need the endpoint make sure the setting are the same as <i> PROVISIONING AN OBJECT STORAGE INSTANCE ON IBM CLOUD </i> assign the name of your bucket to the variable  <code>bucket_name </code> 

# In[15]:


endpoint = 'https://s3-api.us-geo.objectstorage.softlayer.net'


# From the tutorial <i> PROVISIONING AN OBJECT STORAGE INSTANCE ON IBM CLOUD </i> assign the name of your bucket to the variable  <code>bucket_name </code> 

# In[16]:


bucket_name = "pythonbasicsfordatascienceproject-donotdelete-pr-19mqvavbx8dnqp"

