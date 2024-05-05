![alt text](static/oenotrus-logo-small.png)

# Oenotrus Online Wine Store

## Table of Contents

1. **Introduction**
2. **Structure**
3. **Design**
4. **Limitations**
5. **Features**
6. **Technologies**
7. **Development Lifecycle**
8. **Testing**
9. **Deployment**
10. **Usage**
11. **Collaboration**
12. **Acknowledgments**
13. **Further Development**
14. **Final Notes**

### Introduction

Oenotrus is a full stack web application designed for the Unit 4 project in the Code Institute Gateway Qualifications Level 5 Diploma in Web Application Development course. It provides the user (browsers, shoppers and wine enthusiasts) with a fully functional online store presenting a small range of handpicked wines covering some of the most popular categories in the market.

As a B2C e-commerce platform Oenotrus provides the framework for business users to present, market and sell their stock of wines direct to consumers, who are able to browse, select and purchase the available wines online in an aesthetically pleasing, responsive and fully functional website across all common devices and browsers.

The live website can be found here <https://oenotrus-b46392d15346.herokuapp.com/>

### Structure

##### Architecture

Gym Logger is built with HTML5, custom CSS, JavaScript and Python in the Django full-stack framework to create a responsive and interactive full-stack web application which also contains back-end functionality that allows users to create, store and manipulate relevant data records.

![alt text](static/oenotrus-mockup.png)

##### User Experience Design

For first time users I want the site to be easily navigable and the products easily browsable, laid out in a clear, concise and yet attractive way combining sufficient information and CTAs to satisfy the business user's desire to sell and the customer's desire to make an informed purchase.

For first time users I want to offer simple functionality to create an account and store their information including order history, default delivery details and wishlisted products. This will facilitate new purchases for the business user

For returning customers I want them to quickly be able to access their wishlisted wines and order history. This will help provide the business user with repeat orders.
For returning customers I want them to be able to review their purchases in such a way as to provide extra incentive for new customers to browse the site and place their first orders.

###### UX Design Principles

![alt text](static/oenotrus-ux-principles.png)

###### User Stories

![alt text](static/oenotrus-user-stories.png)

##### Navigation

The full stack application consists of a landing homepage with a hero background image with top navigation, a footer, and a simple and clear call to action taking the user to the full wine list. The navigation dropdown allows the user to view all wines, but also to browse by specific category, and also to navigate to specials based on extra criteria.

The main wines page is sortable and allows the user to filter by relevant criteria, or perform a specific search. Product images along with key information is displayed and each product contains a link to a full detail page for the wine in question.

From their users can add to cart if they are customers or shoppers, or if they are admin users they can edit/delete products from this detail page. The cart page contains the product image, main product details, price, line subtotal and full total. The checkout page consists of a submittable form with Stripe integration.

There is also a profile page where registered customers can view their order history. Additional functionality is provided where registered users can see a wishlist of wines they would like to purchase, and leave reviews for wines they have already bought and tasted.

Pages extend the base template for consistency.

### Design

##### Colour Scheme

Over a white background Gold #e3c69f is the main accent colour, supported by a Maroon #741515 . Colours from Bootstrap classes are also used for user confirmations and notifications.

##### Typography

For clarity the main font used is Montserrat.

##### Imagery

The Oenotrus logo is deployed in the header of all pages for consistency and brand visibility and is responsive for different screensizes.

##### Wireframes

###### Homepage/Landing Page

![alt text](static/oenotrus-landing-page.png)

###### Products Page

![alt text](static/oenotrus-products-page.png)

###### Products Detail Page

![alt text](static/oenotrus-product-details-page.png)

###### User Profile Page

![alt text](static/oenotrus-user-profile-page.png)

###### Shopping Cart Page

![alt text](static/oenotrus-cart-page.png)

###### Checkout Page

![alt text](static/oenotrus-checkout-page.png)

### Limitations

Stripe currently the only linked API

### Features

- Responsive main navigation bar
- Filter product functions and search bar
- Dropdown for new and registered users
- Register and login functions
- Linked database
- Full add to cart and checkout functionality
- Wishlist and review functionality
- User confirmations
- Further information pages

### Technologies

- **HTML** This project uses HTML as the main language used to complete the structure of the website.
- **CSS** This project uses custom written CSS to style the Website.
- **JavaScript/JQuery** This project uses custom written JavaScript to add interactive elements to the website and allow the user to achieve their goals.
- **Bootstrap** The Bootstrap framework is used throughout this website for layouts and styling. This has also been used to import JavaScript/JQuery where necessary.
- **Python** This project uses Python to communicate with the database allowing the recording and manipulation of user data.
- **Django**
- **ElephantSQL** - Postgres Database created with MongoDB
- **Font Awesome** Font awesome Icons are used in the Body of the site and for the Social media links contained in the Footer section of the website.
- **Google Fonts** Google fonts are used throughout the project to import the fonts.
- **Gitpod** The IDE used throughout development
- **GitHub** GithHub is the hosting site used to store the source code for the Website.
- **Heroku** Deploys the live version of the application.
- **Google Chrome Developer Tools** Google Chrome's built in developer tools are used to inspect page elements and help debug issues with the site layout and test different CSS styles.
- **Balsamiq Wireframes** This was used to create wireframes for 'The Skeleton Plane' stage of UX design.
- **Lucid Chart** Chart was used to create the diagrams for Use Case scenarios, UX Design Principles, and Project Lifecycle planning.

