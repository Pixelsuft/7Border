is_builded=False


from os import system as cmd_run
from sys import argv
from os import environ as env
from os import access as file_exists
from os import F_OK as check_param
env['__COMPAT_LAYER']='WinXPSp3'
with_7_style=False
if '-prog' in argv:
    is_prog_arg=0
    prog_to_run=''
    for i in range(len(argv)):
        if is_prog_arg==1:
            is_prog_arg=2
            prog_to_run=argv[i]
        elif is_prog_arg==2:
            prog_to_run+=' '+argv[i]
        elif argv[i]=='-prog':
            is_prog_arg=1
    prog_to_run=prog_to_run.replace('"','')
    prog_to_run=prog_to_run.replace("'","")
    cmd_run('"'+prog_to_run+'"')
    exit()
else:
    for i in argv:
        if i=='-win7style':
            with_7_style=True
    if with_7_style==False:
        if is_builded==True:
            cmd_run(argv[0] + ' -win7style')
        else:
            cmd_run('python '+argv[0] + ' -win7style')
        exit()

#code
from ttkthemes import themed_tk as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import filedialog

root = tk.ThemedTk()
root.title('7Border')
root.iconbitmap('data\\icon.ico')
root.geometry('400x50')
root.resizable(False, False)

txt = ttk.Entry(root,width=100)
txt.place(x=0,y=0, height=18)

def about_def():
    messagebox.showinfo('Information!','Created by Pixelsuft, 2020\nFor Windows 10')

def run_app_def():
    prog=txt.get()
    prog=prog.replace('"','')
    prog=prog.replace("'","")
    if prog=='':
        messagebox.showerror('Error!','Launchstring is empty!')
    else:
        if file_exists(prog, mode=check_param)==False:
            messagebox.showerror('Error!','File is not exists!')
        else:
            if is_builded==True:
                cmd_run('start '+argv[0] + ' -win7style -prog '+prog)
            else:
                cmd_run('start python '+argv[0] + ' -win7style -prog '+prog)

def open_def():
    file_name=filedialog.askopenfile(
        parent=root,
        title='Open program',
        filetypes=[("All files (*.*)", "*.*")]
    )
    try:
        txt.delete(0)
        txt.insert(0, file_name.name)
    except:
        print('Ignoring...')

select = ttk.Button(root, text="Select", command=open_def)
select.place(x=0, y=20, width=120)

about = ttk.Button(root, text="About", command=about_def)
about.place(x=140, y=20, width=120)

run_app = ttk.Button(root, text="Start", command=run_app_def)
run_app.place(x=280, y=20, width=120)

root.set_theme('winxpblue')
root.mainloop()