import cv2
import torch
import torchvision
import numpy as np

def gstreamer_pipeline(flip_method=0):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)640, height=(int)480, "
        "format=(string)NV12, framerate=(fraction)30/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! "
        "appsink"
        % (flip_method)
    )

# Load a pretrained face detection model
face_detection_model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)

# Set the model to evaluation mode
face_detection_model.eval()

# Load the video capture object
cap = cv2.VideoCapture(0)

if cap.isOpened() == False:
    print("Unable to read camera")
else:
    # Get the frame information
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    
    # Create a video writer object to save the video
    out = cv2.VideoWriter('C:/Users/rkdau/OneDrive/사진/카메라 앨범/face.avi',
                    cv2.VideoWriter_fourcc(*'XVID'),
                    30.0,
                    (frame_width, frame_height))       
    
    # The transformation to apply to the image before running it through the model
    transform = torchvision.transforms.Compose([
        torchvision.transforms.ToTensor(),
        torchvision.transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    while True:
        # Capture a frame from the video stream
        ret, frame = cap.read()
        
        # Convert the image from BGR to RGB format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Convert the image to a PyTorch tensor
        image = transform(frame).unsqueeze(0)
        
        # Run the face detection model on the image
        with torch.no_grad():
            output = face_detection_model(image)
        
        # The output is a list with a single dictionary containing the detection results
        faces = output[0]['boxes']
        
        # Draw rectangles around the detected faces
        for face in faces:
            x1, y1, x2, y2 = face.numpy().astype(int)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        # Write the resulting frame to the output video
        out.write(frame)
        
        # Display the resulting frame
        cv2.imshow('frame', frame)

        if cv2.waitKey(0) & 0xFF == ord('q') :
            break
cap.release()
out.release()
cv2.destroyAllWindows()