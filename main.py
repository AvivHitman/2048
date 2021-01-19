import tkinter as tk
from welcome import Welcome


def main():

    root = tk.Tk()
    Welcome(root)

  #  def on_close():
   #     print("kkk")

   # root.protocol("WM_DELETE_WINDOW", on_close)

    root.mainloop()





if __name__ == "__main__":
    main()

