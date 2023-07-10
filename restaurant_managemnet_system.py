import matplotlib.pyplot as plt

class Dish:
    # ''' Represent a Dish'''

    def __init__(self, name, price, description):
        '''Initialize the dish'''
        self.name = name
        self.price = price
        self.description = description
    def __str__(self) :
        return f"{self.name} : {self.description} , {self.price}"

class MainDish(Dish):
    # '''Main Dish - Respresent subclass of Dish'''

    def __init__(self, name, price, description, cuisine):
        '''Initialize Main Dish & Cuisine'''
        super().__init__(name, price, description)
        self.cuisine = cuisine
    def __str__(self):
        return f"{super().__str__()} , {self.cuisine}"

class Dessert(Dish):
    # '''Desert - Represent subclass of Dish.'''

    def __init__(self, name, price, description, texture):
        # '''Initialize Main Dish & Texture'''
        super().__init__(name, price, description)
        self.texture = texture
    def __str__(self):
        return f"{super().__str__()} , {self.cuisine}"

# Menu class to manage the dishes

class Menu:
    # '''Represent the menu of restaurant.'''

    def __init__(self):
        # '''Initialize the Menu'''
        self.items=[]
        self.data=[]
        # self.data=Menu.f.readlines()

    def _add_dish(self,dish):
        # '''Add a dish to your menu.'''

        self.items.append(dish)
    # def _remove_dish(self, dish):
    #     self.items.remove(dish)


    def _save_to_file(self):
        # '''Save added dish in database.'''

        with open('menu.txt', "a+") as f:
            for dish in self.items:
                f.write(str(dish) + "\n")
    def search_dish(self):
        # '''Search for a dish.'''

        with open('menu.txt', "r") as f:
            self.data=f.readlines()
            item=input('enter a dish to be searched:')
            for i in range(len(self.data)):
                if item in self.data[i]:
                    print(self.data[i],end='')
                    break
                else:
                    print('Sorry! Item is not available !')
    def display_menu(self):
        # '''Display the menu'''

        with open("menu.txt", "r") as f:
            self.data=f.readlines()
            for dish in self.data:
                print(dish,end='')
                
class Order(Menu):
    # '''Represent Class Order to manage Order functionality'''

    def __init__(self):
        # '''Initialize Order class'''

        self.order_items=[]
        self.bill=[]
        self.price=[]
        self.quantity=[]
        self.total=0
    def order_item(self):
            # '''Order your food'''

            Menu.display_menu(self)
            self.order_items=input('Enter a dish you want to order: ').split(',')
            print('Your order is : ')
            for i in range(len(self.order_items)):
                for j in range(len(self.data)):
                    if self.order_items[i] in self.data[j]:
                        print(self.data[j],end='')
                        self.bill.append(self.data[j])
                        self.quantity.append(int(input('enter quantity:')))
                        self.price.append(int(self.data[j].split(',')[1]))
            for i in range(len(self.order_items)):
                self.total+=(self.price[i] * self.quantity[i])
            # print(self.total)

    def show_bill(self):
        # '''Show bill to customer.'''

        print('-'*50)
        print('Your Bill is:')
        print('-'*50)
        for i in range(len(self.bill)):
            print(f"{self.bill[i]} X {self.quantity[i]}")
        print('SUB TOTAL : ',self.total)
        print('CGST(9%)',(self.total*9)/100)
        print('SGST(9%)',(self.total*9)/100)
        self.total+=2*((self.total*9)/100)
        print('Amount Incl of All Taxes : ',self.total)

class User():
    # """Represent a simple user profile."""

    def __init__(self, name, username, email):
        """Initialize the user."""
        self.name = name
        self.username = username
        self.email = email

