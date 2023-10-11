# GraphQL_ProductApp

## Installation
Use the package manager [pip] to install the required file from requirement.txt file (pip install -r requirements.txt).

## Run Server
Make migrations and run django server.
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

## Create user through GraphiQL
Successfull registration of user will trigger the django mail to sent the verification token, which currently is printed in the python console.

--- GraphiQL ---
URL : http://localhost:8000/users/graphql/

    mutation{
        register(
            email: "adnan@gmail.com",
            username: "adnan",
            password1: "adnan99@123",
            password2: "adnan99@123",
        ){
            success,
            errors,
            token,
            refreshToken,
        }
    }

## Verify User with the token printed in python console.

--- GraphiQL ---
URL : http://localhost:8000/users/graphql/

    mutation{
        verifyAccount(token: "eyJ1c2VybmFtZSI6ImFkbmFuIiwiYWN0aW9uIjoiYWN0aXZhdGlvbiJ9:1qpv7k:Q--Wif46Rp0SboS6J4LqHcfarxvf-jXVLaQggMN48GU"),
        {
            success,
            errors
        }
    }

## Quering all Products.

--- GraphiQL ---
URL : http://localhost:8000/products/graphql/
    query{
        allProducts{
            name
            price
            productType{
                name
            }
            category{
                name
            }
            brand{
                name
            }
        }
    }

## Mutation for Create a Product (Brands, Category, Type already existing in DB.)

--- GraphiQL ---
URL : http://localhost:8000/products/graphql/

    mutation firstMutation{
        createProduct(name:"Bonart Dragee Pistachio 100g" brand:"Bonart" type:"Chocolates" category:"Chocolate & Sweets" price:"5.45"){
            product{
                name
            }
        }
    }