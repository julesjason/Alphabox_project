function required()
{
    let page = document.querySelector("form")
    var empt= document.forms["form1"]["name"]["email"]["password_1"]["password_2"].value;
    if (page == "")
    {
        alert("Please enter coresponding value");
        return false;
    }
    else 
    {
        return true;
    }
}