class Admin:
    # """A user with administrative privileges."""

    def __init__(self, name, password):
        """Initialize the admin."""
        self.name=name
        self.password=password
        self.admin_to_file()
        # self.login_a(self.name,self.password)
        self.d_items=[]
    
    def login_a(self,name,password):
        with open('admin.txt','r') as f:
            d=f.readlines()
            for i in range(len(d)):
                if(d[i].split(' : ')[0]==name and d[i].split(' : ')[1]==password):
                    print(f'Welcome Back {self.name}')
                    self.choice_a()
                else:
                    print('Wrong Username / Password')

    def admin_to_file(self):
        '''Save admin data into file'''
        with open('admin.txt','w') as f:
            f.write(self.name + " : " + self.password)
        
    def add_manager(self):
        '''Appoint manager for your restaurant'''
        name=input('Name : ')
        username=input('Username : ')
        email=input('Email : ')
        position=input('Position :')
        password=input('Password : ')
        with open('manager.txt','a+') as f:
            s=name + " " + username + " " + email + " " + position + " " + password +'\n'
            f.write(s)
            print('Details has been successfully Added')

    def view_detail_manager(self):
        '''View detail of manager'''
        with open('manager.txt','r') as f:
            data=f.readlines()
            for i in data:
                print(i)

    def favourite_dish(self):
        '''Keep track of favourite dishes.'''
        with open('custreview.txt','r') as f:
            data=f.readlines()
            for i in range(len(data)):
                d=data[i].split(' : ')[1][:-1]
                d_data=d.split(' , ')
                for i in range(len(d_data)):
                    self.d_items.append(d_data[i])
                # print(self.d_items)
            freq = {}
            for i in self.d_items:
                if (i in freq):
                    freq[i] += 1
                else:
                    freq[i] = 1
            # print(freq)
            names = list(freq.keys())
            values = list(freq.values())

            plt.bar(names, values)
            plt.xlabel('Dish Name')
            plt.ylabel('Total Likes')
            plt.title('Favourite Dish')
            plt.show()

    def choice_a(self):
        admin=0
        ch=0
        while admin!=4:
            print('''
1.Add manager details
2.Show Details of Manager
3.Show Favourite Dish
4.Quit''')
            admin=int(input())
            # admin=int(input())
            if admin!=1 and admin!=2 and admin!=3 and admin!=4:
                print('Incorrect Choice !')
                admin=int(input())
            else:
                if admin==1:
                    self.add_manager()
                if admin==2:
                    self.view_detail_manager()
                if admin==3:
                    self.favourite_dish()
                if admin==4:
                    self.choice_a()

class Manager(Menu):
    def __init__(self):
        # Admin.__init__(self)
        Menu.__init__(self)
        self.uname=''
        self.paswd=''

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.uname + "!")

    def login(self,uname,paswd):
        self.uname=uname
        self.paswd=paswd
        with open('manager.txt','r') as f:
            data=f.readlines()
            # print(data)
            for i in range(len(data)):
                if self.uname in data[i]:
                    # print(data[i].split(' '))
                    if self.paswd==data[i].split(' ')[4][:-1] :
                        print(' Login Successful !')
                        self.greet_user()
                        self.choice()
                    else:
                        print('password is incorrect')
                else:
                    print('username is incorrect')
                    # return

    def add_to_menu(self):
        dish_name=input('enter your dish name:')
        dish_price=input('enter your dish price')
        dish_desc=input('enter description of your dish')
        c_or_d=input('cuisine or dessert? c/d')
        if c_or_d=='c':
            dish_cuisine=input('enter cuisine of your dish:')
            self._add_dish(str(MainDish(dish_name,dish_price,dish_desc,dish_cuisine)))
        elif c_or_d=='d':
            dish_texture=input('enter texture of your dessert:')
            self._add_dish(str(MainDish(dish_name,dish_price,dish_desc,dish_texture)))
        self._save_to_file()

    def remove_from_menu(self):
        with open('menu.txt','r') as f:
            self.data=f.readlines()
        with open('menu.txt','w') as f:
            dish_name=input('enter your dish name:')
            for i in range(len(self.data)):
                if dish_name not in self.data[i]:
                    f.write(self.data[i])
                else:
                    print(f"{dish_name} is successfully removed !" )
            f.seek(0)
            self.display_menu()

    def update_menu(self):
        dish_name=input('enter a dish name to be modified:')
        dish_n_name=input('Dish Name:')
        dish_price=input('Price :')
        dish_desc=input('Description') 
        c_or_d=input('cuisine or dessert? c/d')
        with open('menu.txt','r') as f:
            self.data=f.readlines()
        with open('menu.txt','w') as f:
            for i in range(len(self.data)):
                if dish_name in self.data[i]:
                    if c_or_d=='c':
                        dish_cuisine=input('enter cuisine of your dish:')
                        f.write(str(MainDish(dish_n_name,dish_price,dish_desc,dish_cuisine)) + '\n')
                    elif c_or_d=='d':
                        dish_texture=input('enter texture of your dessert:')
                        f.write(str(MainDish(dish_n_name,dish_price,dish_desc,dish_texture)) + '\n')
                else:
                    f.write(self.data[i])

            self._save_to_file()


    def choice(self):
        ch=0
        while(ch!=6):
            ch=int(input('''
    Enter your choice for your action:
    1.Add a dish to menu
    2.Remove dish from menu
    3.Update Menu
    4.Search Dish
    5.Display Menu
    6.Quit'''))
            if ch==1:
                self.add_to_menu()
            if ch==2:
                self.remove_from_menu()
            if ch==3:
                self.update_menu()
            if ch==4:
                self.search_dish()
            if ch==5:
                self.display_menu()
            if ch==6:
                return

