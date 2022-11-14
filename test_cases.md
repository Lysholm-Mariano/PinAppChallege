TEST CASES

1) Check Login Functionality: 
    Test case: Check response on entering no valid Password
    Expected result: An error message of wrong data
    test steps:
        Given an user already created for mercadolibre
        When user click "Ingresá"
        and the login screen is loaded
        and user types valid mail and "Continuar" button
        and user types no valid password 
        and user clicks "Iniciar sesión" button
        Then a message showing an errors appears


2) Check search Functionality (automatized one):
    Test case: Check response on searching different objects
    Expected result: A list of objects related to the description is shown
    test steps:
        Given Mercadolibre home page is displayed
        When user searchs for an object
        Then the search result title and url contains the description

3) Check opening a products description:
    Test case: Check response on clicking on a product
    Expected result: A page with full description is loaded with a "Comprar ahora" Button
    test steps:
        Given a list of products
        When user clicks any of them
        Then the product's page is displayed, with a full description and a button to buy the item