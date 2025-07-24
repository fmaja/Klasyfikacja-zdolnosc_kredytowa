install.packages("readODS")
library(readODS)

dane <- read_ods("C:/Users/crwar/OneDrive/Pulpit/PROGRAMOWANIE/SEMESTR 4/MAD/MADv2/baza.ods")

par(mfrow=c(2,1))

#Boxploty

boxplot(dane$X2, main = "Boxplot dla: Czas trwania kredytu (w miesiącach)", col = "lightgreen")

boxplot(dane$X5, main = "Boxplot dla: Kwota kredytu", col = "lightpink")

boxplot(dane$X8, main = "Boxplot dla: Rata w stosunku do dochodu", col = "lightblue")

boxplot(dane$X11, main = "Boxplot dla: Czas zamieszkania pod aktualnym adresem", col = "lightseagreen")

boxplot(dane$X13, main = "Boxplot dla: Wiek klienta", col = "yellow")

boxplot(dane$X16, main = "Boxplot dla: Liczba aktualnych kredytów w tym banku", col = "red")

boxplot(dane$X21, main = "Boxplot dla: Klasa", col = "green")


#Histogramy
par(mfrow=c(2,1))

hist(dane$X2, main = "Histogram dla: Czas trwania kredytu (w miesiącach)", col = "lightgreen")

hist(dane$X5, main = "Histogram dla: Kwota kredytu", col = "lightpink")

hist(dane$X8, main = "Histogram dla: Rata w stosunku do dochodu", col = "lightblue")

hist(dane$X11, main = "Histogram dla: Czas zamieszkania pod aktualnym adresem", col = "lightseagreen")

hist(dane$X13, main = "Histogram dla: Wiek klienta", col = "yellow")

hist(dane$X16, main = "Histogram dla: Liczba aktualnych kredytów w tym banku", col = "red")

hist(dane$X21, main = "Histogram dla: Klasa", col = "green")
