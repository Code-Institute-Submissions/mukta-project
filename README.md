# Mukta - Yoga and Wellbeing

## Introduction

This is Mukta - Yoga and Wellbeing. An e-commerce website developed by Mariana Stefani. This website is for everyone who is after great quality wellbeing and yoga products.
Here the user can also check out the yoga and wellbeing workshops that are taking place in the city of London.

## UX (User Experience)

### Project Goals

The purpose of this project is to offer the best quality yoga and wellbeing products.
Users will have the possibility to register on the website, choose products in the store, add to the shopping cart and make the payment. Once registered, the user can also check which wellbeing and yoga events are taking place in the city of London and can leave reviews regarding their past purchases, the website as well as workshops they have attended.

#### **User Goals:**

- Browse yoga and wellbeing products at a good price.
- Choose what yoga and wellbeing products I'd like to buy, add them to the shopping cart and pay.
- Find yoga and wellbeing classes or workshops that are happening in the city of London.
- Be able to write, edit and delete a review about my experience with my purchase/ website navigation/ workshops I have attended.

#### **User Stories:**

- As a user, I expect to browse what products the website offers.
- As a user, I expect to find the product I'm looking for, add it to the shopping bag and pay for it. All with intuitive navigation.
- As a user, I expect to be able to register to the website so it will keep my details for future purchases as well as be able to check my previous purchases.
- As a user, I expect to be able to leave a review regarding the product I have purchased or about the website or about a workshop I had been to. Also, I want to be able to edit or delete this review.
- As a user, I expect to find the best workshops and events about yoga or wellbeing happening in London.

#### **Site Owner Goals:**

As an admin user:

- I expect to be able to log in as a superuser and create, update and delete workshops and events on the website.
- I expect to provide users with a safe and secure e-commerce platform.
- I expect to encourage users to register on the site, so they will have access to the best yoga and wellbeing workshops taking place in London.
- I need to be able to attract attention to my products.

## User Requirements and Expectations:

**Requirements:**

- Navigate through the pages of the website intuitively.
- The content displayed in a visually appealing manner.
- Navigate the website on any device.
- Add products to the shopping cart and update the basket amounts.
- Buy items in the shopping cart in a safely and securely.
- View past orders and user details on my profile section.

**Expectations:**

- Navigation takes the user directly to the desired page of the website.
- The users' payment data will not be kept in the website's database.
- The website will guarantee the safe storage of user details.
- The website will have intuitive navigation.
- The website will have a responsive design.
- Content is well presented and visually satisfying.

## Wireframes

