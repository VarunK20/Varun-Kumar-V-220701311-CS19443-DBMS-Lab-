# Varun-Kumar-V-220701311-CS19443-DBMS-Lab
---

### Art Gallery Management
Art Gallery Management application allows users to register, login, and manage photo albums. Here's an abstract of the key features and functionality:
**User Authentication**

Users can register by providing their first name, last name, username, email, and password.
Registered users can log in using their username and password.
The user information is stored in a MySQL database table called users.

**Photo Album Management**

Logged-in users can create, view, edit, and delete photo albums.
Each photo album has an album name, description, and artist name associated with it.
The album information is stored in a MySQL database table called photo_album.

**Image Management**

Users can add images to their photo albums by selecting image files from their local system.
The image data is stored in a MySQL database table called images, which has a foreign key relationship with the photo_album table.
The application displays the images associated with each album in a scrollable grid layout.

**User Interface**

The application has a main window with buttons for login and registration.
After successful login, the user is presented with a home page that displays their photo albums.
The home page has an "Add Album" button to create new albums.
Each album is displayed with its name, description, artist, and a button to add images.
For each album, there are buttons to edit or delete the album.
The application uses various PyQt5 widgets, layouts, and dialogs to create the user interface.

**Database Connectivity**

The application uses the mysql.connector library to connect to a MySQL database.
SQL queries are executed to perform CRUD (Create, Read, Update, Delete) operations on the database tables.

---

### Tech Stack
**PyQt5 (Python)**
**MySQL**

---

### Steps to run the application
1. Activate the virtual environment
venv\Scripts\activate
2. Set up your own MySQL database
3. Run the main file
python main.py


---

### Sample Output Images
![Screenshot 2024-06-07 095615](https://github.com/VarunK20/Varun-Kumar-V-220701311-CS19443-DBMS-Lab-/assets/167336838/39f4c8a4-e763-4797-bec4-d5c5fdc8d2ee)

![Screenshot 2024-06-07 095633](https://github.com/VarunK20/Varun-Kumar-V-220701311-CS19443-DBMS-Lab-/assets/167336838/2d5043ab-bde9-4410-a935-2f250249fba1)

![Screenshot 2024-06-07 095912](https://github.com/VarunK20/Varun-Kumar-V-220701311-CS19443-DBMS-Lab-/assets/167336838/93390689-ee20-4280-bd67-facc921b762b)

![Screenshot 2024-06-07 095841](https://github.com/VarunK20/Varun-Kumar-V-220701311-CS19443-DBMS-Lab-/assets/167336838/ddf14095-271c-4d14-840d-10aad3d75a3e)

![Screenshot 2024-06-07 100316](https://github.com/VarunK20/Varun-Kumar-V-220701311-CS19443-DBMS-Lab-/assets/167336838/dc9fc208-84ff-4aeb-b1d3-a8eaa452f3ef)

![Screenshot 2024-06-07 100728](https://github.com/VarunK20/Varun-Kumar-V-220701311-CS19443-DBMS-Lab-/assets/167336838/e5f87dad-ad30-4aec-b4ab-06eb98596fde)

---

### Team Members
| No. | Name | Roll No |
| --- | ---- | ------- |
|1. | [Varun Kumar V](https://github.com/VarunK20) | 220701311 |
|2. | [Varun G](https://github.com/gvarun1609) |220701310|

