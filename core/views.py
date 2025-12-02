from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Recipe, Profile
from django.db.models import Q
from .forms import ProfileForm

def signup(request):
    if request.method == "POST":
        username = request.POST['email']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "User already exists.")
            return redirect('signup')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created")
        return redirect('login')
    
    return render(request, "core/signup.html")

def user_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('login')
    
    return render(request, 'core/login.html')

@login_required(login_url='login')
def dashboard(request):
    query = request.GET.get('q')              
    category = request.GET.get('category')
    recipes = Recipe.objects.all()
    
    if query:
        recipes = recipes.filter(
            Q(title__icontains=query) |
            Q(ingredients__icontains=query)
        )
    
    if category:
        recipes = recipes.filter(category=category)
    
    username_only = request.user.username.split("@")[0]
    
    return render(request, 'core/dashboard.html', {
        'recipes': recipes,
        'username_only': username_only,
        'selected_category': category,
        'query': query
    })

@login_required(login_url='login')
def home(request):
    return render(request, 'core/dashboard.html')

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def add_recipe(request):
    if request.method == "POST":
        title = request.POST.get('title')
        ingredients = request.POST.get('ingredients')
        instructions = request.POST.get('instructions')
        image = request.FILES.get('image')
        category = request.POST["category"]

        Recipe.objects.create(
            user=request.user,
            title=title,
            ingredients=ingredients,
            instructions=instructions,
            image=image,
            category=category
        )
        return redirect('dashboard')
    
    return render(request, 'core/add_recipe.html')

def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, "core/recipe_detail.html", {"recipe": recipe})

@login_required(login_url="login")
def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if recipe.user != request.user:
        messages.error(request, "You are not allowed to delete this recipe.")
        return redirect("dashboard")
    recipe.delete()
    messages.success(request, "Recipe deleted successfully.")
    return redirect("dashboard")

@login_required(login_url='login')
def add_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('dashboard')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'core/add_profile.html', {'form': form})
    