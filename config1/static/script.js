function required()
{
    var empt= document.forms["form1"]["name"]["email"]["password_1"]["password_2"].value;
    if (empt == "")
    {
        alert("Please enter coresponding value");
        return false;
    }
    else 
    {
        return true;
    }
}