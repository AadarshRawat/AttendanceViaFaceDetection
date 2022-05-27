<div align ="center" margin-left='40%'>
<h1>Attendance Via Face Recognition </h1>
 </div>
<p align="center" >
  <img src="https://github.com/AadarshRawat/AttendanceViaFaceDetection/blob/master/DjangoMinorProject/Project/static/images/homepageavf.png" width="60%" height="50%"/>
</p>  
<br>
As the name of the project suggests, it takes attendance via face recognition ,this project involves building an attendance system which utilizes facial recognition to mark the presence. Over
the past few years, face detection technology has evolved a great deal. It is one of the best
personal identification systems that is robust

<h2>Project Planning</h2>
<b>This project is divided into four stages.
  
- In stage one I use OpenCv to detect and recognise faces, and store the
 information of present students in a list.
  
- In stage two, I use REST API to make a HTTPS PUT request to send the
information about the present students to the django project in JSON format.

- In stage three, I receive this information, store, and update the attendance in
the database and export it into a csv/xls file.

- In stage four,  I create a webpage which is used to download/access and take
attendance.
  
<h2>How to Run ?</h1>
  
  - Clone it on your computer.
  
  - Make a separate python virtual environment or use the default one already installed on your machine.
  
  - Install the required libraries and framework given in requirements.txt .
  
  - go to the following directory \DjanoMinorProject3\DjangoMinorProject\Project
  
  - Run `python manage.py runserver` inside \DjanoMinorProject3\DjangoMinorProject\Project directory  to run the project
  
 ## Project Preview:
<figure>
<img src="https://github.com/AadarshRawat/AttendanceViaFaceDetection/blob/master/DjangoMinorProject/Project/static/images/homepageavf.png" width="40%" height="40%"/>
  <br>
<figcaption align = "center"><b>Fig.1 - Home Page</b></figcaption>
</figure>

  <br>

<figure>
<img src="https://github.com/AadarshRawat/AttendanceViaFaceDetection/blob/master/DjangoMinorProject/Project/static/images/attendance.png" width="40%" height="40%"/>
  <br>
  <figcaption align="center"><b>Fig 2-OpenCV Window</b></figcaption>
</figure>
  <br>
<figure>
<img src="https://github.com/AadarshRawat/AttendanceViaFaceDetection/blob/master/DjangoMinorProject/Project/static/images/confirmationavf.png" width="40%" height="40%"/>
  <br>
  <figcaption align="center"><b>Fig 3-Confirmation Page</b></figcaption>
</figure>
  
   <br>
<figure>
<img src="https://github.com/AadarshRawat/AttendanceViaFaceDetection/blob/master/DjangoMinorProject/Project/static/images/attendancelist.png" width="40%" height="40%"/>
  <br>
  <figcaption align="center"><b>Fig 4-Attendance</b></figcaption>
</figure>

  
