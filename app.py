import random,time,tkinter as tk
from tkinter import messagebox, simpledialog  
from db import init_db,ins,gts
with open("words.txt","r") as f:
    words=f.read().split()
class TypeMaster:
    def __init__(self,root):
        self.root=root
        self.root.title("TypeMaster")
        self.root.geometry("700x500")
        init_db()
        self.start_time=None
        self.word_count=30
        self.words=random.sample(words,self.word_count)
        self.current_index=0
        self.label=tk.Label(root,text="TypeMaster",font=("Consolas",14))
        self.label.pack(pady=20)
        self.text_box=tk.Text(root,height=5,width=60,font=("Consolas",14))
        self.text_box.pack()
        self.text_box.bind("<KeyPress>", self.on_key_press)
        self.target_label=tk.Label(root,text=" ".join(self.words),wraplength=600,font=("Consolas",14))
        self.text_box.focus_set()
        self.target_label.pack(pady=10)
        self.finish_btn=tk.Button(root,text="Finish", command=self.calculate_results)
        self.finish_btn.pack(pady=10)
        self.leaderboard_btn=tk.Button(root,text="View Leaderboard", command=self.show_leaderboard)
        self.leaderboard_btn.pack()
    def on_key_press(self, event):
        print("[DEBUG] Key pressed:", event.char)
        self.start_timer(event)
    def start_timer(self,event=None):
        if self.start_time is None: 
            self.start_time=time.time()
            print("[DEBUG] Timer started at", self.start_time)  
    def calculate_results(self):
        print("[DEBUG] Start time when calculating:", self.start_time)  
        if self.start_time is None: 
            messagebox.showwarning("Wait", "Please start typing first!")
            return
        input_text=self.text_box.get("1.0",tk.END).strip()
        if not input_text:  
            messagebox.showwarning("Wait", "Please start typing first!")
            return
        elapsed=max(time.time()-self.start_time,1)
        words=input_text.split()
        correct=sum(1 for i in range(min(len(words),len(self.words)))if words[i]==self.words[i])
        wpm=round((len(words)/elapsed)*60)
        accuracy=round((correct/self.word_count)*100,2)
        name=simpledialog.askstring("Your Name", "Enter your name:")  # Fixed: was tk.simpledialog
        if name:
            ins(name, wpm, accuracy)
            messagebox.showinfo("Results", f"Name: {name}\nWPM: {wpm}\nAccuracy: {accuracy}%")
            self.root.destroy()
    def show_leaderboard(self):
        top_scores=gts()
        leaderboard_text="\n".join([f"{i+1}.{name}-{wpm}WPM({acc}% accuracy)" for i,(name,wpm,acc,_) in enumerate(top_scores)])
        messagebox.showinfo("Leaderboard",leaderboard_text or "No scores yet")  # Fixed typo: "socres" -> "scores"
if __name__=="__main__":
    root=tk.Tk()
    app=TypeMaster(root)
    root.mainloop()