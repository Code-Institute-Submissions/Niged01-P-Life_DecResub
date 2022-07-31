## Contents
- [Unit Testing](#unit-testing)
    - [Testing Views](#testing-views)
    - [Testing Forms](#testing-forms)
- [Validator Testing](#validator-testing)
    - [Lighthouse Test](#lighthouse-test)
    - [W3C Markup Validation](#w3c-markup-validation)
    - [W3C CSS Validation](#w3c-css-validation)
    - [PEP8 validation](#pep8-validaton)
- [User Story Testing](#user-story-testing)
    - [Admin](#admin)
    - [General User](#general-user)
    - [Member User](#member-user)
- [Final testing](#final-testing)

## Unit Testing

- I have used Django TestCase for automated testing for Views, and form files

### Testing Views
- Tested views to see if they are functioning as expected and returns the page the user needs to be at.
    
- Home page

![testing home page views](./assets/documentation/indexpage-test.png)


- Blog page

![testing blog page views](./assets/documentation/blogpage-test.png)

- Profile Page

![testing for profile page views](./assets/documentation/profilepage-test.png)

- Publishing Blogs Page

![testing for publishing blog views](./assets/documentation/publishpage-test.png)

Result :

![result for views tests](./assets/documentation/test-for-views-result.png)

### Testing Forms
- Tested forms for comment form and blog form to make sure fields are expected and the form is submitted to where it should be.

- Testing blogform

![test for blogform](./assets/documentation/test-blogform.png)

- Testing Comment forms

![tests for comment form](./assets/documentation/test-commentform.png)

Result:

![result for form tests](./assets/documentation/formstests-results.png)

## Validator Testing

### Lighthouse Test

- Lighthouse result for desktop
    - The 89 is around image rendering and is out of my abilities at this time.

![lighthouse report desktop](./assets/documentation/testdesktop.png)

- Lighthouse result for mobile

![lighthouse result for mobile](./assets/documentation/testmobile.png)

### W3C Markup Validation

- Home page

![home page HTML test](./assets/documentation/html-indexpage.png)

- Blog page

![blog page HTML test](./assets/documentation/html-blogpage.png)

- Blog detail page

![blog-detail page HTML test](./assets/documentation/html-blogdetail-page.png)

- Register Page

![register page HTML test](./assets/documentation/html-registerpage.png)

- Login Page

![login page HTML test](./assets/documentation/html-loginpage.png)

- My Blogs Page

![My blogs page HTML test](./assets/documentation/html-myblogspage.png)

- Profile page

![Profile page HTML test](./assets/documentation/html-profilepage.png)

- Publish page

![publish page HTML test](./assets/documentation/html-publishpage.png)

### W3C CSS Validation

- No errors or warnings found

![Css validation test](./assets/documentation/css-check.png)

### PEP8 validation
- There was only one error found in the views, documented it in the bugs section on the Readme document. It was resolved and then passed the tests.

- Unit testing for forms

![unit testing for forms](./assets/documentation/unittest-forms.png)

- Unit testing for views

![Unit testing for views](./assets/documentation/unittest-views.png)

- blog app urls

![blog app urls](./assets/documentation/blogapp-urls.png)

- admin.py

![admin.py pep8](./assets/documentation/pep8-admin.py.png)

- apps.py

![apps.py pep8](./assets/documentation/pep8-apps.py.png)

- asgi.py

![asgi.py pep8](./assets/documentation/pep8-asgi.py.png)

- forms.py

![forms.py pep8](./assets/documentation/pep8-forms.py.png)

- models.py

![models.py pep8](./assets/documentation/pep8-models.py.png)

- project url.py

![project url pep8](./assets/documentation/pep8-projecturl.png)

- views.py bug

![views.py bug pep8](./assets/documentation/pep8-views.py-bug.png)

- views.py resolved

![views.py resolved pep8](./assets/documentation/pep8-views.py.png)

- wsgi.py

![wsgi.py pep8](./assets/documentation/pep8-wsgi.py.png)

## User Story Testing

### Admin
- As Site Admin, I can approve/disapprove blogs and comments so that I can filter out objectionable Content.

![admin approve](./assets/documentation/admin-authorize.png)

- As Site Admin I can create, post, edit or delete blogs so that I can share and manage my blogs.
- As Site Admin I can have all the functionality of a member user so that I can be involved with the blog site.

![admin site](./assets/documentation/admin-view.png)

### General User

- As a general user, I can view a list of blogs so that I can select one to read.

![blog page](./assets/documentation/site-blogpage.png)

- As a general user, I can click on a blog so that I can read the whole blog.
- As a general user, I can view the number of likes on a blog, so that I can see which is most popular.
- As a general user, I can view comments on individual blogs so I can read the full conversation.

![blog-detail page](./assets/documentation/site-blogdetails-notloggedin.png)

- As a general user, I can register for an account to take full member user benefits.

![register page](./assets/documentation/site-registerpage.png)

### Member User

- As a member user, I can create, post, edit or delete blogs so that I can share and manage my blogs.

![manage blogs](./assets/documentation/site-manageblogs.png)

![publish blog](./assets/documentation/site-publishblog.png)

- As a member user, I can like/unlike blogs so that I can interact with the content.
- As a member user, I can leave comments on a blog, so that I can be involved with the conversation.

![blog detail page](./assets/documentation/site-detailloggedin.png)

## Final testing
- All pages have been tested on desktop, tablet, and mobile, links and buttons have been tested and appear satisfactory.

back to the [README.md](README.md)