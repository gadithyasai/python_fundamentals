#!/usr/bin/env python
# coding: utf-8

# In[45]:


#Activity-1:

class Restaurant: #Class definination
    
    def __init__(self,Name,Cuisine_type): #attributes passing bu constructor method
        
        self.Name=Name
        
        self.Cuisine_type=Cuisine_type
        
    def describe_restaurant(self):
        
        print(f'Welcome to {self.Name} with empty stomaches...We assure you to go out Fully.. ')
        
        print(f'\nWe serve you all categories of cuisines to ensures your Abdomen feel pleased.....')
        
        print(f'\nThe famous dish at dine is {self.Cuisine_type} ')
        
    def open_restaurant(self):
        
        print('...We serve whenever you feel Hungry...')
        


# In[ ]:





# In[46]:


restaurant=Restaurant('The Hungers Hubs','Special Andhra Meals') #instance/object passing


# In[ ]:





# In[47]:


restaurant.describe_restaurant() #accessign the methods of a class


# In[ ]:





# In[49]:


restaurant.open_restaurant() #accessign the methods of a class


# In[ ]:





# In[ ]:


#Activity-2:


# In[50]:


class IceCreamStand(Restaurant):
    
    def __init__(self,*flavours):
        
        self.flavours=flavours
        
    def list_of_items(self):
        
        print(f'List of icreams available are:\n')
        
        for i in self.flavours:
            
            print(f'-{i}')
    


# In[52]:


icreams=IceCreamStand('Vennila','Strawberry','Butter-Scotch','Chocolate','Pineapple','Red-Velvet','Black-Forest')


# In[54]:


icreams.list_of_items()


# In[55]:


icreams.open_restaurant()


# In[58]:


icreams.describe_restaurant('The Hungers Hub','Andhra Meals') #how to handle this situation???


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




