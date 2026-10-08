from tkinter import filedialog, messagebox
import cv2

def video_verification_and_upload(window,results_list):

    file = filedialog.askopenfilename(
        title = "İşlenecek videoyu seçin.",
        filetypes=[("Video Dosyaları","*.mp4")]
    )

    if not file:
        return

    if file.lower().endswith((".mp4")):
        try:
            test_video = cv2.VideoCapture(file)
            succeed, _ = test_video.read()
            test_video.release()

            if succeed:
                results_list[0] = file
                messagebox.showinfo("Başarılı", "Video başarıyla yüklendi.")
                window.destroy()
            else:
                messagebox.showerror("Bozuk Dosya", "Bu dosya video gibi görünüyor ama okunamıyor")
        except:
            messagebox.showerror("Hata","Dosya okunurken bir hata oluştu.")
    else:
        messagebox.showerror("Geçersiz Dosya","Lütfen sadece geçerli bir video uzantısı seçin.")

    