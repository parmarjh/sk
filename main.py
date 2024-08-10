import streamlit as st
import cv2
import numpy as np
import mediapipe as mp

def convert_and_process(uploaded_file):
    with open("temp.mp4", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Convert to desired format (replace with your preferred format)
    cap = cv2.VideoCapture("temp.mp4")
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

    # Initialize Mediapipe Pose
    mp_pose = mp.solutions.pose
    with mp_pose.Pose() as pose:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Convert to RGB for Mediapipe
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(image)

            # Draw skeleton stickfigure (basic implementation)
            if results.pose_landmarks:
                for id, lm in enumerate(results.pose_landmarks.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y  
 * h)
                    cv2.circle(image, (cx, cy), 5, (255, 0, 0), cv2.FILLED)  


            # Write the frame with stickfigures to the output video
            out.write(image)

    cap.release()
    out.release()

def main():
    st.title("Video Upload and Processing")
    uploaded_file = st.file_uploader("Upload a video")
    if uploaded_file is not None:
        convert_and_process(uploaded_file)
        st.video('output.mp4')

if __name__ == '__main__':
    main()
