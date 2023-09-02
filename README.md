# Save Food

Save Food is a web application pilot project that provides the platform for people to share food instead of throwing them away or leaving them to spoil. On the other hand, poeple are also able to view the posted food items and chat their owners for the food to be reserved and picked up at the given location.

The live link can be found here: [Live Site - Save Food](https://save-food-3b2a71b51608.herokuapp.com/)

![Mock Up](docs/readme_images/save-food-mockup.jpg)

## Table of Contents
- [Save Food](#save-food)
  - [Table of Contents](#table-of-contents)
- [User-Experience-Design](#user-experience-design)
  - [The-Strategy-Plane](#the-strategy-plane)
    - [Site-Goals](#site-goals)
    - [Agile Planning](#agile-planning)
      - [Epics](#epics)
      - [User Stories](#user-stories)
  - [The-Scope-Plane](#the-scope-plane)
  - [The-Structure-Plane](#the-structure-plane)
    - [Features](#features)
    - [Features Left To Implement](#features-left-to-implement)
  - [The-Skeleton-Plane](#the-skeleton-plane)
    - [Wireframes](#wireframes)
    - [Database-Design](#database-design)
    - [Security](#security)
  - [The-Surface-Plane](#the-surface-plane)
    - [Design](#design)
    - [Colour-Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
  - [Technolgies](#technolgies)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Version Control](#version-control)
    - [Heroku Deployment](#heroku-deployment)
  - [Credits](#credits)

# User-Experience-Design

## The-Strategy-Plane

### Site-Goals

The site is aimed at providing a platform for people to share food. Registered users are able to chat owners of the posted food items and through that confirm their reservation and later pick it up at the given location. 
Owners of food item posts are able to edit, delete and have a reserved status on their posts when necessary.

This is to help in reducing food wastage and greenhouse gas emmision as well as saving natural resources and the planet. In the end people get fed and it is a happier society.

### Agile Planning

This project was developed using agile methodologies by delivering small features in incremental sprints. There were 3 sprints in total, spaced out evenly over four and half weeks.

All projects were assigned to epics, prioritized chronologically as, Must have, should have and could haves. They were assigned to sprints and stories based on their level of complexity. Implementation was done in order of the aforementioned priority. It was done this way to ensure that all core requirements were completed first to give the project a complete feel, with the nice to have features being added should there be the capacity.

The Kanban board was created using github projects and can be located [here](https://github.com/users/samuelandersoncodes/projects/1) and can be viewed to see more information on the project cards. All stories except the documentation tasks have a full set of acceptance criteria in order to define the functionality that marks that story as complete.

![Kanban image](docs/readme_images/save-food-kanban.jpg)

### Save Food issues
![Kanban image](docs/readme_images/save-food-issue.jpg)

#### Epics

The project had 6 main Epics (milestones):

**EPIC 1 - Base Setup**

The base setup epic is for all stories needed for the base set up of the application. Without the base setup, the app would not be possible so it was the first epic to be delivered as all other features depend on the its completion.

**EPIC 2 - Stand alone Pages**

The stand alone pages epic is for small pages that did not have enough stories to warrant their own full epics. Instead of creating epics for tiny features, these small deliverables were all added under this epic.

**EPIC 3 - Authentication Epic**

The authentication epic is for all stories related to the registration, login and authorization of views. This epic provides critical functionality and value as without it users would not be able to securely post and edit food items as well as chat item owners for food reservation.

**EPIC 4 - Food item posts Epic**

The item posts epic is for all stories that relate to creating, viewing, updating and deleting food item posts. This allows logged in users who are owners of respective posts to easily edit and delete posts when necessary and also reserve food items for users who really need them. Through this epic, all other users are able to post and view other food item posts.

**EPIC 5 - Deployment Epic**

This epic is for all stories related to deploying the app to heroku so that the site is live for users.

**EPIC 6 - Documentation**

This epic is for all document related stories and tasks that are needed to document the software development lifecycle of the application. It aims to deliver quality documentation, explaining all stages of development and necessary information on running, deploying and using the application.
