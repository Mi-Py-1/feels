# Feels App

Overview
The Feels App is a Django-based social media platform designed to foster meaningful interactions by allowing users to share posts, express their feelings, and engage with others. The app includes features such as user authentication, post creation, and a "Contact Us" form for user feedback.

The project aims to solve the problem of creating a safe and inclusive online space where users can share their thoughts and emotions. Its value lies in its simplicity, accessibility, and focus on inclusivity, ensuring that users of all abilities can interact with the platform seamlessly.


UX Design Process

User Stories in GitHub Feels Project: 

https://github.com/users/Mi-Py-1/projects/12

![User Stories](images/user-stories-feels.png "User Stories")

![Agile working](Agile.png "Agile")

Wireframes

Wireframe Links:

![Splash Page Wireframe](images/Splash-Page.png "Splash Page Wireframe")

![Home Page Wireframe](images/Home-Page.png "Home Page Wireframe")

Rationale:

The wireframes were designed with usability and accessibility in mind. 

Key considerations include:

High Contrast: Ensures readability for users with visual impairments.
Clear Navigation: Simplifies navigation for all users, including those using assistive technologies.
Responsive Design: Optimized for various screen sizes to ensure usability on mobile, tablet, and desktop devices.

Design Rationale

Layout: A clean and minimalistic layout was chosen to reduce cognitive load and improve focus on content.
Color Scheme: A neutral color palette with high contrast was used to enhance readability and accessibility.
Typography: Sans-serif fonts were selected for their clarity and legibility.
Accessibility Guidelines: The design adheres to WCAG 2.1 guidelines, ensuring compatibility with screen readers and keyboard navigation.

Reasoning for Any Final Changes

Significant Changes:
The navigation bar was simplified to improve usability for keyboard-only users.
The "Contact Us" form was redesigned to include clear labels and error messages for better accessibility.

Impact:
These changes enhance inclusivity by ensuring the app is usable for individuals with disabilities, such as those relying on screen readers or keyboard navigation.


Key Features

Feature 1: User Authentication
Description: Users can sign up, log in, and log out securely. Passwords are hashed for security, and authentication is handled using Django's built-in authentication system.
Purpose: Ensures that only authorized users can access certain features, such as creating posts or interacting with others.
Implementation: Includes custom user models to allow for role-based functionality (e.g., admin vs. regular user).

Feature 2: Post Creation and Interaction
Description: Users can create, update, and delete posts. Other users can interact with posts by adding "feels" (ratings) to express their emotions.
Purpose: Encourages user engagement and provides a platform for sharing thoughts and feelings.
Implementation: Posts are stored in a database, and interactions are tracked using foreign key relationships.

Feature 3: Contact Us Form
Description: A simple form that allows users to send feedback or inquiries. Submitted messages are sent to a designated email address.
Purpose: Provides a direct communication channel between users and the app administrators.
Implementation: Uses Django's form handling and email backend to process and send messages.

Inclusivity Notes

Accessibility: All features are designed with accessibility in mind, adhering to WCAG 2.1 guidelines. For example:
Forms include clear labels and error messages for screen reader compatibility.
Navigation is keyboard-friendly, ensuring usability for users with motor impairments.
Diverse User Needs: The app's features are simple and intuitive, catering to users with varying levels of technical proficiency, including those with SEND (Special Educational Needs and Disabilities).

Deployment

Platform

The app is deployed on Heroku, a cloud platform that simplifies deployment and scaling of web applications.

High-Level Deployment Steps

Prepare the Project for Deployment:

Install necessary packages like gunicorn and whitenoise for serving the app and static files.

Add a Procfile to specify the web server.

Create a runtime.txt file to specify the Python version.

Set Up the Heroku App: Log in to Heroku using the CLI: 'heroku login'

Create a new Heroku app or link to an existing one.

Push the Code to Heroku: 'heroku git:remote -a feels'

Push the code to Heroku's remote repository: 'git push heroku main'

Run Migrations and Collect Static Files and apply database migrations: 'heroku run python manage.py migrate'

Collect static files: 'heroku run python manage.py collectstatic --noinput'

Open the App: Launch the app in your browser: 'heroku open'


Verification and Validation

Functionality Testing: Verified that all features (e.g., user authentication, post creation, and the contact form) work as expected in the deployed version.

Accessibility Checks: Ensured that the deployed app adheres to WCAG 2.1 guidelines, including keyboard navigation and screen reader compatibility.

