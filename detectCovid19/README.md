# Covid-Detection-Using-X-ray-Images
In today’s world, Machine learning and Deep learning have become essential in every Industry, be it business analytics or agriculture. 
One such industry is the healthcare industry, which has a huge scope for ML and DL. These techniques could be used for faster detection
of fatal diseases which can be treated if they’re detected in earlier stages. In our project we’re trying to detect Covid-19 using X-ray
images. X-ray helps us to determine the extent of virus spread, but this method needs a trained eye to even tell the difference between 
a normal and affected X-Ray, sometimes the difference is so minimal between a normal Chest X-Ray and Covid-19 affected Chest X-Ray that 
it goes undetected, hence if we can build a deep learning model, which can detect Covid-19 easily and quickly, with high precision and 
recall (since a model with low recall and precision can cause hazards to the patient, if the disease goes undetected) we can help reduce
the test detection time and help reduce the spread of virus. 


## The proposed CNN model:
CNN is  an Artificial Neural Network that has been most popularly used for Image analysis. We can think of CNN as an Artificial Neural 
Network that has some specialization for being able to pick out or detect patterns. This pattern detection is what makes CNN very useful
for Image analysis.

Screenshot below shows the UI of the flask app. On the navigation panel of the website various helpful links are provided to ease the navigation between pages of the site. 
To run the app python 3.8, tensorflow 2.2.0 version must be available on the system. Then install all the libraries and packages using anaconda distribution.

Once all requirements are met, open the terminal into the directory which contains 'app.py' file and run the command 'python app.py'
Then open the localhost: http://127.0.0.1:5000/ in the browser.

<img src="https://github.com/salonitayal/Covid-Detection-Using-X-ray-Images/blob/master/detectCovid19/screenshots/Screenshot%20from%202021-05-10%2019-21-51.png">


On clicking the Detect Covid-19 button user can easily reach to the webpage (as shown in screenshot below) of the app where X-ray image is uploaded and prediction is given. 


<img src="https://github.com/salonitayal/Covid-Detection-Using-X-ray-Images/blob/master/detectCovid19/screenshots/Screenshot%20from%202021-05-11%2000-00-14.png">

After uploading the X-ray image prediction is given as shown in screenshot below.

<img src="https://github.com/salonitayal/Covid-Detection-Using-X-ray-Images/blob/master/detectCovid19/screenshots/Screenshot%20from%202021-05-10%2019-25-15.png">

The figure below specifies on the website about the project.

<img src="https://github.com/salonitayal/Covid-Detection-Using-X-ray-Images/blob/master/detectCovid19/screenshots/Screenshot%20from%202021-05-10%2019-49-38.png">

### Project is open for suggestions. This is developed for study purposes only.