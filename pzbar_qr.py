from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
import time
 
def decode(im, i) :
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(im)
    # Print results
    print("qtde: ", i)
    for obj in decodedObjects:
        print('Type : ', obj.type)
        print('Data : ', obj.data.decode("utf-8"),'\n')
    return decodedObjects

# Display barcode and QR code location
def display(im, decodedObjects):
    # Loop over all decoded objects
    for decodedObject in decodedObjects:
        points = decodedObject.polygon
        # If the points do not form a quad, find convex hull
        if len(points) > 4 :
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            hull = list(map(tuple, np.squeeze(hull)))
        else :
            hull = points
        # Number of points in the convex hull
        n = len(hull)
        # Draw the convext hull
        for j in range(0,n):
            cv2.line(im, hull[j], hull[ (j+1) % n], (255,0,0), 3)

    # Display results
    cv2.imshow("Results", im)
    cv2.waitKey(0)
# Main
if __name__ == '__main__':
    inicio = time.time()
    cap = cv2.VideoCapture(0)
    # Read image
    x =0
    while (x < 101):
        _, img = cap.read()
        decodedObjects = decode(img, x)
        fim = time.time()
        print(fim - inicio)
        inicio = fim
        x = x+1
    #display(img, decodedObjects)
