
# coding: utf-8

# ### import modules

# In[205]:


import matplotlib.pyplot as plt
import numpy as np
import random


# ### simple plot

# In[276]:


y = [1,2,3,4,5]

plt.plot(y) # x預設值為[0,1,2,3,4,...]
plt.show() 


# In[6]:


# magic 指令
get_ipython().run_line_magic('matplotlib', 'inline')


# In[210]:


x = [x for x in range(100)]
y = 33+10*np.random.rand(100)


plt.plot(x,y)
plt.grid()


# ### two plots in one figure

# In[77]:


x = np.linspace(-np.pi,np.pi,200)
y,y2 = np.sin(x), np.cos(x)


plt.plot(x,y,"g--",label="sin")
plt.plot(x,y2,"k-.",label="cos")
plt.legend()


# ### Line customization
# 
# - color:
# https://xkcd.com/color/rgb/
# 
# - line/marker style:
# https://www.labri.fr/perso/nrougier/teaching/matplotlib/#figures-subplots-axes-and-ticks
# 
# <div style="display:inline-block;">
#     <a href="https://imgur.com/OaaO9GE" ><img src="https://i.imgur.com/OaaO9GE.png" title="source: imgur.com" align="left" width = 42%>
#     </a>
#     <a href="https://imgur.com/IhUOXv6"><img src="https://i.imgur.com/IhUOXv6.png" title="source: imgur.com" align="right" width = 50%>
#     </a>
# </div>
# 

# In[285]:


x = np.linspace(-np.pi,np.pi,30)
y = np.sin(x)

# change line color
# plt.plot(x,y,color="red")
# plt.plot(x,y,color=(0.8,0.1,0.1)) #rgb
# plt.plot(x,y,color="0.09")
plt.plot(x,y,color="#029386")
# plt.plot(x,y,color="k")
# plt.plot(x,y,color="r")
plt.plot(x,y,"k")


# In[294]:


# some line styles

# plt.plot(x,y,linestyle="-")
plt.plot(x,y,linestyle="--")
# plt.plot(x,y,linestyle="-.")
# plt.plot(x,y,linestyle=":")

# change line width
# plt.plot(x,y,linewidth=14)

# some markers
# plt.plot(x,y,marker="D")
plt.plot(x,y,marker="o")
# plt.plot(x,y,marker="s")
# plt.plot(x,y,marker="x")
# plt.plot(x,y,marker="^")

# markersize
# plt.plot(x,y,marker="^",markersize=30)

plt.plot(x,y,"k--D",lw=4,ms=6)

#grid
plt.plot([],[])
plt.grid()
plt.grid(True,color="g",linewidth=4,linestyle="-.")


# ### Ticks
# ticks:https://jakevdp.github.io/PythonDataScienceHandbook/04.10-customizing-ticks.html

# In[298]:


x = np.linspace(-np.pi,np.pi,200)

plt.plot(x,np.sin(x),"k")
plt.plot(x,np.cos(x),"k-.")

plt.xticks([-np.pi,0,np.pi])
plt.yticks([-1,0,1])

plt.xticks([-np.pi,0,np.pi],
          ["left","middle","right"])
# plt.yticks([-1,0,1],
#           ["top","middle","bottom"])

# plt.xticks([])
# plt.yticks([])

# ax = plt.axes()
# ax.yaxis.set_major_locator(plt.NullLocator())
# ax.xaxis.set_major_formatter(plt.NullFormatter())

# ax.yaxis.set_major_locator(plt.MaxNLocator(10))



# ### Legends
# 
# location:
# https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.legend.html
# <table align="left" style="width:500px;">
# <thead valign="bottom">
# <tr class="row-odd"><th class="head">Location String</th>
# <th class="head">Location Code</th>
# </tr>
# </thead>
# <tbody valign="top">
# <tr class="row-even"><td>‘best’</td>
# <td>0</td>
# </tr>
# <tr class="row-odd"><td>‘upper right’</td>
# <td>1</td>
# </tr>
# <tr class="row-even"><td>‘upper left’</td>
# <td>2</td>
# </tr>
# <tr class="row-odd"><td>‘lower left’</td>
# <td>3</td>
# </tr>
# <tr class="row-even"><td>‘lower right’</td>
# <td>4</td>
# </tr>
# <tr class="row-odd"><td>‘right’</td>
# <td>5</td>
# </tr>
# <tr class="row-even"><td>‘center left’</td>
# <td>6</td>
# </tr>
# <tr class="row-odd"><td>‘center right’</td>
# <td>7</td>
# </tr>
# <tr class="row-even"><td>‘lower center’</td>
# <td>8</td>
# </tr>
# <tr class="row-odd"><td>‘upper center’</td>
# <td>9</td>
# </tr>
# <tr class="row-even"><td>‘center’</td>
# <td>10</td>
# </tr>
# </tbody>
# </table>

