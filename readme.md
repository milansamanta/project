# POKEBOOK

## DESCRIPTION:

The **POKEBOOK** is a web-based application designed to provide users with detailed information about various Pokémon. Built using **HTML, CSS, JavaScript, Flask, Bootstrap, and SQLite**, this application serves as a comprehensive Pokédex, allowing users to browse, search, and explore Pokémon from different generations. With an intuitive interface and a seamless user experience, the app offers Pokémon enthusiasts a centralized place to access and store Pokémon-related data efficiently. Users can create an account, log in to save their favorite Pokémon, and explore various Pokémon attributes in a structured manner.

### Features

- **Interactive UI**: The app is designed with a responsive and user-friendly interface using **Bootstrap** to ensure accessibility on different devices, including desktops, tablets, and mobile phones.
- **Search Functionality**: Users can easily search for Pokémon by name or ID, making it convenient to find specific Pokémon quickly.
- **Detailed Pokémon Data**: The application provides details about each Pokémon, including their name, type(s), and stats.
- **Image Display**: Each Pokémon entry includes an image sourced from an API and names and IDs stored locally in the database.
- **Other Varients**: We can also access every other varient of any pokemon
- **User Authentication**: Users can register, log in, and log out of their accounts to personalize their experience.
- **SQLite Database**: All Pokémon data is stored in an **SQLite** database, ensuring fast retrieval and efficient data management.
- **Flask Backend**: The **Flask** web framework powers the backend of the application, handling database interactions, API requests, and routing.
- **REST API Integration**: The app integrates external APIs to fetch updated Pokémon information dynamically.
- **Lightweight & Fast**: Built with performance in mind, the app ensures minimal loading time and optimized rendering.

### Technology Stack

- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Backend:** Flask (Python)
- **Database:** SQLite
- **API Integration:** Pokémon API (PokéAPI)

### How It Works

1. **Homepage & Pokémon Listing:**

   - When users visit the application, they are greeted with a homepage featuring a list of Pokémon, displayed with their names and images.
   - The listing is according to their dex no. to manage large datasets effectively.

2. **Search :**

   - Users can enter a Pokémon’s name or ID into the search bar to quickly find the desired Pokémon.
   - Searching a perticular keyword also gives search suggesions

3. **Pokémon Detail Page:**

   - Clicking on a Pokémon from the list opens a detailed view where users can see some attributes of the Pokémon, including its base stats.

4. **User Registration & Authentication:**

   - Users can register an account and securely log in to access additional features such as saving favorite Pokémon.
   - Passwords are securely hashed before being stored to ensure user security.
   - Users can log out of their accounts when finished browsing.

5. **Database Management:**

   - The Pokémon data is stored in an SQLite database, which the Flask application queries to serve information efficiently.
   - Admins can update or add new Pokémon records manually if needed.

### Installation Guide

1. Set up the SQLite database:
   ```bash
   flask db upgrade
   ```
2. Run the Flask app:
   ```bash
   flask run
   ```
3. Open a web browser and go to:
   ```
   http://127.0.0.1:5000
   ```

### Future Enhancements

- **Filtering Options:** Allow users to filter Pokémon based on moves, abilities, and evolutions.
- **Enhanced UI/UX:** Improve the visual appeal with animations and advanced styling.
- **Mobile App Version:** Develop a mobile-friendly version with offline support.
- **Expanding:** Giving details other databses like moveset and typings

### Conclusion

The Pokedex App serves as a functional and visually appealing Pokémon database, offering an engaging experience for fans and learners alike. Built with Flask and SQLite for backend efficiency, and Bootstrap for responsive design, this app provides a seamless browsing experience. Whether a user wants to quickly look up a Pokémon's stats, explore different evolutions, or save their favorite Pokémon, this application makes it all easy and enjoyable. With the added user authentication system, users can personalize their experience, and future updates aim to make the application even more interactive and feature-rich. This app is a valuable tool for Pokémon enthusiasts and a great project to showcase web development skills.

### About CS50
CS50 is a openware course from Havard University and taught by David J. Malan

Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, and software engineering. Languages include C, Python, and SQL plus students’ choice of: HTML, CSS, and JavaScript (for web development).

Thank you for all CS50.

- Where I get CS50 course?
https://cs50.harvard.edu/x/2025/