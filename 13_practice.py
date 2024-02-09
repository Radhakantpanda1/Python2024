# 1 wap to ask user to enter name of 3 movies, sort them and displat them
movieList=[]

movieName=input("Enter the name of movie1: ")
movieList.append(movieName);
movieName=input("Enter the name of movie2: ")
movieList.append(movieName);
movieName=input("Enter the name of movie3: ")
movieList.append(movieName);
movieList.sort()
print(movieList);

#2 WAP to check if  a list contains pallindrome elements or not
list1=[1,"abc","abc",1]
start=0;
end=len(list1)-1
while start<end :
  if(list1[start]==list1[end]):
    start+=1
    end-=1

  else:
    print("Not a pallindrome")
    break;
  
if(not (start<end)):
 print('pallindrome')


#
grades=("c","d", "a", "b", "a", "c", "b", "a", "d", "c");
countA=grades.count("a");
countB=grades.count("b");
countC=grades.count("b");
countD=grades.count("d");
print("A grade count =", countA)
print("B grade count =", countB)
print("C grade count =", countC)
print("D grade count =", countD)
gradelist=[countA,countB,countC,countD]
print(gradelist)
gradelist.sort();
print(gradelist);