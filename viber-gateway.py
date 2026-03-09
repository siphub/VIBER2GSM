from flask import Flask, request
import pyautogui
import time

app = Flask(__name__)

# --- PRECISION COORDINATES ---
VIBER_UI_X, VIBER_UI_Y = 25, 45       # Viber App Activation (Top Left)
DIAL_INPUT_X, DIAL_INPUT_Y = 83, 260   # Search/Dial Field
HANGUP_X, HANGUP_Y = 1009, 789         # Red Hangup Button
# -----------------------------

@app.route('/dial')
def handle_dial():
    number = request.args.get('number')
    if not number:
        return "Error: No number", 400

    # Otomatik + Ekleme Mantığı
    formatted_num = f"+{number}" if not str(number).startswith('+') else number

    # Execution
    pyautogui.click(VIBER_UI_X, VIBER_UI_Y) # Focus Viber
    time.sleep(0.5)
    pyautogui.click(DIAL_INPUT_X, DIAL_INPUT_Y) # Click Dial Area
    time.sleep(0.3)
    pyautogui.typewrite(formatted_num)
    pyautogui.press('enter')
    
    print(f"Siphub: {formatted_num} is being dialed.")
    return f"Dialing {formatted_num}", 200

@app.route('/hangup')
def handle_hangup():
    pyautogui.click(HANGUP_X, HANGUP_Y)
    print("Siphub: Call Terminated.")
    return "Terminated", 200

if __name__ == '__main__':
    # ÖNEMLİ: Windows'ta CMD'yi 'Yönetici' olarak açıp çalıştır.
    app.run(host='0.0.0.0', port=5000)
