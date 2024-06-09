# Importing neccessory libraries
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image,ImageTk
import numpy
import numpy as np

# Loading the Model
from keras.models import load_model
model=load_model('Age_Sex_Detection.keras')

# Initialize the GUI
top=tk.Tk()
top.geometry('800x600')
top.title('Age and Gender Detector')
top.configure(background='#EAF9FF')

# Initializing the Lables (one for age and other for gender)
label1=Label(top,background='#EAF9FF',font=('arial','15','bold'))
label2=Label(top,background='#EAF9FF',font=('arial','15','bold'))
sign_image=Label(top)

# Defining the Detect Function which detects the age and gender of the person in image using model
def Detect(file_path):
    global label_packed
    image=Image.open(file_path)
    image = image.resize((48, 48), Image.Resampling.NEAREST)
    image=numpy.expand_dims(image,axis=0)
    image=np.array(image)
    image=np.delete(image,0,1)
    image=np.resize(image,(48,48,3))
    print(image.shape)
    sex_f=["Male","Female"]
    image=np.array([image])/255
    pred=model.predict(image)
    age=int(np.round(pred[1][0]))
    sex=int(np.round(pred[0][0]))
    print("Predicted Age is "+str(age))
    print("Predicted Gender is "+sex_f[sex])
    label1.configure(foreground="#000000",text=age)
    label2.configure(foreground="#000000",text=sex_f[sex])
    
# Defining Show_detect button function
def show_Detect_Button(file_path):
    Detect_b=Button(top,text="Detect Image",command=lambda: Detect(file_path),padx=10,pady=5)
    Detect_b.configure(background="#364156",foreground='white',font=('arial',10,'bold'))
    Detect_b.place(relx=0.79,rely=0.46)
    
# Defining Upload Image Function
def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))  
        im=ImageTk.PhotoImage(uploaded)
        
        sign_image.configure(image=im)
        sign_image.image=im
        label1.configure(text='')
        label2.configure(text='')
        show_Detect_Button(file_path)
    except:
        pass
    
upload=Button(top,text="Upload an Image",command=upload_image,padx=10,pady=5)
upload.configure(background="#364156",foreground='white',font=('arial',10,'bold'))
upload.pack(side='bottom',pady=50)
sign_image.pack(side='bottom',expand=True)

label1.pack(side="bottom",expand=True)
label2.pack(side="bottom",expand=True)
heading=Label(top,text="Age and Gender Detector",pady=20,font=('arial','20','bold'))
heading.configure(background="#F0F8FF",foreground='#011638')
heading.pack()
top.mainloop()