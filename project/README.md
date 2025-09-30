# Live Travel
#### Video Demo: [[URL HERE](https://youtu.be/MrO4RiUk80k)]
#### Description:

This project is a **Live Travel** built using **Flask** (a Python web framework), HTML, CSS, and some additional front-end design elements. The project’s main purpose is to provide a structured platform where users can explore travel packages, learn about destinations, and book their trips through an interactive form. The site also includes navigation, login and signup options, and styled content that reflects a real-world booking experience.

The project is designed to simulate a simplified version of a travel agency’s booking platform, while still adhering to clean coding practices and modularity. My goal was to build something practical, functional, and visually appealing, while at the same time keeping the code maintainable and easy to understand for future development.

---

### Project Structure and Files

The project contains several files and folders, each serving a specific purpose:

1. **app.py**
   This is the backend file that runs the Flask application.
   - It defines routes such as `/home`, `/about`, `/contact`, `/packages`, and `/login`.
   - It also manages the connection between the front-end HTML files and the backend server.
   - Flask’s `render_template` function is used to connect the HTML templates with the app.
   - I considered adding more advanced backend features (like a database), but for the scope of this project, I focused on the core structure and routing.

2. **Templates Folder (HTML files)**
   This folder contains all the front-end pages of the site. Each file has a unique role:
   - `home.html`: The homepage, displaying the main banner, navigation bar, and welcome message.
   - `about.html`: Information about the company or project.
   - `contact.html`: A page where users can view contact details or fill in a form to reach out.
   - `packages.html`: A page listing available travel packages, with images, descriptions, and a “Book Now” button.
   - `login.html`: A login/signup page for user access.
   Each HTML page is connected to the global CSS file for styling consistency.

3. **Static Folder**
   - **CSS file (style.css)**: Contains all the styles for the project. I created a central stylesheet to keep the design uniform. It includes styling for navigation, forms, buttons, and the layout of sections.
   - **Images folder**: Contains all the images used across the website (such as the logo and travel photos). Correct placement of this folder is critical, since Flask requires a `static` folder to properly load assets.

---

### Design Choices

When building this project, I debated several design decisions:

- **Why Flask?**
  I chose Flask because it is lightweight, easy to set up, and allows me to separate backend logic from frontend templates clearly. Django would have been too heavy for this project’s scope.

- **Template System:**
  I decided to use Flask’s Jinja templating to organize HTML files. This gave me flexibility to reuse components like the navigation bar and footer across all pages.

- **Central CSS File:**
  Instead of repeating styles in multiple files, I created one `style.css` file in the static folder. This keeps the design consistent and makes future changes much easier.

- **Form Centering:**
  For the booking form, I experimented with multiple CSS approaches. At first, I thought of using body-level flexbox, but eventually I created a `.form-container` class with flex alignment to center the form independently, which gave me more control without affecting the rest of the page.

- **Login/Signup Button Styling:**
  I customized the “Login/Sign Up” link in the navigation bar so that it stands out. While the other links remain simple, this button has a distinct color and rounded borders to draw user attention.

---

### Functionality

- **Navigation Bar:**
  A responsive navigation menu with links to all the main pages.
- **Packages Page:**
  Displays a grid of destinations with “Book Now” buttons. Clicking the button takes the user to a booking form.
- **Booking Form:**
  Allows the user to enter details such as name, email, and preferred travel package. The form is styled to be centered and user-friendly.
- **Login/Signup Page:**
  A form where users can log in with credentials. In the future, this could be expanded with database support.

---

### Running the Project

To run the project:
1. Install Flask (if not installed already):
   ```bash
   pip install flask
   ```
2. Run the Flask app:
   ```bash
   flask run
   ```
3. Open the browser and go to `http://127.0.0.1:5000` to view the homepage.

It is important that all HTML files remain inside the **templates** folder, and all images and CSS files remain inside the **static** folder, otherwise Flask will not be able to load them correctly.

---

### Challenges and Learning

One of the main challenges was ensuring that static files (images and CSS) loaded properly. Flask requires strict organization of files, and at first the images did not appear because I placed them incorrectly. Another challenge was form alignment. It took experimenting with flexbox and CSS to make the booking form look professional.

I also learned the importance of file structure and consistent naming. For example, I had to carefully double-check the image folder path to match Flask’s requirements.

---

### Future Improvements

There are several features I would add if I had more time:
- **Database Integration** (SQLite or MySQL) to store user bookings and login credentials.
- **Admin Dashboard** to manage packages, view customer inquiries, and monitor bookings.
- **Payment Integration** to allow users to pay online securely.
- **Responsive Design Enhancements** to ensure the site works perfectly on mobile devices.

---

### Conclusion

This project allowed me to combine backend logic with frontend design in a practical, real-world scenario. By using Flask, I learned how to structure routes, link templates, and manage static files properly. The design choices reflect both usability and maintainability, and the final product is a clean, user-friendly travel booking website.

I am proud of this project because it demonstrates not only technical implementation but also design thinking and problem-solving skills. It serves as a solid foundation that can be expanded into a larger application with more advanced features in the future.
