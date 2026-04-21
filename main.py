import cv2
import mediapipe as mp
import numpy as np

# --- 1. KONFIGURASI UKURAN & TEKS ---
WIDTH, HEIGHT = 640, 480
FONT = cv2.FONT_HERSHEY_PLAIN
TEXT_CONTENT = "KICAU MANIA"

# --- KONFIGURASI MEDIAPIPE ---
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

# --- INISIALISASI KAMERA & VIDEO ---
cap = cv2.VideoCapture(1)
video_path = 'assets/kicau-mania.mp4'
kicau_vid = cv2.VideoCapture(video_path)

while cap.isOpened():
    success, img = cap.read()
    if not success: break

    # Prep Webcam
    img = cv2.flip(img, 1)
    img = cv2.resize(img, (WIDTH, HEIGHT))
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    dua_tangan_terdeteksi = False
    if results.multi_hand_landmarks and len(results.multi_hand_landmarks) == 2:
        dua_tangan_terdeteksi = True
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # --- WINDOW 1: WEBCAM ---
    cv2.imshow("WEBCAM", img)

    # --- WINDOW 2: VIDEO KICAU MANIA ---
    if dua_tangan_terdeteksi:
        vid_success, vid_frame = kicau_vid.read()
        
        if not vid_success:
            kicau_vid.set(cv2.CAP_PROP_POS_FRAMES, 0)
            _, vid_frame = kicau_vid.read()

        if vid_frame is not None:
            vid_frame = cv2.resize(vid_frame, (WIDTH, HEIGHT))

            # TEKS KICAU MANIA
            cv2.putText(vid_frame, TEXT_CONTENT, (200, 80), FONT, 3, (0, 0, 0), 6, cv2.LINE_AA) # Outline hitam
            cv2.putText(vid_frame, TEXT_CONTENT, (200, 80), FONT, 3, (0, 0, 255), 3, cv2.LINE_AA)

            cv2.imshow("Kicau Mania Mode", vid_frame)
    else:
        kicau_vid.set(cv2.CAP_PROP_POS_FRAMES, 0)
        black_frame = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
        cv2.putText(black_frame, "ARE YAOW REDII??", (160, HEIGHT//2), FONT, 2.5, (0, 0, 255), 2)
        cv2.imshow("Kicau Mania Mode", black_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
kicau_vid.release()
cv2.destroyAllWindows()