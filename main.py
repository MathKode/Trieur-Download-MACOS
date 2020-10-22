"""
Ce programme est un code python qui a pour but de classer les fichiers d'un repertory (Celui
ou vous avez mis ce fichier...)
Pour le lancer, c'est très simple :
  Ouvré le terminal
  Aller dans le dossier ou se trouve le fichier main.py
Pour vous balladez dans un terminal : cd ou cd .. (et ls pour lister)
  Enfin executé le programme avec "python3 main.py &" (le & signifie arrière plan : peut être
supprimé)
  Pour finir, il suffit de "kill" le processus (si vous l'avez mis en arrière plan, il faut
ecrire kill [num_du_processus] ou, si vous n'avez pas mis le &, fermer le Terminal)
--- Written by BiMathAx STUDIO 21/10/2020 (dd/MM/YYYY) at 13:20 ---
"""

import os
import time

chemin = '~/Downloads'

if True :
  file = os.listdir()
  if 'Image' not in file :
    os.system("mkdir "+ str(chemin) + "/ Image")
  if 'Exe' not in file :
    os.system("mkdir "+ str(chemin) + "/ Exe")
  if 'Pdf' not in file :
    os.system("mkdir " + str(chemin)+ "/ Pdf")
  if 'Son' not in file :
    os.system("mkdir " + str(chemin)+ "/ Son") 
  if 'Zip' not in file :
    os.system("mkdir " + str(chemin)+ "/ Zip")
  if 'Reste' not in file :
    os.system("mkdir " + str(chemin)+ "/ Reste")
  if 'Word' not in file :
    os.system("mkdir "+ str(chemin) + "/ Word")
  if 'Video' not in file :
    os.system("mkdir "+ str(chemin) + "/ Video")

FT = ["Image","Exe","Pdf","Son","Zip","main.py","Reste","Word","Video"]
Img = ['tif','png','ai','jpg','eps','gif','svg','psd','bmp','jpeg']
Word = ['doc','docm','docx','dot','dotm','dotx','htm','odt','rtf','txt','wps','xml','xps','csv','dbf','dif','mht','ods','slk','xlam','xls','xlsb','xlsm','xlsx','xlt','xltx','xlw','xml','xps','bmp','emf','odp','pot','potm','potx','ppa','ppam','pps','ppsm','ppt','pptm','pptx','rtf','thmx','tif','wmv','xml','xps']
Pdf = ['pdf','Pdf']
Exe = ['bat','exe','dmg','pkg']
Son = ['riff','wav','bwf','ogg','aiff','caf','raw','flac','alac','shorten','ac-3','mp3','mp3pro','mxp4','aac','aa','wave']
Video = ['avi','mov','mpg','mpa','asf','wma','mp2','m2p','vob','mp4']
Zip = ['zip','rar','7z']
while True :
  file = os.listdir()
 
  for i in file :
    
    if i not in FT :
      print(i)
      ls = i.split('.')
      extension = ls[-1]
      del ls[-1]
      n = ".".join(ls).split(' ')
      #print(n)
      if len(n) > 1 :
        name = "/"
        p = 1
        for word in n :
          if p == len(n) :
            name = name + str(word)
          else :
            name = name + str(word) + "\ "
          p += 1
        name = name + "." +  str(extension)
        #print(name)
      else :
        name = "/" + str(n[0]) + "." + str(extension)

      #print(name)
      if extension.lower() in Img :
        os.system("mv " + str(chemin) + str(name) + " "  + str(chemin) + "/Image")
      elif extension.lower() in Word :
        os.system("mv " + str(chemin) + str(name) + " "  + str(chemin) + "/Word")
      elif extension.lower() in Pdf :
        os.system("mv " + str(chemin) + str(name) + " "  + str(chemin) + "/Pdf")
      elif extension.lower() in Exe :
        os.system("mv " + str(chemin) + str(name) + " "  + str(chemin) + "/Exe")
      elif extension.lower() in Son :
        os.system("mv " + str(chemin) + str(name) + " "  + str(chemin) + "/Son")
      elif extension.lower() in Video :
        os.system("mv " + str(chemin) + str(name) + " "  + str(chemin) + "/Video")
      elif extension.lower() in Zip :
        os.system("mv " + str(chemin) + str(name) + " "  + str(chemin) + "/Zip")
      else :
        os.system("mv " + str(chemin) + str(name) + " "  + str(chemin) + "/Reste")
    
  time.sleep(1)
      
