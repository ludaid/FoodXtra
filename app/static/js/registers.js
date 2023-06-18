function register()
{
    if(!isNaN(f.name.value))
    {
        alert("enter name in character format");
        f.name.focus();
        return false;
    }
    if(isNaN(f.age.value))
    {
        alert("enter valid age");
        f.age.focus();
        return false;
    }
   
    var a= /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
    if(!(f.email.value.match(a)))
    {
        f.email.focus();
        alert("enter the valid email");
        return false;
    }
    
    if(f.phone1.value.length!=10)
    {
        alert("enter valid mobile number")
        f.phone1.focus()
        return false;
    }
    if(isNaN(f.phone1.value))
    {
        alert("enter valid mobile number")
        f.phone1.focus()
        return false;
    }
    return true;
}