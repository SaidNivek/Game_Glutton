# Game Gluttons

## Project Description
This site is called Game Gluttons. It is an app used to explore popular board games and store a collection of your own board games. Users will be able to login/sign-up and save games to their collection. If not signed up, they will be able to browse popular games and see descriptions of them.  It's main goal is to recreate some of the functionality of boardgamegeeks.com. 
I will be using Django/PostgreSQL to create this app, utilizing its login/signup functionality for user authentication.

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

## Wireframes
### Home Page
![image](https://user-images.githubusercontent.com/89223981/171911119-e9b0528e-c187-428c-b56c-19b9c37ce0f8.png)

### Game Detail Page
![image](https://user-images.githubusercontent.com/89223981/171911200-fbe56e2f-3c96-4000-9d68-46538de8e1b7.png)

### User Profile Page
![image](https://user-images.githubusercontent.com/89223981/171911224-bea82d42-ef04-48f6-9b30-206635394384.png)

### Login/Signup Pages
![image](https://user-images.githubusercontent.com/89223981/171911342-695a3786-26b8-4b2d-980d-c4fee8fb182e.png)

## ERD
![image](https://user-images.githubusercontent.com/89223981/171916031-2268d54a-b2e6-49fb-84aa-005ef70019df.png)

## Installation Instructions

## Known Issues

## Major Hurdles

## Future Goals & Implementation

## API
I will use the Board Game Geek API to seed my own database with data. The API is free to use and does not require any authentication. It's docs can be found [here](https://boardgamegeek.com/wiki/page/BGG_XML_API2).

## Feasibility Study
If needed, I will include one here.  Before I begin with the real coding, I will ensure that I can properly seed a PostrgreSQL database with the data I need from the Board Game Geeks API.  If not, I will have to switch to using a MERN Stack and not Django


- **Scope:** What are you planning to build? What do you reasonably think you can implement in the time period?
- **User Stories:** Who is your user? What features will your app have?
- **Wireframes:** Sketch out what your core pages will look like and how they will work. Consider making a *paper prototype* to demonstrate and/or test key user interactions.
- **Data Models:** Draw out the models and any associations for your project in an entity relationship diagram (ERD).
- **Milestones:** Divide your work into parts - the most essential features for your MVP, features that are important but not essential, and features that can be saved for a later iteration. Create 3-5 major milestones with dates outlining when you expect essential features will be done.
- **Feasibility Study (optional):** If you're using an external API or scraping a website, make sure you can get that data. If you're using a new language, framework, or tool, go through its getting started tutorial. ***We will ask to see your results.***

### Notes from Capstone Reqs for end of project README.md updates/confirmation of completion
- A **working full-stack application**, hosted somewhere on the internet.
- A **git repository hosted on Github**, with frequent commits dating back to the beginning of the project.
- A **link to your hosted working app** in the URL section of your Github repo.
- **A `README.md` file** with:
    - A **link to your hosted working app**.
    - A paragraph-long **description** (elevator pitch) of your project.
    - A list of the **technologies used**.
    - A list of **installation steps** for the app itself and any dependencies - how would another developer run your site locally?
    - Link to your **user stories** - who are your users, what do they want, and why?
    - Link to your **wireframes** – sketches of major views / interfaces in your application.
    - Link to your **entity relationship diagrams** – plan out your data relationships before coding.
    - Descriptions of any **unsolved problems** or **future features**.
