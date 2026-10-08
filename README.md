# Detection_of_walking_problems
Fikir yapay zeka yardımıyla kullanıcının yürüme videosunu bir arayüzden yükleyip ortaya çıkan verilerle nörolojik,kas-iskelet ve eklem sorularını tespit etmeye çalışmak.
# Requirements
python 3.14.7   (Programlama dili)
opencv-python   (Video ile alakalı işlemler)
mediapipe       (Vücut koordinatları gibi bilgiler[Google-yapay zeka])
numpy           (Matematik motoru)
fastdtw         (Referanstan yola çıkarak karşılaştırma(elimizde az veri olacağı için bu yöntemi daha hızlı bulduk))
scipy           (fastdtw için matematik)