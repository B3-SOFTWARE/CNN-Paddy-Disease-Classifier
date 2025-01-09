Lofty Agrotech Internship
An Image Classification Project for Identifying Plant Diseases
________________________________________
Day 1:
03/01/2025
We met Mr. Hariprasath Balachandar, the Managing Director at Lofty Agrotech, who briefed us on the project and shared the various internship opportunities available at Lofty Agrotech.
The project goal was to develop a Machine Learning model to identify and classify diseased paddy crops. We were instructed to split into teams and start working on the problem statement.
________________________________________
Day 2:
04/01/2025
We received a dataset containing 10 folders, each with images of various paddy crop diseases:
1.	bacterial_leaf_blight
2.	bacterial_leaf_streak
3.	bacterial_panicle_blight
4.	blast
5.	brown_spot
6.	dead_heart
7.	downy_mildew
8.	hispa
9.	normal
10.	tungro
The folders had varying numbers of images for each disease, ranging from 330 to 1700 images per class.
Our initial approach focused on building a Convolutional Neural Network (CNN) to classify just two classes:
1.	Normal
2.	Dead Heart
Using a small dataset of around 50 images per class, the model was trained without preprocessing. However, the results were underwhelming, as the loss dropped to a very low value (negative million).
After applying preprocessing with a basic filter and downscaling, the model was trained for 25 epochs, achieving:
•	Training Accuracy: 87%

![download](https://github.com/user-attachments/assets/2e9684a7-1bf0-4260-a8da-31b5a61f9818)

________________________________________
Day 3:
06/01/2025
We selected 400 images for each class and applied advanced preprocessing techniques, including:
1.	BGR to Grayscale Conversion (BGR2GRAY): Reduced unnecessary color information.
2.	Green Channel Enhancement: Focused on the leaf color, which is critical for identifying diseases.
The preprocessed images were fed into a CNN, and the model was trained with 400 images per class for 25 epochs. This resulted in:
•	Training Accuracy: 70%
•	Testing Accuracy:  70%

![download](https://github.com/user-attachments/assets/ea5479d9-dc8a-4899-8a78-e9a35b5059f6)
![image](https://github.com/user-attachments/assets/6a650dce-0435-40bb-a730-ef18f3bcc845)

________________________________________
Day 4:
07/01/2025
The preprocessing pipeline was further enhanced to include:
1.	Contrast Enhancement using LAB Color Space: Improved the visibility of subtle disease patterns.
2.	Edge Detection: Highlighted patterns like spots and streaks.
3.	Combined Features: Merged edges and green channel enhancement for a comprehensive feature set.
We used MobileNetV2, a pre-trained model, fine-tuned with the processed dataset. The training process included:
•	Training Epochs: 25
•	Batch Size: 32
•	Learning Rate: 0.001 (with early stopping to prevent overfitting)
Results:
•	Training Accuracy: 94.5%
•	Testing Accuracy: 94.5%
![WhatsApp Image 2025-01-07 at 22 56 03_eddb4aad](https://github.com/user-attachments/assets/6c707416-5200-4b56-b027-ad26d6c692af)

________________________________________
Day 5:
08/01/2025
We evaluated the fine-tuned MobileNetV2 model on a new set of test images sampled from the dataset (10 images per class). The following enhancements were made:
1.	Validation Pipeline: Automated batch prediction and visualization of predictions.
2.	Accuracy Computation: Calculated the accuracy for individual classes and overall average accuracy.

________________________________________
Day 6:
09/01/2025


