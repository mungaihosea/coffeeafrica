from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login as login_user, logout, authenticate
from django.contrib.auth.models import User
from transactions import calenderutil
from django.shortcuts import redirect
from .models import SellerFactoryEmployee, SellerFactory, Buyer
from django.views.generic import View
from django.urls import reverse
from transactions.models import Order, Auction


def homepage(request):
    return render(request, "homepage.html", {})


def profile(request):
    return render(request, "profile.html", {})


def logout(request):
    return redirect("accounts:homepage")

def login(request):
    error = None
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("pass")
        try:
            user = User.objects.get(email=email)
            if user.check_password(password) == True:
                login_user(request, user)
                return redirect("accounts:dashboard")
        except User.DoesNotExist:
            error = "incorrect email or password"
    return render(request, "login.html", {"error": error})


def dashboard(request):
    if request.user.is_authenticated:
        user = request.user
    else:
        return redirect("account:login")
    context = {"user": user}
    try:
        print(user.sellerfactoryemployee.factory)
        order_queryset = Order.objects.filter(employee=user.sellerfactoryemployee)
        auctions = Auction.objects.filter(factory=user.sellerfactoryemployee.factory)
        n = 0
        for order in order_queryset:
            if order.auction == auctions[0]:
                n += 1
        auctions = Auction.objects.all()
        prices = []
        months_price = []
        months = []
        for auction in auctions:
            price = auction.price_per_tonne
            months_price.append(auction.date)
            prices.append(price)
        sumprice = sum(prices)
        months = calenderutil.getAllMonthsStr()
        try:
            mean_price = sumprice / len(prices)
        except:
            mean_price = 0
        context = {
            "prices": prices,
            "months_price": months_price,
            "months": months,
            "MeanPrice": round(mean_price, 3),
        }

        context["auctions"] = auctions
        context["orders"] = n
        context["order_queryset"] = order_queryset

        print(context)
        return render(request, "seller_dashboard.html", context)
    except AttributeError:
        order_queryset = Order.objects.filter(buyer=user.buyer)
        auctions = []
        for order in order_queryset:
            auction = order.auction
            if auction not in auctions:
                auctions.append(auction)
        notifications = []
        for order in order_queryset:
            if order.status == 1 and not order.shipping_address:
                notification = Notification(
                    1,
                    "view_order",
                    f"Your Order for the {order.auction} has been accepted",
                    order.id,
                    "transactions",
                )
                notifications.append(notification)
        auctions = Auction.objects.all()
        prices = []
        months_price = []
        months = []
        for auction in auctions:
            price = auction.price_per_tonne
            months_price.append(auction.date)
            prices.append(price)
        sumprice = sum(prices)
        months = calenderutil.getAllMonthsStr()
        try:
            mean_price = sumprice / len(prices)
        except:
            mean_price = 0
        context = {
            "prices": prices,
            "months_price": months_price,
            "months": months,
            "MeanPrice": round(mean_price, 3),
        }
        context["notifycount"] = len(notifications)

        context["auctions"] = auctions
        context["order_queryset"] = order_queryset

        context["notifications"] = notifications

        orders = Order.objects.filter(buyer=user.buyer)
        context["orders"] = len(orders)
        context["pending"] = len(Order.objects.filter(buyer=user.buyer, status=0))
        context["confirmed"] = len(Order.objects.filter(buyer=user.buyer, status=1))
        context["processed"] = len(Order.objects.filter(buyer=user.buyer, status=2))
        context["completed"] = len(Order.objects.filter(buyer=user.buyer, status=3))
        factories = []
        for order in order_queryset:
            if order.employee.factory not in factories:
                factories.append(order.employee.factory)
        context["factories"] = factories
        return render(request, "buyer_dashboard.html", context)



class Notification:
    def __init__(self, type, action, messsage, id, app_name):
        self.type = type
        self.action = action
        self.message = messsage
        self.id = id
        self.app_name = app_name


class GetFactoriesView(View):
    def get(self, request, *args, **kwargs):
        context = {"factories": SellerFactory.objects.all()}
        return render(request, "factories.html", context)

def create_account(request):
    logout(request)
    return render(request, "create_account.html", {})

def create_buyer_account(request):
    if request.method == "POST":
        print(request.POST)
        if request.POST['username'] and request.POST['email'] and request.POST['pass'] and request.POST['repeatpass'] and request.POST['country'] and request.POST['address'] and request.POST['phone']:
            print("they all came in ")
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['pass']
            repeat_password = request.POST['repeatpass']
            country = request.POST['country']
            phone = request.POST['phone']
            address = request.POST['address']
            profile_photo = request.POST['profilepicture']
            email_queryset = User.objects.filter(email = email)
            if email_queryset.__len__() == 0:
                if password == repeat_password:
                    user = User.objects.create(username = username, email = email)
                    user.set_password(password)
                    user.save()
                    buyer = Buyer.objects.create(user = user ,country = country, address = address, profile_picture = profile_photo, phone = phone)
                    buyer.save()
                    return render(request, 'account_success.html', {})
                else:
                    print('passwords do not match')
            else:
                print("a user with that email already exists")
            

    return render(request, 'create_buyer_account.html', {})

def create_seller_account(request):
    if request.method == "POST":
        if request.POST['factoryphone'] and request.POST['factoryemail'] and request.POST['factoryname'] and request.POST['tradelicense'] and request.POST["factorylogo"] and request.POST['username'] and request.POST['email'] and request.POST['pass'] and request.POST['repeatpass'] and request.POST['country'] and request.POST['address'] and request.POST['phone']:
            if request.POST['pass'] == request.POST['repeatpass']:
                factory = SellerFactory.objects.create(factory_name = request.POST['factoryname'], factory_email=request.POST['factoryemail'], phone = request.POST['factoryphone'], country = request.POST['country'], trade_license = request.POST['tradelicense'], factory_logo = request.POST['factorylogo'])
                email = request.POST['email']
                username = request.POST['username']
                password = request.POST['pass']
                repeat_password = request.POST['repeatpass']
                country = request.POST['country']
                phone = request.POST['phone']
                address = request.POST['address']
                profile_photo = request.POST['profilepicture']
                email_queryset = User.objects.filter(email = email)
                company_email_queryset = SellerFactory.objects.filter(factory_email = email)
                if email_queryset.__len__() == 0 and company_email_queryset.__len__() == 0:
                    if password == repeat_password:
                        user = User.objects.create(username = username, email = email)
                        user.set_password(password)
                        user.save()
                        SellerFactoryEmployee.objects.create(factory = factory, user = user, country = country, address = address, profile_picture = profile_photo, phone = phone)
                        return render(request, 'account_success.html', {})
                    else:
                        print('passwords do not match')
                else:
                    print("a user with that email already exists")
            else:
                print("passwords do not match")
    return render(request, "create_seller_account.html", {})