import pandas as pd
import time
from PIL import Image,ImageFont, ImageDraw


"""
This program is for landscape type id cards 1000s of id cards within minutes 
"""


font1 = ImageFont.truetype("arial.ttf",30)
font2 = ImageFont.truetype("arial.ttf",15)
df = pd.read_excel('/home/nerd/Downloads/id.xlsx',names= ['Timestamp','PHOTO','NAME OF THE STUDENT','GUARDIAN NAME','CLASS','SECTION','ROLL NUMBER','DATE OF BIRTH','ADDRESS','CONTACT NUMBER','ADDMISSION NUMBER','BLOOD GROUP'])
data = pd.DataFrame(df)
#Loading excel data using pandas and than convertig it into data frame 
new_data = data.drop(['Timestamp'],axis=1,inplace=True)
#We are permanently droping a column name timestamp in this program using inplace = True

# Defining a function 
def excel_data():
    Imgs = Image.new('RGB',(793,1122),(255,255,255))
    draw = ImageDraw.Draw(Imgs)
     # Creating a white stage of dim and then drawing 
    val = 0
    for cards in range(10,len(data['NAME OF THE STUDENT']),10):  # For getting of all the number of pices of id
        #Iterating through all id card for step value of 10 cards from the excel file
        for y in range(126,1000,190): # For getting hold co-ordinates for y-axis
            Photo = Image.open(f'/home/nerd/campt130/Image/bg{val}'+'.png')   #opening images ** aspect ratio will  
            draw.text((50,50),'School','black',font=font1)                     #  not change change it using thumnail
            draw.text((150,y),f'Name: {data.iloc[val][1]}','black',font=font2)  # method otherwise, actual image will
            draw.text((150,y+20),f'Class:{data.iloc[val][3]}','black',font=font2)  # be pasted 
            draw.text((150,y+40),f'Roll no.:{data.iloc[val][5]}   Sec:{data.iloc[val][4]}','black',font=font2)
            draw.text((150,y+60),f'Blood Group :{data.iloc[val][10]}','red',font=font2)
            draw.text((150,y+80),f'Gaurdian Name :{data.iloc[val][2]}','black',font=font2)
            draw.text((150,y+100),f'Phone No. :{data.iloc[val][8]}','black',font=font2)
            Photo.thumbnail((250,250))
            Imgs.paste(Photo,(60,y))       #pasting images 

            val += 1
            draw.text((480,y),f'Name: {data.iloc[val][1]}','black',font=font2)
            draw.text((480,y+20),f'Class:{data.iloc[val][3]}','black',font=font2)
            draw.text((480,y+40),f'Roll no.:{data.iloc[val][5]}   Sec:{data.iloc[val][4]}','black',font=font2)
            draw.text((480,y+60),f'Blood Group :{data.iloc[val][10]}','red',font=font2)
            draw.text((480,y+80),f'Gaurdian Name :{data.iloc[val][2]}','black',font=font2)
            draw.text((480,y+100),f'Phone No. :{data.iloc[val][8]}','black',font=font2) 
            Imgs.paste(Photo,(420,y))
            

            val += 1

            if val == cards:         # This condition would be saving the data of 10 id cards in one sheet 
               Imgs.save(f'ID_card {val/10}'+'.png')    # And then saving it
               Imgs.close()
               Imgs = Image.new('RGB',(793,1122),(255,255,255))
               draw = ImageDraw.Draw(Imgs)

               
            
                

excel_data()