Security Measures

Environment Variables: Sensitive data like the SECRET_KEY and database credentials are stored securely in Heroku's environment variables.

DEBUG Mode: Disabled DEBUG in production to prevent exposure of sensitive information.

HTTPS: Heroku automatically enforces HTTPS for secure communication.


AI Implementation and Orchestration

Use Cases and Reflections

Code Creation

Reflection: AI tools were used to accelerate the development process by generating boilerplate code, such as models, views, and forms. This allowed for rapid prototyping and reduced repetitive tasks.

Examples:
Reverse prompts were used to explore alternative solutions for implementing the "Contact Us" form.
Question-and-answer prompts helped resolve specific challenges, such as configuring email backends and handling form submissions.

Debugging

Reflection: AI-assisted debugging helped identify and resolve logic errors in the application. For example:
Issues with migrations were resolved by using AI to suggest commands like --fake migrations.
AI provided insights into improving maintainability by simplifying complex logic in views and models.
Impact: These interventions ensured the app's functionality while maintaining clean and readable code.

Performance and UX Optimization

Reflection: AI-driven suggestions were applied to optimize the app's performance and user experience. Minimal manual adjustments were needed to implement these improvements.
Examples:
Optimized database queries for post retrieval to reduce load times.
Enhanced the responsiveness of the UI by refining Bootstrap-based layouts.


Automated Unit Testing (If undertaken)

Reflection: AI-generated test cases were used to improve test coverage and ensure functionality. Adjustments were made to align the tests with the app's requirements.
Examples:
Inclusive test cases were generated to cover edge cases, such as invalid form submissions and accessibility checks.

Overall Impact

Efficiency Gains:

Faster debugging and prototyping.
Comprehensive testing with minimal manual intervention.
Improved code quality and maintainability.
Challenges:
Contextual adjustments were required for AI-generated outputs to align with project goals.
These challenges were effectively resolved, enhancing the app's inclusivity and accessibility.


Testing Summary

Manual Testing

Devices and Browsers Tested:

Desktop: Google Chrome, Mozilla Firefox, Microsoft Edge.
Mobile: Safari (iOS), Chrome (Android).
Assistive Technologies: NVDA screen reader (Windows), VoiceOver (macOS/iOS), and keyboard-only navigation.

Features Tested:

User authentication (signup, login, logout).
Post creation, updating, and deletion.
Adding "feels" (ratings) to posts.
Navigation across pages (e.g., home, contact us).
Contact Us form submission and email delivery.

Results:

All critical features worked as expected.

Accessibility checks passed, including screen reader compatibility and keyboard navigation.

Minor adjustments were made to improve error message visibility on the "Contact Us" form.

Changes made to bring scores for python testing above 90% average and javascript testing above 95%.

![Javascript testing](images/Testing.png "Javascript testing")

Automated Testing (If undertaken)
Tools Used:

Django's built-in TestCase framework.
Features Covered:

User authentication workflows.
CRUD operations for posts.
Validation of the "Contact Us" form.
Adjustments Made:

AI-generated test cases were refined to include edge cases, such as invalid form submissions and missing required fields.
Accessibility-focused test cases were added to ensure compliance with WCAG 2.1 guidelines.


Future Enhancements

Potential Improvements

Voice Input Capabilities:

Add support for voice commands to allow users to navigate the app and create posts using speech.
This would enhance accessibility for users with motor impairments or those who prefer voice interaction.

Multilingual Support:

Implement language translation features to make the app accessible to a global audience.
Provide localized versions of the app for non-English speakers.

Enhanced Notifications:

Introduce real-time notifications for user interactions, such as when someone adds a "feel" to a post or sends a message via the "Contact Us" form.

Improved Analytics:

Add a dashboard for users to view analytics about their posts, such as the number of interactions or "feels" received.

Dark Mode:

Provide a dark mode option to improve usability for users in low-light environments and reduce eye strain.
Accessibility Enhancements:

Further refine keyboard navigation and screen reader support.
Add ARIA (Accessible Rich Internet Applications) roles and attributes to improve compatibility with assistive technologies.

Mobile App Version:

Develop a native mobile app for iOS and Android to provide a seamless experience for mobile users.

Considerations for Accessibility

Ensure that all future features adhere to WCAG 2.1 guidelines.
Test new features with assistive technologies, such as screen readers and keyboard-only navigation.
Gather feedback from users with disabilities to identify areas for improvement.