# In[302]:


x = np.linspace(-np.pi,np.pi,200)

plt.plot(x,np.sin(x),"k",label="sine")
plt.plot(x,np.cos(x),"k-.",label="cosine")

plt.legend()

# change location
plt.legend(loc="upper right")
plt.legend(loc=4)

# # frame
plt.legend(frameon=False)

# # change location
# plt.legend(bbox_to_anchor=(1,1))

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Example\nMSSB")


# ### xlims ylims setting

# In[305]:


x = np.linspace(-np.pi,np.pi,200)

plt.plot(x,np.sin(x),"k",label="sine")
plt.plot(x,np.cos(x),"k-.",label="cosine")


# plt.xlim([x.min()*1.5, x.max()*1.5])
# plt.ylim([y.min()*1.5, y.max()*1.5])

xmin, xmax, ymin, ymax = x.min()*1.5 , x.max()*1.5, y.min()*1.5, y.max()*1.5
plt.axis([xmin, xmax, ymin, ymax])


# ### spines
# 
# spine:https://matplotlib.org/api/spines_api.html
# 
# 
# <dl class="method">
# <dt id="matplotlib.spines.Spine.set_position">
# <code class="descname">set_position</code><span class="sig-paren">(</span><em>position</em><span class="sig-paren">)</span><a class="headerlink" href="#matplotlib.spines.Spine.set_position" title="Permalink to this definition">¶</a></dt>
#     <dd><p>set the position of the spine</p>
#     <p>Spine position is specified by a 2 tuple of (position type,
#     amount). The position types are:</p>
#     <ul class="simple">
#     <li>‘outward’ : place the spine out from the data area by the
#     specified number of points. (Negative values specify placing the
#     spine inward.)</li>
#     <li>‘axes’ : place the spine at the specified Axes coordinate (from
#     0.0-1.0).</li>
#     <li>‘data’ : place the spine at the specified data coordinate.</li>
#     </ul>
#     <p>Additionally, shorthand notations define a special positions:</p>
#     <ul class="simple">
#     <li>‘center’ -&gt; (‘axes’,0.5)</li>
#     <li>‘zero’ -&gt; (‘data’, 0.0)</li>
#     </ul>
#     </dd>
# 
# </dl>
# 
# 

# In[152]:


# plt.plot([],[])

x = np.random.rand(10)
y = np.random.rand(10)
plt.scatter(x,y)

ax = plt.gca() # get current axis
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
for tick in ax.xaxis.get_ticklabels():
    tick.set_rotation(45)
    tick.set_alpha(0.3)
    tick.set_fontsize(16)
ax.spines['bottom'].set_position(("axes",0.5))
ax.spines['left'].set_position(("axes",0.5))
ax.xaxis.set_ticks_position('top')
ax.yaxis.set_ticks_position('right')


# ###  add text
# Text:https://matplotlib.org/api/_as_gen/matplotlib.pyplot.text.html
# 
# keyword args:https://matplotlib.org/api/text_api.html#matplotlib.text.Text
# 
# matplotlib.pyplot.text(x, y, s, fontdict=None, withdash=False, **kwargs)
# 
# 
# 

# In[308]:


data = np.random.rand(10)
plt.plot(data) # x值=[0,1,2,...], y值隨機

plt.text(8, 0.8, "(8,0.8)") # text(x座標,y座標,"文字")

font = {
    "family":"Agency FB",
    "fontsize":25,
    "color":(0.8,0.5,0.5)
}
plt.text(1,data[1],"Text_here",fontdict=font) # text(x座標,y座標,"文字", fontdict={文字格式})

plt.text(2,data[2],"Another Text",color="#FF00F9", size=50, rotation=-30, style="italic",alpha=.5)


# ### anotations
# 
# anotations: https://matplotlib.org/tutorials/text/annotations.html#plotting-guide-annotation

