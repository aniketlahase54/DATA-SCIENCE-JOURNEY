# Write file 
data = "Data Analyst with skills in SQL, Python, and Power BI, specialized in transforming raw business data into actionable insights through end-to-end analytics solutions including data extraction, exploratory data analysis (EDA), advanced DAX measures, and interactive KPI dashboards. Strong analytical and problem-solving skills with the ability to support pricing, inventory management, and performance optimization"

file = open("demo.txt","w")
file.write(data)
file.close()


#Read file
file = open("demo.txt","r")
data = file.read()
print(data)

#Readline
file = open("demo.txt","r")
data = file.readline()
print(data)

# Readlines
file = open("demo.txt","r")
data = file.readlines()
print(data)

#Append
file = open("demo.txt","a")
data = file.write("\nAniket lahase")
print(data)
file.close()

#Delete File
import os 
os.remove("demo.txt")

#Using with Statement (Best Practice)
with open("demo.txt","r") as file:
    data = file.read()
    print(data)
