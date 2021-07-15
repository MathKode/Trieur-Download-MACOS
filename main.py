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
upgrade : 15/07/2021 at 11:34
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
  if 'Code' not in file :
    os.system("mkdir "+ str(chemin) + "/ Code")
  if 'log.txt' not in file :
    os.system("touch "+ str(chemin) + "/ log.txt")

FT = ["Image","Exe","Pdf","Son","Zip","main.py","Reste","Word","Video","log.txt","Code"]
Img = ['tif','png','ai','jpg','eps','gif','svg','psd','bmp','jpeg']
Word = ['doc','docm','docx','dot','dotm','dotx','htm','odt','rtf','txt','wps','xml','xps','csv','dbf','dif','mht','ods','slk','xlam','xls','xlsb','xlsm','xlsx','xlt','xltx','xlw','xml','xps','bmp','emf','odp','pot','potm','potx','ppa','ppam','pps','ppsm','ppt','pptm','pptx','rtf','thmx','tif','wmv','xml','xps']
Pdf = ['pdf','Pdf']
Exe = ['bat','exe','dmg','pkg']
Son = ['riff','wav','bwf','ogg','aiff','caf','raw','flac','alac','shorten','ac-3','mp3','mp3pro','mxp4','aac','aa','wave','m4a']
Video = ['avi','mov','mpg','mpa','asf','wma','mp2','m2p','vob','mp4']
Zip = ['zip','rar','7z']
Code = ['py','html','css','json','bat','sh','htm','md','adb','ahk','applescript','asm','bas','bf','birl','bmp','bro','c','cc','cljc','cmd','vbs','chai','cpp','cs','cr','sql','smv','swift']

while True :
  file = os.listdir()
  #print(file)
  for i in file :
    if i not in FT :
      
      #Replce for all ["'"," ",'"'] by "\'" and "\ "
      name = "/" + i
      #print(name)
      for c in ["'"," ",'"'] :
        name = name.split(c)
        name = f"\{c}".join(name)
      #print(name)

      extension = name.split('.')[-1]
      
      if extension.lower() in Img :
        os.system("mv " + str(chemin) + str(name) + " "  + str(chemin) + "/Image")
        os.system(f'echo "{i} ->" Image >> log.txt ')
      elif extension.lower() in Word :
        os.system("mv " + str(chemin) + str(name) + " "  + str(chemin) + "/Word")
        os.system(f'echo "{i} ->" Word >> log.txt ')
      elif extension.lower() in Pdf :
        os.system("mv " + str(chemin) + str(name) + " "  + str(chemin) + "/Pdf")
        os.system(f'echo "{i} ->" Pdf >> log.txt ')
      elif extension.lower() in Exe :
        os.system("mv " + str(chemin) + str(name) + " "  + str(chemin) + "/Exe")
        os.system(f'echo "{i} ->" Exe >> log.txt ')
      elif extension.lower() in Son :
        os.system("mv " + str(chemin) + str(name) + " "  + str(chemin) + "/Son")
        os.system(f'echo "{i} ->" Son >> log.txt ')
      elif extension.lower() in Video :
        os.system("mv " + str(chemin) + str(name) + " "  + str(chemin) + "/Video")
        os.system(f'echo "{i} ->" Video >> log.txt ')
      elif extension.lower() in Zip :
        os.system("mv " + str(chemin) + str(name) + " "  + str(chemin) + "/Zip")
        os.system(f'echo "{i} ->" Zip >> log.txt ')
      elif extension.lower() in Code :
        os.system("mv " + str(chemin) + str(name) + " "  + str(chemin) + "/Code")
        os.system(f'echo "{i} ->" Code >> log.txt ')
      else :
        os.system("mv " + str(chemin) + str(name) + " "  + str(chemin) + "/Reste")
        os.system(f'echo "{i} ->" Reste >> log.txt ')
  time.sleep(1)
      
