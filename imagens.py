import cv2
import time

detector = cv2.QRCodeDetector()
inicio = time.time()
x = 0

print("entrou no while, decodificando")
teste = cv2.imread('C:\\Users\\eduar\\Documents\\UFSC\\Fase 10\\TCC2\\codigo_Rasp\\im30.png')
data, _, _ = detector.detectAndDecode(teste)
fim = time.time()
print(fim - inicio)
inicio = fim
x = x+1

if data:
    print("data found: ", data, x)
else :
    print("segue o baile, pq nao encontramos QRCODE")
print(x, " vezes")

print("entrou no while, decodificando")
teste = cv2.imread('C:\\Users\\eduar\\Documents\\UFSC\\Fase 10\\TCC2\\codigo_Rasp\\im70.png')
data, _, _ = detector.detectAndDecode(teste)
fim = time.time()
print(fim - inicio)
inicio = fim
x = x+1

if data:
    print("data found: ", data, x)
else :
    print("segue o baile, pq nao encontramos QRCODE")
print(x, " vezes")

print("entrou no while, decodificando")
teste = cv2.imread('C:\\Users\\eduar\\Documents\\UFSC\\Fase 10\\TCC2\\codigo_Rasp\\im100.png')
data, _, _ = detector.detectAndDecode(teste)
fim = time.time()
print(fim - inicio)
inicio = fim

if data:
    print("data found: ", data, x)
else :
    print("segue o baile, pq nao encontramos QRCODE")
print(x, " vezes")

x = x+1

cv2.destroyAllWindows()