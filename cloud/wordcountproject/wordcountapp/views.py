from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return render(request, 'home.html')

# Kelime sayma fonksiyonu
def count_word(txt_file):
    # Dosyadaki tüm kelimeleri bir listeye böl
    words = txt_file.split()

    # Kelimeleri ve sayımlarını tutmak için bir sözlük oluştur
    words_dict = {}
    for word in words:
        if word not in words_dict.keys():
            words_dict[word] = 1
        else:
            words_dict[word] += 1
    
    # Kelimeleri sayım değerine göre azalan sırada sırala
    sorted_words = sorted(words_dict.items(), key=lambda item: item[1], reverse=True)

    # Yeni bir liste oluştur ve her kelimenin sayımını formatlayarak bu listeye ekle
    new_words = []
    for word, count in sorted_words:
        new_words.append(f"Kelime: {word} /// Sayısı: {count}")
    
    return new_words

# Kelime sayma view fonksiyonu
def word_count(request):   
    # Eğer istek POST ise ve bir dosya gönderildiyse
    if request.method == "POST" and request.FILES.get("file"):
        txt_file = request.FILES['file']
        file_content = txt_file.read().decode('utf-8')  
        counted_words = count_word(file_content)
        
        # Kelime sayım sonuçlarını word_count.html şablonuna gönder
        return render(request, 'word_count.html', context={"word_count": counted_words})
    else:
        return render(request, 'home.html')
