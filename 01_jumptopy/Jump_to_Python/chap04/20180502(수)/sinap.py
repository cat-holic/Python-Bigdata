
temStr= "이유덕,이재영,권종표,이재영,박민호,강상희,이재영," +\
    "김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌";
strList = temStr.split(',');

kim_count=0;
lee_count=0;
for i in strList:
    if i[0]=="김":kim_count+=1;
    elif i[0]=="이":lee_count+=1;
print("kim_count : %d\nlee_count: %d" %(kim_count,lee_count));
print(strList.count("이재영"));

strList = list(set(strList));
print(strList);
strList.sort();
print(strList);
print("a\ta")