The wireframes for this project were created at [Moqups](https://moqups.com/).
View my wireframes [here](#).

## Features

### Existing Features

- Users can create an account, log in, view past orders and have access to the workshops page.
- A 'my profile' section where users can see previous purchases and update their details.
- Users can create, update or delete a review when logged in.
- A 'reviews' page where users can read other users reviews.
- A 'my reviews' page where users can create, edit, delete a review as well as read their past reviews.
- A search bar that displays the website products based on the users' search query.
- A products page where users can click on the item and will be directed to the product details page.
- A shopping cart where users can add the products they would like to purchase and update their quantities.
- A 'checkout' page where users can pay for their chosen items using the Stripe API which will process the payment details and place their order.

### Features Left to implement

- Add more products.
- Create a 'contact us' form.
- Users can register with their social media accounts.
- A reset password link.

## Information Architecture

### Database Choice:

- During development of this project I worked with the standard **sqlite3** database that comes installed with Django.
- In the production version of Mukta - Yoga and Wellbeing, the database is a **PostgreSQL** database, hosted and provided by **Heroku**.

### Mukta Yoga and Wellbeing Data Models:

The user model used in this project is provided by Django. You can find more informtaion about this [here](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/)

#### The Order Model

| _Title_          | _Key in DB_     | _Form Validation type_                                                               | _Data type_   |
| ---------------- | --------------- | ------------------------------------------------------------------------------------ | ------------- |
| Order Number     | order_number    | max_length=32, null=False, editable=False                                            | CharField     |
| User Profile     | user_profile    | UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders' | ForeignKey    |
| Full Name        | full_name       | max_length=50, null=False, blank=False                                               | CharField     |
| Email            | email           | max_length=254, null=False, blank=False                                              | EmailField    |
| Phone Number     | phone_number    | max_length=20, null=False, blank=False                                               | CharField     |
| Country          | country         | blank_label='Country \*', null=False, blank=False                                    | CountryField  |
| Post Code        | postcode        | max_length=20, null=True, blank=True                                                 | CharField     |
| Town or City     | town_or_city    | max_length=40, null=False, blank=False                                               | CharField     |
| Street Address 1 | street_address1 | max_length=80, null=False, blank=False                                               | CharField     |
| Street Address 2 | street_address2 | max_length=80, null=True, blank=True                                                 | CharField     |
| County           | county          | max_length=80, null=True, blank=True                                                 | CharField     |
| Date             | date            | auto_now_add=True                                                                    | DateTimeField |
| Delivery Cost    | delivery_cost   | max_digits=6, decimal_places=2, null=False, default=0                                | DecimalField  |
| Order Total      | order_total     | max_digits=10, decimal_places=2, null=False, default=0                               | DecimalField  |
| Grand Total      | grand_total     | max_digits=10, decimal_places=2, null=False, default=0                               | DecimalField  |
| Original Bag     | original_bag    | null=False, blank=False, default=''                                                  | TextField     |
| Stripe PID       | stripe_pid      | max_length=254, null=False, blank=False, default=''                                  | CharField     |

#### The OrderLineItem Model

| _Title_         | _Key in DB_    | _Form Validation type_                                                             | _Data Type_  |
| --------------- | -------------- | ---------------------------------------------------------------------------------- | ------------ |
| Order           | order          | Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems' | ForeignKey   |
| Product         | product        | Product, null=False, blank=False, on_delete=models.CASCADE                         | ForeignKey   |
| Product Colour  | product_colour | max_length=2, null=True, blank=True                                                | CharField    |
| Quantity        | quantity       | null=False, blank=False, default=0                                                 | IntegerField |
| Line Item Total | lineitem_total | max_digits=6, decimal_places=2, null=False, blank=False, editable=False            | DecimalField |

#### The Category Model

| _Title_       | _Key in DB_   | _Form Validation type_                | _Data Type_ |
| ------------- | ------------- | ------------------------------------- | ----------- |
| Name          | name          | max_length=254                        | CharField   |
| Friendly Name | friendly_name | max_length=254, null=True, blank=True | CharField   |

#### The Product Model

| _Title_     | _Key in DB_ | _Form Validation type_                                       | _Data Type_  |
| ----------- | ----------- | ------------------------------------------------------------ | ------------ |
| Category    | category    | 'Category', null=True, blank=True, on_delete=models.SET_NULL | ForeignKey   |
| SKU         | sku         | max_length=254, null=True, blank=True                        | CharField    |
| Name        | name        | max_length=254                                               | CharField    |
| Description | description | max_length=254                                               | TextField    |
| Has Option  | has_option  | default=False, null=True, blank=True                         | BooleanField |
| Price       | price       | max_digits=6, decimal_places=2                               | DecimalField |
| Image URL   | image_url   | max_length=1024, null=True, blank=True                       | URLField     |
| Image       | image       | null=True, blank=True                                        | ImageField   |

#### The UserProfile Model

| _Title_                  | _Key in DB_             | _Form Validation type_                       | _Data Type_   |
| ------------------------ | ----------------------- | -------------------------------------------- | ------------- |
| User                     | user                    | User, on_delete=models.CASCADE               | OneToOneField |
| Default Full Name        | default_full_name       | max_length=80, null=True, blank=True         | CharField     |
| Default Phone Number     | default_phone_number    | max_length=20, null=True, blank=True         | CharField     |
| Default Street Address 1 | default_street_address1 | max_length=80, null=True, blank=True         | CharField     |
| Default Street Address 2 | default_street_address2 | max_length=80, null=True, blank=True         | CharField     |
| Default Town or City     | default_town_or_city    | max_length=40, null=True, blank=True         | CharField     |
| Default County           | default_county          | max_length=80, null=True, blank=True         | CharField     |
| Default Post Code        | default_postcode        | max_length=20, null=True, blank=True         | CharField     |
| Default Country          | default_country         | blank_label='Country', null=True, blank=True | CountryField  |

#### The Review Model

| _Title_     | _Key in DB_ | _Form Validation type_         | _Data Type_   |
| ----------- | ----------- | ------------------------------ | ------------- |
| User        | user        | User, on_delete=models.CASCADE | ForeignKey    |
| Title       | title       | max_length=10                  | CharField     |
| Content     | content     | max_length=45                  | TextField     |
| Date Posted | date_posted | default=timezone.now           | DateTimeField |

#### The Workshop Model

| _Title_    | _Key in DB_ | _Form Validation type_                                                                                            | _Data Type_ |
| ---------- | ----------- | ----------------------------------------------------------------------------------------------------------------- | ----------- |
| Title      | title       | max_length=100                                                                                                    | CharField   |
| Date       | date        | "Date (YYYY-MM-DD)\*", auto_now_add=False, auto_now=False, blank=True                                             | DateField   |
| Location   | location    | max_length=100                                                                                                    | CharField   |
| Time       | time        | max_length=10                                                                                                     | CharField   |
| Instructor | instructor  | max_length=100                                                                                                    | CharField   |
| Content    | content     |                                                                                                                   | TextField   |
| Images     | images      | "Image URL\*", max_length=1024, null=True, blank=True                                                             | URLField    |
| Order      | order       | "Add 'order-md-first' or 'order-md-last' accordingly\*", max_length=14, null=True, blank=True                     | CharField   |
| Divider    | divider     | "Add 'workshop-divider' (Unless it\'s the last workshop one on the page)\*", max_length=16, null=True, blank=True | CharField   |

## Technologies Used

The technologies used were:

### Languages

- [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [JSON](https://www.json.org/json-en.html)
- [Python](https://www.python.org/)

### Libraries

- [Bootstrap](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
- [Django](https://www.djangoproject.com/)
- [Font Awesome](https://fontawesome.com/icons)
- [Google Fonts](https://fonts.google.com/)
- [JQuery](https://jquery.com)
- [Psycopg2](https://pypi.org/project/psycopg2/)
- [Stripe](https://stripe.com/gb)

### Tools

- [Git](https://github.com/)
- [Heroku](http://www.heroku.com)
- [Moqups](https://moqups.com/)
- [Visual Studio Code](https://code.visualstudio.com/)

### Databases:

- [PostgreSQL - Production](https://www.postgresql.org/)
- [SQlite3 - Development](https://www.sqlite.org/index.html)

## Testing

- HTML was checked on [HTML Validator](https://validator.w3.org/).
- CSS was checked on [CSS Validator](http://csslint.net/).
- JavaScript was checked on [JS Hint Validator](https://jshint.com/).
- JSON was checked on [JSON Validator](https://jsonlint.com/).
- The responsiveness of this website was tested constantly during the development process. It was tested in real desktops, tablets and mobile devices as well as on Google Chrome developer tools.
- The website was tested on different browsers such as Google Chrome, Safari, Internet Explorer and Mozilla Firefox.
- I asked friends and family members to test the functionalities of the website on desktop and mobile devices. Their feedback was used to improve website usability.

### Tests

**Navbar Links**

- **Plan:** User clicks on each navbar link and is directed to chosen page.
- **Result:** This test passed.

**Registration Page**

- **Plan:** User will fill the registration form and will receive a confirmation e-mail.
- **Result:** This test passed.

**Login Page**

- **Plan:** After clicking on the verification link on the e-mail, the user can login with username or e-mail and password and is directed to the idex page.
- **Result:** This test passed.

**My Profile Page - When User is Logged In**

- **Plan:** If the user have purshased someting in the past, they will have their order gistory and their details displayed.
- **Result:** This test has passed.

**Products Button**

- **Plan:** User clicks the **_“Check our products”_** button and is directed to the products page.
- **Result:** This test has passed.

**Workshop Button - When User is Logged In**

- **Plan:** User clicks the **_“Check our workshops”_** button and is directed to the workshops page.
- **Result:** This test has passed.

**Workshop Button - When User isn't Logged In**

- **Plan:** User clicks the **_“Register here”_** button and is directed to the registration page.
- **Result:** This test has passed.

**Products Page**

- **Plan:** User clicks on a product and is directed to the product detail.
- **Result:** This test has passed.

**Product Detail Page**

- **Plan:** User clicks on the **_“Add to bag”_** button and a message container shows on the top of the page with a bag summary and **_“Go to secure checkout”_** button .
- **Result:** This test has passed.

- **Plan:** User clicks on **_“+”_** or **_“-”_** buttons and the product quantity increment or decrement accordingly.
- **Result:** This test has passed.

**Products Page - For Superuser**

- **Plan:** Superuser clicks on **_"Add New Product"_** button and is redirected to the add product form.
- **Result:** This test have passed.

**Add Product Page - For Superuser**

- **Plan:** Superuser fills the form with relevant information, clicks on **_Post_** and a new product is created.
- **Result:** This test have passed.

**Product Detail Page - For Superuser**

- **Plan 1:** Superuser clicks on **_update_** button and is redirected to the products form with pre-filled information. Superuser changes what is needed and click **_Post_**. Update is saved and superuser is redirected to the products page.
- **Result:** This test have passed.

- **Plan 2:** Superuser clicks on **_delete_** button and is redirected to the delete product page. If clicks the **_Yes, Delete_** button, the product is deleted. If clicks the **_Cancel_** button is redirected to the products page.
- **Result:** This test have passed.

**Checkout Page**

- **Plan:** User fills the form with personal information and use credit card number **_4000058260000005_**, MM/YY as **_04/24_**, CVC as **_744_** and post code as **_SW1A 0AA_** to complete a purshase.
- **Result:** This test has passed.

**Reviews Page - When User isn't Logged In**

- **Plan:** User clicks on **_"Add Review"_** and is redirected to login page.
- **Result:** This test have passed.

**Reviews Page - When User is Logged In**

- **Plan:** User clicks on **_"Add Review"_** and is redirected to the add review form.
- **Result:** This test have passed.

**Workshops Page**

- **Plan:** User clicks on the **_Workshop title_** and is redirected to the workshop detail page.
- **Result:** This test have passed.

**Workshops Page - For Superuser**

- **Plan:** Superuser clicks on **_"Add New Workshop"_** button and is redirected to the add workshop form.
- **Result:** This test have passed.

**Add Workshops Page - Only for Superuser**

- **Plan:** Superuser fills the form with relevant information, clicks on **_Post_** and a new workshop is created.
- **Result:** This test have passed.

**Workshop Detail Page - When User is Superuser**

- **Plan 1:** Superuser clicks on **_update_** button and is redirected to the workshop form with pre-filled information. Superuser changes what is needed and click **_Post_**. Update is saved and superuser is redirected to the workshops page.
- **Result:** This test have passed.

- **Plan 2:** Superuser clicks on **_delete_** button and is redirected to the delete workshop page. If clicks the **_Yes, Delete_** button, the workshops is deleted. If clicks the **_Cancel_** button is redirected to the workshops page.
- **Result:** This test have passed.

## Note for the assessor

To test the CRUDs functionalities as **normal user**:

| **Username** | **Password**     |
| ------------ | ---------------- |
| testuser     | test4321         |

To test the CRUDs functionalities as **superuser**:

| **Username**      | **Password**          |
| ----------------- | --------------------- |
| testsuperuser     | superuser4321         |

To purchase a product, use the information below:

| Card Number      | MM/YY | CVC | Post Code |
|------------------|-------|-----|-----------|
| 4000058260000005 | 04/24 | 744 | SW1A 0AA  |