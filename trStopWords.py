stopWords = ["ama","böyle","dolayısıyla","her","ki","olmak","sadece","yaptığı",
"ancak","böylece","edecek","herhangi","kim","olması","siz","yaptığını",
"arada","bu","eden","herkesin","kimse","olmayan","şey","yaptıkları",
"ayrıca","buna","ederek","hiç","mı","olmaz","şöyle","yerine",
"bana","bundan","edilecek","hiçbir","mi","olsa","şu","yine",
"bazı","bunlar","ediliyor","için","mu","olsun","şunları","yoksa",
"belki","bunları","edilmesi","ile","mü","olup","tarafından","zaten",
"ben","bunların","ediyor","ilgili","nasıl","olur","üzere",
"beni","bunu","eğer","ise","ne","olursa","var",
"benim","bunun","etmesi","işte","neden","oluyor","vardı",
"beri","burada","etti","itibaren","nedenle","ona","ve",
"bile","çok","ettiği","itibariyle","o","onlar","veya",
"bir","çünkü","ettiğini","kadar","olan","onları","ya",
"birçok","da","gibi","karşın","olarak","onların","yani",
"biri","daha","göre","kendi","oldu","onu","yapacak",
"birkaç","de","halen","kendilerine","olduğu","onun","yapılan",
"biz","değil","hangi","kendini","olduğunu","öyle","yapılması",
"bize","diğer","hatta","kendisi","olduklarını","oysa","yapıyor",
"bizi","diye","hem","kendisine","olmadı","pek","yapmak",
"bizim","dolayı","henüz","kendisini","olmadığı","rağmen","yaptı","en","kaç","herşey","sa"]

def isStopWord(parameter):
    for word in stopWords:
        if(word == parameter):
            return True

    return False

