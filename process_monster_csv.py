#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 21:26:22 2021

@author: michael
"""
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import csv
import pandas as pd
import os

filepath="/home/michael/Documents/D&D/gpt_creatures"
Tk().withdraw()
file=askopenfilename(initialdir=filepath,filetypes = (("csv files","*.csv"),("all files","*.*")))
#filename=os.path.basename(file)
monster=open(file)
mons_data=next(csv.reader(monster))
col_list=['Name','meta','AC','HP','Speed','Str','Strmod','Dex','Dexmod','Con'
          ,'Conmod','Int','Intmod','Wis','Wismod','Cha','Chamod','Saves'
          ,'Skills','Senses','Langs','CR','Traits','Actions','Legendary'
          ,'ImgUrl','DmgImn','CondImn','DmgRes','DmgVln','Reactions']
mons_data_labelled = pd.DataFrame(data=[mons_data],columns=col_list)
md=mons_data_labelled
#mons_data_labelled=pd.read_csv(filepath)
#pd.read_csv(usecols=cols)

output=str("___"+
"\n> ## "+md.Name.values[0]+
"\n>*"+md.meta.values[0]+"*"+
"\n> ___"+
"\n> - **Armor Class** "+md.AC.values[0]+
"\n> - **Hit Points** "+md.HP.values[0]+
"\n> - **Speed** "+md.Speed.values[0]+
"\n>___"+
"\n>|STR|DEX|CON|INT|WIS|CHA|"+
"\n>|:---:|:---:|:---:|:---:|:---:|:---:|"+
"\n>|"+md.Str.values[0]+" "+md.Strmod.values[0]+"|"+md.Dex.values[0]+" "+md.Dexmod.values[0]+"|"+md.Con.values[0]+" "+md.Conmod.values[0]+"|"+md.Int.values[0]+" "+md.Intmod.values[0]+"|"+md.Wis.values[0]+" "+md.Wismod.values[0]+"|"+md.Cha.values[0]+" "+md.Chamod.values[0]+"|"+
"\n>___")
if md.Saves.values[0]=="nan":
    saves=""
else:
    saves=("\n> - **Saving Throws** "+md.Saves.values[0])
if md.Skills.values[0]=="nan":
    skills=""
else:
    skills=("\n> - **Skills** "+md.Skills.values[0])
if md.DmgVln.values[0]=="nan":
    dmgvln=""
else:
    dmgvln=("\n> - **Damage Vulnerabilities** "+md.DmgVln.values[0])
#"\n> - **Saving Throws** "+md.Saves.values[0]+
#"\n> - **Skills** "+md.Skills.values[0]+
#"\n> - **Damage Vulnerabilities** "+md.DmgVln.values[0]+
if md.DmgRes.values[0]=="nan":
    dmgres=""
else:
    dmgres=("\n> - **Damage Resistances** "+md.DmgRes.values[0])
if md.DmgImn.values[0]=="nan":
    dmgimn=""
else:
    dmgimn=("\n> - **Damage Immunities** "+md.DmgImn.values[0])
if md.CondImn.values[0]=="nan":
    condimn=""
else:
    condimn=("\n> - **Condition Immunities** "+md.CondImn.values[0])
#"\n> - **Damage Resistances** "+md.DmgRes.values[0]+
#"\n> - **Damage Immunities** "+md.DmgImn.values[0]+
#"\n> - **Condition Immunities** "+md.CondImn.values[0]+
output=output+saves+skills+dmgvln+dmgres+dmgimn+condimn
output=output+("\n> - **Senses** "+md.Senses.values[0]+
"\n> - **Languages** "+md.Langs.values[0]+
"\n> - **Challenge** "+md.CR.values[0]+
"\n> ___")

actions_normal=md.Actions.values[0]
actions_legendary=md.Legendary.values[0]
actions_reactions=md.Reactions.values[0]

if md.Traits.values[0]=="nan":
    traits=""
else:
    traits=md.Traits.values[0]
output=output+"\n> "+traits
'''
\n> ***Pack Tactics.*** These guys work together. Like super well, you don't even know.
\n>
\n> ***Pack Tactics.*** These guys work together. Like super well, you don't even know.
'''

if actions_normal=="nan":
    actions=""
else:
    actions=("\n> ### Actions"+"\n> "+actions_normal)
output=output+actions
'''
\n> ### Actions
\n> ***Dual Cobra Wristlock.*** *Melee Weapon Attack:* +4 to hit, reach 5ft., one target. *Hit* 5 (1d6 + 2) 
\n>
\n> ***Super Hip Submission.*** *Melee Weapon Attack:* +4 to hit, reach 5ft., one target. *Hit* 5 (1d6 + 2) 
'''

if actions_reactions=="nan":
    reactions=""
else:
    reactions=("\n> ### Reactions"+"\n> "+actions_reactions)
output=output+reactions
'''
\n> ### Reactions
\n> ***Somersault Stump Fists.*** *Melee Weapon Attack:* +4 to hit, reach 5ft., one target. *Hit* 5 (1d6 + 2) 
'''

if actions_legendary=="nan":
    legendary=""
else:
    legendary=("\n> ### Legendary Actions"+"\n> "+actions_legendary)
output=output+legendary
'''
\n> ### Legendary Actions
\n> Some blurb about how you can use legendary actions
\n>
\n> ***Somersault Stump Fists.*** *Melee Weapon Attack:* +4 to hit, reach 5ft., one target. *Hit* 5 (1d6 + 2) 
\n>
\n> ***DDT Powerbomb.*** *Melee Weapon Attack:* +4 to hit, reach 5ft., one target. *Hit* 5 (1d6 + 2) 
'''