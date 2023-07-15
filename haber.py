import feedparser


rss_url= " "
print("Merhaba Günlük  Haberleri İnceleme Uygulamasına Hoşgeldiniz ...")
print("1-Son Dakika Haberleri")
print("2-Türkiye Haberleri")
print("3-Dünya Haberleri")
print("4-Bilim Teknoloji Haberleri")
print("5-Kültür Sanat Haberleri")
print("6-Ekonomi Haberleri")
print("7-Spor Haberleri")
secim=int(input("Haber konunuzu belirtin: "))

if secim==1:
    rss_url="https://www.cnnturk.com/feed/rss/all/news"
if secim==2:
    rss_url="https://www.cnnturk.com/feed/rss/turkiye/news"
if secim==3:
    rss_url="https://www.cnnturk.com/feed/rss/dunya/news"
if secim==4:
    rss_url="https://www.cnnturk.com/feed/rss/bilim-teknoloji/news"
if secim==5:
    rss_url="https://www.cnnturk.com/feed/rss/kultur-sanat/news"
if secim==6:
    rss_url="https://www.cnnturk.com/feed/rss/ekonomi/news"
if secim==7:
    rss_url="https://www.cnnturk.com/feed/rss/spor/news"



feed = feedparser.parse(rss_url)

if secim == 1:
    print("Haber Liste Konusu: Son Dakika Haberleri")
if secim == 2:
    print("Haber Liste Konusu: Türkiye Haberleri")
if secim == 3:
    print("Haber Liste Konusu: Dünya Haberleri")
if secim == 4:
    print("Haber Liste Konusu: Bilim Teknoloji Haberleri")
if secim == 5:
    print("Haber Liste Konusu: Kültür Sanat Haberleri")
if secim == 6:
    print("Haber Liste Konusu: Ekonomi Haberleri")
if secim == 7:
    print("Haber Liste Konusu: Spor Haberleri")

print("\n")

for entry in feed.entries:
    print("Haber Başlığı:", entry.title)
    print("Haber Saati:", entry.published)
    print("Haber Linki:", entry.link)
    print("\n")
 
input()
