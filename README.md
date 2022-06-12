# Game Gluttons

## Project Description
This site is called Game Gluttons. It is an app used to explore popular board games and store a collection of your own board games. Users will be able to login/sign-up and save games to their collection. If not signed up, they will be able to browse popular games and see descriptions of them.  It's main goal is to recreate some of the functionality of boardgamegeeks.com. 
I will be using Django/PostgreSQL to create this app, utilizing its login/signup functionality for user authentication.

## Link to App
https://game-gluttons.herokuapp.com/

## Installation Instructions
- To download the source code, go here: https://github.com/SaidNivek/game_gluttons 
- Fork the code to your own GitHub page. 
- Clone the repo to your local environment. 
- Install all dependencies. -- Note: Ensure that your environment is able to host a virtual environment and utilize Django for the code to work properly
- In your terminal, ```python3 manage.py runserver```
- Go to your web browser and go to ```localhost:8000```

## Technologies Used
- Django
- Python
- API calls (XML responses)

## MVP User Stories
### As a user I want to:
Either logged in or not:
- Browse popluar games, displaying their images, name, rating
- Click on a game and see a detailed view of that game's information
- Search for a game by name and have it and similarly named games display on the screen (If I type 'Cat' I should get Catan, Catacombs, etc.)
- Access an About page that has informatiom about me, my love of board games, my game collection, and where to find my LinkedIn / GitHub

If not logged in:
- Be able to sign-up for an account
- Be able to login with an already created account

If logged in:
- Be able to logout from the website
- Access a user page with their information and their collection of games
- Update their user profile
- Delete their user profile

## Stretch User Stories
### As a user I want to:
Either logged in or not:
- Read reviews for each game
- See likes for a game

If not logged in:
- Create an account/login using Google/etc.

If logged in:
- Add a game to a personal collection of games from the game's detail page
- Add a game to a personal collection from a user detail page
- Remove a game from their collection from the game's details page
- Remove a game to a personal collection from a user detail page
- Write reviews to a game
- Delete reviews from a game
- Like a game
- Remove a like from a game
- Request for a new game to be added to the database (needs authorization from admin)
- Set a favorite game within your user profile

## Known Issues
There are currently no known issues with the most up-to-date build.

## Major Hurdles
- The XML API was quite difficult to work with and utilize effectively, particularly when it came to the Search functionality of the game
- The Search functionality was difficult, as it requires several API calls with multiple checks and conditionals to ensure the most useful and usable data was returned and stored in the database
- Using the database for collections and wishlists proved to be too difficult for this iteration of the app, due to the way the databases are set up, along with the ID used from the API, making connecting the databases by primary key not as useful/feasible at this time

## Future Goals & Implementation
- I would like to tackle adding wishlists and game collections by users to their profiles.  This would require some thought as to how to incorporate the current structure of the database or to refactor the databases into something else with more readily usable primary keys.
- Favoriting games that you own or showcasing your current favorite game on your profile page.
- Allowing users to look at wishlists and collections from other users.
- Reviews and ratings by users for each game.

## API
I will use the Board Game Geek API to seed my own database with data. The API is free to use and does not require any authentication. It's docs can be found [here](https://boardgamegeek.com/wiki/page/BGG_XML_API2).

## ERD
![image](https://user-images.githubusercontent.com/89223981/171916031-2268d54a-b2e6-49fb-84aa-005ef70019df.png)

## Original Wireframes
### Home Page
![image](https://user-images.githubusercontent.com/89223981/171911119-e9b0528e-c187-428c-b56c-19b9c37ce0f8.png)

### Game Detail Page
![image](https://user-images.githubusercontent.com/89223981/171911200-fbe56e2f-3c96-4000-9d68-46538de8e1b7.png)

### User Profile Page
![image](https://user-images.githubusercontent.com/89223981/171911224-bea82d42-ef04-48f6-9b30-206635394384.png)

### Login/Signup Pages
![image](https://user-images.githubusercontent.com/89223981/171911342-695a3786-26b8-4b2d-980d-c4fee8fb182e.png)

### Notes from Capstone Reqs for end of project README.md updates/confirmation of completion

- **A `README.md` file** with:
    - A **link to your hosted working app**.
    - A paragraph-long **description** (elevator pitch) of your project.
    - A list of the **technologies used**.
    - A list of **installation steps** for the app itself and any dependencies - how would another developer run your site locally?
    - Link to your **user stories** - who are your users, what do they want, and why?
    - Link to your **wireframes** – sketches of major views / interfaces in your application.
    - Link to your **entity relationship diagrams** – plan out your data relationships before coding.
    - Descriptions of any **unsolved problems** or **future features**.