# In[319]:


data = np.random.rand(10)
plt.plot(data)
plt.annotate("Text",(2,0.5),(1,0.2),arrowprops= dict())

plt.annotate("peak",
             (np.where(data==data.max())[0][0],data.max()), # where to point
             xycoords='data', 
             xytext=(np.where(data==data.max())[0][0]+1,data.max()-0.1), # where to put text
             arrowprops = dict(facecolor="grey",shrink=0.09)) # arrow property

plt.annotate("fixed arrow",
             (0.8,0.8),xycoords='axes fraction',
             xytext=(0.5,0.5),textcoords='axes fraction',
             arrowprops = dict(arrowstyle="->")
            )

# plt.show()


# ### subplot

# In[320]:


plt.figure(1,figsize=(16,16)) #(num,figsize=(width,height))
plt.plot([],[])
plt.show()


# In[321]:


#Two figures
fig = plt.figure(figsize = (16,8))
x = np.linspace(0,10,50)
y = np.sin(x)
plt.plot(x,y)

fig2 = plt.figure(2,figsize = (16,8))
plt.plot(x,np.cos(x))


# In[323]:


# subplot

fig = plt.figure(figsize=(16,8))
x = np.linspace(0,10,100)

# t1 = fig.add_subplot(2,1,1) # 亦可以(211)來表示
# t1.plot(x,np.sin(x),label="sine")
# t1.legend()

# t2 = fig.add_subplot(2,1,2)
# t2.plot(x,np.cos(x))

ax1 = plt.subplot(2,1,1)
ax1.plot(x,np.sin(x))

ax2 = plt.subplot(2,1,2)
ax2.plot(x,np.cos(x))


# In[196]:


# different arrangement
plt.figure(figsize=(16,16))
a1 = plt.subplot(231)
a2 = plt.subplot(232)
a3 = plt.subplot(233)
a4 = plt.subplot(212)

a1.text(0.5,0.5,"A1",size=16,alpha=.5)
a2.text(0.5,0.5,"A2",size=16,alpha=.5)
a3.text(0.5,0.5,"A3",size=16,alpha=.5)
a4.text(0.5,0.5,"A4",size=32,alpha=.5)


# In[198]:


# use subplot2grid
plt.figure(figsize=(16,16))

a1 = plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=1)
a1.plot(x,np.sin(x**2))

a2 = plt.subplot2grid((3,3),(1,0),colspan=1,rowspan=2)
a2.plot(x,np.cos(x))

a3 = plt.subplot2grid((3,3),(1,1),colspan=2,rowspan=1)
a3.plot(x,np.exp(x))

a4 = plt.subplot2grid((3,3),(2,1))
a4.plot(x,np.log(x+1))

a5 = plt.subplot2grid((3,3),(2,2))
a5.plot(x,np.log(x+4e-4))


# In[ ]:


#Gridspec
# import matplotlib.gridspec as gridspec
# fig = plt.figure(figsize=(12,8))
# G = gridspec.GridSpec(2,4)
# a1 = plt.subplot(G[0,1:]) #[0,1~3]
# a2 = plt.subplot(G[0,0])
# a3 = plt.subplot(G[1,:])


# In[202]:


#subplots that share the same axis
f,((a1,a2,a3),(a4,a5,a6)) = plt.subplots(2,3,sharex=True,sharey=True,figsize=(16,8))
a1.plot(x,np.exp(x))
a2.plot(x,x**2)
a3.plot(x,2**x)

# add title/xlabel/ylabel

a1.set_title("test1")
a2.set_title("test2")

a1.set_xlabel("x-1")
a2.set_xlabel("x-2")

a1.set_ylabel("y-1")
a2.set_ylabel("y-2")


# In[332]:



#Axes add_axes([left,bottom,width,height])
left,bottom,width,height = 0.05,0.05,0.88,0.88

fig = plt.figure(figsize=(16,16))
a1 = fig.add_axes([left,bottom,width,height])
a2 = fig.add_axes([0.15,0.15,0.2,0.2])
a3 = fig.add_axes([0.85,0.85,0.3,0.2])

x = np.linspace(0,1,50)
a1.plot(x,np.log(1/(x+5e-2)))
a2.plot(x,np.random.rand(50))
a3.plot(x,x+np.random.rand(50))
plt.savefig("../Users/user/Downloads/test.PNG")

