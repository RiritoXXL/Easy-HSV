from termcolor import colored

text = "╔╗──╔╗╔══╗╔══╗─╔═══╗───╔══╗─╔╗╔╗───╔╗╔══╗╔══╗╔══╗╔══╗╔╗╔══╗╔══╗\n║║──║║║╔╗║║╔╗╚╗║╔══╝───║╔╗║─║║║║───║║║╔═╝║╔╗║║╔╗║║╔╗║║║║╔═╝╚╗╔╝\n║╚╗╔╝║║╚╝║║║╚╗║║╚══╗───║╚╝╚╗║╚╝║───║╚╝║──║║║║║║║║║║║║║╚╝║───║║─\n║╔╗╔╗║║╔╗║║║─║║║╔══╝───║╔═╗║╚═╗║───║╔╗║──║║║║║║║║║║║║║╔╗║───║║─\n║║╚╝║║║║║║║╚═╝║║╚══╗───║╚═╝║─╔╝║───║║║╚═╗║╚╝║║╚╝║║╚╝║║║║╚═╗╔╝╚╗\n╚╝──╚╝╚╝╚╝╚═══╝╚═══╝───╚═══╝─╚═╝───╚╝╚══╝╚══╝╚══╝╚══╝╚╝╚══╝╚══╝"
colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'white']
for i, letter in enumerate(text):
    color = colors[i % len(colors)]
    print(colored(letter, color), end='')

def get_selected_image():
    selected = image_list.curselection()
    if selected:
        selected_image = image_list.get(selected[0])
        close_app()  
        openhsv(selected_image)
    else:
        print("No image selected.")

def close_app():
    root.destroy()


def openhsv(str):
    import cv2
    import numpy as np


    if __name__ == '__main__':
        def nothing(*arg):
            pass


    cv2.namedWindow( "Easy HSV" )



    img = cv2.imread('assets/' + str)
    cv2.createTrackbar('h1', "Easy HSV", 0, 255, nothing)
    cv2.createTrackbar('s1', "Easy HSV", 0, 255, nothing)
    cv2.createTrackbar('v1', "Easy HSV", 0, 255, nothing)
    cv2.createTrackbar('h2', "Easy HSV", 255, 255, nothing)
    cv2.createTrackbar('s2', "Easy HSV", 255, 255, nothing)
    cv2.createTrackbar('v2', "Easy HSV", 255, 255, nothing)
    crange = [0,0,0, 0,0,0]

    while True:
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
        h1 = cv2.getTrackbarPos('h1', "Easy HSV")
        s1 = cv2.getTrackbarPos('s1', "Easy HSV")
        v1 = cv2.getTrackbarPos('v1', "Easy HSV")
        h2 = cv2.getTrackbarPos('h2', "Easy HSV")
        s2 = cv2.getTrackbarPos('s2', "Easy HSV")
        v2 = cv2.getTrackbarPos('v2', "Easy HSV")

        h_min = np.array((h1, s1, v1), np.uint8)
        h_max = np.array((h2, s2, v2), np.uint8)

        thresh = cv2.inRange(hsv, h_min, h_max)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        img_copy = img.copy()
        cv2.drawContours(img_copy, contours, -1, (0, 255, 0), 2)
        cv2.imshow("Easy HSV", img_copy)
    
        ch = cv2.waitKey(5)
        if ch == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

import os
from tkinter import Tk, Listbox, END, filedialog, Button, messagebox

def update_list(folder_path):
    global image_list
    image_list.delete(0, END)
    valid_extensions = [".jpg", ".png", ".bmp"]
    file_count = 0
    for filename in os.listdir(folder_path):
        for ext in valid_extensions:
            if filename.lower().endswith(ext):
                image_list.insert(END, filename)
                file_count += 1
                break

    if file_count == 0:
        messagebox.showinfo("No Images Found", "The selected folder does not contain any supported image files.")

root = Tk()
root.title("Easy HSV")

assets_folder = os.path.join(os.path.dirname(__file__), "assets")
image_list = Listbox(root, width=40, height=20)
update_list(assets_folder)
image_list.pack(pady=20)

select_button = Button(root, text="Select Image", command=get_selected_image)
select_button.pack(pady=10)

root.mainloop()
