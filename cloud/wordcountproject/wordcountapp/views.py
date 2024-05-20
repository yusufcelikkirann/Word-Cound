from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page(request):
    return render(request, 'home.html')
    
# def word_count(request):
#     print("==============================")
#     print(request.method)
#     print(request.FILES.keys())
#     print("==============================")
#     if request.method == "POST":
#         if 'file' in request.FILES.keys():
#             file = request.FILES['file']
#             words = file.read().decode('utf-8')
#         return render(request, 'word_count.html',  {"words", words})
    
#     elif request.method == 'GET':
#         return render(request, 'home.html')
#     else:
#         return render(request, "home.html")

import findspark
findspark.init()
from itertools import islice

from pyspark.sql import SparkSession
from pyspark.conf import SparkConf

# spark = SparkSession.builder\
#     .master('local')\
#         .appName('PysparkWordCountApp')\
#             .getOrCreate()

# sc = spark.sparkContext 

# def count_word(txt_file):
#     rdd = sc.parallelize([txt_file])
#     # WordCount for genres
#     all_words = rdd.flatMap(lambda word: word.split(' ')) \
#         .map(lambda word : (word, 1)) \
#         .reduceByKey(lambda x, y, : x + y)

#     sortedWordsCounts = sorted(all_words.collect(), key=lambda x : x[1], reverse=True)
#     sortedWordsCounts = spark.sparkContext.parallelize(sortedWordsCounts)

#     return [f"Word : {word} : Count : {count}" for word, count in sortedWordsCounts.collect()]

def count_word(txt_file):
    words = txt_file.split()

    words_dict = {}
    for word in words:
        if word not in words_dict.keys():
            words_dict[word] = 1
        else:
            words_dict[word] += 1
    
    new_words = []
    
    for word, count in words_dict.items():
        new_words.append(f"Word : {word} Count : {count}")
    return new_words
    

    
def word_count(request):   
    if request.method == "POST" and request.FILES.get("file"):
        txt_file = request.FILES['file']
        file_content = txt_file.read().decode('utf-8')  
        counted_words = count_word(file_content)
        
        return render(request, 'word_count.html', context={"word_count" : counted_words})
    
    
    