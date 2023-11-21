# 2023-02-DSM-GRUPO-02

# sempre ao abrir o terminal acesse a pasta apps

cd apps

# apos acessar a pasta apps para rodar o manage.py utilize a seguinte sintaxe

python ..\manage.py startapp product

# depois

python ..\manage.py runserver

# ou 

python ..\manage.py makemigrations

# ou 

python ..\manage.py migrate

# python ..\manage.py createsuperuser






diagrama: 

@startuml DER 

class category{
    id
    vehicle_type
    description
    
}

class vehicle{
    model
    brand
    year
    color 
    is_active 
    category: Category
}

class driver{
driver_first_name
driver_last_name
driver_adress
driver_cellphone
driver_email
license 
    order: Order
    product: Product
}

class order{
    total_price  
    status  
    payment_method
    client: Client
}

class client{
    client_first_name  
    client_last_name  
    client_address  
    client_cellphone  
    client_email  
    
     
}

class client_socialnetwork{
    client: Client
    socialnetwork: Socialnetwork
}

class socialnetwork{
    name  
    email
}

vehicle *-- category
client --* client_socialnetwork
socialnetwork --*  client_socialnetwork
client --* order
order --* driver
vehicle --* driver

@enduml


