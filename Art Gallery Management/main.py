import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QDialog, QMessageBox, QListWidget, QFileDialog, QHBoxLayout, QScrollArea, QGridLayout
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
import mysql.connector

class UserListWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('User List')
        self.resize(400, 300)
        layout = QVBoxLayout()
        label = QLabel('User List')
        label.setFont(QFont('Arial', 16))
        layout.addWidget(label)
        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)
        self.setLayout(layout)

    def loadUsers(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="gallery_user",
                password="varun2711",
                database="art_gallery"
            )

            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            self.list_widget.clear()
            for row in rows:
                user_info = f"{row[0]} - {row[1]} {row[2]} ({row[3]})"
                self.list_widget.addItem(user_info)
            conn.close()
        except mysql.connector.Error as e:
            print(f'Failed to retrieve users: {e}')

class ArtGalleryManagement(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Art Gallery Management')
        self.resize(600, 400)
        self.setStyleSheet('background-color: #40618E;')
        layout = QVBoxLayout()
        label = QLabel('ART GALLERY MANAGEMENT')
        label.setStyleSheet('color: #4CAF50; font-size: 34px; font-weight: bold;')
        label.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(250, 20, 250, 300)
        login_button = QPushButton('Login')
        login_button.setStyleSheet('background-color: #008CBA; color: white;')
        login_button.setFont(QFont('Arial', 14))
        login_button.clicked.connect(self.showLogin)
        registration_button = QPushButton('Register')
        registration_button.setStyleSheet('background-color: #171065; color: white;')
        registration_button.setFont(QFont('Arial', 14))
        registration_button.clicked.connect(self.showRegistration)
        layout.addWidget(label)
        layout.addWidget(login_button)
        layout.addWidget(registration_button)
        self.setLayout(layout)

    def showLogin(self):
        login_form = LoginForm(self)
        if login_form.exec_() == QDialog.Accepted:
            username = login_form.username_edit.text()
            self.showHomePage(username)

    def showRegistration(self):
        registration_form = RegistrationForm(self)
        registration_form.exec_()

    def showHomePage(self, username):
        self.home_page = HomePage(username)
        self.home_page.show()

class RegistrationForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Registration Form')
        self.first_name_edit = QLineEdit()
        self.last_name_edit = QLineEdit()
        self.username_edit = QLineEdit()
        self.email_edit = QLineEdit()
        self.password_edit = QLineEdit()
        self.confirm_password_edit = QLineEdit()
        self.first_name_edit.setStyleSheet('color: white;')
        self.last_name_edit.setStyleSheet('color: white;')
        self.username_edit.setStyleSheet('color: white;')
        self.email_edit.setStyleSheet('color: white;')
        self.password_edit.setStyleSheet('color: white;')
        self.confirm_password_edit.setStyleSheet('color: white;')
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.confirm_password_edit.setEchoMode(QLineEdit.Password)
        layout = QVBoxLayout()
        self.addFormField(layout, 'First Name:', self.first_name_edit)
        self.addFormField(layout, 'Last Name:', self.last_name_edit)
        self.addFormField(layout, 'Username:', self.username_edit)
        self.addFormField(layout, 'Email:', self.email_edit)
        self.addFormField(layout, 'Password:', self.password_edit)
        self.addFormField(layout, 'Confirm Password:', self.confirm_password_edit)
        self.setLayout(layout)
        self.ok_button = QPushButton('OK')
        self.cancel_button = QPushButton('Cancel')
        self.ok_button.setStyleSheet('color: white;')
        self.cancel_button.setStyleSheet('color: white;')
        layout.addWidget(self.ok_button)
        layout.addWidget(self.cancel_button)
        self.ok_button.clicked.connect(self.register)
        self.cancel_button.clicked.connect(self.reject)

    def addFormField(self, layout, label_text, edit_widget):
        label = QLabel(label_text)
        label.setStyleSheet('color: white;')
        layout.addWidget(label)
        layout.addWidget(edit_widget)

    def register(self):
        first_name = self.first_name_edit.text()
        last_name = self.last_name_edit.text()
        username = self.username_edit.text()
        email = self.email_edit.text()
        password = self.password_edit.text()
        confirm_password = self.confirm_password_edit.text()

        if not (first_name and last_name and username and email and password and confirm_password):
            QMessageBox.critical(self, 'Error', 'All fields are required!')
            return

        if password != confirm_password:
            QMessageBox.critical(self, 'Error', 'Passwords do not match!')
            return

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="gallery_user",
                password="varun2711",
                database="art_gallery"
            )

            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (first_name, last_name, username, email, password) VALUES (%s, %s, %s, %s, %s)",
                           (first_name, last_name, username, email, password))
            conn.commit()
            conn.close()

            QMessageBox.information(self, 'Success', 'Registration Successful!')
            self.accept()  
        except mysql.connector.Error as e:
            QMessageBox.critical(self, 'Error', f'Failed to register user: {e}')

class LoginForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Login')
        self.username_edit = QLineEdit()
        self.password_edit = QLineEdit()
        self.username_edit.setStyleSheet('color: white;')
        self.password_edit.setStyleSheet('color: white;')
        self.password_edit.setEchoMode(QLineEdit.Password)
        layout = QVBoxLayout()
        self.addFormField(layout, 'Username:', self.username_edit)
        self.addFormField(layout, 'Password:', self.password_edit)
        self.setLayout(layout)
        self.ok_button = QPushButton('Login')
        self.cancel_button = QPushButton('Cancel')
        self.ok_button.setStyleSheet('color: white;')
        self.cancel_button.setStyleSheet('color: white;')
        layout.addWidget(self.ok_button)
        layout.addWidget(self.cancel_button)
        self.ok_button.clicked.connect(self.login)
        self.cancel_button.clicked.connect(self.reject)

    def addFormField(self, layout, label_text, edit_widget):
        label = QLabel(label_text)
        label.setStyleSheet('color: white;')
        layout.addWidget(label)
        layout.addWidget(edit_widget)

    def login(self):
        username = self.username_edit.text()
        password = self.password_edit.text()

        if not (username and password):
            QMessageBox.critical(self, 'Error', 'Username and password are required!')
            return

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="gallery_user",
                password="varun2711",
                database="art_gallery"
            )

            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
            row = cursor.fetchone()

            if row:
                QMessageBox.information(self, 'Success', 'Login Successful!')
                self.accept()  
            else:
                QMessageBox.critical(self, 'Error', 'Invalid username or password!')

            conn.close()
        except mysql.connector.Error as e:
            QMessageBox.critical(self, 'Error', f'Failed to authenticate user: {e}')

