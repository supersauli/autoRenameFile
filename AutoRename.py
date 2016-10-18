import os

print (os.getcwd())
absPath = os.getcwd()
path="."
fileList = []
import pdb

# i=0
# for file  in os.listdir(path):
#     newFileName = '[%d].txt' %i
#    # print(newFileName)
#     absFileName = absPath+"\\"+file
#     if  file.endswith(".py" ) ==0:
#     	if(os.path.isfile(absFileName)):
#                      os.rename(absFileName,absPath+"\\"+newFileName)
#                      i=i+1
#字幕文件
subtitleType = ['.ass']
#视频文件
moveType = ['.mkv','.avi','.mp4']
#压缩文件
compressType=['.tar','.rar','.zip','.7z']

def IsFileType(file,typeList):
	#print(typeList)
	for v in typeList:
		if  file.endswith(v) == True:
			#print("------",v,file)
			return True ,v
	return False

#是否是脚本文件
def IsScriptType(file):
	if  file.endswith('.py') == True:
		return True
	else:
		return False
#是否是压缩文件
def IsCompressedFileType(file):
	return IsFileType(file,compressType)
#是否是字幕文件
def IsSubtitleType(file):
	return IsFileType(file,subtitleType)
#是否是视频文件
def IsMoveType(file):
	return  IsFileType(file,moveType)
#是否是文件夹
def IsDirType(file):
	if os.path.isfile(file) == True:
		return False
	else:
		return True

def ShowList(list):
	for v in list:
		print(v)
#获得视频文件类型
def GetMoveType(file):
	return IsFileType(file,moveType)
#获得字幕类型
def GetSubtitleType(file):
	return IsFileType(file,subtitleType)

keyList=[]
index = 0

while index <10:
	keyList .append('['+'0'+str(index)+']')
	keyList.append('['+str(index)+']')
	index = index+1
while index<20:
	keyList .append('['+str(index)+']')
	index = index+1




def AutochangeFileName(path):
	subtitleList=[]
	moveList=[]
	#pdb.set_trace()
	for file  in os.listdir(path):
	#print(file)
		file = path +'\\'+ file
		if  IsDirType(file):
			AutochangeFileName(file)
			continue
		if  IsScriptType(file):
			continue
		if IsMoveType(file):
			moveList.append(file)
		elif IsSubtitleType(file):
                      		 subtitleList.append(file)

	
	for mv in moveList:
		for key in keyList:
			if mv.find(key)  >=0:
				for sub in subtitleList :
					index = sub.find(key)
					if index >=0:
						IsMoveFind,rMoveType = GetMoveType(mv)
						if IsMoveFind == True:
							IsSubtitleFind,rSubtitleType = GetSubtitleType(sub)
							if IsSubtitleFind == True:
								newFileName = mv.replace(rMoveType,rSubtitleType)
								os.rename(sub,newFileName)
								#print(newFileName)
						break
				break

					#os.rename(sub,absPath+"\\"+newFileName)

     
AutochangeFileName(absPath)
#ShowList(moveType)
