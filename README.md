# iShop - Welcome to the future!

## 1. Features
### 1.1 The WebPage
A Webpage where Customers can buy all sortes of clothes/shoes in various sizes/colors. There is a search and filter function making it so much easier! There is also a paginator in the bottomw of the page making it so much easier to view our items. The Previous/Next button wont work if there isnt any more products to see. 

Note: The storage unit where we keep our products is rather small so we have a limited amount of products in right now. But in a year or two, our salesmanager "Andy", estimates we will be bigger than Amazon. So better join now before we start demanding a monthly fee for free shipping.

### 1.2 Transactions
All transactions are handled through PayPal in a secure way. Just buy an item and you´ll see! We even make it easier for you the next time you purchase something because your shipment details will be stored! So now you just have to click on the "confirm transaction" button and its done! To make you feel safe and secure we even send you a confirmation mail that the transactions has be done. So be sure to keep and eye on your inbox.
![image](https://github.com/GlennJohansson85/shop/assets/139962883/457fe1f3-fab8-4d7d-9a9b-c8fe34f984c2)

### 1.3 Cart
If you have a low income you can always come back and your items will be stored in your cart. However, if the items you want are popular and we run out of stock thats a "YOU" problem. You wont be able to buy these items anymore (but for the right price...)
What else is there...If you find something you really like you can always increase the number of items you want within your cart. You can even remove items but we dont recommend it.

### 1.4 Register
All of our Customers are welcome to register to our site. We just need your shipping details, a email we can communicate through and a unique password which you want to keep for yourself. If you are like "Andy" though and keep on forgetting stuff you can always reset your password by providing the mail you registered with. In less than a second you´ll be able to create a new on through the mail we sent you. Be sure when creating a new password to remember it because you need to confirm it. Be sure to write the same word in both places otherwise it wont go through.

### 1.5 Dashboard
When registered you will have your very own dashboard. Here you can edit your profile and even upload a picture of yourself to show all your new iShop friends! 
You will be able to see all you orders through "My Orders" and If you wanna dive deeper you can even click on them to get specifics!

## 3. Gallery
This is a big project. Instead of screenshots its better to pay the project a visist instead!


## 4. Testing
### 4.1 Functional Tests
#### 4.1.1 Homepage Load Test
* Objective: Ensure the homepage loads correctly.
* Procedure: Access the homepage URL.
* Expected Result: The homepage loads with all elements (header, main content, footer) displayed correctly.

#### 4.1.2 Category Dropdown Menu Test
* Objective: Verify the category dropdown menu functionality.
* Procedure: Click on the "Categories" button in the header.
* Expected Result: The dropdown menu appear, displaying all categories correctly.

#### 4.1.3 Search Functionality Test
* Objective: Test the search feature.
* Procedure: Enter a keyword in the search bar and click the search icon.
* Expected Result: The search results page load items with containing the keyword in the title and description.

#### 4.1.3 User Authentication Test (Guest)
* Objective: Ensure guest users see the correct options.
* Procedure: Access the website without logging in.
* Expected Result: The header displays "Welcome Guest!" with options to "Login" and "Register".

### 4.1.4 User Authentication Test (Logged In)
* Objective: Verify the header for logged-in users.
* Procedure: Log in with a test user account.
* Expected Result: The header displays "Welcome [User Name]!" with options for "Dashboard" and "Logout".

### 4.1.5 Cart Functionality Test
* Objective: Check the cart icon and count.
* Procedure: Add items to the cart and check the cart icon in the header.
* Expected Result: The cart icon displays with the correct item count in the badge.

### 4.1.6 Mobile View Burger Menu Test
* Objective: Verify the burger menu functionality on mobile devices.
* Procedure: Resize the browser window to mobile dimensions and click the burger menu icon.
* Expected Result: Fail: I´ve used bootstrap very own documentation for this so I assume something custom made is affecting the proper response.

### 4.1.7 Responsive Design Test
* Objective: Ensure the header is responsive.
* Procedure: Test the header across various screen sizes (desktop, tablet, mobile).
* Expected Result: The header adjusts correctly (just the navbar that works wrong), with elements stacking or hiding as appropriate.

### 4.2 Usability Tests
#### 4.2.1 Navigation Usability Test
* Objective: Test the ease of navigation for users.
* Procedure: Have users perform tasks like searching for a product, accessing categories, and checking the cart.
* Expected Result: Users should find it intuitive to navigate the site without assistance.

#### 4.2.2 Form Usability Test
* Objective: Ensure the search and login forms are user-friendly.
* Procedure: Have users perform searches and log in with test accounts.
* Expected Result: Forms are easy to fill out, with clear instructions and feedback.

### 4.3 Performance Tests
#### 4.3.1 Page Load Speed Test
* Objective: Ensure the homepage loads quickly.
* Procedure: Measure the time taken for the homepage to load.
* Expected Result: The homepage load within an acceptable time frame (e.g., under 3 seconds).

#### 4.3.2 Responsive Load Test
* Objective: Test performance across different devices.
* Procedure: Measure page load times on desktop, tablet, and mobile devices.
* Expected Result: Pages load on all devices.

### 4.4 Security Tests
#### 4.4.1 Login Security Test
* Objective: Ensure login functionality is secure.
* Procedure: Attempt login with invalid credentials.
* Expected Result: The system do not allow access and display an appropriate error message.

#### 4.4.2 Form Validation Test
* Objective: Verify that all forms have proper validation.
* Procedure: Test form submissions with invalid data (e.g., empty fields, incorrect formats).
* Expected Result: Forms display appropriate validation error messages.

### 4.5 Cross-Browser Tests
#### 4.5.1 Browser Compatibility Test
* Objective: Ensure the header displays correctly across different browsers.
* Procedure: Test the website on Chrome, Firefox, Safari, Edge, and Internet Explorer.
* Expected Result: The header function and display correctly in all tested browsers.

### 4.6 Accessibility Tests.
#### 4.6.1 Keyboard Navigation Test
* Objective: Verify that all interactive elements are accessible via keyboard.
* Procedure: Navigate the site using only the keyboard.
* Expected Result: All interactive elements are focusable and operable via keyboard.


### 5. Unfixed
### 5.1 Just a note:
This is my 5th project restart. The reason why I´m saying this because I dont want you to think that the hours I´ve spent on this repo is the only ones. 

I have two other projects which I gave up due to migrations error. 
* https://github.com/GlennJohansson85/hitech
* https://github.com/GlennJohansson85/techboy

### 5.2 I wish I could have:
 * Fixed the navbar in mobileview
 * Add stock per item, size and color. Now it is just per item.
 * Add more search filter than just product category.
 * Customer Reviews - Rating System
 * Add more style to the the page.
 * 




## 5. Deployment

## 6. Credits

## 7. Media
