import tkinter as tk
import random

BEATS = {"Rock": "Scissors", "Scissors": "Paper", "Paper": "Rock"}
EMOJI = {"Rock": "🪨", "Paper": "📄", "Scissors": "✂️"}

class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rock Paper Scissors")
        self.geometry("340x480")
        self.resizable(False, False)
        self.configure(bg="#fff8f0")
        self.you = 0
        self.pc  = 0
        self._build()

    def _build(self):
        tk.Label(self, text="🎮 Rock Paper Scissors",
                 font=("Comic Sans MS", 15, "bold"),
                 bg="#fff8f0", fg="#333").pack(pady=(20, 2))

        sf = tk.Frame(self, bg="#fdebd0", pady=8)
        sf.pack(fill="x", padx=28, pady=14)
        tk.Label(sf, text="You", font=("Comic Sans MS", 11, "bold"),
                 bg="#fdebd0", fg="#555").grid(row=0, column=0, padx=44)
        tk.Label(sf, text="CPU", font=("Comic Sans MS", 11, "bold"),
                 bg="#fdebd0", fg="#555").grid(row=0, column=2, padx=44)
        tk.Label(sf, text="vs", font=("Comic Sans MS", 12),
                 bg="#fdebd0", fg="#bbb").grid(row=0, column=1)
        self.lbl_you_score = tk.Label(sf, text="0",
                 font=("Comic Sans MS", 28, "bold"),
                 bg="#fdebd0", fg="#27ae60")
        self.lbl_you_score.grid(row=1, column=0, padx=44)
        self.lbl_pc_score = tk.Label(sf, text="0",
                 font=("Comic Sans MS", 28, "bold"),
                 bg="#fdebd0", fg="#e74c3c")
        self.lbl_pc_score.grid(row=1, column=2, padx=44)

        ef = tk.Frame(self, bg="#fff8f0")
        ef.pack(pady=6)
        self.lbl_you_pick = tk.Label(ef, text="❓",
                 font=("Helvetica", 40), bg="#fff8f0")
        self.lbl_you_pick.grid(row=0, column=0, padx=18)
        tk.Label(ef, text="vs", font=("Comic Sans MS", 12),
                 bg="#fff8f0", fg="#ccc").grid(row=0, column=1)
        self.lbl_pc_pick = tk.Label(ef, text="❓",
                 font=("Helvetica", 40), bg="#fff8f0")
        self.lbl_pc_pick.grid(row=0, column=2, padx=18)

        self.lbl_result = tk.Label(self, text="👇 Pick one to play!",
                 font=("Comic Sans MS", 12, "bold"),
                 bg="#fff8f0", fg="#555")
        self.lbl_result.pack(pady=8)


        self.btn_frame = tk.Frame(self, bg="#fff8f0")
        self.btn_frame.pack(pady=4)
        for label, val, bg in [
            ("🪨\nRock",     "Rock",     "#fad7a0"),
            ("📄\nPaper",    "Paper",    "#a9cce3"),
            ("✂️\nScissors", "Scissors", "#f1948a"),
        ]:
            tk.Button(self.btn_frame, text=label,
                      font=("Comic Sans MS", 11, "bold"),
                      bg=bg, fg="#333",
                      activebackground=bg,
                      relief="flat", width=7, height=3,
                      cursor="hand2",
                      command=lambda v=val: self.play(v)).pack(side="left", padx=6)

       
        self.btn_again = tk.Button(self, text="🔄  Play Again",
                 font=("Comic Sans MS", 11, "bold"),
                 bg="#a8d8a8", fg="#1a5c1a",
                 activebackground="#91c991",
                 relief="flat", padx=20, pady=7,
                 cursor="hand2", command=self.play_again)

    def play(self, choice):
        pc = random.choice(list(BEATS))
        self.lbl_you_pick.config(text=EMOJI[choice])
        self.lbl_pc_pick.config(text=EMOJI[pc])

        if choice == pc:
            msg, color = "🤝 It's a Tie!", "#e67e22"
        elif BEATS[choice] == pc:
            msg, color = "🎉 You Win!", "#27ae60"
            self.you += 1
        else:
            msg, color = "😅 You Lose!", "#e74c3c"
            self.pc += 1

        self.lbl_result.config(text=msg, fg=color)
        self.lbl_you_score.config(text=str(self.you))
        self.lbl_pc_score.config(text=str(self.pc))

        self.btn_frame.pack_forget()
        self.btn_again.pack(pady=14)

    def play_again(self):
        self.lbl_you_pick.config(text="❓")
        self.lbl_pc_pick.config(text="❓")
        self.lbl_result.config(text="👇 Pick one to play!", fg="#555")
        self.btn_again.pack_forget()
        self.btn_frame.pack(pady=4)

if __name__ == "__main__":
    Game().mainloop()