class HomePage(QWidget):
    def __init__(self, username):
        super().__init__()
        self.setWindowTitle('Home Page')
        self.resize(800, 600)
        self.username = username
        self.header_layout = QVBoxLayout()
        self.username_label = QLabel(f"Logged in as: {self.username}")
        self.header_layout.addWidget(self.username_label)
        self.add_album_button = QPushButton('Add Album')
        self.add_album_button.clicked.connect(self.addAlbum)
        self.header_layout.addWidget(self.add_album_button)
        self.albums_layout = QVBoxLayout()
        self.header_layout.addLayout(self.albums_layout)
        self.loadAlbums()
        self.setLayout(self.header_layout)

    def loadAlbums(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="gallery_user",
                password="varun2711",
                database="art_gallery"
            )
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM photo_album")
            albums = cursor.fetchall()
            for i in reversed(range(self.albums_layout.count())):
                widget = self.albums_layout.itemAt(i).widget()
                if widget:
                    widget.deleteLater()
            for album in albums:
                album_widget = self.createAlbumWidget(album)
                self.albums_layout.addWidget(album_widget)

            conn.close()
        except mysql.connector.Error as e:
            print(f'Failed to load albums: {e}')

    def createAlbumWidget(self, album):
        album_widget = QWidget()
        layout = QVBoxLayout()
        album_name_label = QLabel(f"Album Name: {album[1]}")
        description_label = QLabel(f"Description: {album[2]}")
        artist_label = QLabel(f"Artist: {album[3]}")

        layout.addWidget(album_name_label)
        layout.addWidget(description_label)
        layout.addWidget(artist_label)
        add_images_button = QPushButton('Add Images')
        add_images_button.clicked.connect(lambda: self.addImages(album[0]))
        layout.addWidget(add_images_button)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_widget = QWidget()
        grid_layout = QGridLayout()
        scroll_widget.setLayout(grid_layout)
        scroll_area.setWidget(scroll_widget)
        layout.addWidget(scroll_area)

        album_widget.scroll_area = scroll_area
        album_widget.grid_layout = grid_layout
        self.loadImages(album[0], grid_layout)
        edit_button = QPushButton('Edit')
        edit_button.clicked.connect(lambda: self.editAlbum(album[0]))

        delete_button = QPushButton('Delete')
        delete_button.clicked.connect(lambda: self.deleteAlbum(album[0]))

        button_layout = QHBoxLayout()
        button_layout.addWidget(edit_button)
        button_layout.addWidget(delete_button)

        layout.addLayout(button_layout)

        album_widget.setLayout(layout)
        return album_widget
    
    def get_images_for_album(album_id):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="gallery_user",
                password="varun2711",
                database="art_gallery"
            )
            cursor = conn.cursor()
            query = "SELECT image_data FROM images WHERE album_id = %s"
            cursor.execute(query, (album_id,))
            images = cursor.fetchall()

            conn.close()
            return images

        except mysql.connector.Error as e:
            print(f'Failed to retrieve images: {e}')
            return None


    def addAlbum(self):
        dialog = AddAlbumDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            album_data = dialog.getAlbumData()
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="gallery_user",
                    password="varun2711",
                    database="art_gallery"
                )
                cursor = conn.cursor()
                cursor.execute("INSERT INTO photo_album (album_name, description, artist) VALUES (%s, %s, %s)",
                               (album_data['album_name'], album_data['description'], album_data['artist']))
                conn.commit()
                conn.close()
                self.loadAlbums()
            except mysql.connector.Error as e:
                print(f'Failed to add album: {e}')

    def editAlbum(self, album_id):
        dialog = EditAlbumDialog(self, album_id)
        if dialog.exec_() == QDialog.Accepted:
            album_data = dialog.getAlbumData()
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="gallery_user",
                    password="varun2711",
                    database="art_gallery"
                )
                cursor = conn.cursor()
                cursor.execute("UPDATE photo_album SET album_name = %s, description = %s, artist = %s WHERE album_id = %s",
                               (album_data['album_name'], album_data['description'], album_data['artist'], album_id))

                conn.commit()
                conn.close()
                self.loadAlbums()
            except mysql.connector.Error as e:
                print(f'Failed to edit album: {e}')

    def deleteAlbum(self, album_id):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="gallery_user",
                password="varun2711",
                database="art_gallery"
            )
            cursor = conn.cursor()
            cursor.execute("DELETE FROM images WHERE album_id = %s", (album_id,))
            cursor.execute("DELETE FROM photo_album WHERE album_id = %s", (album_id,))
            conn.commit()
            conn.close()
            self.loadAlbums()
        except mysql.connector.Error as e:
            print(f'Failed to delete album: {e}')

class AddAlbumDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Add Album')
        self.album_name_edit = QLineEdit()
        self.description_edit = QLineEdit()
        self.artist_edit = QLineEdit()
        layout = QVBoxLayout()
        self.addFormField(layout, 'Album Name:', self.album_name_edit)
        self.addFormField(layout, 'Description:', self.description_edit)
        self.addFormField(layout, 'Artist:', self.artist_edit)
        self.setLayout(layout)
        self.ok_button = QPushButton('OK')
        self.cancel_button = QPushButton('Cancel')
        layout.addWidget(self.ok_button)
        layout.addWidget(self.cancel_button)
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

    def addFormField(self, layout, label_text, edit_widget):
        label = QLabel(label_text)
        layout.addWidget(label)
        layout.addWidget(edit_widget)

    def getAlbumData(self):
        return {
            'album_name': self.album_name_edit.text(),
            'description': self.description_edit.text(),
            'artist': self.artist_edit.text()
        }

class EditAlbumDialog(AddAlbumDialog):
    def __init__(self, parent=None, album_id=None):
        super().__init__(parent)
        self.setWindowTitle('Edit Album')
        self.album_id = album_id
        self.loadAlbumData()

    def loadAlbumData(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="gallery_user",
                password="varun2711",
                database="art_gallery"
            )
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM photo_album WHERE album_id = %s", (self.album_id,))
            album = cursor.fetchone()
            self.album_name_edit.setText(album[1])
            self.description_edit.setText(album[2])
            self.artist_edit.setText(album[3])

            conn.close()
        except mysql.connector.Error as e:
            print(f'Failed to load album data: {e}')

app = QApplication(sys.argv)
main_window = ArtGalleryManagement()
main_window.show()
sys.exit(app.exec_())