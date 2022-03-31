# Fit At Home

![Mobile Header](static/images/readme/#)

https://fit-at-home.herokuapp.com/

## Author

Arthur Henrique El Mezaonik Martins

## Table of Contents


## Project Overview

Fit At Home's main target are those who have a healthy life and don't like to keep having fast food, but also don't have time or skills to cook nice and healthy food.

But not just those guys can consume our product, our product is for everyone that wants to try a new food or simply doesn't know how to cook.

We offer appetizers and main plates, from Vegan food to a plate base on Beef or Pork, and you can have it all on your doorstep without the need to wash the pans after.

## UX

Our main target are those who have a healthy life and but don't have time or skills to cook nice and healthy food. To solve those problems we offer two things.

First is our menu which has a variety of healthy foods, where the costumer can choose between one of our colelctions (appetizer, beef, chicken, pork, fish and vegan) and receive the prepered food at home.

The second is our blog page, where we will have posts teaching how to prepare a nice food, but not just that, also posts talking about healthy life and exercices.

## Target Audience

1. Users that don't have time to prepare their healthy meal

2. Users that have time to cook but don't know how to prepare a nice and healthy meal

3. Users looking for healthy food recipes

4. Users looking for tips about healthy life anf exerceise

## Design Choices

### Colors

The main colors are green and orange, they were chosen to give the impression from something healthier/natural.

The other colors used are mainly black and white, to give a good contrast with the main colors.

![Color Pallet](static/images/readme/#)

### Images

The main image on the home page was chosen to represent that the site wants to bring information about food.

The product images were chosen to represent the food related.

The post images were chosen to represent the post related.

### Design Elements

- desktop navigation
- mobile navigation
- footer
- containers/cards
- buttons
- text input
- textarea inputs
- dropdowns
- toasts
- check boxes
- images
- icons
- file pickers

### Animations and Transitions

- There is a 'loading' animation on checkout page while the payment is being processed

### Frameworks

- Bootstrap 5

- Jquery

## Wireframes

### Initial Mobile

### Initial Desktop

## ERD

![ERD](static/images/readme/#)

## Agile Process

### Github User Stories

### Kanban Board



## Testing

### Validation Testing

* Lighthouse

    - Before mobile:

    ![Lighthouse before mobile](static/images/readme/tests/mobile-report.PNG)

    ![Lighthouse before mobile accessibility](static/images/readme/tests/mobile-accessibilityproblem.PNG)

    ![Lighthouse before mobile seo](static/images/readme/tests/mobile-seoproblem.PNG)

    - After mobile:

    ![Lighthouse after mobile](static/images/readme/tests/mobile-reportfixed.PNG)

    - Before desktop:

    ![Lighthouse before desktop](static/images/readme/tests/desktop-report.PNG)

    ![Lighthouse before desktop accessibility](static/images/readme/tests/desktop-accessibilityproblem.PNG)

    ![Lighthouse before desktop seo](static/images/readme/tests/desktop-seoproblem.PNG)

    - After desktop:

    ![Lighthouse after desktop](static/images/readme/tests/desktop-reportfixed.PNG)

* HTML Validation

    - Before:

    ![HTML Validation before](static/images/readme/tests/html-check.PNG)

    - After:

    ![HTML Validation after](static/images/readme/tests/html-checkfixed.PNG)

* CSS Validation

    - Before:

    ![CSS Validation before](static/images/readme/tests/css-check.PNG)

    - After:

    ![CSS Validation after](static/images/readme/tests/css-checkfixed.PNG)

* JS Validation

    ![JS Validation ](static/images/readme/tests/js-check.PNG)
    
    - This function is beeing used just on the html file, that's the reason I couldn't fix this erros.

* PEP 8
        
    - No errors found. Files tested website.form.py, website.models.py, website.views.py, website.urls.py, and milestone04.urls.py.

### Manual Testing

[Manual Test Worksheet](https://docs.google.com/spreadsheets/d/1bAlIK_KV-b2nTUmMAlzxKgcm_HXzy-OZRs0tYtHcEks/edit?usp=sharing)

### Bugs

* No bugs reported

### Unifxed Bugs

* No bugs remaining

## Agile

### User Stories

[Created Epic And User Stories](https://github.com/arthurmezaonik/new_portfolio_project_04/issues)

### Kanban Board

[Kanban Board](https://github.com/arthurmezaonik/new_portfolio_project_04/projects/1)

## Deployment

This application will be deployed via [Heroku](https://heroku.com)

### Creating App.

1. Ensure all code is correct and ready for deployment.

2. Enter the following code to import the required dependencies to the requirements.txt file:
    > pip3 freeze > requirements.txt

    - Heroku will use this file to import the dependencies that are required.

3. Log into or sign up to Heroku(it's free).

    - If signing up, you will need to wait and accept an authentication email.

4. Navigate to Dashboard. 

5. Click "New" and select "create new app" from the drop-down menu. This is found in the upper right portion of the window.

6. Provide a name for your application, this needs to be unique, and select your region.

7. Click "Create App".

### Setting up database

1. Navigate to "Resources" and click on the field "add-ons".

2. Add Heroku Postgres to the project.

### Setting up Heroku App

1.	Navigate to "Settings" and scroll down to "config vars".

    - That’s where you would store sensitive data that needs to kept secret. On my case my file SECRET_KEY, DATABASE_URL, CLOUDINARY_URL.

2. Click "Reveal Config Var", in the field key I entered the CREDS word and in the value field I copied the content as past there.

### App Deployment

1. Navigate to the "Deploy" section.

2. Scroll down to "Deployment Method" and select "GitHub".

3. Authorize the connection of Heroku to GitHub.

4. Search for your GitHub repository name, and select the correct repository.

5. For Deployment there are two options, Automatic Deployments or Manual.

    - Automatic Deployment: This will prompt Heroku to re-build your app each time you push your code to GitHub.

    - Manual Deployment: This will only prompt Heroku to build your app when you manually tell it to do so.

6. Ensure the correct branch is selected "master/Main", and select the deployment method that you desire. In this case, I will be using Automatic Deployment

## Credits

### Acknowledgments

* Code Institute: I think therefore I blog Project

* Youtube channel Codemy

    - Used Django lesson videos

* Malia Havlicek: Reviewing and giving suggestions how to improve my project.

### Media

* Plumber Image: https://www.independent.co.uk/life-style/plumber-invoice-elderly-burnley-uk-james-anderson-free-depher-a9109146.html

* Electrician Image: https://www.tws.edu/blog/skilled-trades/is-becoming-an-electrician-a-good-career-choice/

* Small Repairs Image: https://fixer.com/basic-tools-homeowners-should-have-for-small-repairs/

* Flooring Image: https://www.popularmechanics.com/home/interior-projects/how-to/a9384/8-tips-for-laying-a-plastic-laminate-floor-15903907/

* Painting Image: https://www.2dodone.com/blog/ins-outs-proper-painting-job/

* Cleaner Image: https://theconversation.com/whats-the-school-cleaners-name-how-kids-not-just-cleaners-are-paying-the-price-of-outsourcing-115443

* Other Services Image: https://www.bestinsingapore.co/best-handyman-singapore/

* Publish Image: https://www.istockphoto.com/pt/vetorial/multitasking-construction-worker-gm977762380-265820198

* Find Image: https://www.istockphoto.com/vector/laptop-and-hands-on-the-keyboard-gm926105800-254122512