class Customer(User,Order,Menu):
    def __init__(self):
        Menu.__init__(self)
        Order.__init__(self)
        
    def greet_cust(self , name, username, email):
        """Display a personalized greeting to the user."""
        super().__init__(name, username, email)
        print("\nWelcome ! " + self.name + " !")
        # self.choice_c()

    def choice_c(self):
        ch=0
        while(ch!=5):
            ch=int(input('''
    Enter your choice for your action:
    1.View Menu
    2.Order
    3.View Bill
    4.Feedback
    5.Quit'''))
            if ch==1:
                self.display_menu()
            elif ch==2:
                self.order_item()
            elif ch==3:
                self.show_bill()
            elif ch==4:
                self.feedback()
            elif ch==5:
                return

    def feedback(self):
        dish=input('Enter your favourite dishes! \n').split(',')
        s=self.name + ' : ' + ' , '.join(dish)
        print(s)
        with open('custreview.txt','a+') as f:
            f.write(s + '\n')

class Restaurant:
    """A class representing a restaurant."""
    def __init__(self,name):
        self.r_name=name
        # self.open_restaurant()

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = self.r_name + " serves wonderful " +"."
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.r_name + " is open. Come on in!"
        print("\n" + msg)

class Start(Restaurant,Manager,Admin,Customer,User):
    def __init__(self, name):
        Restaurant.__init__(self,name)
        Manager.__init__(self)
        Admin.__init__(self , 'ManushiOza' ,'Manushi$2435')
        Customer.__init__(self)
        self.menu()

    def menu(self):
        self.describe_restaurant()
        self.open_restaurant()

        print('''
    Enter your role:
    1.Admin
    2.Manager
    3.Customer
    4.Quit''')

        ch=0
        while (ch!=4):
            ch=int(input())
            # print(ch)
            # print(type(ch))
            if ch!=1 and ch!=2 and ch!=3 and ch!=4:
                print('Incorrect Choice !')
            else:
                if ch==1:
                    # print('Welcome !' + self.name)
                    yes=0
                    while yes!=2:
                        yes=int(input('''
    1. Login
    2. Quit'''))
                        if (yes==1):
                            a_name=input('Enter your Username : ')
                            a_password=input('Enter your Password : ')
                            # Admin.__init__(self,'ManushiOza','Manushi#123')
                            self.login_a(a_name,a_password)

                        if yes==2:
                            self.menu()
                if ch==2:
                    yes=0
                    while yes!=2:
                        yes=int(input('''
    1. Login
    2. Quit'''))
                        if (yes==1):
                            uname=input('Enter your Username : ')
                            password=input('Enter your Password : ')
                            self.login(uname,password)
                        if yes==2:
                            self.menu()

                if ch==3:
                    c_ch=0
                    while c_ch!=2:
                        print('''
    Welcome !
    1. Let's Order!
    2.Quit''')
                        c_ch=int(input())
                        if c_ch==1:
                            name=input('Enter Your Name : ')
                            u_name=input('Enter your Username  : ')
                            e_mail=input('Enter your Email:')
                            self.greet_cust( name , u_name , e_mail)
                            self.choice_c()
                        if c_ch==2:
                            self.menu()

                if ch==4:
                    print('Thank You !')
            


# manushi=Admin('ManushiOza', 'm_oza', 'manushi2003@gmail.com','manushi#2409')
res=Start('When Do We Eat')
# # manushi.add_manager()
# manushi=Manager('m_oza','manushi#2409')
# manushi.login()

# vedanshi=Customer('VedanshiOza' , 'v_oza' , 'voza0812@gmail.com')

# menu=Menu()
# order=Order()
# menu._add_dish(MainDish('Pasta',150,'white sauce pasta','italian'))
# menu._add_dish(MainDish('Cheesecake',150,'red velvet cheesecake','soft'))
# menu._save_to_file()
# # menu.list_dishes()
# order.order_item()
# order.show_bill()

# eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
# eric.describe_user()
# eric.greet_user()

# willie = User('willie', 'burger', 'willieburger', 'wb@example.com', 'alaska')
# willie.describe_user()
# willie.greet_user()