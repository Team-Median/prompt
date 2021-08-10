# Software Requirements

## Vision

What is the vision of this product?

- Our product will have the capability to web scrape a given website for specific information, in this case we will be focusing on hard to purchase items ie. Jordan's, Yeezy's, special collaborations among popular designers.

What pain point does this project solve?

- People like stuff and these days the hot items (GPUs, gaming consoles, trendy shoes) are being bought up and being resold on the grey market at exorbitant prices. Users need a way to check for their hot items from multiple pages to beat the bots used by these scalpers to have a fighting chance at getting these items in their carts.

Why should we care about your product?

- Our product will allow a user to simplify the process of checking on whether an item is in stock. By automating the process and programming it to run at specific intervals, it removes the redundancy of refreshing the page. Our product doesn't need to eat or use the restroom, it will continue to run as long as the user needs it to.

## Scope (In/Out)

- IN - What will your product do?
  - Describe the individual features that your product will do.
  - High overview of each. Only need to list 4-5
  - The web scraping tool will give the user a list of retailers to choose from
  - The web scraping tool search for a given item
  - It will then return a list of results

- OUT - What will your product not do?
  - Will not attempt to circumvent any website policies or break any laws
  - Will not exploit any backdoors or known vulnerabilities of the websites

## Minimum Viable Product vs

What will your MVP functionality be?

- Display welcome message with instructions
- Can take input of the name of a store and item search string
- Return a report of available items scraped from the page. - Include hyperlink to page
- Save the name and search string.
- Repeat search on an interval.
- User can keep the app running while taking care of other tasks.

What are your stretch goals?

Stretch
What stretch goals are you going to aim for?

- Export scapped data in a CSV format

## Functional Requirements

List the functionality of your product. This will consist of tasks such as the following:

1. An admin can create and delete user accounts
2. A user can update their profile information
3. A user can search all of the products in the inventory

Data Flow

Our web scraping tool that will check the availability of a hot item from a user's list of preferred shops. We create an input box, where we take in the item name and the user copies the url of an item search for their item from a selected store. That creates a search hit list. When they run a "prompt search", it scrapes the pages for listings that came up as "available", and prints out a list of available items. Thinking that can include a link to the search page, which should result in them seeing the available item. Can it auto run periodically? Can it alert the user? - Why it is cool does multiple searches for you and helps you get your desired hot items. It is lightweight and can run in the background.

## Non-Functional Requirements

Non-functional requirements are requirements that are not directly related to the functionality of the application but still important to the app.

Examples include:

  1. Utility
    - People like stuff and these days the hot items (GPUs, gaming consoles, trendy shoes) are being bought up and being resold on the grey market at exorbitant prices. Users need a way to check for their hot items from multiple pages to beat the bots used by these scalpers to have a fighting chance at getting these items in their carts.
  2. Usability
    - Our web scraper will be utilized within the command line, they will be given options between pre-selected shops. This makes the process very user friendly, and easy to use. Once the application has been turned on, it will return the results in a easy to read format.

Pick 2 non-functional requirements and describe their functionality in your application.

## Working Doc Links

Below are links to our Working google docs:

1. Mock Up:
https://docs.google.com/presentation/d/1SWBAjJXceREa7V6lhg4yFn_Gb3JaTqAsJQqLuxo8ivQ/edit?usp=sharing 

2. 