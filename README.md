## Here is what I still need to work on, as of 3rd of April: 

- Add content
- Do Testing
- Finish README 


[Link to Deployed Website](https://fullstackframeworks-project.herokuapp.com)

# Code Institute Milestone Project 
## Full Stack Frameworks with Django 

> Be good to your skin. You'll wear it every day for the rest of your life. 

[![Build Status](https://travis-ci.com/MelBiggs/fullstack-frameworks-project.svg?branch=master)](https://travis-ci.com/MelBiggs/fullstack-frameworks-project)

Welcome to FaceValue. 

This a fictional e-commerce site selling skin products from all over the world, for all skin types and issues. 

Users can log in and find products according to type (e.g. moisturiser, eye cream) or category (e.g. face or body products). Customers can then review the products they buy. Users can read the blog to learn more about particular skin issues, and what we have found works the best. 

## Demo


## UX

This project is part of my studies in Full Stack Software Development with the Code Institute. This is my final project for this course, for the module **Full Stack Frameworks**.

The objective given for this project was *"Bring your own idea(s) to life, based on providing value to users to address a specific real or imagined need."* I wanted to incorporate elements of the other project ideas that were given by Code Institute. For example, one of the ideas was to build an auction place to sell historical artifacts, where users can find, learn about and acquire artifacts they are interested in. The site owner will earn money selling items.

I wanted to build a website that I myself would be interested in visiting. My idea was to create a website selling skin care products and to create a community to help people with their skin issues by finding out what worked for others. I wanted to create a place where users can go and see their particular skin issue discussed and they can find products relating to that issue. I wanted to include a blog where they can find more information on a variety of skin issues. 

I looked at the other project ideas given by the Code Institute and worked them into my idea: 

**Potential features to include:**
* Create an online store focused on selling various reliable skin products

* Allow users to search items based on various fields, e.g. product type (moisturiser, toner, nightcream, daycream)

* Allow users to filter items based on skin issue and currency

* Allow users to see the price, image and other basic details about the product on the search page

* When in the specific item, users would be able to learn about the product, the company, it's ingredients and the sites opinions on it, for example, what skin problems this tackled well*.

* Users have to be registered for this to purchase this. 

* Allow registered users to write reviews about the products, only if they purchased them.

* Include pagination and/or other dynamic display actions.


### User Stories

This site is intended for use by anyone who has an interest in skincare or has a particular issue they want to find products to relieve. They can find these products which can be filtered and purchase them online. The target audience is broad as skin issues don't chose an age or gender. Anyone who has an interest in purchasing a product or reading a blog to aid them in their skin care journey will find interest in this website. 

**_"As a user I would like to"_**

* view all products and blog posts without logging in 
* view the site from any device (mobile, tablet, desktop)
* leave a review for products I liked
* be able to register and log in/out
* be able to change my password 
* filter products based on a particular skin issue
* find products for my face or my body 
* search through all products and blogposts 
* find products of a particular type e.g. moisturisers
* comment on blog posts 
* upvote products I have enjoyed 
* see how many views a blogpost has 
* to be able to buy products I found worked
* do all the above on an easily navigated and attractive website 
* have a shopping cart I can easily add and remove items from
* filter blog posts by age


### Design

I wanted to style the website with a clean, semi-clinical look. 

#### Colour Scheme

| Colour Code   | Description   | 
| ------------- |:-------------:| 
| #6c757d       | deep blueish grey|
| #fff7ff       | pale pink     | 


![Colour Palette](static/img/colour-palette.png)

#### Typography

I used [Poppins](https://fonts.google.com/specimen/Poppins) as my navigation bar font and [Roboto](https://fonts.google.com/specimen/Roboto) as the font for the project body.  

#### Frameworks

* [Bootstrap](https://getbootstrap.com/) - 
Having used Materialize for my last project, I was happy to make a return to Bootstrap as I find it to be a great framework and easy to use.

* [JQuery](https://jquery.com/) - 
The project uses JQuery to simplify DOM manipulation.

* [Django](https://www.djangoproject.com/) - 
Django is a free and open-source web framework that I've used to render the back-end Python with the front-end Bootstrap.

#### Icons

I used [Font Awesome](https://fontawesome.com/icons?d=gallery) for the icons in my project

### Wireframes
 
[Here is a link to my wireframes](UXD)

## Features

**_"A user can.."_**

- register and set up an account with FaceValue.
- reset their password from the login page. 
- view all products from the _SkinCare_ dropdown. They can also view by whether it's a Face or Body product.
- view all blog posts from the _SkinCare_ dropdown. 
- view individual products and blog posts. 
- select the specific product type they want (e.g. moisturiser, cleanser) from the _What are you looking for?_ dropdown.
- comment on a specific blog post.
- review a specific product and leave a star rating. 
- see the average star rating for a specific product in the detail page. 
- approve comments and reviews and edit blog posts if they are the admin superuser.
- pay for products through Stripe (as this is a fictional site, it only processes test card payments.)
- use pagination to move through the products and blog posts. 
- search for a product or blog by name 
- save products for later, which get displayed on their profile page. 

### Features left to implement

I would like to add the following features in time: 
* Calculating the shipping and handling fees into the total value
* Expand the currency used to include GBP and USD
* Add a Previously Purchased section to the user profile page  
* Sending an email with the order confirmation to the user when payment is processed. 
* Build staff-friendly pages which display all the needed information for smooth shipping. 

## Technologies Used

* [Gitpod](https://www.gitpod.io/) -  Gitpod is the code editor I used
* [Github](https://github.com/) - Github was used as remote storage
* [FontAwesome](https://fontawesome.com/) - Font Awesome is a great library of icons. I used this library for any icons.
* [Google Fonts](https://fonts.google.com/) - There is a great selection of fonts in the Google Fonts library, some of which I used in my project.

### Frontend Technologies

* [HTML](https://en.wikipedia.org/wiki/HTML) - HTML was used to control the layout and the structure of the project.
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - Cascading Style Sheets are used to describe the appearance of a website and I used it to make my website look appealing to the user.
* [JQuery](https://jquery.com/) - jQuery is the primary JavaScript functionality.
* [Bootstrap](https://getbootstrap.com/) - This is the front-end framework for layout and design.
* [Amazon AWS](https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Fconsole.aws.amazon.com%2Fconsole%2Fhome%3Fstate%3DhashArgs%2523%26isauthcode%3Dtrue&client_id=arn%3Aaws%3Aiam%3A%3A015428540659%3Auser%2Fhomepage&forceMobileApp=0#) - I stored my staticfiles and media in AWS 

### Backend Technologies

* [Python]( https://www.python.org/) - This is the back-end programming language.
* [Heroku]( https://heroku.com/) - The app is hosted on Heroku.
* [Django](https://www.djangoproject.com/) - Django is a Python web framework I used.
* [Django](https://www.postgresql.org/) - Through Heroku, this is a relational SQL database plugin.

Further details on all Python packages used on this project can be found in the [requirements.txt](requirements.txt) file. 

### General Technologies

* [Stripe](https://stripe.com/ie) - Stripe allows the user to make secure payments.

### Also

[Gifox](https://gifox.io/) - I used Gifox to record the website demo for my README file. I recorded it off the website [Am I Responsive](http://ami.responsivedesign.is/?url=https%3A%2F%2Fmelbiggs.github.io%2Fifd-milestoneproject%2F#)


## Testing

### Validators

#### HTML

[W3C Markup Validation Service]( https://validator.w3.org/)

The HTML for *accounts*, *blog*, *cart*, *checkout*, *home*, *products* and *base.html* all came back fine, although it did not like that I didn't have a DOCTYPE for each HTML page. 

#### CSS

[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

#### JavaScript

[JSHint]( https://jshint.com/)

#### Python

[PEP8]( http://pep8online.com/)

A few files contained lines which were too long so once these were adjusted, they passed the validator without issue. 

* *Accounts App* - `backends.py`, `forms.py`, `url_reset.py`, `urls.py` and `views.py` came back with 'All right'. 

* *Blog App* - `forms.py`, `models.py`, `urls.py` and `views.py` came back with 'All right'. 

* *Cart App* - `contexts.py`, `models.py`, `urls.py` and `views.py` came back with 'All right'. 

* *Checkout App* - `forms.py`, `models.py`, `urls.py` and `views.py` came back with 'All right'. 

* *Home App* - `views.py` came back with 'All right'.

* *Products App* -  `admin.py`, `forms.py`, `models.py`, `urls.py` and `views.py` came back with 'All right'. 

* *Search Apps* - `urls.py` and `views.py` came back with 'All right'. 

I also checked `custom_storages.py` and that also came back with an 'All right'. 


### Issues/Bugs


### Automated Testing

All automated testing was done using [Travis-CI](https://travis-ci.com/). Travis was used throughout the unit testing of this project to provide continuous integration with the deployed site. The Travis Documentation provides all the info needed to set it up.

Django's built-in unittest library module and TestCase subclass 

#### User Story Testing

Having gone through all the user stories above and looked at my website with those in mind, I believe the site meets those needs. My friends and family were kind enough to also test the site for me on their own devices and were able to move through it with ease.

#### Compatibility

To ensure a broad range of users can successfully use the site, I tested it across major browsers in both desktop and mobile configuration.

I tested the responsiveness of the site, page by page. All pages were made to look at attractive as possible on all screen sizes. For example, the checkout and cart have a scrolling table for smaller screens.


## Deployment

This project can be viewed on [Heroku](https://fullstackframeworks-project.herokuapp.com)

### Local Deployment

To run this programme locally on your own machine, you'll need the following: 
- An IDE (like [Gitpod](https://www.gitpod.io/))
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [GIT](https://www.atlassian.com/git/tutorials/install-git)
- [Python3](https://www.python.org/downloads/)

Then: 

1. Clone this GitHub repository by either clicking the green "Clone or download" button above in order to download the project as a zip-file (unzip it first), or by entering the following command into the Git CLI terminal:
    - `git clone https://github.com/MelBiggs/fullstack-frameworks-project.git`
2. Open your preferred IDE then open a terminal session in the unzip folder or cd to the correct location.
3. Create a `.env` file with your own credentials.
4. If needed, Upgrade pip locally with:
    - `pip3 install --upgrade pip`
5. Install all requirements from the requirements.txt file using this command:
    - `pip3 -r requirements.txt`
6. In the IDE terminal, use the following command to launch the Django project:
    - `python3 manage.py runserver`
7. Make migrations to create the database schema:
    - `python3 manage.py makemigrations`
    - `python3 manage.py migrate`
8. Generate a superuser to access the Django Admin Panel and then assign an admin username, email, and secure password:
    - `python3 manage.py createsuperuser`
9. Once the program is running, go to the local link provided and add /admin to the end of the url. Here log in with your superuser account and create instances within the new database.


### Remote Deployment

Once you do the steps above, you can then deploy the site remotely on Heroku with the following steps:

1. Create a `requirements.txt` file using the terminal command `pip3 freeze > requirements.txt`.
2. Create a Procfile to tell Heroku what type of application is being deployed using gunicorn, and how to run it:
    - `echo web: gunicorn facevalue.wsgi:application > Procfile`
3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.
4. Create a new app on the Heroku website by clicking the "New" button. Give it a name and set the region to whichever is applicable for your location.
5. In the Heroku Resources tab, navigate to the *Add-Ons* section and search for *Heroku Postgres*. Make sure to select the free *Hobby* level. This will allow you to have a remote database instead of using the local sqlite3 database, and can be found in the *Settings* tab. You'll need to update your `.env` file with your new database-url details.
6. From the heroku dashboard of your application, click on *Deploy* and then *Deployment method* and select GitHub.
7. Link Heroku to the correct GitHub repository.
8. Click on *Settings* and *Reveal Config Vars*.
9. Set your config vars, as below: 

| Key       | Value        | 
| ------------- |:-------------:| 
| AWS_ACCESS_KEY_ID    | `<your key>`|
| AWS_SECRET_ACCESS_KEY    | `<your key>`|  
| DATABASE_URL| `<your key>` |
| DISABLE_COLLECTSTATIC| 1|
| SECRET_KEY| `<your key>`|
| STRIPE_PUBLISHABLE| `<your key>`|
| STRIPE_SECRET| `<your key>` |

10. Back in your IDE, you'll have to connect to your new database, migrate your models and create a new superuser. 
11. On your Heroku dashboard, click *Deploy*. Scroll down to *Manual Deploy*, select the master branch then click *Deploy Branch*.
12. Once built, you can view app. 


## Credits 

### Media

The favicon is used is from [Favicon.io](https://favicon.io/)

The index page carousel images were found at [Goop](https://goop.com/wp-content/uploads/2011/04/Update-Natural-and-Organic-Skin-CareSEO-AP1104952.jpg) and [Pinterest](https://www.pinterest.co.uk/pin/717972365568820262/) and edited by myself. 

All images for the products were found on their brand's websites. 

### Code

* When I was working out how to get tag filtering working (i.e. filtering by skin issue), these sources really helped me:
    - https://stackoverflow.com/questions/4915920/how-to-delete-an-item-in-a-list-if-it-exists - This helped me remove 'page' from filter_keys
    - https://stackoverflow.com/questions/24763045/capture-all-url-parameters-in-django-views-py - This helped me in getting all the GET parameters
    - https://stackoverflow.com/questions/16819222/how-to-return-dictionary-keys-as-a-list-in-python - This taught me how to get keys using `[*]`

* These code snippets helped me find the URL query parameters with JavaScript so that the pagination worked with filters and to make the checkbox stay selected :
    - https://medium.com/@junaidahmed/get-url-query-params-with-jquery-js-c12f5fed0f71
    - https://stackoverflow.com/questions/10930048/get-checkbox-with-specific-value
    - https://stackoverflow.com/questions/4735342/jquery-to-loop-through-elements-with-the-same-class

* These websites helped me flesh out my password reset view and to add a subject line:
    - https://github.com/django/django/blob/master/django/contrib/auth/templates/registration/password_reset_subject.txt 
    - https://simpleisbetterthancomplex.com/tutorial/2016/09/19/how-to-create-password-reset-view.html 

* This question on Stack Overflow helped me to target a URL for my All, Face and Body Products tab:
    - https://stackoverflow.com/questions/34649131/javascript-how-to-check-if-url-contains-a-word/34649157

* This code showed me how to add stars ratings as part of reviews and to the review form: 
    - https://github.com/nashio/star-rating-svg/
    - https://stackoverflow.com/questions/28607727/how-to-calculate-average-with-django
    - https://stackoverflow.com/questions/6862250/change-a-django-form-field-to-a-hidden-field

* This code helped me to disable the Add button on my product page: 
    - https://blog.revillweb.com/jquery-disable-button-disabling-and-enabling-buttons-with-jquery-5e3ffe669ece

* For my cart, I found this template really useful: 
    - https://jsfiddle.net/bootstrapious/wc6g251x

* For the blog layout, parts of this template were helpful: 
    - https://colorlib.com/preview/theme/miniblog/

* When I was starting on the pagination, this video had some really comprehensive help: 
    - https://www.youtube.com/watch?v=Z8MDdDyB_6A 

I also received tips on snippets of my code through [Stack Overflow](https://stackoverflow.com/), [CodePen]( https://codepen.io/) and [W3Schools](https://www.w3schools.com/).

### Acknowledgements

I received inspiration for the theme of this project from websites like [Cult Beauty](https://www.cultbeauty.co.uk/) and [Glossier](https://www.glossier.com/).

I am very grateful to my mentor **Guido Cecilio** for his help and guidance throughout the project. I would also like to thank my mam and my friends for helping me test the responsiveness of the website. I would also like to thank the Code Institute tutors for their helpful comments and advise on my project. 

[Link to Deployed Website](https://fullstackframeworks-project.herokuapp.com/)
