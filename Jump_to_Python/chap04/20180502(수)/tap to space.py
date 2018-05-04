#coding: cp949

txtFile = open("tapfile.txt",'r');
FileStr = txtFile.read();
FileStr.replace('\t',"    ");
txtFile.close();
txtFile = open("tapfile.txt",'w');
txtFile.write(FileStr);
txtFile.close();
