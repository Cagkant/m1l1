from flask import Flask
import random

facts_list = ["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
"2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.",
"Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.",
"2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.",
"Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır.",
"Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
"Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor.",
"Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız."
]

sifre = ""
karaks = "qwertyuıopğüasdfghjklşizxcvbnmöç1234567890.,<>:;-_*?=)(/&%+^'!}][{§½$#£>}])"

app = Flask(__name__)

@app.route("/rastgele_gercekler")
def hello_world():
    return f'<p>{random.choice(facts_list)}. Anasayfaya dönmek için:</p><a href = "/"> Tıkla </a></p>'

@app.route("/farklıbise")
def bise():
    return f"<p>Şişman ablam yer altında, dalları yer üstünde. Cevap için:</p><a href = '/cevap'> Tıkla </a>"

@app.route("/cevap")
def cvp():
    return f"<p>Cevap havuçtu. Anasayfaya dönmek için:</p><a href = '/'> Tıkla </a>"



@app.route("/")
def real_world():
    return f'<p>Teknoloji hakkında bilgi almak için:</p><a href = "/rastgele_gercekler"> Tıkla </a> <p> bilmece için</p><a href = "/farklıbise"> Tıkla </a>'


app.run(debug=True, port=5000)