### Development Lifecycle

![alt text](static/oenotrus-development-lifecycle.png)

#### Iteration 1
- Inception: the shopping user is considering to purchase wines online. The business user is a wine shop owner looking for a new sales channel.
- Task: the developer/programmer creates a base template from which to extend the relevant framework demonstrating the layour and functionality of the site.
- Increment: the developer creates a HTML framework within Django, setting up Allauth framewrork and a home app along with responsive nav bar header.

#### Iteration 2
- Inception: the shopping user would like to browse available wines, search for something specific, or peruse based on category. The business user has provided a set of products potentially meeting this demand.
- Task: to meet this need the developer/programmer creates a framework to show these products and their appeal, as well as begin the ordering flow.
- Increment: the developer/programmer creates the product app to show the full list and detail of available wines, along with search and filter functions and an add to cart app.

#### Iteration 3
- Inception: the shopping user would like to complete their purchase of selected wines.
- Task: to meet this need the developer/programmer creates the checkout function along with stripe integration, and the user profile to store delivery information and order history
- Increment: cart and checkout apps created with verification and user confirmation, then the propfile app. Product admin functionality created for the business user.

#### Iteration 4
- Inception: the shopping user has completed their purchase and would like to continue viewing the site, adding their thoughts and plans for future orders.
- Task: to meet this need the developmer/programmer creates further functionality for user feedback and ongoing usage.
- Increment: wishlist and review functionality created. Heroku deployment prepared. Testing and bug fixes finalised. Heroku final deployment.

#### Initial Data Model

![alt text](static/oenotrus-initial-data-model.png)

### Testing

#### Strategy

The project depends upon the ability to store and manipulate information provided by each user. Testing is therefore firstly designed to ensure that all input elements function correctly, are validated, and stored in a usable format. These inputs need to be contained in a framework meeting responsivity and accessibility guidelines, so procedures to ensure this will also be implemented. Users will need to see all of their information in one place so testing procedures to ensure all actions are confirmed and then displayed on the profile page will also be devised.

All elements should remain on the screen at sizes above 300px. All internal nav links should direct to the correct pages. All external links should open in a new window. All form inputs should be validated on submission. Form results should vary depending on user submitted information.

All testing conducted on live deployed pages.

#### Initial Bugs (pre-deployment)

- On product detail pages the increase item quantity button would only increase the quantity in the cart but not in the box on the product page. Solved with function handleEnableDisable.
- Subtotal not correctly showing in cart page initially, solved by adding a missing trailing slash in JS
- Initially the background image shown on the homepage would show on all other pages. Solved by using blan overlays with CSS class.
- A horizontal line positioning bug on the all product page was identified and solved through css - margin auto and important tag.


#### Manual Testing

![alt text](static/oenotrus-manual-testing.png)

#### Testing Videos

https://github.com/HawesJM/oenotrus/tree/main/static/videos

##### Nu Html Checker

![alt text](static/index-page-html-checked.png)
![alt text](static/all-wines-page-html-checked.png)
![alt text](static/wine-detail-html-checked.png)
![alt text](static/cart-page-html-checked.png)
![alt text](static/checkout-page-html-checked.png)
![alt text](static/product-management-html-checked.png)

##### W3C CSS Validation

![alt text](static/oenotrus-css-validation.png)

##### Lighthouse Checking

![alt text](static/oenotrus-lighthouse-checking.png)

##### WAVE Accessibility Checking

![alt text](static/oenotrus-pep8-compliance.png)

##### JSHint Checking

![alt text](static/oenotrus-jshint-no-errors.png)

##### PEP8 Compliance Checking

![alt text](static/oenotrus-pep8-compliance.png)

### Deployment

##### Local Deployment

- navigate to the Oenotrus repository - https://github.com/HawesJM/oenotrus.git 
- click on the "Code" button, located just above the file list
-in the dropdown menu, click on the clipboard icon to copy the repository's URL
- open the terminal in your code editor and navigate to the directory where you want to clone the repository
- run the following command:
- git clone https://github.com/HawesJM/oenotrus.git
- install packages from the requirements.txt file using this command: pip3 install -r requirements.txt
- create a .env file for your own credentials
- to launch the Django app, run command: python3 manage.py runserver
- to stop the app: CTRL+C
- make migrations to set up the database:
python3 manage.py makemigrations
python3 manage.py migrate
-create superuser to access the Django Admin Panel:
python3 manage.py createsuperuser

##### Elephant SQL Database

- go to the ElephantSQL website
- sign-up with your GitHub account
- click Create new instance
- enter a name and choose plan 
- select the region and data center closest to you
- once created, click on the new database name to view the database URL
- use the database URL as a credential in your .env file

##### AWS

 - login or create an account
 - set up S3 Bucket
 - set up IAM User Group and User
 - connect Django to the bucket

##### Heroku Deployment

- login or create a new Heroku account
- selected to create a new app
- choose name and region
- set relevant config vars
- ensure procfile is added and sensitive information is hidden
- deploy from main branch

### Usage

The live deployed app is publicly available at https://oenotrus-b46392d15346.herokuapp.com/ for users to access freely and navigate accordingly. Free registration is necessary to browse the full site and access full functionality.

### Acknowledgments

I'd like to thank my Code Institute assigned mentor Daisy McGirr for her support and input.


### Further Development

- Subscribe to new products
- Repeat order function
- Forgot password feature
- Shipping information
- Special offers and new arrivals